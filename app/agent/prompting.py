from typing import Literal


def detect_mode(user_input: str) -> str:
    text = (user_input or "").lower()
    if any(k in text for k in ["gửi tiết kiệm", "tiết kiệm", "lãi suất", "sổ tiết kiệm"]):
        return "savings"
    if any(k in text for k in ["thẻ tín dụng", "credit card"]):
        return "credit_card"
    if any(k in text for k in ["vay mua nhà", "vay tiêu dùng", "vay vốn", "khoản vay"]):
        return "loan"
    return "general"


def business_role_text(mode: str) -> str:
    if mode == "savings":
        return (
            "You are acting as a savings and bank interest rate consultant. "
            "Focus on comparing terms, interest rates, pros and cons of each deposit option."
        )
    if mode == "credit_card":
        return (
            "You are acting as a credit card consultant. "
            "Focus on analyzing incentives, annual fees, eligibility, and bad debt risks."
        )
    if mode == "loan":
        return (
            "You are acting as a loan consultant (personal loans, mortgages). "
            "Focus on explaining interest rates, loan terms, Loan-to-Value (LTV) ratios, and risks."
        )
    return (
        "You are a banking financial consultant in Vietnam in 2026, "
        "explaining concepts clearly for general customers."
    )


def build_generation_prompt(
    *,
    business_role: str,
    internal_context_text: str,
    web_context_text: str,
    summary_text: str,
    user_input: str,
) -> str:
    prompt = f"""
{business_role}

GROUNDING INFORMATION:
- PDF SECTION (Internal):
{internal_context_text or "[Empty: No relevant PDF chunks found]"}
- WEB SECTION (If search permitted):
{web_context_text or "[No web content available]"}

MANDATORY RULES (STRICT COMPLIANCE):
1) Do not hallucinate. Every "factual" assertion requiring specific data (numbers, %, age, LTV ratio, debt-to-income ratio, bank-specific rates, timelines, document requirements...) MUST appear in the PDF SECTION or WEB SECTION above.
2) If the PDF/WEB SECTION does not contain the necessary information, state clearly: "The documents do not specify" or "Information not found in available documents/web content". Do not invent numbers or terms.
3) Integrate information from both sections seamlessly into a single professional response without mentioning the data source.
4) When providing numerical examples: if actual data is missing from PDF/WEB, use a hypothetical example and clearly mark it as a "hypothetical example (does not reflect actual interest rates/fees)".

Conversation Summary (if any):
{summary_text or "[No summary available.]"}

Customer Question:
{user_input}

RESPONSE REQUIREMENTS:
- Explain clearly, step-by-step, avoiding difficult technical jargon.
- Always provide reasons for recommendations (pros/cons).
- If appropriate, compare 2-3 options using bullet points (compare terms, rates, costs, risks).
- Add 1-2 numerical examples (e.g., interest payable, savings accumulated over time).
- If "real-time" data is needed (current rates, new fee schedules...), only provide if it exists in the WEB SECTION; otherwise, state "Documents do not specify, please check the latest rates at the bank".
""".strip("\n")

    return prompt