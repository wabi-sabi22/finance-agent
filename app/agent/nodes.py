from typing import Any, List, Dict
from langchain_core.messages import HumanMessage, AIMessage

from app.services.llm_service import llm_service
from app.services.vector_service import VectorService
from app.services.tools import web_search_service
from app.agent.state import AgentState
from app.core.logger import agent_logger

# Import các hàm helper từ grounding.py mà bạn vừa cập nhật
from app.agent.grounding import (
    MAX_PDF_CHARS,
    MAX_WEB_CHARS,
    format_pdf_chunks,
    format_web_chunks,
    heuristic_need_web,
    truncate,
)
from app.agent.prompting import business_role_text, detect_mode

vector_svc = VectorService()

def smart_rag_node(state: AgentState):
    agent_logger.info("--- TIẾN HÀNH XỬ LÝ: SMART RAG NODE ---")

    # 1. Lấy thông tin đầu vào
    user_input = state["messages"][-1].content
    detected_mode = detect_mode(user_input)

    # 2. Truy xuất dữ liệu nội bộ (PDF)
    # k=4 để lấy đủ lượng thông tin cần thiết
    docs = vector_svc.get_relevant_docs(user_input, k=4)
    internal_context_text = truncate(format_pdf_chunks(docs), MAX_PDF_CHARS)

    # 3. Quyết định Search Web dựa trên logic mới trong grounding.py
    web_results: List[Dict] = []
    
    # Gọi hàm heuristic bạn vừa sửa ở file grounding.py
    if heuristic_need_web(user_input, internal_context_text):
        agent_logger.info(f"🌐 Kích hoạt Web Search cho câu hỏi: {user_input}")
        # Lấy kết quả từ Tavily (trả về list các dict có content và url)
        web_results = web_search_service.search_finance(user_input, max_results=3)
    
    # 4. Định dạng Context Web (Sử dụng hàm format_web_chunks đã có URL)
    web_context_text = truncate(format_web_chunks(web_results), MAX_WEB_CHARS)
    
    # Hợp nhất toàn bộ ngữ cảnh
    all_context_text = "\n\n".join([t for t in [internal_context_text, web_context_text] if t])

    # 5. Xây dựng Prompt để ép AI trích dẫn nguồn Web
    business_role = business_role_text(detected_mode)
    summary_text = state.get("summary") or "Chưa có hội thoại trước đó."

    prompt = f"""
{business_role}

HỆ THỐNG DỮ LIỆU HỖ TRỢ:
--- DỮ LIỆU NỘI BỘ (PDF): ---
{internal_context_text or "[Không tìm thấy thông tin trong file nội bộ]"}

--- DỮ LIỆU THỰC TẾ CẬP NHẬT: ---
{web_context_text or "[Không có dữ liệu bổ trợ]"}

QUY TẮC TRẢ LỜI:
1. TỔNG HỢP THÔNG TIN: Hãy kết hợp thông tin từ cả hai nguồn trên để đưa ra câu trả lời đầy đủ nhất cho khách hàng.
2. PHONG THÁI CHUYÊN GIA: Trả lời một cách tự nhiên, chuyên nghiệp. Không cần nêu rõ thông tin lấy từ nguồn nào (PDF hay Web), hãy trình bày như kiến thức của chính bạn.
3. TÍNH CHÍNH XÁC: Nếu cả hai nguồn đều không có số liệu cụ thể, hãy thông báo cho khách hàng và hướng dẫn họ kiểm tra tại quầy giao dịch, tuyệt đối không tự bịa số liệu.

Tóm tắt bối cảnh: {summary_text}
Câu hỏi của khách hàng: {user_input}
"""

    # 6. Gọi Model
    model = llm_service.get_model()
    try:
        response = model.invoke([HumanMessage(content=prompt)])
    except Exception as e:
        agent_logger.error(f"Lỗi gọi LLM: {str(e)}")
        response = AIMessage(content="⚠️ Hệ thống đang bận, vui lòng thử lại sau giây lát.")

    # 7. Cập nhật trạng thái
    return {
        "messages": [response],
        "context": [all_context_text],
        # Bạn có thể thêm hàm xử lý summary ở đây nếu muốn
    }