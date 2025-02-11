import os
import shutil
from pathlib import Path
from datetime import datetime
from typing import Dict, Any
from langchain_ollama import OllamaLLM
from .code_cleaner import CodeCleaner

class FileSystemManager:
    def __init__(self, root_path: str = "workspace", model_name: str = "deepseek-r1:1.5b"):
        """Initialize FileSystemManager with root directory and AI model."""
        self.root = Path(root_path)
        self.current_path = self.root
        self.model = OllamaLLM(model=model_name)
        self.code_cleaner = CodeCleaner()
        
        # File extension mappings
        self.file_extensions = {
            "python": ".py",
            "javascript": ".js",
            "typescript": ".ts",
            "java": ".java",
            "c++": ".cpp",
            "c": ".c",
            "rust": ".rs",
            "go": ".go",
            "ruby": ".rb",
            "php": ".php",
            "swift": ".swift",
            "kotlin": ".kt",
            "scala": ".scala",
            "html": ".html",
            "css": ".css"
        }
        
        # Create root directory if it doesn't exist
        if not self.root.exists():
            self.root.mkdir(parents=True)

    def generate_code(self, description: str, language: str = "python") -> str:
        """Generate code using the AI model."""
        try:
            prompt = f"""
            Generate complete, runnable {language} code based on this description:
            {description}
            
            The code should:
            - Include all necessary imports
            - Have proper error handling
            - Be well-documented
            - Follow best practices for {language}
            - Be organized and readable
            
            Return only the code without any explanations or markdown.
            """
            
            return self.model.invoke(prompt)
        except Exception as e:
            return f"Error generating code: {e}"

    def write_code(self, filename: str, content: str) -> str:
        """Write and clean generated code."""
        try:
            file_path = self.current_path / filename
            
            # Write initial content
            file_path.write_text(content, encoding='utf-8')
            
            # Clean the code
            if self.code_cleaner.process_and_save(file_path):
                return f"Written and cleaned code in {filename}"
            return f"Written code to {filename}, but cleaning failed"
        except Exception as e:
            return f"Error writing code: {e}"

    def execute_command(self, command: str) -> str:
        """Enhanced command execution with dynamic code generation."""
        command = command.lower().strip()

        # Code generation commands
        if "generate" in command:
            # Handle both formats: "generate X in Y" and "generate X"
            description = command.replace("generate", "", 1).strip()
            language = "python"  # default language
            
            if " in " in description:
                parts = description.split(" in ")
                description = parts[0].strip()
                language = parts[1].strip()
            
            # Generate unique filename based on description
            safe_desc = "".join(c for c in description[:30] if c.isalnum() or c.isspace()).strip()
            safe_desc = safe_desc.replace(" ", "_")
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            extension = self.file_extensions.get(language.lower(), ".txt")
            filename = f"{safe_desc}_{timestamp}{extension}"
            
            # Generate and write code
            code = self.generate_code(description, language)
            return self.write_code(filename, code)

        # Write specific game or application
        elif "write" in command and ("game" in command or "app" in command):
            description = command.split("write")[1].split("to")[0].strip()
            if len(command.split("to")) > 1:
                filename = command.split("to")[1].strip()
            else:
                safe_desc = "".join(c for c in description[:30] if c.isalnum() or c.isspace()).strip()
                safe_desc = safe_desc.replace(" ", "_")
                filename = f"{safe_desc}.py"
            
            code = self.generate_code(description, "python")
            return self.write_code(filename, code)

        # Basic file operations
        elif "create file" in command:
            parts = command.split("create file")[1].strip().split(" with content ")
            file_name = parts[0].strip()
            content = parts[1].strip() if len(parts) > 1 else ""
            return self._create_file(file_name, content)

        elif "create folder" in command or "create directory" in command:
            folder_name = command.split("create folder" if "folder" in command else "create directory")[1].strip()
            return self._create_directory(folder_name)

        elif "delete" in command or "remove" in command:
            name = command.split("delete" if "delete" in command else "remove")[1].strip()
            return self._delete(name)

        elif "read" in command or "cat" in command:
            file_name = command.split("read" if "read" in command else "cat")[1].strip()
            return self._read_file(file_name)

        elif "write" in command and "to" in command:
            parts = command.split("write")[1].strip().split(" to ")
            content = parts[0].strip()
            file_name = parts[1].strip()
            return self._write_file(file_name, content)

        elif "move" in command or "rename" in command:
            parts = command.split("to")
            source = parts[0].split("move" if "move" in command else "rename")[1].strip()
            destination = parts[1].strip()
            return self._move(source, destination)

        elif "copy" in command:
            parts = command.split("copy")[1].strip().split(" to ")
            source = parts[0].strip()
            destination = parts[1].strip()
            return self._copy(source, destination)

        elif "list" in command or "show" in command:
            return self._list_directory()

        elif "cd" in command or "change directory" in command:
            path = command.split("cd" if "cd" in command else "change directory")[1].strip()
            return self._change_directory(path)

        elif "pwd" in command or "current directory" in command:
            return f"Current directory: {self.current_path}"

        else:
            return "Command not recognized. Type 'help' for available commands."

    def _list_directory(self, path: str = "") -> str:
        """List contents of current directory with details."""
        try:
            target_path = self.current_path / path
            contents = []
            for item in target_path.iterdir():
                stats = item.stat()
                item_type = "📁 " if item.is_dir() else "📄 "
                size = stats.st_size
                modified = datetime.fromtimestamp(stats.st_mtime).strftime("%Y-%m-%d %H:%M")
                contents.append(f"{item_type}{item.name} - {size}B - {modified}")

            return "\n".join(contents) if contents else "Directory is empty"
        except Exception as e:
            return f"Error listing directory: {e}"

    def _create_directory(self, name: str) -> str:
        """Create a new directory."""
        try:
            new_dir = self.current_path / name
            new_dir.mkdir(parents=True, exist_ok=True)
            return f"Created directory: {name}"
        except Exception as e:
            return f"Error creating directory: {e}"

    def _create_file(self, name: str, content: str = "") -> str:
        """Create a new file."""
        try:
            new_file = self.current_path / name
            new_file.write_text(content, encoding='utf-8')
            return f"Created file: {name}"
        except Exception as e:
            return f"Error creating file: {e}"

    def _delete(self, name: str) -> str:
        """Delete a file or directory."""
        try:
            target = self.current_path / name
            if target.is_file():
                target.unlink()
                return f"Deleted file: {name}"
            elif target.is_dir():
                shutil.rmtree(target)
                return f"Deleted directory: {name}"
            return f"Not found: {name}"
        except Exception as e:
            return f"Error deleting {name}: {e}"

    def _read_file(self, name: str) -> str:
        """Read contents of a file."""
        try:
            file_path = self.current_path / name
            return file_path.read_text(encoding='utf-8')
        except Exception as e:
            return f"Error reading file: {e}"

    def _write_file(self, name: str, content: str) -> str:
        """Write content to a file."""
        try:
            file_path = self.current_path / name
            file_path.write_text(content, encoding='utf-8')
            return f"Written to {name}"
        except Exception as e:
            return f"Error writing to file: {e}"

    def _move(self, source: str, destination: str) -> str:
        """Move/rename a file or directory."""
        try:
            src_path = self.current_path / source
            dst_path = self.current_path / destination
            src_path.rename(dst_path)
            return f"Moved {source} to {destination}"
        except Exception as e:
            return f"Error moving file: {e}"

    def _copy(self, source: str, destination: str) -> str:
        """Copy a file or directory."""
        try:
            src_path = self.current_path / source
            dst_path = self.current_path / destination
            if src_path.is_file():
                shutil.copy2(src_path, dst_path)
            else:
                shutil.copytree(src_path, dst_path)
            return f"Copied {source} to {destination}"
        except Exception as e:
            return f"Error copying: {e}"

    def _change_directory(self, path: str) -> str:
        """Change current directory."""
        try:
            if path == "..":
                if self.current_path != self.root:
                    self.current_path = self.current_path.parent
            else:
                new_path = self.current_path / path
                if new_path.is_dir():
                    self.current_path = new_path
                else:
                    return f"Directory not found: {path}"
            return f"Current directory: {self.current_path}"
        except Exception as e:
            return f"Error changing directory: {e}"