from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import os

SYSTEM_PROMPT = """
You are a filesystem and code generation assistant that helps users manage their files and write code.
You must interpret user requests and convert them into specific filesystem commands.

For file operations, use these exact command formats:
- GENERATE CODE: "generate <description> in <language>"
- CREATE FILE: "create file <filename>"
- WRITE CODE: "write <description> to <filename>"
- READ FILE: "read file <filename>"
- DELETE/REMOVE: "delete <filename>" or "remove <filename>"
- LIST/SHOW: "list" or "show"
- MOVE/RENAME: "move <source> to <destination>" or "rename <source> to <destination>"
- COPY: "copy <source> to <destination>"
- CREATE DIRECTORY: "create directory <dirname>"
- CHANGE DIRECTORY: "cd <path>" or "change directory <path>"
- PWD: "pwd" or "current directory"

Examples of valid commands:
User: "Generate a snake game with multiplayer support"
Assistant: I'll help you generate that game.
Command: generate a snake game with multiplayer support in python

User: "Create a web scraper in JavaScript"
Assistant: I'll help you create a web scraper.
Command: generate a web scraper application in javascript

User: "Write a neural network implementation"
Assistant: I'll help you create a neural network implementation.
Command: write neural network implementation to nn.py

Current working directory: {cwd}
Previous operations: {context}

User request: {question}

Convert the user's request into the appropriate filesystem command.
Always respond with "Command: <command>" followed by a brief explanation.
"""

def initialize_model(model_name="deepseek-r1:1.5b"):
    """Initialize the language model."""
    return OllamaLLM(model=model_name)

def load_history(filename="conversation_history.txt"):
    """Load conversation history from file."""
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    return ""

def save_history(context, filename="conversation_history.txt"):
    """Save conversation history to file."""
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(context)
        print(f"Conversation history saved to '{filename}'.")
    except Exception as e:
        print("Failed to save conversation history.")
        print("Error: ", e)