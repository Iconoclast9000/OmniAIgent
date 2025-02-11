# OmnitrAIce

OmnitrAIce is an AI-powered code generation and file management system that combines intelligent code generation with robust filesystem operations. It uses the DeepSeek language model to generate clean, production-ready code in multiple programming languages.

## Features

### Code Generation
- Dynamic code generation for multiple programming languages
- Automatic code cleaning and formatting
- Support for various project types (games, apps, utilities)
- Intelligent file naming and organization
- Clean code output without explanatory text or artifacts

### File Management
- Create, read, update, and delete files and directories
- Move and copy operations
- Directory navigation and listing
- UTF-8 support for all file operations
- Detailed file information display

### Supported Languages
- Python
- JavaScript
- TypeScript
- Java
- C++
- C
- Rust
- Go
- Ruby
- PHP
- Swift
- Kotlin
- Scala
- HTML
- CSS

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/OmnitrAIce.git
cd OmnitrAIce
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
pipvinstall langchain-ollama ollama
```

## Usage

Start the application:
```bash
python omniagent.py
```

### Common Commands

1. Generate Code:
```
generate a calculator in javascript
generate a web server in python
generate a todo app in typescript
```

2. File Operations:
```
list                          # List directory contents
create directory projectname  # Create a new directory
create file example.txt       # Create a new file
read file example.txt        # Show file contents
delete file example.txt      # Delete a file
cd foldername               # Change directory
```

## Project Structure

```
OmnitrAIce/
├── src/
│   └── utils/
│       ├── filesystem.py    # Core file system operations
│       ├── code_cleaner.py  # Code cleaning utilities
│       └── chat.py         # Chat interface and prompt handling
├── workspace/              # Generated code directory
├── omniagent.py           # Main application entry point
├── requirements.txt       # Project dependencies
└── README.md             # Documentation
```

## Dependencies

- langchain-ollama
- pathlib
- Python 3.8+

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- DeepSeek for the language model
- LangChain for AI integration
- The open-source community for inspiration and tools