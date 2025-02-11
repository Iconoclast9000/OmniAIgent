import re
from pathlib import Path
from typing import Optional

class CodeCleaner:
    """Clean generated code files by removing explanatory text and formatting artifacts."""
    
    def __init__(self):
        # Patterns to identify code blocks and remove non-code content
        self.patterns = {
            'markdown_code': r'```[\w]*\n(.*?)```',
            'explanation_text': r'Here\'s.*?:|Let\'s.*?:|First,.*?:|Note:.*',
            'prompt_artifacts': r'<.*?>.*?</.*?>',
            'empty_lines': r'\n\s*\n',
            'numbered_steps': r'^\d+\.\s.*$',
            'bullet_points': r'^\s*[-*]\s.*$'
        }
        
        # Language-specific comment indicators
        self.comment_indicators = {
            '.py': '#',
            '.js': '//',
            '.ts': '//',
            '.java': '//',
            '.cpp': '//',
            '.c': '//',
            '.rs': '//',
            '.go': '//',
            '.rb': '#',
            '.php': '//',
            '.swift': '//',
            '.kt': '//',
            '.scala': '//'
        }

    def extract_code_blocks(self, content: str) -> str:
        """Extract code from markdown code blocks if present."""
        code_blocks = re.findall(self.patterns['markdown_code'], content, re.DOTALL | re.MULTILINE)
        if code_blocks:
            return '\n'.join(code_blocks)
        return content

    def remove_explanations(self, content: str) -> str:
        """Remove explanation text and other non-code elements."""
        # Remove various types of explanatory text
        content = re.sub(self.patterns['explanation_text'], '', content, flags=re.MULTILINE)
        content = re.sub(self.patterns['numbered_steps'], '', content, flags=re.MULTILINE)
        content = re.sub(self.patterns['bullet_points'], '', content, flags=re.MULTILINE)
        return content

    def clean_comments(self, content: str, file_extension: str) -> str:
        """Clean up comments while preserving meaningful documentation."""
        comment_char = self.comment_indicators.get(file_extension, '#')
        lines = content.split('\n')
        cleaned_lines = []
        
        for line in lines:
            stripped = line.strip()
            # Keep non-comment lines or meaningful comments
            if (not stripped.startswith(comment_char) or
                len(stripped) > len(comment_char) + 1 and 
                not stripped[len(comment_char):].isspace() and
                not any(text in stripped.lower() for text in ['todo:', 'note:', 'fixme:'])):
                cleaned_lines.append(line)
        
        return '\n'.join(cleaned_lines)

    def clean_code(self, content: str, file_extension: str) -> str:
        """Clean the code content by removing non-code elements."""
        # Extract code from markdown blocks if present
        cleaned = self.extract_code_blocks(content)
        
        # Remove explanation text and artifacts
        cleaned = self.remove_explanations(cleaned)
        cleaned = re.sub(self.patterns['prompt_artifacts'], '', cleaned)
        
        # Clean up comments
        cleaned = self.clean_comments(cleaned, file_extension)
        
        # Clean up multiple empty lines
        cleaned = re.sub(self.patterns['empty_lines'], '\n\n', cleaned)
        
        # Final cleanup
        cleaned = cleaned.strip()
        
        return cleaned

    def clean_file(self, file_path: Path) -> Optional[str]:
        """Read a file, clean its contents, and return the cleaned code."""
        try:
            content = file_path.read_text(encoding='utf-8')
            cleaned_code = self.clean_code(content, file_path.suffix)
            return cleaned_code
        except Exception as e:
            print(f"Error cleaning file {file_path}: {e}")
            return None

    def process_and_save(self, file_path: Path) -> bool:
        """Clean a code file and save the results back to the same file."""
        try:
            cleaned_code = self.clean_file(file_path)
            if cleaned_code is not None:
                file_path.write_text(cleaned_code, encoding='utf-8')
                return True
            return False
        except Exception as e:
            print(f"Error processing file {file_path}: {e}")
            return False