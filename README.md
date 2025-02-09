# OmniAIgent

A powerful AI-driven chat interface that implements filesystem operations and code generation through natural language processing.

## Features

- Natural language file operations
- Code generation capabilities
- Intuitive chat interface
- Built-in game templates
- File and directory management
- Conversation history tracking

## Project Structure

```
OmniAIgent/
├── src/                    # Source code directory
│   ├── __init__.py        # Package initialization
│   └── utils/             # Utility modules
│       ├── chat.py        # Chat interface implementation
│       └── filesystem.py  # Filesystem operations
├── workspace/             # Working directory for file operations
│   └── snake.py          # Generated snake game
├── .venv/                # Virtual environment
├── omniagent.py         # Main application entry point
├── README.md            # Documentation
└── requirements.txt     # Project dependencies
```

## Installation

1. Clone the repository:
   ```bash
   git clone [repository-url]
   cd OmniAIgent
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On Linux/Mac:
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Install Ollama:
   - Visit https://ollama.ai/download
   - Download and install for your operating system

5. Pull required model:
   ```bash
   ollama pull deepseek-r1:1.5b
   ```

## Usage

1. Start the application:
   ```bash
   python omniagent.py
   ```

2. Available commands:
   - List files: `list files`
   - Create file: `create file <name>`
   - Write to file: `write <content> to <file>`
   - Read file: `read file <name>`
   - Delete file: `delete <name>`
   - Create directory: `create directory <name>`
   - Change directory: `cd <path>`
   - Move file: `move <source> to <destination>`
   - Copy file: `copy <source> to <destination>`

3. Code Generation Examples:
   ```
   # Create a snake game
   create file snake.py
   write snake game code to snake.py
   
   # Read the generated code
   read file snake.py
   ```

## Components

### Chat Interface (chat.py)
- Handles natural language processing
- Manages conversation history
- Interprets user commands
- Uses Ollama language model

### Filesystem Manager (filesystem.py)
- Implements file operations
- Handles code templates
- Manages working directory
- Provides error handling

### Code Templates
Currently supported templates:
- Snake Game (Pygame implementation)
- More templates coming soon!

## Dependencies

- langchain-ollama==0.1.3
- langchain-core==0.1.17
- python-dotenv==1.0.0
- requests==2.31.0
- pygame (for running generated games)

## Examples

1. Create and run a snake game:
   ```
   You: create file snake.py
   Result: Created file: snake.py

   You: write snake game code to snake.py
   Result: Created snake.py with snake_game template

   You: read file snake.py
   Result: [Snake game code will be displayed]
   ```

2. Manage files:
   ```
   You: list files
   Result: 📄 snake.py - 3299B - 2025-02-09 09:50
   ```

## Future Enhancements

- Additional game templates
- More code generation capabilities
- Enhanced natural language understanding
- Project template generation
- Multi-file operations
- Code analysis and suggestions

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License.

## Support

For support, please open an issue in the GitHub repository or contact the maintainers directly."# OmniAIgent" 
