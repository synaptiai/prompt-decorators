#!/usr/bin/env python
"""
Basic Decorator Usage - Interactive Examples

This script demonstrates how to use the Prompt Decorators framework for enhancing LLM prompts.
It shows various decorators in action and how to combine them to create sophisticated
prompt engineering solutions.

Note: This script is designed to be converted to a Jupyter notebook
for an interactive experience.
"""

# %% [markdown]
# # Basic Decorator Usage - Interactive Examples
#
# This notebook demonstrates how to use the Prompt Decorators framework for enhancing LLM prompts.
# You'll see various decorators in action and how to combine them to create sophisticated prompt
# engineering solutions.

# %% [markdown]
# ## Setup
#
# First, let's make sure we have the Prompt Decorators framework installed and properly set up.

# %%
# Add the project root to the Python path if running this notebook outside of the project directory
import sys
from pathlib import Path
import os

# Check if the prompt_decorators module is available
try:
    import prompt_decorators
    print("Prompt Decorators framework is already installed.")
except ImportError:
    # Add the parent directory to the Python path
    notebook_dir = Path(os.getcwd())
    project_root = notebook_dir.parent.parent
    sys.path.insert(0, str(project_root))
    print(f"Added project root to Python path: {project_root}")

# %% [markdown]
# ## 1. Using Individual Decorators
#
# Let's start by exploring some individual decorators and seeing how they enhance prompts.

# %%
# Import some basic decorators
from prompt_decorators.decorators.generated.decorators.concise import Concise
from prompt_decorators.decorators.generated.decorators.eli5 import ELI5
from prompt_decorators.decorators.generated.decorators.bullet import Bullet

# Create a sample prompt
prompt = "Explain how neural networks work."
print(f"Original prompt: '{prompt}'\n")

# %%
# Example 1: Concise decorator
concise = Concise(max_words=100, bullet_points=False)
concise_prompt = concise.apply(prompt)
print(f"Concise prompt:\n'{concise_prompt}'\n")

# %%
# Example 2: ELI5 decorator
eli5 = ELI5(age=10)
eli5_prompt = eli5.apply(prompt)
print(f"ELI5 prompt:\n'{eli5_prompt}'\n")

# %%
# Example 3: Bullet decorator
bullet = Bullet(style="numbered", max_points=5)
bullet_prompt = bullet.apply(prompt)
print(f"Bullet prompt:\n'{bullet_prompt}'\n")

# %% [markdown]
# ## 2. Combining Decorators
#
# Now, let's explore how to combine multiple decorators to create more sophisticated prompts.

# %%
# Combine ELI5 and Bullet
combined_prompt_1 = bullet.apply(eli5.apply(prompt))
print(f"ELI5 + Bullet prompt:\n'{combined_prompt_1}'\n")

# %%
# Combine Concise and Bullet
combined_prompt_2 = bullet.apply(concise.apply(prompt))
print(f"Concise + Bullet prompt:\n'{combined_prompt_2}'\n")

# %% [markdown]
# ## 3. Using Advanced Decorators
#
# Let's explore some more advanced decorators for specific use cases.

# %%
from prompt_decorators.decorators.generated.decorators.reasoning import Reasoning
from prompt_decorators.decorators.generated.decorators.step_by_step import StepByStep
from prompt_decorators.decorators.generated.decorators.professional import Professional

# Create an advanced prompt
complex_prompt = "Explain the concept of backpropagation in neural networks and how it relates to gradient descent."

# %%
# Example 4: Step-by-Step Reasoning decorator
step_by_step = StepByStep(show_reasoning=True)
step_prompt = step_by_step.apply(complex_prompt)
print(f"Step-by-Step prompt:\n'{step_prompt}'\n")

# %%
# Example 5: Professional decorator
professional = Professional(industry="technology", formality_level=2)
prof_prompt = professional.apply(complex_prompt)
print(f"Professional prompt:\n'{prof_prompt}'\n")

# %%
# Example 6: Complex combination
complex_combination = bullet.apply(
    professional.apply(
        step_by_step.apply(complex_prompt)
    )
)
print(f"Complex combined prompt:\n'{complex_combination}'\n")

# %% [markdown]
# ## 4. Using Meta-Decorators
#
# Meta-decorators provide a way to manage multiple decorators more easily.

# %%
from prompt_decorators.decorators.generated.decorators.meta.chain import Chain

# Create a chain of decorators
chain = Chain(decorators=[
    step_by_step,
    professional,
    bullet
])

chain_prompt = chain.apply(complex_prompt)
print(f"Chain meta-decorator prompt:\n'{chain_prompt}'\n")

# %% [markdown]
# ## 5. Using the Decorator Registry
#
# The decorator registry provides a way to discover and create decorators dynamically.

# %%
from prompt_decorators.utils import get_registry

# Get the registry
registry = get_registry()

# List available categories
categories = registry.get_categories()
print(f"Available decorator categories: {categories}\n")

# %%
# Find decorators by category
reasoning_decorators = registry.find_decorators_by_category("reasoning")
print(f"Reasoning decorators: {reasoning_decorators}\n")

# %%
# Create a decorator using the registry
reasoning = registry.create_decorator("Reasoning", depth="comprehensive")
if reasoning:
    reasoning_prompt = reasoning.apply(prompt)
    print(f"Reasoning prompt from registry:\n'{reasoning_prompt}'\n")

# %% [markdown]
# ## 6. Practical Exercise: Create a Custom Combination
#
# Now it's your turn! Create a custom decorator combination for a specific use case.

# %%
# Import additional decorators you might need
from prompt_decorators.decorators.generated.decorators.schema import Schema
from prompt_decorators.decorators.generated.decorators.audience import Audience

# Create your custom prompt
custom_prompt = "Analyze the advantages and disadvantages of different machine learning frameworks for a production environment."

# TODO: Create and combine decorators for your specific use case
# For example, create a structured comparison aimed at technical managers

# Your code here

# Print the result
# print(f"Custom decorated prompt:\n'{your_decorated_prompt}'\n")

# %% [markdown]
# ## Conclusion
#
# In this notebook, we've explored how to use various decorators in the Prompt Decorators framework
# to enhance LLM prompts. We've seen:
#
# 1. How to use individual decorators
# 2. How to combine multiple decorators
# 3. How to use advanced decorators for specific use cases
# 4. How to use meta-decorators for easier management
# 5. How to use the decorator registry for discovery and creation
#
# These techniques can be applied to a wide range of use cases, from simple prompt enhancement
# to complex, domain-specific applications.

def main():
    """
    Run through all examples in sequence.
    This function is executed when running as a script but not when imported.
    """
    print("Basic Decorator Usage Examples")
    # The code in the cells above would be executed here
    print("Examples completed. For an interactive experience, convert this script to a Jupyter notebook.")


if __name__ == "__main__":
    main() 