# OmnitrAIce API Documentation

## FileSystemManager

### Code Generation

```python
def generate_code(description: str, language: str = "python") -> str:
```
Generates code based on description using AI model.

**Parameters:**
- `description`: Description of code to generate
- `language`: Target programming language (default: "python")

**Returns:**
- Generated code as string

### File Operations

```python
def execute_command(command: str) -> str:
```
Executes filesystem commands.

**Parameters:**
- `command`: Command string to execute

**Returns:**
- Operation result message

## CodeCleaner

### Code Cleaning

```python
def clean_code(content: str, file_extension: str) -> str:
```
Cleans generated code by removing non-code elements.

**Parameters:**
- `content`: Raw code content
- `file_extension`: File extension for language detection

**Returns:**
- Cleaned code as string

### File Processing

```python
def process_and_save(file_path: Path) -> bool:
```
Process and save cleaned code.

**Parameters:**
- `file_path`: Path to file
- `content`: Code content

**Returns:**
- Success status as boolean

## Command Format

### Code Generation Commands
```
generate <description> in <language>
write <description> to <filename>
```

### File Operations Commands
```
create file <filename>
create directory <dirname>
delete <filename>
read file <filename>
write <content> to <filename>
move <source> to <destination>
copy <source> to <destination>
list
cd <path>
```

## Examples

### Generate Code
```python
# Generate a calculator in JavaScript
result = fs_manager.execute_command("generate a calculator in javascript")

# Create a web server in Python
result = fs_manager.execute_command("generate a web server in python")
```

### File Operations
```python
# Create directory
result = fs_manager.execute_command("create directory myproject")

# Create file
result = fs_manager.execute_command("create file test.py")

# Read file
result = fs_manager.execute_command("read file test.py")
```