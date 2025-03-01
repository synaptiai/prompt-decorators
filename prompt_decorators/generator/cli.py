"""
Command-Line Interface for the Prompt Decorators Generator

This module provides a CLI for generating Python code from decorator definitions.
"""

import argparse
import logging
import sys
from pathlib import Path
from typing import Optional, List

from .registry import scan_registry
from .code_gen import generate_code

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def parse_args(args: Optional[List[str]] = None) -> argparse.Namespace:
    """
    Parse command-line arguments.
    
    Args:
        args: Command-line arguments (defaults to sys.argv[1:])
        
    Returns:
        Parsed arguments
    """
    parser = argparse.ArgumentParser(
        description='Generate Python code from Prompt Decorators registry',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    parser.add_argument(
        '--registry', '-r',
        type=str,
        default=None,
        help='Path to the registry directory'
    )
    
    parser.add_argument(
        '--output', '-o',
        type=str,
        default=None,
        help='Output directory for generated code'
    )
    
    parser.add_argument(
        '--category', '-c',
        type=str,
        nargs='+',
        help='Only process specific categories'
    )
    
    parser.add_argument(
        '--list-categories',
        action='store_true',
        help='List available categories and exit'
    )
    
    parser.add_argument(
        '--verbose', '-v',
        action='count',
        default=0,
        help='Increase verbosity (can be used multiple times)'
    )
    
    parser.add_argument(
        '--quiet', '-q',
        action='store_true',
        help='Suppress all output except errors'
    )
    
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Scan and validate but do not generate code'
    )
    
    return parser.parse_args(args)


def configure_logging(args: argparse.Namespace) -> None:
    """
    Configure logging based on command-line arguments.
    
    Args:
        args: Parsed command-line arguments
    """
    if args.quiet:
        logging.basicConfig(level=logging.ERROR)
    elif args.verbose == 0:
        logging.basicConfig(level=logging.INFO)
    elif args.verbose == 1:
        logging.basicConfig(level=logging.DEBUG)
    else:
        # Extra verbose
        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s'
        )


def find_registry_path(specified_path: Optional[str] = None) -> Path:
    """
    Find the registry directory.
    
    Args:
        specified_path: User-specified path (if any)
        
    Returns:
        Path to the registry directory
    """
    if specified_path:
        path = Path(specified_path)
        if path.exists() and path.is_dir():
            return path
        raise FileNotFoundError(f"Registry path '{specified_path}' not found or not a directory")
    
    # Try to locate the registry relative to this script
    script_dir = Path(__file__).parent.parent.parent
    possible_paths = [
        script_dir / "registry",
        script_dir.parent / "registry",
    ]
    
    for path in possible_paths:
        if path.exists() and path.is_dir():
            return path
    
    raise FileNotFoundError(
        "Could not locate registry directory. Please specify with --registry option."
    )


def find_output_path(specified_path: Optional[str] = None) -> Path:
    """
    Find or create the output directory.
    
    Args:
        specified_path: User-specified path (if any)
        
    Returns:
        Path to the output directory
    """
    if specified_path:
        path = Path(specified_path)
    else:
        # Default to decorators/generated in the current package
        path = Path(__file__).parent.parent / "decorators" / "generated"
    
    # Create the directory if it doesn't exist
    path.mkdir(parents=True, exist_ok=True)
    
    return path


def main(args: Optional[List[str]] = None) -> int:
    """
    Main entry point for the CLI.
    
    Args:
        args: Command-line arguments (defaults to sys.argv[1:])
        
    Returns:
        Exit code (0 for success, non-zero for failure)
    """
    parsed_args = parse_args(args)
    
    # Configure logging
    configure_logging(parsed_args)
    
    try:
        # Find registry path
        registry_path = find_registry_path(parsed_args.registry)
        logger.info(f"Using registry at: {registry_path}")
        
        # Scan registry
        decorators = scan_registry(registry_path)
        logger.info(f"Found {len(decorators)} decorators")
        
        # Filter by category if specified
        if parsed_args.category:
            original_count = len(decorators)
            decorators = [
                d for d in decorators 
                if any(
                    cat in (Path(d.get("_source_file", "")).parts[0] if "_source_file" in d else "") 
                    for cat in parsed_args.category
                )
            ]
            logger.info(
                f"Filtered to {len(decorators)} decorators in categories: {', '.join(parsed_args.category)} "
                f"(from {original_count} total)"
            )
        
        # If just listing categories, do that and exit
        if parsed_args.list_categories:
            categories = set()
            for d in decorators:
                if "_source_file" in d:
                    source_file = Path(d["_source_file"])
                    if len(source_file.parts) > 0:
                        categories.add(source_file.parts[0])
            
            print("Available categories:")
            for category in sorted(categories):
                count = sum(1 for d in decorators if "_source_file" in d and Path(d["_source_file"]).parts[0] == category)
                print(f"  {category} ({count} decorators)")
            
            return 0
        
        # If doing a dry run, exit here
        if parsed_args.dry_run:
            logger.info("Dry run complete. No code generated.")
            return 0
        
        # Generate code
        output_path = find_output_path(parsed_args.output)
        logger.info(f"Generating code to: {output_path}")
        
        generated_files = generate_code(decorators, output_path)
        logger.info(f"Generated {len(generated_files)} files")
        
        return 0
    
    except Exception as e:
        logger.error(f"Error: {e}")
        if parsed_args.verbose > 0:
            import traceback
            traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main()) 