"""
FileSystem Manager module for OmniAIgent with enhanced code writing capabilities
"""

import os
import shutil
from pathlib import Path
from datetime import datetime
from typing import Union, List, Dict

class FileSystemManager:
    """Handles filesystem operations including code writing capabilities"""
    
    def __init__(self, root_path: str = "workspace"):
        """Initialize the FileSystemManager with a root directory"""
        self.root = Path(root_path)
        self.current_path = self.root
        self.create_root_if_not_exists()
        
        # Common code templates
        self.code_templates = {
            "snake_game": '''import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Set up the game window
width = 800
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Snake and food
snake_block = 20
snake_speed = 15

# Initialize clock
clock = pygame.time.Clock()

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, GREEN, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    font_style = pygame.font.SysFont(None, 50)
    mesg = font_style.render(msg, True, color)
    window.blit(mesg, [width / 6, height / 3])

def gameLoop():
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, height - snake_block) / 20.0) * 20.0

    while not game_over:
        while game_close:
            window.fill(BLACK)
            message("You Lost! Press Q-Quit or C-Play Again", RED)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        window.fill(BLACK)
        pygame.draw.rect(window, RED, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, height - snake_block) / 20.0) * 20.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

if __name__ == "__main__":
    gameLoop()
'''
        }

    def create_root_if_not_exists(self):
        """Create the root directory if it doesn't exist."""
        if not self.root.exists():
            self.root.mkdir(parents=True)

    def execute_command(self, command: str) -> str:
        """Parse and execute filesystem commands with code writing support"""
        command = command.lower().strip()
        
        # Code writing operations
        if "write" in command and "game" in command and "code" in command:
            if "snake" in command:
                return self._write_code_template("snake_game", "snake.py")
            # Add more game templates here
            
        # Regular file operations
        elif "create file" in command or "make file" in command:
            file_name = command.split()[-1]
            return self._create_file(file_name)
            
        elif "write" in command and "to" in command:
            parts = command.split(" to ")
            if len(parts) == 2:
                content, file_name = parts
                return self._write_file(file_name, content)
            return "Please specify what to write and the target file"
            
        elif "list" in command or "show" in command or "what's in" in command:
            return self._list_directory()
            
        elif "create directory" in command or "make directory" in command or "mkdir" in command:
            dir_name = command.split()[-1]
            return self._create_directory(dir_name)
            
        elif "delete" in command or "remove" in command:
            target = command.split()[-1]
            return self._delete(target)
            
        elif "read" in command or "show content" in command or "cat" in command:
            file_name = command.split()[-1]
            return self._read_file(file_name)
            
        elif "move" in command or "rename" in command:
            if "to" in command:
                parts = command.split("to")
                source = parts[0].split()[-1]
                destination = parts[1].strip()
                return self._move(source, destination)
            return "Please specify source and destination"
            
        elif "copy" in command:
            if "to" in command:
                parts = command.split("to")
                source = parts[0].split()[-1]
                destination = parts[1].strip()
                return self._copy(source, destination)
            return "Please specify source and destination"
            
        elif "current directory" in command or "pwd" in command:
            return f"Current directory: {self.current_path}"
            
        elif "change directory" in command or "cd" in command:
            new_dir = command.split()[-1]
            return self._change_directory(new_dir)
            
        else:
            return "I don't understand that command. Try basic operations like list, create, delete, read, write, move, or copy."

    def _list_directory(self, path: str = "") -> str:
        """List contents of current directory with details"""
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
        """Create a new directory"""
        try:
            new_dir = self.current_path / name
            new_dir.mkdir(parents=True, exist_ok=True)
            return f"Created directory: {name}"
        except Exception as e:
            return f"Error creating directory: {e}"

    def _create_file(self, name: str, content: str = "") -> str:
        """Create a new file"""
        try:
            new_file = self.current_path / name
            new_file.write_text(content)
            return f"Created file: {name}"
        except Exception as e:
            return f"Error creating file: {e}"

    def _delete(self, name: str) -> str:
        """Delete a file or directory"""
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
        """Read contents of a file"""
        try:
            file_path = self.current_path / name
            return file_path.read_text()
        except Exception as e:
            return f"Error reading file: {e}"

    def _write_file(self, name: str, content: str) -> str:
        """Write content to a file"""
        try:
            file_path = self.current_path / name
            file_path.write_text(content)
            return f"Written to {name}"
        except Exception as e:
            return f"Error writing to file: {e}"

    def _write_code_template(self, template_name: str, filename: str) -> str:
        """Write a code template to a file"""
        try:
            if template_name in self.code_templates:
                file_path = self.current_path / filename
                file_path.write_text(self.code_templates[template_name])
                return f"Created {filename} with {template_name} template"
            return f"Template {template_name} not found"
        except Exception as e:
            return f"Error writing code template: {e}"

    def _move(self, source: str, destination: str) -> str:
        """Move/rename a file or directory"""
        try:
            src_path = self.current_path / source
            dst_path = self.current_path / destination
            src_path.rename(dst_path)
            return f"Moved {source} to {destination}"
        except Exception as e:
            return f"Error moving file: {e}"

    def _copy(self, source: str, destination: str) -> str:
        """Copy a file or directory"""
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
        """Change current directory"""
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