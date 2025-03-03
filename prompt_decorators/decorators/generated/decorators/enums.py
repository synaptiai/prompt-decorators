"""Decorator Enum Definitions.

This module provides enum types used by decorators.
"""

from enum import Enum, auto
from typing import Any, Dict, List, Optional, Union


class AudienceLevelEnum(Enum):
    """The expertise level of the target audience."""

    beginner = auto()
    intermediate = auto()
    expert = auto()
    technical = auto()


class MotivationalIntensityEnum(Enum):
    """The level of motivational energy and enthusiasm."""

    mild = auto()
    moderate = auto()
    high = auto()


class MotivationalFocusEnum(Enum):
    """The primary motivational approach to emphasize."""

    achievement = auto()
    growth = auto()
    resilience = auto()
    purpose = auto()
    balanced = auto()


class StyleShiftAspectEnum(Enum):
    """The specific style aspect to modify."""

    formality = auto()
    persuasion = auto()
    urgency = auto()
    confidence = auto()
    complexity = auto()


class DetailedDepthEnum(Enum):
    """The level of detail and comprehensiveness."""

    moderate = auto()
    comprehensive = auto()
    exhaustive = auto()


class RemixPreserveEnum(Enum):
    """What aspects of the original content to prioritize preserving."""

    facts = auto()
    structure = auto()
    tone = auto()
    comprehensiveness = auto()


class AsExpertExperienceEnum(Enum):
    """The experience level of the expert."""

    junior = auto()
    senior = auto()
    leading = auto()
    pioneering = auto()


class NarrativeStructureEnum(Enum):
    """The narrative structure to employ."""

    classic = auto()
    nonlinear = auto()
    case_study = auto()


class NarrativeLengthEnum(Enum):
    """The relative length of the narrative."""

    brief = auto()
    moderate = auto()
    extended = auto()


class AcademicStyleEnum(Enum):
    """The academic discipline style to follow."""

    humanities = auto()
    scientific = auto()
    legal = auto()


class AcademicFormatEnum(Enum):
    """The citation format to use for references."""

    APA = auto()
    MLA = auto()
    Chicago = auto()
    Harvard = auto()
    IEEE = auto()


class CreativeLevelEnum(Enum):
    """The degree of creative thinking to apply."""

    moderate = auto()
    high = auto()
    unconventional = auto()


class ProfessionalFormalityEnum(Enum):
    """The level of formality to maintain in the response."""

    standard = auto()
    high = auto()
    executive = auto()


class ConciseLevelEnum(Enum):
    """The degree of conciseness to apply."""

    moderate = auto()
    high = auto()
    extreme = auto()


class ExtremesVersionsEnum(Enum):
    """Which extreme versions to include."""

    radical = auto()
    minimal = auto()
    both = auto()


class PriorityModeEnum(Enum):
    """How to handle conflicts between decorators."""

    override = auto()
    merge = auto()
    cascade = auto()


class ContextScopeEnum(Enum):
    """Which aspects of decorators to contextualize."""

    terminology = auto()
    examples = auto()
    structure = auto()
    all = auto()


class ContextLevelEnum(Enum):
    """The expertise level to target within the domain."""

    beginner = auto()
    intermediate = auto()
    expert = auto()
    mixed = auto()


class CustomPriorityEnum(Enum):
    """How to prioritize custom rules relative to other decorators."""

    override = auto()
    supplement = auto()
    fallback = auto()


class BuildOnReferenceEnum(Enum):
    """What to build upon from the previous context."""

    last = auto()
    specific = auto()
    all = auto()


class BuildOnApproachEnum(Enum):
    """How to build upon the referenced content."""

    extend = auto()
    refine = auto()
    contrast = auto()
    synthesize = auto()


class ReasoningDepthEnum(Enum):
    """The level of detail in the reasoning process."""

    basic = auto()
    moderate = auto()
    comprehensive = auto()


class ToneStyleEnum(Enum):
    """The desired tone and style for the response."""

    formal = auto()
    casual = auto()
    friendly = auto()
    technical = auto()
    humorous = auto()


class OutputFormatFormatEnum(Enum):
    """The format to use for the response."""

    json = auto()
    markdown = auto()
    yaml = auto()
    xml = auto()
    plaintext = auto()


