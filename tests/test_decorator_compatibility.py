#!/usr/bin/env python
"""
Decorator Compatibility Test Script

This script analyzes decorator definitions to check for compatibility and conflicts.
It verifies that the compatibility information in each decorator is consistent.
"""

import argparse
import json
import os
import sys
from pathlib import Path
from collections import defaultdict

# --- Configuration ---

# Add the prompt-decorators directory to the path for imports
sys.path.append(str(Path(__file__).resolve().parent.parent))

# --- Helper Functions ---

def load_decorators(directory_path):
    """Load all decorator JSON files from a directory and its subdirectories"""
    decorators = {}
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.json') and not file.startswith('_'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r') as f:
                        data = json.load(f)
                        name = data.get("decoratorName")
                        if name:
                            decorators[name] = {
                                "data": data,
                                "path": file_path
                            }
                except (json.JSONDecodeError, IOError) as e:
                    print(f"Error loading {file_path}: {e}")
    
    return decorators

def check_conflicts(decorators):
    """Check conflicts between decorators for consistency"""
    conflict_issues = []
    
    # Track conflicts for bi-directional validation
    conflict_map = defaultdict(set)
    
    # Build the conflict map
    for name, decorator in decorators.items():
        conflicts = decorator["data"].get("compatibility", {}).get("conflicts", [])
        for conflict in conflicts:
            conflict_map[name].add(conflict)
    
    # Create a static copy of the conflict map for iteration
    static_conflict_map = {k: set(v) for k, v in conflict_map.items()}
    
    # Check for asymmetric conflicts
    for name, conflicts in static_conflict_map.items():
        for conflict in conflicts:
            if conflict in decorators and name not in conflict_map[conflict]:
                conflict_issues.append({
                    "type": "asymmetric_conflict",
                    "decorator1": name,
                    "decorator2": conflict,
                    "message": f"Asymmetric conflict: {name} lists {conflict} as a conflict, but not vice versa"
                })
    
    # Check if conflicts reference non-existent decorators
    for name, conflicts in static_conflict_map.items():
        for conflict in conflicts:
            if conflict not in decorators:
                conflict_issues.append({
                    "type": "unknown_conflict",
                    "decorator": name,
                    "conflict": conflict,
                    "message": f"Unknown conflict: {name} lists {conflict} as a conflict, but it doesn't exist"
                })
    
    return conflict_issues

def check_requires(decorators):
    """Check if required decorators exist"""
    require_issues = []
    
    for name, decorator in decorators.items():
        requires = decorator["data"].get("compatibility", {}).get("requires", [])
        for required in requires:
            if required not in decorators:
                require_issues.append({
                    "type": "unknown_requirement",
                    "decorator": name,
                    "requires": required,
                    "message": f"Unknown requirement: {name} requires {required}, but it doesn't exist"
                })
    
    return require_issues

def check_versions(decorators):
    """Check for version compatibility issues"""
    version_issues = []
    
    for name, decorator in decorators.items():
        compatibility = decorator["data"].get("compatibility", {})
        min_version = compatibility.get("minStandardVersion")
        max_version = compatibility.get("maxStandardVersion")
        
        if min_version and max_version:
            min_parts = [int(x) for x in min_version.split('.')]
            max_parts = [int(x) for x in max_version.split('.')]
            
            if min_parts > max_parts:
                version_issues.append({
                    "type": "version_conflict",
                    "decorator": name,
                    "message": f"Version conflict: minStandardVersion {min_version} is greater than maxStandardVersion {max_version}"
                })
    
    return version_issues

def check_models(decorators):
    """Check for model compatibility issues"""
    model_issues = []
    
    for name, decorator in decorators.items():
        models = decorator["data"].get("compatibility", {}).get("models", [])
        
        if not models:
            model_issues.append({
                "type": "no_models",
                "decorator": name,
                "message": f"No models specified for {name}"
            })
    
    return model_issues

def main():
    parser = argparse.ArgumentParser(description="Check compatibility between prompt decorators")
    parser.add_argument("registry_path", help="Path to the decorator registry directory")
    parser.add_argument("--verbose", "-v", action="store_true", help="Show detailed information")
    args = parser.parse_args()
    
    # Load all decorators
    decorators = load_decorators(args.registry_path)
    if not decorators:
        print(f"No decorators found in {args.registry_path}")
        return 1
    
    print(f"Loaded {len(decorators)} decorators")
    if args.verbose:
        for name in sorted(decorators.keys()):
            print(f"  - {name}")
    print()
    
    # Run checks
    conflict_issues = check_conflicts(decorators)
    require_issues = check_requires(decorators)
    version_issues = check_versions(decorators)
    model_issues = check_models(decorators)
    
    all_issues = conflict_issues + require_issues + version_issues + model_issues
    
    # Report results
    if all_issues:
        print(f"Found {len(all_issues)} issues:")
        for issue in all_issues:
            print(f"  - {issue['message']}")
        return 1
    else:
        print("No compatibility issues found!")
        return 0

if __name__ == "__main__":
    sys.exit(main()) 