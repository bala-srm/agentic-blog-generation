from langchain_groq import ChatGroq
from pydantic import SecretStr
from dotenv import load_dotenv
import os


class GroqLLM:
    def __init__(self):
        load_dotenv()

    def get_llm(self):
        """
        Initialize and return the Groq LLM.
        
        Returns: ChatGroq: An instance of the ChatGroq LLM.
        """
        # Read the GROQ_API_KEY from the .env file (loaded in __init__ via load_dotenv())
        self.groq_api_key = os.getenv("GROQ_API_KEY")

        # If the key was found, explicitly set it in os.environ so any library
        # that reads the environment directly can also access it
        if self.groq_api_key is not None:
            os.environ["GROQ_API_KEY"] = self.groq_api_key

        # Create the ChatGroq LLM instance using the specified model
        llm = ChatGroq(
            model="llama-3.1-8b-instant",   # The Groq-hosted Llama 3.1 8B model
            # SecretStr wraps the raw string so Pydantic/LangChain treats it as
            # sensitive data — it won't be accidentally printed or logged in plain text.
            # The conditional passes None if no key was found, letting ChatGroq
            # fall back to its own environment-variable lookup.
            api_key=SecretStr(self.groq_api_key) if self.groq_api_key is not None else None
        )
        return llm  # Return the ready-to-use LLM object
    