class BlindSpotsDepthEnum(Enum):
    """How thoroughly to analyze for blind spots."""

    basic = auto()
    thorough = auto()
    comprehensive = auto()


class BlindSpotsPositionEnum(Enum):
    """Where to place the blind spots analysis."""

    after = auto()
    before = auto()
    integrated = auto()


class ForcedAnalogyComprehensivenessEnum(Enum):
    """How comprehensively to map concepts between domains."""

    basic = auto()
    comprehensive = auto()
    detailed = auto()


class InductiveStructureEnum(Enum):
    """The pattern of inductive reasoning to follow."""

    generalization = auto()
    causal = auto()
    statistical = auto()
    analogical = auto()


class RootCauseMethodEnum(Enum):
    """The specific root cause analysis methodology to apply."""

    fivewhys = auto()
    fishbone = auto()
    pareto = auto()


class AnalogicalDepthEnum(Enum):
    """Level of detail in developing the analogy."""

    brief = auto()
    moderate = auto()
    extended = auto()


class ContrarianApproachEnum(Enum):
    """The specific contrarian approach to take."""

    outsider = auto()
    skeptic = auto()
    devils_advocate = auto()


class RedTeamStrengthEnum(Enum):
    """How aggressive or challenging the red team analysis should be."""

    moderate = auto()
    aggressive = auto()
    steelman = auto()


class NegativeSpaceFocusEnum(Enum):
    """The specific aspect of negative space to emphasize."""

    implications = auto()
    missing = auto()
    unstated = auto()
    comprehensive = auto()


class NegativeSpaceDepthEnum(Enum):
    """How deeply to explore the negative space."""

    surface = auto()
    moderate = auto()
    deep = auto()


class NegativeSpaceStructureEnum(Enum):
    """How to present the negative space analysis."""

    before = auto()
    after = auto()
    integrated = auto()
    separate = auto()


class FactCheckUncertainEnum(Enum):
    """How to handle uncertain information."""

    mark = auto()
    exclude = auto()
    qualify = auto()


class FactCheckStrictnessEnum(Enum):
    """The threshold for considering information verified."""

    low = auto()
    moderate = auto()
    high = auto()


class LimitationsDetailEnum(Enum):
    """The level of detail in the limitations statement."""

    brief = auto()
    moderate = auto()
    comprehensive = auto()


class LimitationsPositionEnum(Enum):
    """Where to place the limitations statement in the response."""

    beginning = auto()
    end = auto()


class LimitationsFocusEnum(Enum):
    """The primary aspect to focus on in the limitations."""

    knowledge = auto()
    methodology = auto()
    context = auto()
    biases = auto()
    all = auto()


class BreakAndBuildBreakdownEnum(Enum):
    """Primary approach for the critical breakdown phase."""

    weaknesses = auto()
    assumptions = auto()
    risks = auto()
    comprehensive = auto()


class BreakAndBuildIntensityEnum(Enum):
    """How thorough and challenging the breakdown phase should be."""

    mild = auto()
    thorough = auto()
    intense = auto()


class StressTestSeverityEnum(Enum):
    """The intensity level of the stress conditions."""

    moderate = auto()
    severe = auto()
    extreme = auto()


class UncertaintyFormatEnum(Enum):
    """How to format uncertainty indications in the response."""

    inline = auto()
    section = auto()
    confidence = auto()


class UncertaintyThresholdEnum(Enum):
    """The threshold for flagging uncertain content."""

    low = auto()
    medium = auto()
    high = auto()


class FindGapsAspectsEnum(Enum):
    """The specific types of gaps to focus on finding."""

    questions = auto()
    resources = auto()
    stakeholders = auto()
    risks = auto()
    dependencies = auto()
    comprehensive = auto()


class FindGapsDepthEnum(Enum):
    """How thoroughly to analyze for gaps."""

    basic = auto()
    thorough = auto()
    exhaustive = auto()


class CiteSourcesStyleEnum(Enum):
    """The placement and format of citations within the response."""

    inline = auto()
    footnote = auto()
    endnote = auto()


