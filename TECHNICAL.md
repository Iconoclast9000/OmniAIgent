# OmnitrAIce Technical Documentation

## Architecture Overview

OmnitrAIce is built with a modular architecture consisting of three main components:

1. **FileSystemManager** - Core file operations and code generation
2. **CodeCleaner** - Code processing and cleaning
3. **Chat Interface** - User interaction and command processing

### FileSystemManager (filesystem.py)

The FileSystemManager class handles all filesystem operations and code generation:

```python
class FileSystemManager:
    def __init__(self, root_path: str = "workspace", model_name: str = "deepseek-r1:1.5b"):
        # Initialize filesystem and AI model
```

Key Features:
- File and directory operations (create, read, update, delete)
- Dynamic code generation using AI
- File type detection and handling
- Error handling and logging
- UTF-8 encoding support

### CodeCleaner (code_cleaner.py)

The CodeCleaner class processes generated code to ensure clean, production-ready output:

```python
class CodeCleaner:
    def __init__(self):
        # Initialize cleaning patterns and language settings
```

Features:
- Removes explanatory text and artifacts
- Cleans up code formatting
- Handles language-specific comments
- Preserves important documentation
- Multiple cleaning strategies

### Chat Interface (chat.py)

The chat interface manages user interaction and command processing:

```python
SYSTEM_PROMPT = """
You are a filesystem and code generation assistant...
"""
```

Features:
- Natural language command processing
- Context management
- History tracking
- Error reporting
- User feedback

## Code Generation Process

1. **Command Processing**
   - Parse user input
   - Extract language and description
   - Generate filename

2. **Code Generation**
   - Create AI prompt
   - Generate initial code
   - Apply language-specific formatting

3. **Code Cleaning**
   - Remove non-code elements
   - Clean formatting
   - Apply language standards
   - Save final output

## Supported File Operations

1. **Basic Operations**
   - create file/directory
   - read file
   - write to file
   - delete file/directory
   - move/rename
   - copy

2. **Advanced Operations**
   - code generation
   - code cleaning
   - directory traversal
   - file search

## Error Handling

The system implements comprehensive error handling:

1. **File Operations**
   - Permission errors
   - File not found
   - Path issues
   - Encoding problems

2. **Code Generation**
   - Model errors
   - Invalid input
   - Language support
   - Output validation

3. **Code Cleaning**
   - Format errors
   - Invalid code
   - Syntax issues
   - Encoding problems

## Best Practices

1. **Code Generation**
   - Use descriptive prompts
   - Specify language when needed
   - Review generated code
   - Test before deployment

2. **File Management**
   - Use appropriate file extensions
   - Maintain directory structure
   - Back up important files
   - Follow naming conventions

3. **System Usage**
   - Keep workspace organized
   - Clean up unused files
   - Monitor system resources
   - Update dependencies regularly

## Development Guidelines

1. **Adding New Features**
   - Follow existing patterns
   - Document changes
   - Add error handling
   - Update tests

2. **Code Style**
   - Follow PEP 8
   - Use type hints
   - Document functions
   - Write clear comments

3. **Testing**
   - Write unit tests
   - Test edge cases
   - Verify file operations
   - Check code generation

## Performance Considerations

1. **File Operations**
   - Use appropriate buffer sizes
   - Handle large files properly
   - Cache when beneficial
   - Clean up temporary files

2. **Code Generation**
   - Optimize prompts
   - Cache common generations
   - Use appropriate model settings
   - Monitor resource usage

3. **System Resources**
   - Monitor memory usage
   - Handle concurrent operations
   - Clean up resources
   - Log performance metrics