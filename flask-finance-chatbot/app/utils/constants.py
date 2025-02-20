# Finance-related topics for validation
FINANCE_TOPICS = [
    "savings", "saving", "budget", "budgeting", "invest", "investing", "investments", 
    "stocks", "mutual funds", "retirement", "financial planning", "credit score", 
    "cryptocurrency", "insurance", "real estate", "taxes", "income", "expenses", 
    "debt", "interest rates", "mortgage", "financial goals", "money", "banking",
    "loan", "credit card", "portfolio", "dividend", "bond", "etf", "fund",
    "financial", "finance", "bank", "investment", "market", "trading", "trade",
    "401k", "ira", "roth", "pension", "asset", "liability", "net worth",
    "compound interest", "diversification", "risk management", "emergency fund", "credit score"
]

# Identity-related keywords
IDENTITY_KEYWORDS = [
    "who are you", "what are you", "your name", 
    "who you are", "tell me about yourself"
]

# Thank you related keywords
THANK_YOU_KEYWORDS = [
    "thank you", "thanks", "thank u", "thx", "tysm", "ty"
]

# Response Messages
IDENTITY_RESPONSE = """I am your AI Financial Advisor developed by Kevin Gomez powered with OpenAI, which is designed and focused for personal finance topics \
including savings, investments, budgeting, and more. How can I assist you with your financial questions today?"""

NON_FINANCE_RESPONSE = """I can only provide advice related to personal finance. Please ask about savings, investments, \
budgeting, or similar topics."""

THANK_YOU_RESPONSE = """Thank you for using AI Financial Advisor! Have a great day, and feel free to return anytime for more financial guidance."""

ERROR_MESSAGES = {
    "empty_message": "Message cannot be empty",
    "invalid_json": "Invalid JSON",
    "general_error": "An error occurred while processing your request"
} 