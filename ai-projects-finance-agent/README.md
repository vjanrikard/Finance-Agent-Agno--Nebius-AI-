# 💰 Finance Agent (Agno + Nebius AI + Real-Time Market Data)

An intelligent AI-powered finance assistant that provides comprehensive market intelligence through natural language queries. Tracks live stock and cryptocurrency prices, analyzes analyst recommendations, delivers breaking financial news, and presents everything in clean, actionable formats. Built with Agno framework and Nebius AI Studio for professional-grade financial analysis.

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Agno](https://img.shields.io/badge/Agno-AI_Framework-green?style=for-the-badge)](https://github.com/agno-ai)
[![Nebius](https://img.shields.io/badge/Nebius-AI_Studio-blue?style=for-the-badge)](https://nebius.ai/)
[![Finance](https://img.shields.io/badge/Finance-Real_Time_Data-gold?style=for-the-badge&logo=yahoo&logoColor=white)](https://finance.yahoo.com/)

✨ **Features**

📈 **Real-Time Market Data**: Live stock and cryptocurrency prices with historical analysis and trend identification

🎯 **Analyst Intelligence**: Professional buy/sell/hold recommendations with target prices and sentiment analysis from top financial institutions

📰 **Breaking News Integration**: Latest financial headlines, earnings reports, and market-moving events with intelligent relevance scoring

🖥️ **Interactive Web Playground**: Live-updating Agno interface that visualizes agent reasoning and tool execution in real-time

📊 **Smart Data Visualization**: Structured tables for numerical data, formatted summaries, and comparative analysis with professional presentation

🧠 **Natural Language Processing**: Ask complex financial questions in plain English and receive institutional-quality analysis

🗂️ **Project structure**
```
.
├─ app.py             # Web UI and application wiring logic
├─ main.py            # Local agent runner and entry point
├─ .env.example       # Environment variable template for API keys
├─ requirements.txt   # Python dependencies and package versions
└─ README.md          # Comprehensive project documentation
```

🚀 **Quickstart**

**Prerequisites**
- Python 3.10 or higher
- **NEBIUS_API_KEY** (Nebius AI Studio access)

**1) Clone & install**
```bash
git clone https://github.com/AbdullahRasheed45/ai-projects-finance-agent.git
cd ai-projects-finance-agent

# Install dependencies
pip install -r requirements.txt
```

**2) Configure environment**
```bash
# Create environment file
cp .env.example .env

# Edit .env with your API key:
NEBIUS_API_KEY=your_nebius_api_key_here
```

**3) Run the agent**
```bash
python main.py
```

🌐 **Access**: Navigate to `http://localhost:8000` for the interactive web playground with live agent visualization.

🧠 **How it works (financial intelligence)**

**1. Query Understanding**: Advanced NLP processes complex financial questions and identifies required data types (prices, analysis, news)

**2. Multi-Tool Orchestration**: Intelligent tool selection and execution:
   - **Market Data Tools**: Real-time and historical price fetching
   - **Analysis Tools**: Professional recommendation aggregation  
   - **News Tools**: Relevant headline discovery and summarization

**3. Data Integration**: Synthesizes information from multiple financial sources into coherent, actionable insights

**4. Professional Formatting**: Presents data in institutional-quality tables, charts, and summaries optimized for financial decision-making

💡 **Example queries & capabilities**

**Real-Time Market Analysis**:
- *"What's the current price of AAPL and how has it performed this week?"*
- *"Show me Tesla's stock price with 5-day moving average"*
- *"Get Bitcoin's price in USD and compare to Ethereum"*

**Professional Investment Research**:
- *"Show me analyst recommendations for TSLA with target prices"*
- *"What do Wall Street analysts think about Microsoft's outlook?"*
- *"Compare buy/sell ratings for GOOGL vs AMZN"*

**Market Intelligence & News**:
- *"Get the latest news about Bitcoin and crypto regulations"*
- *"What are the recent headlines affecting Apple stock?"*
- *"Show me breaking news for renewable energy sector"*

**Comparative Analysis**:
- *"Compare Google and Amazon performance over the last month"*
- *"Which performed better: tech stocks or financial stocks this quarter?"*
- *"Show me FAANG stocks price comparison year-to-date"*

**Sector & Market Overview**:
- *"What's happening in the semiconductor industry today?"*
- *"Give me an overview of cryptocurrency market sentiment"*
- *"How are banking stocks performing after the Fed announcement?"*

📊 **Output formats & data presentation**

**Price Data Tables**:
```
┌─────────────┬──────────────┬─────────────┬──────────────┬─────────────┐
│ Ticker      │ Price        │ Change      │ Change %     │ Volume      │
├─────────────┼──────────────┼─────────────┼──────────────┼─────────────┤
│ AAPL        │ $184.52      │ +$2.34      │ +1.29%       │ 45.2M       │
│ TSLA        │ $248.87      │ -$3.21      │ -1.27%       │ 67.8M       │
│ NVDA        │ $461.23      │ +$12.45     │ +2.78%       │ 34.5M       │
└─────────────┴──────────────┴─────────────┴──────────────┴─────────────┘
```

**Analyst Recommendations**:
```
📈 AAPL - Apple Inc.
• Strong Buy (12 analysts) | Buy (8) | Hold (3) | Sell (0)
• Average Target: $195.50 (+5.95% upside)
• Key Catalysts: iPhone 15 cycle, Services growth, AI integration
```

**News Digest**:
```
🗞️ Latest TSLA News:
• "Tesla Delivers Record Q3 Results, Beats Estimates" - Reuters (2h ago)
• "Musk Announces New Gigafactory Plans for 2024" - Bloomberg (4h ago)  
• "Tesla Stock Upgraded by Goldman Sachs" - CNBC (1d ago)
```

⚙️ **Advanced configuration**

**Model Selection & Performance**:
```python
# Configure Nebius AI models for different use cases
MODELS = {
    'fast': 'llama-3-8b-instruct',      # Quick market updates
    'balanced': 'llama-3-70b-instruct', # Standard analysis
    'premium': 'llama-3.3-70b-instruct' # Complex financial modeling
}
```

**Market Data Customization**:
```python
# Customize data fetching parameters
MARKET_CONFIG = {
    'default_period': '5d',           # Default historical data range
    'update_interval': '1m',          # Real-time update frequency
    'extended_hours': True,           # Include pre/post market data
    'currency_conversion': 'USD',     # Base currency for comparisons
    'volume_threshold': 100000        # Minimum volume for recommendations
}
```

**News & Analysis Settings**:
```python
# Configure news sources and analysis depth
NEWS_CONFIG = {
    'sources': ['reuters', 'bloomberg', 'cnbc', 'marketwatch'],
    'relevance_threshold': 0.7,       # News relevance scoring
    'max_articles': 10,               # Articles per query
    'sentiment_analysis': True,       # Include sentiment scoring
    'time_window': '24h'              # News recency filter
}
```

**Output Formatting**:
```python
# Customize data presentation
DISPLAY_CONFIG = {
    'decimal_places': 2,              # Price precision
    'percentage_format': True,        # Show % changes
    'color_coding': True,             # Green/red for gains/losses
    'table_style': 'professional',   # Formatting theme
    'include_charts': False           # ASCII chart generation
}
```

🔧 **Tool integration & extensibility**

**Market Data Sources**:
- **Yahoo Finance**: Real-time quotes, historical data, company fundamentals
- **Alpha Vantage**: Technical indicators, forex rates, commodity prices
- **CoinGecko**: Cryptocurrency data, market cap rankings, DeFi metrics
- **Financial Modeling Prep**: Professional financial statements, ratios

**News & Analysis Providers**:
- **DuckDuckGo News**: Unbiased headline aggregation
- **Reuters/Bloomberg APIs**: Premium financial journalism
- **SEC EDGAR**: Official company filings and regulatory documents
- **Social Sentiment**: Twitter/Reddit market sentiment analysis

**Custom Tool Development**:
```python
# Add specialized financial tools
def options_analysis_tool(ticker: str, expiry: str) -> dict:
    """Analyze options chain for given ticker and expiry"""
    return fetch_options_data(ticker, expiry)

def earnings_calendar_tool(timeframe: str = 'week') -> list:
    """Get upcoming earnings announcements"""
    return fetch_earnings_calendar(timeframe)

def insider_trading_tool(ticker: str) -> list:
    """Track insider buying/selling activity"""
    return fetch_insider_transactions(ticker)
```

📈 **Typical analysis workflows**

**Daily Market Monitoring**:
1. **Portfolio Check** → Agent fetches current positions and performance
2. **News Scan** → Identifies relevant headlines affecting holdings
3. **Alert Generation** → Flags significant price movements or news events
4. **Summary Report** → Comprehensive daily market update

**Investment Research Process**:
1. **Fundamental Analysis** → Retrieves key financial metrics and ratios
2. **Technical Analysis** → Analyzes price trends and trading patterns  
3. **Analyst Consensus** → Aggregates professional recommendations
4. **Risk Assessment** → Evaluates volatility and downside protection
5. **Investment Thesis** → Synthesizes analysis into actionable insights

**Market Event Tracking**:
1. **Event Identification** → Monitors earnings, announcements, economic data
2. **Impact Analysis** → Assesses potential market effects
3. **Sector Implications** → Evaluates broader industry impacts
4. **Trading Opportunities** → Identifies potential profit scenarios

🔒 **Security & compliance**

**Data Privacy & Protection**:
- Secure API key management with environment variable isolation
- No storage of personal financial information or trading positions
- Encrypted communication with all financial data providers
- Regular security audits and dependency updates

**Financial Compliance**:
- **Educational Purpose Disclaimer**: All outputs clearly marked as informational only
- **Not Financial Advice**: Explicit warnings about professional consultation requirements
- **Data Source Attribution**: Transparent sourcing of all financial information
- **Rate Limiting**: Respectful API usage within provider terms of service

**Risk Management**:
```python
# Implement safeguards for financial data
RISK_CONTROLS = {
    'max_position_size': None,        # No position recommendations
    'disclaimer_required': True,      # Always show risk warnings
    'data_verification': True,        # Cross-check multiple sources
    'update_timestamps': True,        # Show data freshness
    'source_transparency': True       # Always cite data sources
}
```

🐛 **Troubleshooting & optimization**

**Common Issues & Solutions**:

**Authentication & API Problems**:
- **"NEBIUS_API_KEY Missing"** → Verify `.env` file exists and key is correctly formatted
- **"Rate Limited"** → Implement delays between requests or upgrade API plan
- **"Invalid Ticker Symbol"** → Add symbol validation and suggestion system

**Performance Optimization**:
- **Slow Market Data** → Switch to faster data providers or cache recent results
- **Memory Usage** → Limit historical data ranges for large dataset queries  
- **Response Time** → Use faster Nebius models for real-time price queries

**Data Quality Issues**:
- **Stale Prices** → Verify market hours and data source freshness
- **Missing Fundamentals** → Check ticker symbol accuracy and company coverage
- **Inconsistent News** → Implement relevance scoring and duplicate detection

**Web Interface Problems**:
- **UI Not Loading** → Verify port availability (default: 8000) and firewall settings
- **Real-Time Updates** → Check WebSocket connections and browser compatibility
- **Display Formatting** → Clear browser cache and check CSS/JavaScript loading

🚀 **Advanced features & extensions**

**Portfolio Management Integration**:
```python
# Connect to brokerage APIs for live portfolio tracking
def portfolio_performance_tool() -> dict:
    """Track real portfolio performance and allocations"""
    return {
        'total_value': get_portfolio_value(),
        'daily_pnl': calculate_daily_pnl(),
        'top_performers': get_best_positions(),
        'risk_metrics': calculate_portfolio_risk()
    }
```

**Algorithmic Trading Signals**:
```python
# Generate trading signals based on analysis
def trading_signal_tool(ticker: str, strategy: str) -> dict:
    """Generate buy/sell signals using technical analysis"""
    return {
        'signal': determine_signal(ticker, strategy),
        'confidence': calculate_confidence_score(),
        'entry_price': suggest_entry_price(),
        'risk_level': assess_position_risk()
    }
```

**Economic Calendar Integration**:
```python
# Track macroeconomic events affecting markets
def economic_events_tool(timeframe: str = 'week') -> list:
    """Get upcoming economic announcements and Fed events"""
    return fetch_economic_calendar(timeframe)
```

☁️ **Deployment & scaling**

**Local Development**:
```bash
# Development mode with debug logging
export DEBUG=true
export LOG_LEVEL=debug
python main.py --dev
```

**Production Deployment**:
- **AWS/GCP/Azure**: Enterprise deployment with auto-scaling and load balancing
- **Docker Container**: Containerized deployment with environment variable injection
- **Kubernetes**: Orchestrated deployment with high availability and monitoring

**Performance Monitoring**:
```python
# Add monitoring and analytics
MONITORING_CONFIG = {
    'response_time_tracking': True,
    'api_usage_analytics': True,
    'error_rate_monitoring': True,
    'user_query_patterns': True,
    'data_source_reliability': True
}
```

**Enterprise Integration**:
```python
# API wrapper for enterprise systems
from fastapi import FastAPI
from finance_agent import FinanceAgent

app = FastAPI()
agent = FinanceAgent()

@app.post("/market-analysis")
async def analyze_market(request: AnalysisRequest):
    return await agent.comprehensive_analysis(request.symbols)

@app.get("/portfolio-summary")  
async def portfolio_summary(user_id: str):
    return await agent.generate_portfolio_report(user_id)
```

📚 **Educational resources & learning**

**Financial Concepts Covered**:
- **Technical Analysis**: Moving averages, RSI, MACD, Bollinger Bands
- **Fundamental Analysis**: P/E ratios, revenue growth, debt levels
- **Market Sentiment**: News sentiment, analyst consensus, insider activity
- **Risk Management**: Volatility metrics, correlation analysis, diversification

**AI & Finance Applications**:
- **Natural Language Processing** for financial text analysis
- **Machine Learning** for pattern recognition in market data  
- **Agent Architecture** for complex financial workflow automation
- **Real-Time Systems** for market data processing and alerts

**Professional Development**:
- Foundation for fintech application development
- Introduction to algorithmic trading concepts
- Market data API integration patterns
- Financial compliance and risk management principles

⚠️ **Important disclaimers**

**Educational Purpose**: This project is designed for educational and demonstration purposes only. It is **NOT financial advice**.

**Risk Warning**: All financial investments carry risk. Past performance does not guarantee future results. Always consult with qualified financial professionals before making investment decisions.

**Data Accuracy**: While we strive for accuracy, market data may be delayed or contain errors. Always verify critical information with official sources before acting.

**Regulatory Compliance**: Users are responsible for complying with local financial regulations and licensing requirements when using this tool professionally.

📜 **License**

MIT License - see [LICENSE](LICENSE) file for complete terms. Part of the "Awesome AI Apps" collection.

## 📞 Connect & Support

<div align="center">

### 🚀 Ready to Build Intelligent Finance Applications?

[![Portfolio](https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&logo=About.me&logoColor=white)](https://techvibes360.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/abdullahrasheed-/)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:abdullahrasheed45@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/AbdullahRasheed45)

**Let's revolutionize financial intelligence with AI!**

</div>

---

*Built with ❤️ using cutting-edge AI and financial data technologies. Perfect for learning fintech development and building intelligent market analysis applications.*
