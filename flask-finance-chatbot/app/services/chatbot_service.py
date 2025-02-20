from app.services.openai_service import OpenAIService
from app.utils.constants import (
    FINANCE_TOPICS, 
    IDENTITY_KEYWORDS, 
    THANK_YOU_KEYWORDS,
    IDENTITY_RESPONSE, 
    NON_FINANCE_RESPONSE,
    THANK_YOU_RESPONSE
)
from app.utils.error_handlers import ValidationError, OpenAIError

class ChatbotService:
    """Service for handling chat interactions"""
    
    def __init__(self):
        self.openai_service = OpenAIService()

    def is_finance_question(self, prompt: str) -> bool:
        """Check if the user question is related to personal finance."""
        prompt_lower = prompt.lower()
        return any(topic in prompt_lower for topic in FINANCE_TOPICS)

    def is_identity_question(self, prompt: str) -> bool:
        """Check if the question is about the chatbot's identity."""
        prompt_lower = prompt.lower()
        return any(keyword in prompt_lower for keyword in IDENTITY_KEYWORDS)

    def is_thank_you_message(self, prompt: str) -> bool:
        """Check if the message is a thank you message."""
        prompt_lower = prompt.lower()
        return any(keyword in prompt_lower for keyword in THANK_YOU_KEYWORDS)

    def generate_response(self, user_message: str) -> str:
        """Generate a response to the user's message"""
        try:
            # Check if it's a thank you message first
            if self.is_thank_you_message(user_message):
                return THANK_YOU_RESPONSE

            # Check if it's an identity question
            if self.is_identity_question(user_message):
                return IDENTITY_RESPONSE
            
            # Check if it's a finance-related question
            if not self.is_finance_question(user_message):
                return NON_FINANCE_RESPONSE
                
            # For finance questions, use OpenAI
            response = self.openai_service.generate_completion(user_message)
            return response
        except Exception as e:
            # Re-raise the exception to be handled by the route error handlers
            raise e 