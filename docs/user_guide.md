# OmnitrAIce User Guide

## Getting Started

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/OmnitrAIce.git
cd OmnitrAIce
```

2. Set up virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Quick Start

1. Start the application:
```bash
python omniagent.py
```

2. Generate your first code:
```
generate a hello world program in python
```

## Basic Usage

### Code Generation

1. **Simple Generation**
```
generate a calculator in javascript
```

2. **Specific Language**
```
generate a web server in python
generate a todo app in typescript
```

3. **Complex Projects**
```
generate a chat application with websockets in python
generate a react component for user authentication
```

### File Management

1. **Directory Operations**
```
list                          # List contents
create directory myproject    # Create directory
cd myproject                 # Change directory
```

2. **File Operations**
```
create file test.py          # Create file
write Hello World to test.py # Write to file
read file test.py           # Read file
delete test.py              # Delete file
```

## Advanced Features

### Code Cleaning

All generated code is automatically cleaned to:
- Remove explanatory text
- Format properly
- Add appropriate imports
- Include error handling

### Multiple Languages

Supported languages include:
- Python
- JavaScript
- TypeScript
- Java
- C++
- And more...

## Best Practices

1. **Code Generation**
- Be specific in descriptions
- Specify language when needed
- Review generated code
- Test before use

2. **File Management**
- Organize files logically
- Use meaningful names
- Back up important files
- Clean up unused files

## Troubleshooting

### Common Issues

1. **Generation Fails**
- Check language support
- Simplify description
- Try different phrasing

2. **File Operations Fail**
- Check permissions
- Verify paths
- Check file existence

### Error Messages

Common error messages and solutions:
```
Error: File not found
Solution: Check file path and name

Error: Permission denied
Solution: Check file permissions

Error: Invalid command
Solution: Check command syntax
```

## Tips and Tricks

1. **Efficient Code Generation**
- Use clear descriptions
- Include key requirements
- Specify language features

2. **File Organization**
- Use descriptive names
- Create logical directory structure
- Clean up regularly

3. **Performance**
- Generate code in batches
- Clean up unused files
- Organize workspace