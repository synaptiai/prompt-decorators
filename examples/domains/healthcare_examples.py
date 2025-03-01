#!/usr/bin/env python
"""
Healthcare-Specific Decorator Examples

This script demonstrates how to use the Prompt Decorators framework
for healthcare-specific applications, such as medical documentation,
patient education, and clinical decision support.
"""

import sys
from pathlib import Path

# Add the project root to the Python path
project_root = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(project_root))

from prompt_decorators.decorators.generated.decorators.professional import Professional
from prompt_decorators.decorators.generated.decorators.eli5 import ELI5
from prompt_decorators.decorators.generated.decorators.fact_check import FactCheck
from prompt_decorators.decorators.generated.decorators.schema import Schema
from prompt_decorators.decorators.generated.decorators.limitations import Limitations
from prompt_decorators.decorators.generated.decorators.bullet import Bullet
from prompt_decorators.decorators.generated.decorators.balanced import Balanced
from prompt_decorators.decorators.generated.decorators.audience import Audience
from prompt_decorators.decorators.generated.decorators.step_by_step import StepByStep
from prompt_decorators.decorators.generated.decorators.meta.chain import Chain
from prompt_decorators.utils import get_registry


def medical_documentation_example():
    """
    Example of using decorators for generating structured medical documentation.
    """
    print("\n=== Medical Documentation Example ===\n")
    
    # Create a schema for SOAP notes (Subjective, Objective, Assessment, Plan)
    soap_schema = Schema(schema={
        "subjective": "string",
        "objective": {
            "vital_signs": {
                "blood_pressure": "string",
                "heart_rate": "string",
                "respiratory_rate": "string",
                "temperature": "string",
                "oxygen_saturation": "string"
            },
            "physical_examination": ["string"]
        },
        "assessment": ["string"],
        "plan": ["string"],
        "follow_up": "string"
    })
    
    # Create a professional decorator for medical context
    professional = Professional(
        industry="healthcare",
        formality_level=3
    )
    
    # Create a fact-checking decorator to ensure accuracy
    fact_check = FactCheck(
        verification_level=3,
        cite_sources=True
    )
    
    # Combine decorators
    prompt = "Create a medical note for a 45-year-old male patient with type 2 diabetes presenting with increased thirst, frequent urination, and a non-healing foot ulcer."
    
    # Apply decorators in sequence
    decorated_prompt = soap_schema.apply(
        fact_check.apply(
            professional.apply(prompt)
        )
    )
    
    print("Original prompt:")
    print(f"  \"{prompt}\"\n")
    
    print("Decorated prompt:")
    print(f"  \"{decorated_prompt}\"")


def patient_education_example():
    """
    Example of using decorators for patient education materials.
    """
    print("\n=== Patient Education Example ===\n")
    
    # Create decorators for patient education
    eli5 = ELI5(age=14)  # Aim for high school reading level
    bullet = Bullet(style="dash")
    balanced = Balanced(
        perspectives=["benefits", "risks", "alternatives"]
    )
    
    # Combine decorators for patient education
    prompt = "Explain the process and implications of taking statin medications for high cholesterol."
    
    # Apply decorators in sequence
    decorated_prompt = bullet.apply(
        balanced.apply(
            eli5.apply(prompt)
        )
    )
    
    print("Original prompt:")
    print(f"  \"{prompt}\"\n")
    
    print("Decorated prompt:")
    print(f"  \"{decorated_prompt}\"")


def clinical_decision_support_example():
    """
    Example of using decorators for clinical decision support.
    """
    print("\n=== Clinical Decision Support Example ===\n")
    
    # Create decorators for clinical decision support
    step_by_step = StepByStep(
        show_reasoning=True,
        steps=["data analysis", "differential diagnosis", "recommended actions"]
    )
    
    professional = Professional(
        industry="healthcare",
        formality_level=2
    )
    
    limitations = Limitations(
        highlight_uncertainties=True,
        include_disclaimer=True
    )
    
    # Create a schema for the assessment output
    assessment_schema = Schema(schema={
        "differential_diagnosis": ["string"],
        "recommended_tests": ["string"],
        "treatment_options": ["string"],
        "red_flags": ["string"],
        "references": ["string"]
    })
    
    # Combine decorators for clinical decision support
    prompt = "Analyze a case of a 58-year-old female with sudden onset chest pain radiating to the left arm, shortness of breath, and nausea."
    
    # Apply decorators in sequence
    decorated_prompt = assessment_schema.apply(
        limitations.apply(
            professional.apply(
                step_by_step.apply(prompt)
            )
        )
    )
    
    print("Original prompt:")
    print(f"  \"{prompt}\"\n")
    
    print("Decorated prompt:")
    print(f"  \"{decorated_prompt}\"")


def medical_research_summary_example():
    """
    Example of using decorators for summarizing medical research.
    """
    print("\n=== Medical Research Summary Example ===\n")
    
    # Create audience-specific decorator
    audience = Audience(
        audience_type="healthcare_professionals",
        expertise_level="expert",
        role="researcher"
    )
    
    # Create decorators for research summary
    fact_check = FactCheck(
        verification_level=3,
        cite_sources=True
    )
    
    balanced = Balanced(
        perspectives=["strengths", "limitations", "practical implications"]
    )
    
    # Chain the decorators
    chain = Chain(decorators=[
        audience,
        fact_check,
        balanced
    ])
    
    # Apply to a research summary prompt
    prompt = "Summarize the current research on mRNA vaccine technology and its applications beyond COVID-19."
    decorated_prompt = chain.apply(prompt)
    
    print("Original prompt:")
    print(f"  \"{prompt}\"\n")
    
    print("Decorated prompt:")
    print(f"  \"{decorated_prompt}\"")


def patient_communication_example():
    """
    Example of using decorators for patient communication.
    """
    print("\n=== Patient Communication Example ===\n")
    
    # Get registry for accessing decorators by name
    registry = get_registry()
    
    # Create empathetic decorator (assuming it exists in the registry)
    empathetic = registry.create_decorator(
        "Empathetic",
        empathy_level=3,
        acknowledge_emotions=True
    )
    
    # Create other decorators
    eli5 = ELI5(age=12)
    step_by_step = StepByStep(
        show_reasoning=False,  # Don't show medical reasoning to patient
        steps=["explanation", "next steps", "follow-up care"]
    )
    
    # Apply decorators for patient communication
    prompt = "Explain to a patient that their biopsy results indicate early-stage breast cancer and the recommended treatment options."
    
    # Apply decorators in sequence (if empathetic exists, otherwise skip it)
    if empathetic:
        decorated_prompt = step_by_step.apply(
            eli5.apply(
                empathetic.apply(prompt)
            )
        )
    else:
        decorated_prompt = step_by_step.apply(
            eli5.apply(prompt)
        )
    
    print("Original prompt:")
    print(f"  \"{prompt}\"\n")
    
    print("Decorated prompt:")
    print(f"  \"{decorated_prompt}\"")


def main():
    """Run all healthcare examples."""
    print("=== Healthcare-Specific Decorator Examples ===")
    
    medical_documentation_example()
    patient_education_example()
    clinical_decision_support_example()
    medical_research_summary_example()
    patient_communication_example()
    
    print("\nAll examples completed successfully.")


if __name__ == "__main__":
    main() 