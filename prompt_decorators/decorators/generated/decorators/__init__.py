"""
Decorator Classes

This package provides classes for all decorators in the Prompt Decorators specification.
"""

# Import all decorators
from .abductive import Abductive
from .academic import Academic
from .alternatives import Alternatives
from .analogical import Analogical
from .as_expert import AsExpert
from .audience import Audience
from .balanced import Balanced
from .blind_spots import BlindSpots
from .break_and_build import BreakAndBuild
from .build_on import BuildOn
from .bullet import Bullet
from .chain import Chain
from .cite_sources import CiteSources
from .comparison import Comparison
from .compatibility import Compatibility
from .concise import Concise
from .conditional import Conditional
from .confidence import Confidence
from .constraints import Constraints
from .context import Context
from .contrarian import Contrarian
from .creative import Creative
from .custom import Custom
from .debate import Debate
from .decision_matrix import DecisionMatrix
from .decorator_name import DecoratorName
from .deductive import Deductive
from .detailed import Detailed
from .eli5 import ELI5
from .extension import Extension
from .extremes import Extremes
from .fact_check import FactCheck
from .find_gaps import FindGaps
from .first_principles import FirstPrinciples
from .forced_analogy import ForcedAnalogy
from .inductive import Inductive
from .layered import Layered
from .limitations import Limitations
from .mece import MECE
from .motivational import Motivational
from .narrative import Narrative
from .negative_space import NegativeSpace
from .nested import Nested
from .outline import Outline
from .output_format import OutputFormat
from .override import Override
from .peer_review import PeerReview
from .persona import Persona
from .precision import Precision
from .prioritize import Prioritize
from .priority import Priority
from .professional import Professional
from .quality_metrics import QualityMetrics
from .reasoning import Reasoning
from .red_team import RedTeam
from .refine import Refine
from .remix import Remix
from .root_cause import RootCause
from .schema import Schema
from .socratic import Socratic
from .steelman import Steelman
from .step_by_step import StepByStep
from .stress_test import StressTest
from .style_shift import StyleShift
from .summary import Summary
from .table_format import TableFormat
from .timeline import Timeline
from .tone import Tone
from .tree_of_thought import TreeOfThought
from .uncertainty import Uncertainty
from .version import Version

__all__ = [
    "Abductive",
    "Academic",
    "Alternatives",
    "Analogical",
    "AsExpert",
    "Audience",
    "Balanced",
    "BlindSpots",
    "BreakAndBuild",
    "BuildOn",
    "Bullet",
    "Chain",
    "CiteSources",
    "Comparison",
    "Compatibility",
    "Concise",
    "Conditional",
    "Confidence",
    "Constraints",
    "Context",
    "Contrarian",
    "Creative",
    "Custom",
    "Debate",
    "DecisionMatrix",
    "DecoratorName",
    "Deductive",
    "Detailed",
    "ELI5",
    "Extension",
    "Extremes",
    "FactCheck",
    "FindGaps",
    "FirstPrinciples",
    "ForcedAnalogy",
    "Inductive",
    "Layered",
    "Limitations",
    "MECE",
    "Motivational",
    "Narrative",
    "NegativeSpace",
    "Nested",
    "Outline",
    "OutputFormat",
    "Override",
    "PeerReview",
    "Persona",
    "Precision",
    "Prioritize",
    "Priority",
    "Professional",
    "QualityMetrics",
    "Reasoning",
    "RedTeam",
    "Refine",
    "Remix",
    "RootCause",
    "Schema",
    "Socratic",
    "Steelman",
    "StepByStep",
    "StressTest",
    "StyleShift",
    "Summary",
    "TableFormat",
    "Timeline",
    "Tone",
    "TreeOfThought",
    "Uncertainty",
    "Version",
]