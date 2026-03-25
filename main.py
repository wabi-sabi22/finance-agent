import gradio as gr
from app.agent.graph import finance_graph
from app.core.logger import agent_logger
from dotenv import load_dotenv

load_dotenv()

def predict(message, history):
    """
    Interface function to connect Gradio UI with LangGraph logic.
    """
    agent_logger.info(f"New User Request: {message}")
    
    try:
        # Define the initial state for the financial agent
        state = {
            "messages": [("user", message)],
            "context": [],
            "summary": None,
        }

        # Run the compiled LangGraph workflow
        result = finance_graph.invoke(state)
        
        # Extract the final answer from the AI
        final_response = result["messages"][-1].content
        agent_logger.info("Agent processed request successfully.")
        
        return final_response

    except Exception as e:
        agent_logger.error(f"System Error: {str(e)}")
        if "rate_limit_exceeded" in str(e).lower():
            return "âš ï¸ System is busy (Rate Limit). Please wait 10 seconds and try again."
        return f"âš ï¸ An unexpected error occurred: {str(e)}"

# Professional Chat Interface Setup
demo = gr.ChatInterface(
    fn=predict,
    title=" AI Finance Advisor ",
    description="Advanced RAG Agent for Banking & Investment (Vietcombank Data Focus).",
    examples=[
        "What is the annual fee for Visa Signature?",
        "Compare VCB savings interest rates with other banks today.",
        "Should I open a credit card or a savings account for long-term growth?"
    ],
)

if __name__ == "__main__":
    
    demo.launch(server_name="0.0.0.0", server_port=7860)
