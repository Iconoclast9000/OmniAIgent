# Project Structure and Command Flow

This document explains the project structure diagram and command flow visualization.

## Project Structure (`project_structure.mmd`)

The project structure diagram shows the organization of the OmnitrAIce project:

### Main Components
1. **Root Directory**
   - README.md
   - requirements.txt
   - TECHNICAL.md
   - omniagent.py

2. **Source Code** (`src/`)
   - utils/
     - filesystem.py
     - chat.py
     - code_cleaner.py

3. **Documentation** (`docs/`)
   - architecture.md
   - api.md
   - user_guide.md
   - index.md
   - diagrams/

4. **Workspace**
   - Generated code files
   - Temporary files
   - Output directory

## Command Flow (`command_flow.svg`)

The command flow diagram illustrates how commands are processed:

### Flow Stages
1. **User Input**
   - Command entry
   - Initial validation

2. **Command Parser**
   - Command type identification
   - Parameter extraction
   - Validation

3. **Command Types**
   - Code Generation
   - File Operations
   - System Commands

4. **Response Handler**
   - Result formatting
   - Error handling
   - User feedback

### Command Categories

1. **Code Generation**
   ```
   generate <description> in <language>
   write <description> to <filename>
   ```

2. **File Operations**
   ```
   create file/directory
   read/write/delete
   move/copy
   ```

3. **System Commands**
   ```
   list
   help
   exit
   ```

## Integration Points

The diagrams show how different components interact:

1. **File System Integration**
   - Command processing
   - File operations
   - Code storage

2. **Command Processing**
   - Input parsing
   - Command routing
   - Response handling

3. **Documentation Structure**
   - Technical docs
   - User guides
   - API reference

## Using the Diagrams

These diagrams serve different purposes:

1. **Project Structure**
   - Understanding project organization
   - Locating components
   - Planning modifications

2. **Command Flow**
   - Understanding command processing
   - Debugging issues
   - Planning new features