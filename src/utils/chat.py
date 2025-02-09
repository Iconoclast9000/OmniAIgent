"""
Chat interface module for OmniAIgent with code generation support
"""

from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import os

SYSTEM_PROMPT = """
You are a filesystem and code generation assistant that helps users manage their files and write code.
You must interpret user requests and convert them into specific filesystem commands.

For file operations, use these exact command formats:
- CREATE FILE: "create file <filename>"
- WRITE CODE: "write <type> game code to <filename>"
- WRITE TO FILE: "write <content> to <filename>"
- READ FILE: "read file <filename>"
- DELETE FILE: "delete <filename>"
- LIST FILES: "list files"
- MOVE FILE: "move <source> to <destination>"
- COPY FILE: "copy <source> to <destination>"
- CREATE DIRECTORY: "create directory <dirname>"
- CHANGE DIRECTORY: "cd <path>"

Examples of valid commands:
User: "Create a new Python file called game.py"
Assistant: I'll help you create that file.
Command: create file game.py

User: "Write a basic snake game"
Assistant: I'll help you create a snake game.
Command: write snake game code to snake.py

Current working directory: {cwd}
Previous operations: {context}

User request: {question}

Convert the user's request into the appropriate filesystem command.
Always respond with "Command: <command>" followed by a brief explanation.
"""

def initialize_model(model_name="deepseek-r1:1.5b"):
    """Initialize the language model"""
    return OllamaLLM(model=model_name)

def load_history(filename="conversation_history.txt"):
    """Load conversation history from file"""
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    return ""

def save_history(context, filename="conversation_history.txt"):
    """Save conversation history to file"""
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(context)
        print(f"Conversation history saved to '{filename}'.")
    except Exception as e:
        print("Failed to save conversation history.")
        print("Error: ", e)