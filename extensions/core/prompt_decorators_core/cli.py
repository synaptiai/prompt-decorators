"""
Command-line interface for the Prompt Decorators Core extension package.
"""

import argparse
import json
import sys
from typing import List, Optional

from .api import APIRequest


def parse_args(args: Optional[List[str]] = None) -> argparse.Namespace:
    """
    Parse command-line arguments.
    
    Args:
        args: Command-line arguments. If None, sys.argv[1:] is used.
        
    Returns:
        Parsed arguments.
    """
    parser = argparse.ArgumentParser(
        description="Prompt Decorators Core CLI",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    
    parser.add_argument(
        "prompt",
        help="Decorated prompt text or file path (use @file.txt to read from file)",
    )
    
    parser.add_argument(
        "--model",
        "-m",
        default="gpt-4",
        help="Model to use for the request",
    )
    
    parser.add_argument(
        "--temperature",
        "-t",
        type=float,
        default=0.7,
        help="Temperature for the request",
    )
    
    parser.add_argument(
        "--max-tokens",
        type=int,
        help="Maximum number of tokens to generate",
    )
    
    parser.add_argument(
        "--output",
        "-o",
        choices=["json", "decorated", "instructions", "prompt"],
        default="json",
        help="Output format",
    )
    
    parser.add_argument(
        "--output-file",
        "-f",
        help="Output file path (default: stdout)",
    )
    
    return parser.parse_args(args)


def read_prompt(prompt_arg: str) -> str:
    """
    Read prompt from argument or file.
    
    Args:
        prompt_arg: Prompt argument or file path.
        
    Returns:
        Prompt text.
    """
    if prompt_arg.startswith("@"):
        file_path = prompt_arg[1:]
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return f.read()
        except Exception as e:
            print(f"Error reading file {file_path}: {e}", file=sys.stderr)
            sys.exit(1)
    return prompt_arg


def main(args: Optional[List[str]] = None) -> None:
    """
    Main entry point for the CLI.
    
    Args:
        args: Command-line arguments. If None, sys.argv[1:] is used.
    """
    parsed_args = parse_args(args)
    
    # Read prompt
    prompt_text = read_prompt(parsed_args.prompt)
    
    # Create API request
    request = APIRequest.from_decorated_prompt(
        model=parsed_args.model,
        decorated_prompt=prompt_text,
        temperature=parsed_args.temperature,
        max_tokens=parsed_args.max_tokens,
    )
    
    # Generate output
    if parsed_args.output == "json":
        output = request.to_json()
    elif parsed_args.output == "decorated":
        output = request.get_decorated_prompt()
    elif parsed_args.output == "instructions":
        output = request.get_system_instructions()
    elif parsed_args.output == "prompt":
        output = request.prompt
    else:
        output = request.to_json()
    
    # Write output
    if parsed_args.output_file:
        try:
            with open(parsed_args.output_file, "w", encoding="utf-8") as f:
                f.write(output)
        except Exception as e:
            print(f"Error writing to file {parsed_args.output_file}: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        print(output)


if __name__ == "__main__":
    main() 