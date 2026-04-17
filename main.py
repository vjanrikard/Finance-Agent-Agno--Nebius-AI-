# import necessary python libraries
import sys
from agno.agent import Agent
from agno.models.nebius import Nebius
from agno.tools.yfinance import YFinanceTools
from agno.tools.duckduckgo import DuckDuckGoTools
import os
from pathlib import Path
from dotenv import load_dotenv
# Load environment variables from secure location outside project
load_dotenv(Path.home() / "OneDrive" / "Secrets" / "NEBIUS_API_KEY.env")
# create the AI finance agent
agent = Agent(
    name="xAI Finance Agent",
    model=Nebius(
            id="meta-llama/Llama-3.3-70B-Instruct",
            api_key=os.getenv("NEBIUS_API_KEY")
    ),
    tools=[
        DuckDuckGoTools(),
        YFinanceTools(
            enable_stock_price=True,
            enable_analyst_recommendations=True,
            enable_stock_fundamentals=True,
        ),
    ],
    instructions = ["Always use tables to display financial/numerical data. For text data use bullet points and small paragrpahs."],
    markdown = True,
    )

def main() -> int:
    user_query = " ".join(sys.argv[1:]).strip()
    if not user_query:
        user_query = input("Ask a finance question: ").strip()

    if not user_query:
        print("No question provided.")
        return 1

    try:
        response = agent.run(user_query)
        print(response.content)
        return 0
    except Exception as exc:
        print(f"Error: {exc}")
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
