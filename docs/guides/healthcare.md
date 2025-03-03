# Healthcare Guide: Using Prompt Decorators in Medical Applications

This guide demonstrates how prompt decorators can enhance healthcare applications by ensuring compliance with regulations, improving the quality of medical information, and maintaining patient privacy. Healthcare professionals and developers can use these techniques to create more effective and responsible AI-assisted healthcare solutions.

## Table of Contents

- [Introduction](#introduction)
- [Regulatory Compliance](#regulatory-compliance)
- [Privacy Protection](#privacy-protection)
- [Medical Accuracy](#medical-accuracy)
- [Patient Communication](#patient-communication)
- [Medical Research](#medical-research)
- [Clinical Decision Support](#clinical-decision-support)
- [Best Practices](#best-practices)
- [Case Studies](#case-studies)

## Introduction

Healthcare applications of AI require special consideration due to regulatory requirements, the sensitive nature of medical data, and the potential impact on patient outcomes. Prompt decorators offer a systematic approach to addressing these challenges by:

1. Enforcing regulatory compliance
2. Protecting patient privacy
3. Ensuring medical accuracy
4. Adapting communication to patient needs
5. Supporting ethical research practices
6. Enhancing clinical decision support

## Regulatory Compliance

Healthcare applications must comply with various regulations such as HIPAA (US), GDPR (EU), and other regional healthcare data protection laws. Decorators can help enforce compliance:

### `ComplianceCheck` Decorator

```python
from prompt_decorators import ComplianceCheck

# Create a HIPAA compliance decorator
hipaa_compliant = ComplianceCheck(
    regulation="HIPAA",
    required_elements=["phi_protection", "minimum_necessary", "authorization"],
    audit_trail=True,
    enforcement_level="strict"
)

# Apply to your prompt
compliant_prompt = hipaa_compliant("Please summarize the patient information")

# The decorator will transform the prompt to ensure compliance
```

### `ConsentVerification` Decorator

```python
from prompt_decorators import ConsentVerification

# Create a consent verification decorator
consent_check = ConsentVerification(
    consent_types=["data_processing", "ai_assistance", "data_sharing"],
    verification_method="explicit",
    record_consent=True
)

# Apply to your interaction
verified_prompt = consent_check("Analyze the following patient data")
```

## Privacy Protection

Protecting patient privacy is paramount in healthcare applications:

### `Anonymizer` Decorator

```python
from prompt_decorators import Anonymizer

# Create an anonymizer for medical data
medical_anonymizer = Anonymizer(
    entities=["name", "address", "phone", "email", "mrn", "ssn", "dob"],
    method="replacement",  # Alternatives: "redaction", "generalization"
    preserve_medical_context=True
)

# Apply to a prompt containing sensitive information
anonymized_prompt = medical_anonymizer("Patient John Doe (DOB: 01/15/1980) has been diagnosed with hypertension")

# Results in: "Patient [NAME] (DOB: [DATE]) has been diagnosed with hypertension"
```

### `MinimumNecessary` Decorator

```python
from prompt_decorators import MinimumNecessary

# Create a minimum necessary decorator
min_necessary = MinimumNecessary(
    purpose="treatment",  # Alternatives: "payment", "operations", "research"
    role="physician",  # User role determines access level
    data_categories=["diagnosis", "medications", "vitals"]
)

# Apply to reduce information to only what's necessary
filtered_prompt = min_necessary("Patient has hypertension, diabetes, financial issues, and family problems")

# Results in only sharing medically relevant information for treatment
```

## Medical Accuracy

Ensuring medical information is accurate and evidence-based:

### `EvidenceBased` Decorator

```python
from prompt_decorators import EvidenceBased

# Create an evidence-based medicine decorator
evidence_based = EvidenceBased(
    evidence_level="high",  # Requires high-quality evidence
    citation_required=True,
    recency_threshold=2,  # Max 2 years old
    medical_guidelines=["AMA", "WHO"]
)

# Apply to medical information
validated_prompt = evidence_based("Recommend treatment for acute myocardial infarction")
```

### `MedicalDisclaimers` Decorator

```python
from prompt_decorators import MedicalDisclaimers

# Create appropriate medical disclaimers
disclaimers = MedicalDisclaimers(
    include=["not_medical_advice", "consult_physician", "emergency_warning"],
    placement="prefix",  # Alternatives: "suffix", "both"
    emphasis_level="high"
)

# Apply to outputs
disclaimed_output = disclaimers("Based on the symptoms described, this could be symptoms of several conditions")
```

## Patient Communication

Adapting communication for different patient needs:

### `HealthLiteracy` Decorator

```python
from prompt_decorators import HealthLiteracy, Chain

# Create a health literacy level adapter
literacy_adapter = HealthLiteracy(
    level="low",  # Alternatives: "medium", "high"
    simplify_terms=True,
    include_explanations=True,
    visual_aids=True
)

# Combine with other decorators
patient_communication = Chain([
    literacy_adapter,
    EvidenceBased(evidence_level="high"),
    MedicalDisclaimers()
])

# Apply to patient information
patient_friendly = patient_communication("The patient has been diagnosed with hypertension")
```

### `CulturallySensitive` Decorator

```python
from prompt_decorators import CulturallySensitive

# Create culturally sensitive communication
cultural_adapter = CulturallySensitive(
    language="spanish",
    cultural_context="hispanic",
    health_beliefs=True,
    localize_examples=True
)

# Apply to health information
culturally_adapted = cultural_adapter("Here's information about managing diabetes through diet")
```

## Medical Research

Supporting ethical and effective medical research:

### `ResearchProtocol` Decorator

```python
from prompt_decorators import ResearchProtocol

# Create a research protocol decorator
protocol = ResearchProtocol(
    irb_approved=True,
    protocol_id="MED-2023-456",
    study_phase="clinical_trial_3",
    inclusion_criteria=["age>=18", "diagnosed_hypertension"],
    exclusion_criteria=["pregnant", "severe_comorbidities"]
)

# Apply to research queries
research_prompt = protocol("Analyze the relationship between medication adherence and blood pressure control")
```

### `BlindedAnalysis` Decorator

```python
from prompt_decorators import BlindedAnalysis

# Create a blinded analysis decorator
blinded = BlindedAnalysis(
    blind_level="double",  # Double-blind study
    group_anonymization=True,
    prevent_unblinding=True
)

# Apply to analysis prompts
blinded_analysis = blinded("Compare outcomes between treatment and control groups")
```

## Clinical Decision Support

Enhancing clinical decision-making:

### `ClinicalGuidelines` Decorator

```python
from prompt_decorators import ClinicalGuidelines

# Create a clinical guidelines decorator
guidelines = ClinicalGuidelines(
    source="ACC/AHA",  # American College of Cardiology/American Heart Association
    condition="hypertension",
    year=2023,
    recommendation_strength="strong"
)

# Apply to treatment recommendations
guideline_based = guidelines("Recommend treatment for a 65-year-old with stage 2 hypertension")
```

### `DiagnosticAccuracy` Decorator

```python
from prompt_decorators import DiagnosticAccuracy

# Create a diagnostic accuracy enhancer
diagnostic = DiagnosticAccuracy(
    sensitivity_specificity=True,
    differential_diagnosis=True,
    confidence_levels=True,
    test_recommendations=True
)

# Apply to diagnostic assistance
accurate_diagnosis = diagnostic("Patient presents with chest pain, shortness of breath, and diaphoresis")
```

## Best Practices

For optimal use of prompt decorators in healthcare:

1. **Prioritize patient safety**: Always include appropriate disclaimers and ensure medical accuracy
2. **Layer compliance measures**: Use multiple compliance and privacy decorators together
3. **Adapt to the audience**: Use different decorators for patients vs. healthcare professionals
4. **Document everything**: Maintain records of prompts, decorators used, and responses for audit purposes
5. **Regular updates**: Keep medical information and guidelines current
6. **Test with clinicians**: Validate decorator effectiveness with healthcare professionals
7. **Transparency**: Make it clear to users when AI is being used and how information is processed
8. **Feedback loop**: Create mechanisms for reporting inaccuracies or compliance issues
9. **Local regulations**: Adapt decorators to comply with local healthcare regulations
10. **Emergency protocols**: Include clear warnings for emergency situations requiring immediate care

## Case Studies

### Telehealth Triage System

```python
from prompt_decorators import Chain, SymptomAnalysis, Urgency, HealthLiteracy, MedicalDisclaimers

# Create a telehealth triage system
triage_system = Chain([
    HealthLiteracy(level="medium"),
    SymptomAnalysis(comprehensive=True),
    Urgency(levels=["emergency", "urgent", "routine", "self-care"]),
    MedicalDisclaimers(include=["emergency_warning", "not_diagnosis"])
])

# Apply to patient-reported symptoms
triage_response = triage_system("I've been having severe chest pain radiating to my left arm for the last hour")
```

### Clinical Documentation Assistant

```python
from prompt_decorators import Chain, MedicalCoding, StructuredNote, ComplianceCheck

# Create a clinical documentation assistant
documentation_assistant = Chain([
    StructuredNote(format="SOAP"),
    MedicalCoding(systems=["ICD-10", "CPT"]),
    ComplianceCheck(regulation="HIPAA")
])

# Apply to clinical notes
structured_note = documentation_assistant("Patient presented with fever and cough. Diagnosed with acute bronchitis. Prescribed amoxicillin.")
```

By following this guide, healthcare professionals and developers can leverage prompt decorators to build more effective, compliant, and patient-centered healthcare applications.

## Additional Resources

- [Prompt Decorators Documentation](../index.md)
- [HIPAA Compliance Guide](../compliance/hipaa.md)
- [Medical Accuracy Decorators](../api/medical_decorators.md)
- [Patient Communication Tutorial](../tutorials/patient_communication.md)