class CiteSourcesFormatEnum(Enum):
    """The citation format to use."""

    APA = auto()
    MLA = auto()
    Chicago = auto()
    Harvard = auto()
    IEEE = auto()


class QualityMetricsScaleEnum(Enum):
    """Rating scale to use for evaluations."""

    _1_5 = auto()
    _1_10 = auto()
    percentage = auto()
    qualitative = auto()


class BalancedStructureEnum(Enum):
    """How to structure the different perspectives."""

    alternating = auto()
    sequential = auto()
    comparative = auto()


class PeerReviewCriteriaEnum(Enum):
    """Primary criteria to focus on in the review."""

    accuracy = auto()
    methodology = auto()
    limitations = auto()
    completeness = auto()
    all = auto()


class PeerReviewStyleEnum(Enum):
    """The tone and approach of the peer review."""

    constructive = auto()
    critical = auto()
    balanced = auto()


class PeerReviewPositionEnum(Enum):
    """Where to place the peer review relative to the main content."""

    after = auto()
    before = auto()
    alongside = auto()


class ConfidenceScaleEnum(Enum):
    """The method used to express confidence levels."""

    percent = auto()
    qualitative = auto()
    stars = auto()
    numeric = auto()


class PrecisionLevelEnum(Enum):
    """The degree of precision to apply."""

    moderate = auto()
    high = auto()
    scientific = auto()


class AlternativesDiversityEnum(Enum):
    """How different or varied the alternatives should be from each other."""

    low = auto()
    medium = auto()
    high = auto()


class SummaryLengthEnum(Enum):
    """Relative length of the summary."""

    short = auto()
    medium = auto()
    long = auto()


class SummaryPositionEnum(Enum):
    """Where to position the summary in relation to any full content."""

    beginning = auto()
    end = auto()
    standalone = auto()


class NestedStyleEnum(Enum):
    """Visual style for hierarchical levels."""

    bullet = auto()
    numbered = auto()
    mixed = auto()


class TableFormatFormatEnum(Enum):
    """Format style for the table representation."""

    markdown = auto()
    ascii = auto()
    csv = auto()


class TableFormatAlignmentEnum(Enum):
    """Text alignment within table cells."""

    left = auto()
    center = auto()
    right = auto()


class LayeredLevelsEnum(Enum):
    """The granularity of explanation levels to include."""

    sentence_paragraph_full = auto()
    basic_intermediate_advanced = auto()
    summary_detail_technical = auto()


class LayeredProgressionEnum(Enum):
    """How to structure the progression between layers."""

    separate = auto()
    nested = auto()
    incremental = auto()


class ComparisonFormatEnum(Enum):
    """The presentation format for the comparison."""

    table = auto()
    prose = auto()
    bullets = auto()


class BulletStyleEnum(Enum):
    """The visual marker used for bullet points."""

    dash = auto()
    dot = auto()
    arrow = auto()
    star = auto()
    plus = auto()


class OutlineStyleEnum(Enum):
    """Numbering or bullet style for the outline."""

    numeric = auto()
    bullet = auto()
    roman = auto()
    alpha = auto()
    mixed = auto()


class TimelineGranularityEnum(Enum):
    """The level of time detail to include in the timeline."""

    day = auto()
    month = auto()
    year = auto()
    decade = auto()
    century = auto()
    era = auto()


class TimelineFormatEnum(Enum):
    """The presentation format for the timeline."""

    list = auto()
    narrative = auto()
    table = auto()


class TimelineDetailsEnum(Enum):
    """The level of detail to include for each timeline event."""

    minimal = auto()
    moderate = auto()
    comprehensive = auto()


class MECEFrameworkEnum(Enum):
    """Optional predefined MECE framework to apply."""

    issue_tree = auto()
    value_chain = auto()
    business_segments = auto()
    stakeholders = auto()
    custom = auto()


class DecisionMatrixScaleEnum(Enum):
    """Rating scale to use for evaluations."""

    _1_5 = auto()
    _1_10 = auto()
    qualitative = auto()
    percentage = auto()


class ConstraintsVocabularyEnum(Enum):
    """Constraints on vocabulary usage."""

    simple = auto()
    technical = auto()
    domain_specific = auto()
    creative = auto()
