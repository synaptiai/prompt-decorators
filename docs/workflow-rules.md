# Cursor Workflow Rules

This project has been updated to use the auto rule generator from [cursor-auto-rules-agile-workflow](https://github.com/bmadcode/cursor-auto-rules-agile-workflow).

> **Note**: This script can be safely re-run at any time to update the template rules to their latest versions. It will not impact or overwrite any custom rules you've created.

## Core Features

- Automated rule generation
- Standardized documentation formats
- Code quality and workflow optimization
- Flexible integration options for various development scenarios

## Available Rules

The following rules are currently installed in `.cursor/rules/`:

### Core Standards (0XX)
- `000-cursor-rules.mdc` - Meta-rules for creating and updating Cursor rules
- `050-careful-code-modification.mdc` - Guidelines for careful code modifications
- `060-coding-patterns.mdc` - Standards for maintaining coding patterns
- `070-workflow-preferences.mdc` - Development discipline and workflow preferences

### Documentation Standards (4XX)
- `400-md-docs.mdc` - Markdown documentation standards and formatting

### Templates and Specialized Rules (9XX)
- `900-software-dev-decorators.mdc` - Software Development Prompt Decorators for enhanced code generation

## Software Development Prompt Decorators

The `900-software-dev-decorators.mdc` rule incorporates a powerful set of over 40 specialized prompt decorators designed specifically for software development tasks. These decorators allow you to guide the AI's responses for specific coding scenarios.

### Key Decorator Categories:

1. **Code Generation & Algorithms**
   - `+++Algorithm` - Implement algorithms with specific complexity and approach
   - `+++CodeGen` - Generate code with configurable style and documentation
   - `+++DesignPattern` - Implement software design patterns

2. **Architecture & Design**
   - `+++Architecture` - Design software architecture with specific patterns
   - `+++APIDesign` - Design API interfaces with specific qualities
   - `+++DataModel` - Design data models with appropriate structures
   - `+++SystemDiagram` - Create visual representations of system architecture

3. **Code Quality & Review**
   - `+++CodeReview` - Provide feedback on code quality following defined standards
   - `+++BestPractices` - Apply domain-specific best practices
   - `+++SecurityAudit` - Analyze code for security vulnerabilities
   - `+++Refactor` - Improve existing code structure without changing behavior

4. **Debugging & Troubleshooting**
   - `+++BugDiagnosis` - Systematically diagnose software bugs
   - `+++DebugStrategy` - Outline systematic approach to debugging
   - `+++RootCauseAnalysis` - Identify underlying causes of problems
   - `+++ErrorDiagnosis` - Analyze error patterns with systematic troubleshooting

5. **DevOps & Infrastructure**
   - `+++CICD` - Create or explain CI/CD pipelines
   - `+++Deployment` - Generate deployment approaches
   - `+++Infrastructure` - Generate infrastructure as code templates
   - `+++Monitoring` - Design monitoring solutions

## Workflow Integration Options

### 1. Automatic Rule Application (Recommended)
The core workflow rules are automatically installed in `.cursor/rules/`:
- `901-prd.mdc` - Product Requirements Document standards
- `902-arch.mdc` - Architecture documentation standards
- `903-story.mdc` - User story standards
- `801-workflow-agile.mdc` - Complete Agile workflow (optional)

These rules are automatically applied when working with corresponding file types.

### 2. Notepad-Based Workflow
For a more flexible approach, use the templates in `xnotes/`:
1. Enable Notepads in Cursor options
2. Create a new notepad (e.g., "agile")
3. Copy contents from `xnotes/workflow-agile.md`
4. Use \`@notepad-name\` in conversations

> 💡 **Tip:** The Notepad approach is ideal for:
> - Initial project setup
> - Story implementation
> - Focused development sessions
> - Reducing context overhead

## Getting Started

1. Review the templates in \`xnotes/\`
2. Choose your preferred workflow approach
3. Start using the AI with confidence!

For demos and tutorials, visit: [BMad Code Videos](https://youtube.com/bmadcode)
