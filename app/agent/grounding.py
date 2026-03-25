from typing import List, Dict, Any, Optional
import re
import unicodedata

# Cấu hình giới hạn ký tự để tránh tràn ngữ cảnh (Token limit)
MAX_PDF_CHARS = 5000
MAX_WEB_CHARS = 2500

def normalize_text(s: str) -> str:
    """Chuyển đổi văn bản thành chữ thường và loại bỏ dấu tiếng Việt để so sánh chính xác."""
    s = s or ""
    s = s.lower()
    s = unicodedata.normalize("NFD", s)
    return "".join(ch for ch in s if unicodedata.category(ch) != "Mn")

def truncate(s: str, max_chars: int) -> str:
    """Cắt bớt văn bản nếu quá dài."""
    s = s or ""
    if len(s) <= max_chars:
        return s
    return s[:max_chars] + "\n...[DỮ LIỆU BỊ CẮT BỚT DO QUÁ DÀI]..."

def heuristic_need_web(question: str, internal_context_text: str) -> bool:
    """
    Hàm quyết định khi nào cần tìm kiếm Web.
    Logic: Nếu dữ liệu nội bộ thiếu hoặc câu hỏi mang tính thời sự/so sánh -> Search Web.
    """
    q = normalize_text(question)
    ctx = internal_context_text.strip()
    
    
    # Nếu PDF trả về dưới 500 ký tự, mặc định là không đủ thông tin.
    if len(ctx) < 500:
        return True

    # 2. KIỂM TRA TỪ KHÓA: Nếu hỏi về các ngân hàng khác (PDF thường chỉ có Vietcombank)
    competitors = [
        "bidv", "agribank", "vietinbank", "techcombank", "acb", "tpbank", 
        "sacombank", "mbbank", "hdbank", "vpbank", "shb", "vib", "scb"
    ]
    if any(c in q for c in competitors):
        return True

    # 3. KIỂM TRA TÍNH THỜI SỰ: Nếu hỏi về năm 2026 hoặc dữ liệu "mới nhất"
    realtime_keywords = ["hien tai", "hom nay", "moi nhat", "2025", "2026", "cap nhat", "update"]
    if any(r in q for r in realtime_keywords):
        return True

    # 4. KIỂM TRA SO SÁNH: Các câu hỏi so sánh luôn cần dữ liệu rộng từ Web
    compare_keywords = ["so sanh", "khac gi", "tot hon", "ben nao", "uu dai hon"]
    if any(k in q for k in compare_keywords):
        return True
        
    # 5. KIỂM TRA NỘI DUNG PDF: Nếu trong PDF chứa các cụm từ báo thiếu thông tin
    negative_keywords = ["khong co thong tin", "khong tim thay", "chua duoc cap nhat"]
    if any(n in ctx.lower() for n in negative_keywords):
        return True

    return False

def format_pdf_chunks(docs: list[Any]) -> str:
    """Định dạng các đoạn văn bản trích xuất từ file PDF."""
    formatted: List[str] = []
    for i, d in enumerate(docs):
        meta = getattr(d, "metadata", {}) or {}
        source = meta.get("source", "Nội bộ")
        page = meta.get("page", "?")
        
        chunk_text = getattr(d, "page_content", "") or ""
        formatted.append(f"[NGUỒN PDF - Trang {page}]\nNội dung: {chunk_text}".strip())
    return "\n\n".join(formatted)

def format_web_chunks(web_results: List[dict]) -> str:
    if not web_results:
        return ""
        
    formatted: List[str] = []
    for i, res in enumerate(web_results):
        content = res.get("content", "")
        formatted.append(
            f"--- KẾT QUẢ WEB {i+1} ---\n"
            f"NỘI DUNG: {content}"
        )
    return "\n\n".join(formatted)