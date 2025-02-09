"""
OmniAIgent - A conversational filesystem manager with code generation capabilities
"""

from src.utils.filesystem import FileSystemManager
from src.utils.chat import (
    initialize_model,
    load_history,
    save_history,
    SYSTEM_PROMPT,
)
from langchain_core.prompts import ChatPromptTemplate

def handle_conversation():
    """Main conversation handler"""
    context = load_history()
    fs_manager = FileSystemManager()
    print(
        "Welcome to OmniAIgent! Type 'exit' to quit or 'help' for commands."
    )

    model = initialize_model()
    prompt = ChatPromptTemplate.from_template(SYSTEM_PROMPT)
    chain = prompt | model

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            print("Goodbye!")
            save_history(context)
            break
        elif user_input.lower() == "help":
            print(
                """
Available commands:
- list/show: List directory contents
- create directory <name>: Create a new directory
- create file <name>: Create a new file
- delete/remove <name>: Delete file or directory
- read/cat <file>: Show file contents
- write <content> to <file>: Write to file
- write <type> game code to <file>: Write game code
- move/rename <source> to <destination>
- copy <source> to <destination>
- cd/change directory <path>: Change directory
- pwd/current directory: Show current path
            """
            )
            continue

        try:
            # Get filesystem operation result
            fs_result = fs_manager.execute_command(user_input)

            # Invoke the model with current context and filesystem result
            result = chain.invoke(
                {
                    "context": context,
                    "question": user_input,
                    "cwd": str(fs_manager.current_path),
                }
            )

            # Combine AI response with filesystem operation result
            response = f"{fs_result}\n\nAI: {result}"
            print("Result:", response)

            # Update context
            context += f"\nUser: {user_input}\nSystem: {fs_result}\nAI: {result}"

            # Limit context size
            if len(context.split()) > 1000:
                context = "\n".join(context.split("\n")[-10:])

        except Exception as e:
            print("Error occurred:", e)

if __name__ == "__main__":
    handle_conversation()