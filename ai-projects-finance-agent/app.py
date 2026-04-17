import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.nebius import Nebius
from agno.tools.yfinance import YFinanceTools
from agno.tools.duckduckgo import DuckDuckGoTools
import gradio as gr

# Load environment variables from .env file
load_dotenv()

# Create the AI finance agent
agent = Agent(
    name="AI Finance Agent",
    model=Nebius(
        id="meta-llama/Llama-3.3-70B-Instruct",
        api_key=os.getenv("NEBIUS_API_KEY")
    ),
    tools=[
        DuckDuckGoTools(),
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            stock_fundamentals=True
        )
    ],
    instructions=[
        "Always use tables to display financial/numerical data.",
        "For text data use bullet points and small paragraphs."
    ],
    show_tool_calls=True,
    markdown=True,
)

def respond(user_query: str) -> str:
    """Run the agent on the user's query and return markdown."""
    try:
        return agent.run(user_query)
    except Exception as e:
        return f"Error: {e}"

# Build a Gradio interface
interface = gr.Interface(
    fn=respond,
    inputs=gr.components.Textbox(lines=2, placeholder="Ask a finance question..."),
    outputs=gr.components.Markdown(),
    title="Finance Agent",
    description="Ask questions about stocks, analyst recommendations, fundamentals and recent news."
)

# If running locally (e.g., python app.py), launch Gradio
if __name__ == "__main__":
    interface.launch()
