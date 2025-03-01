"""
Example Decorator Plugin

This is an example plugin for the prompt decorators framework.
"""

from prompt_decorators.core.base import BaseDecorator

# Plugin information
plugin_info = {
    "name": "ExamplePlugin",
    "version": "1.0.0",
    "description": "Example plugin with custom decorators",
    "author": {
        "name": "Prompt Decorators Team",
        "email": "example@example.com"
    },
    "metadata": {
        "category": "example",
        "tags": ["example", "demo"]
    }
}


class FunnyDecorator(BaseDecorator):
    """
    A decorator that adds humor to prompts.
    """
    
    name = "Funny"
    version = "1.0.0"
    category = "humor"
    
    def __init__(self, style: str = "dad_jokes", pun_density: int = 3):
        """
        Initialize the funny decorator.
        
        Args:
            style: Style of humor to use (dad_jokes, puns, sarcasm)
            pun_density: How many puns to include (1-10)
        """
        super().__init__()
        self.style = style
        self.pun_density = max(1, min(10, pun_density))  # Clamp between 1-10
    
    def apply(self, prompt: str) -> str:
        """
        Apply the funny decorator to a prompt.
        
        Args:
            prompt: The original prompt to decorate
            
        Returns:
            The decorated prompt
        """
        humor_instruction = f"Please respond with humor in the style of {self.style}. "
        
        if self.style == "dad_jokes":
            humor_instruction += "Include cheesy dad jokes. "
        elif self.style == "puns":
            humor_instruction += f"Include {self.pun_density} clever puns related to the topic. "
        elif self.style == "sarcasm":
            humor_instruction += "Use light sarcasm and wit in your response. "
        else:
            humor_instruction += "Use general humor in your response. "
        
        humor_instruction += "Make sure your response is both informative AND entertaining."
        
        return f"{humor_instruction}\n\n{prompt}"


class SummaryPointsDecorator(BaseDecorator):
    """
    A decorator that requests summary points at the end of responses.
    """
    
    name = "SummaryPoints"
    version = "1.0.0"
    category = "format"
    
    def __init__(self, count: int = 3, position: str = "end"):
        """
        Initialize the summary points decorator.
        
        Args:
            count: Number of summary points to include
            position: Where to put the summary (start, end)
        """
        super().__init__()
        self.count = max(1, min(10, count))  # Clamp between 1-10
        self.position = position if position in ("start", "end") else "end"
    
    def apply(self, prompt: str) -> str:
        """
        Apply the summary points decorator to a prompt.
        
        Args:
            prompt: The original prompt to decorate
            
        Returns:
            The decorated prompt
        """
        summary_instruction = f"After your main response, please include exactly {self.count} "
        summary_instruction += "key summary points that capture the most important aspects of your answer. "
        
        if self.position == "start":
            summary_instruction = f"Before your detailed response, please include exactly {self.count} "
            summary_instruction += "key points that will be explained further. "
            summary_instruction += "Then provide your complete response. "
        
        return f"{summary_instruction}\n\n{prompt}" 