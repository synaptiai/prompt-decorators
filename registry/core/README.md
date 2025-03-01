# Core Decorators

This directory contains all decorators defined in the original Prompt Decorators specification. These are officially part of the standard and maintained by the Prompt Decorators Working Group.

The decorators are organized into the following categories:

- **minimal**: The 5 core decorators that MUST be implemented by any conforming implementation
- **reasoning**: Decorators that modify how the AI approaches reasoning about a problem
- **structure**: Decorators that specify the structure and format of the AI's response
- **tone**: Decorators that modify the linguistic style and tone of the AI's response
- **verification**: Decorators that focus on ensuring accuracy, balance, and quality
- **meta**: Decorators that modify the behavior of other decorators or provide higher-level control

Each decorator is defined in a JSON file following the registry-entry.schema.json format. 