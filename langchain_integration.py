import getpass
import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate


# Load environment variables
load_dotenv()

class LangchainModel:
    def __init__(self, bot_name):
        self.authenticate()
        self.bot_name = bot_name
        self.model = init_chat_model("llama3-8b-8192", model_provider="groq")
        self.system_prompt = f"You are {self.bot_name} a friendly, helpful, and cheerful assistant. Try to be brief in your responses."

    def authenticate(self):
        if not os.environ.get("GROQ_API_KEY"):
            os.environ["GROQ_API_KEY"] = getpass.getpass("Enter API key for Groq: ")

    def reply(self, user_message: str) -> str:
        try:
            # Define the system prompt (sets the behavior of the assistant)
            system = self.system_prompt

            # Define the human message (the user's input)
            human = user_message

            # Create the prompt template using both system and human messages
            prompt = ChatPromptTemplate.from_messages([("system", system), ("human", human)])

            # Pass the system and user messages through the model
            chain = prompt | self.model
            response = chain.invoke({"text": user_message})

            return response.content
        except Exception as e:
            return f"Error: {e}"







