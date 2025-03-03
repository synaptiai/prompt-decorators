"""
Decorator Enum Definitions

This module provides enum types used by decorators.
"""

from enum import Enum


class AcademicCitationstyleEnum(str, Enum):
    """The citation format to use for references"""
    APA = "APA"
    MLA = "MLA"
    CHICAGO = "Chicago"
    HARVARD = "Harvard"
    IEEE = "IEEE"

class AcademicStyleEnum(str, Enum):
    """The academic discipline style to follow"""
    HUMANITIES = "humanities"
    SCIENTIFIC = "scientific"
    LEGAL = "legal"

class AlternativesDiversityEnum(str, Enum):
    """How different or varied the alternatives should be from each other"""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class AnalogicalDepthEnum(str, Enum):
    """Level of detail in developing the analogy"""
    BRIEF = "brief"
    MODERATE = "moderate"
    EXTENDED = "extended"

class AsExpertExperienceEnum(str, Enum):
    """The experience level of the expert"""
    JUNIOR = "junior"
    SENIOR = "senior"
    LEADING = "leading"
    PIONEERING = "pioneering"

class AudienceLevelEnum(str, Enum):
    """The expertise level of the target audience"""
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    EXPERT = "expert"
    TECHNICAL = "technical"

class BalancedStructureEnum(str, Enum):
    """How to structure the different perspectives"""
    ALTERNATING = "alternating"
    SEQUENTIAL = "sequential"
    COMPARATIVE = "comparative"

class BlindSpotsDepthEnum(str, Enum):
    """How thoroughly to analyze for blind spots"""
    BASIC = "basic"
    THOROUGH = "thorough"
    COMPREHENSIVE = "comprehensive"

class BlindSpotsPositionEnum(str, Enum):
    """Where to place the blind spots analysis"""
    AFTER = "after"
    BEFORE = "before"
    INTEGRATED = "integrated"

class BreakAndBuildBreakdownEnum(str, Enum):
    """Primary approach for the critical breakdown phase"""
    WEAKNESSES = "weaknesses"
    ASSUMPTIONS = "assumptions"
    RISKS = "risks"
    COMPREHENSIVE = "comprehensive"

class BreakAndBuildIntensityEnum(str, Enum):
    """How thorough and challenging the breakdown phase should be"""
    MILD = "mild"
    THOROUGH = "thorough"
    INTENSE = "intense"

class BuildOnApproachEnum(str, Enum):
    """How to build upon the referenced content"""
    EXTEND = "extend"
    REFINE = "refine"
    CONTRAST = "contrast"
    SYNTHESIZE = "synthesize"

class BuildOnReferenceEnum(str, Enum):
    """What to build upon from the previous context"""
    LAST = "last"
    SPECIFIC = "specific"
    ALL = "all"

class BulletStyleEnum(str, Enum):
    """The visual marker used for bullet points"""
    DASH = "dash"
    DOT = "dot"
    ARROW = "arrow"
    STAR = "star"
    PLUS = "plus"

class CiteSourcesFormatEnum(str, Enum):
    """The citation format to use"""
    APA = "APA"
    MLA = "MLA"
    CHICAGO = "Chicago"
    HARVARD = "Harvard"
    IEEE = "IEEE"

class CiteSourcesStyleEnum(str, Enum):
    """The placement and format of citations within the response"""
    INLINE = "inline"
    FOOTNOTE = "footnote"
    ENDNOTE = "endnote"

class ComparisonFormatEnum(str, Enum):
    """The presentation format for the comparison"""
    TABLE = "table"
    PROSE = "prose"
    BULLETS = "bullets"

class ConciseLevelEnum(str, Enum):
    """The degree of conciseness to apply"""
    MODERATE = "moderate"
    HIGH = "high"
    EXTREME = "extreme"

class ConfidenceScaleEnum(str, Enum):
    """The method used to express confidence levels"""
    PERCENT = "percent"
    QUALITATIVE = "qualitative"
    STARS = "stars"
    NUMERIC = "numeric"

class ConstraintsVocabularyEnum(str, Enum):
    """Constraints on vocabulary usage"""
    SIMPLE = "simple"
    TECHNICAL = "technical"
    DOMAIN_SPECIFIC = "domain-specific"
    CREATIVE = "creative"

class ContextLevelEnum(str, Enum):
    """The expertise level to target within the domain"""
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    EXPERT = "expert"
    MIXED = "mixed"

class ContextScopeEnum(str, Enum):
    """Which aspects of decorators to contextualize"""
    TERMINOLOGY = "terminology"
    EXAMPLES = "examples"
    STRUCTURE = "structure"
    ALL = "all"

class ContrarianApproachEnum(str, Enum):
    """The specific contrarian approach to take"""
    OUTSIDER = "outsider"
    SKEPTIC = "skeptic"
    DEVILS_ADVOCATE = "devils-advocate"

class CreativeLevelEnum(str, Enum):
    """The degree of creative thinking to apply"""
    MODERATE = "moderate"
    HIGH = "high"
    UNCONVENTIONAL = "unconventional"

class CustomPriorityEnum(str, Enum):
    """How to prioritize custom rules relative to other decorators"""
    OVERRIDE = "override"
    SUPPLEMENT = "supplement"
    FALLBACK = "fallback"

class DecisionMatrixScaleEnum(str, Enum):
    """Rating scale to use for evaluations"""
    VALUE_1_5 = "1-5"
    VALUE_1_10 = "1-10"
    QUALITATIVE = "qualitative"
    PERCENTAGE = "percentage"

class DetailedDepthEnum(str, Enum):
    """The level of detail and comprehensiveness"""
    MODERATE = "moderate"
    COMPREHENSIVE = "comprehensive"
    EXHAUSTIVE = "exhaustive"

class ExtremesVersionsEnum(str, Enum):
    """Which extreme versions to include"""
    RADICAL = "radical"
    MINIMAL = "minimal"
    BOTH = "both"

class FactCheckStrictnessEnum(str, Enum):
    """The threshold for considering information verified"""
    LOW = "low"
    MODERATE = "moderate"
    HIGH = "high"

class FactCheckUncertainEnum(str, Enum):
    """How to handle uncertain information"""
    MARK = "mark"
    EXCLUDE = "exclude"
    QUALIFY = "qualify"

class FindGapsAspectsEnum(str, Enum):
    """The specific types of gaps to focus on finding"""
    QUESTIONS = "questions"
    RESOURCES = "resources"
    STAKEHOLDERS = "stakeholders"
    RISKS = "risks"
    DEPENDENCIES = "dependencies"
    COMPREHENSIVE = "comprehensive"

class FindGapsDepthEnum(str, Enum):
    """How thoroughly to analyze for gaps"""
    BASIC = "basic"
    THOROUGH = "thorough"
    EXHAUSTIVE = "exhaustive"

class ForcedAnalogyComprehensivenessEnum(str, Enum):
    """How comprehensively to map concepts between domains"""
    BASIC = "basic"
    COMPREHENSIVE = "comprehensive"
    DETAILED = "detailed"

class InductiveStructureEnum(str, Enum):
    """The pattern of inductive reasoning to follow"""
    GENERALIZATION = "generalization"
    CAUSAL = "causal"
    STATISTICAL = "statistical"
    ANALOGICAL = "analogical"

class LayeredLevelsEnum(str, Enum):
    """The granularity of explanation levels to include"""
    SENTENCE_PARAGRAPH_FULL = "sentence-paragraph-full"
    BASIC_INTERMEDIATE_ADVANCED = "basic-intermediate-advanced"
    SUMMARY_DETAIL_TECHNICAL = "summary-detail-technical"

class LayeredProgressionEnum(str, Enum):
    """How to structure the progression between layers"""
    SEPARATE = "separate"
    NESTED = "nested"
    INCREMENTAL = "incremental"

class LimitationsDetailEnum(str, Enum):
    """The level of detail in the limitations statement"""
    BRIEF = "brief"
    MODERATE = "moderate"
    COMPREHENSIVE = "comprehensive"

class LimitationsFocusEnum(str, Enum):
    """The primary aspect to focus on in the limitations"""
    KNOWLEDGE = "knowledge"
    METHODOLOGY = "methodology"
    CONTEXT = "context"
    BIASES = "biases"
    ALL = "all"

class LimitationsPositionEnum(str, Enum):
    """Where to place the limitations statement in the response"""
    BEGINNING = "beginning"
    END = "end"

class MECEFrameworkEnum(str, Enum):
    """Optional predefined MECE framework to apply"""
    ISSUE_TREE = "issue tree"
    VALUE_CHAIN = "value chain"
    BUSINESS_SEGMENTS = "business segments"
    STAKEHOLDERS = "stakeholders"
    CUSTOM = "custom"

class MotivationalFocusEnum(str, Enum):
    """The primary motivational approach to emphasize"""
    ACHIEVEMENT = "achievement"
    GROWTH = "growth"
    RESILIENCE = "resilience"
    PURPOSE = "purpose"
    BALANCED = "balanced"

class MotivationalIntensityEnum(str, Enum):
    """The level of motivational energy and enthusiasm"""
    MILD = "mild"
    MODERATE = "moderate"
    HIGH = "high"

class NarrativeLengthEnum(str, Enum):
    """The relative length of the narrative"""
    BRIEF = "brief"
    MODERATE = "moderate"
    EXTENDED = "extended"

class NarrativeStructureEnum(str, Enum):
    """The narrative structure to employ"""
    CLASSIC = "classic"
    NONLINEAR = "nonlinear"
    CASE_STUDY = "case-study"

class NegativeSpaceDepthEnum(str, Enum):
    """How deeply to explore the negative space"""
    SURFACE = "surface"
    MODERATE = "moderate"
    DEEP = "deep"

class NegativeSpaceFocusEnum(str, Enum):
    """The specific aspect of negative space to emphasize"""
    IMPLICATIONS = "implications"
    MISSING = "missing"
    UNSTATED = "unstated"
    COMPREHENSIVE = "comprehensive"

class NegativeSpaceStructureEnum(str, Enum):
    """How to present the negative space analysis"""
    BEFORE = "before"
    AFTER = "after"
    INTEGRATED = "integrated"
    SEPARATE = "separate"

class NestedStyleEnum(str, Enum):
    """Visual style for hierarchical levels"""
    BULLET = "bullet"
    NUMBERED = "numbered"
    MIXED = "mixed"

class OutlineStyleEnum(str, Enum):
    """Numbering or bullet style for the outline"""
    NUMERIC = "numeric"
    BULLET = "bullet"
    ROMAN = "roman"
    ALPHA = "alpha"
    MIXED = "mixed"

class OutputFormatFormatEnum(str, Enum):
    """The format to use for the response"""
    JSON = "json"
    MARKDOWN = "markdown"
    YAML = "yaml"
    XML = "xml"
    PLAINTEXT = "plaintext"

class PeerReviewCriteriaEnum(str, Enum):
    """Primary criteria to focus on in the review"""
    ACCURACY = "accuracy"
    METHODOLOGY = "methodology"
    LIMITATIONS = "limitations"
    COMPLETENESS = "completeness"
    ALL = "all"

class PeerReviewPositionEnum(str, Enum):
    """Where to place the peer review relative to the main content"""
    AFTER = "after"
    BEFORE = "before"
    ALONGSIDE = "alongside"

class PeerReviewStyleEnum(str, Enum):
    """The tone and approach of the peer review"""
    CONSTRUCTIVE = "constructive"
    CRITICAL = "critical"
    BALANCED = "balanced"

class PrecisionLevelEnum(str, Enum):
    """The degree of precision to apply"""
    MODERATE = "moderate"
    HIGH = "high"
    SCIENTIFIC = "scientific"

class PriorityModeEnum(str, Enum):
    """How to handle conflicts between decorators"""
    OVERRIDE = "override"
    MERGE = "merge"
    CASCADE = "cascade"

class ProfessionalFormalityEnum(str, Enum):
    """The level of formality to maintain in the response"""
    STANDARD = "standard"
    HIGH = "high"
    EXECUTIVE = "executive"

class QualityMetricsScaleEnum(str, Enum):
    """Rating scale to use for evaluations"""
    VALUE_1_5 = "1-5"
    VALUE_1_10 = "1-10"
    PERCENTAGE = "percentage"
    QUALITATIVE = "qualitative"

class ReasoningDepthEnum(str, Enum):
    """The level of detail in the reasoning process"""
    BASIC = "basic"
    MODERATE = "moderate"
    COMPREHENSIVE = "comprehensive"

class RedTeamStrengthEnum(str, Enum):
    """How aggressive or challenging the red team analysis should be"""
    MODERATE = "moderate"
    AGGRESSIVE = "aggressive"
    STEELMAN = "steelman"

class RemixPreserveEnum(str, Enum):
    """What aspects of the original content to prioritize preserving"""
    FACTS = "facts"
    STRUCTURE = "structure"
    TONE = "tone"
    COMPREHENSIVENESS = "comprehensiveness"

class RootCauseMethodEnum(str, Enum):
    """The specific root cause analysis methodology to apply"""
    VALUE_5WHYS = "5whys"
    FISHBONE = "fishbone"
    PARETO = "pareto"

class StressTestSeverityEnum(str, Enum):
    """The intensity level of the stress conditions"""
    MODERATE = "moderate"
    SEVERE = "severe"
    EXTREME = "extreme"

class StyleShiftAspectEnum(str, Enum):
    """The specific style aspect to modify"""
    FORMALITY = "formality"
    PERSUASION = "persuasion"
    URGENCY = "urgency"
    CONFIDENCE = "confidence"
    COMPLEXITY = "complexity"

class SummaryLengthEnum(str, Enum):
    """Relative length of the summary"""
    SHORT = "short"
    MEDIUM = "medium"
    LONG = "long"

class SummaryPositionEnum(str, Enum):
    """Where to position the summary in relation to any full content"""
    BEGINNING = "beginning"
    END = "end"
    STANDALONE = "standalone"

class TableFormatAlignmentEnum(str, Enum):
    """Text alignment within table cells"""
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"

class TableFormatFormatEnum(str, Enum):
    """Format style for the table representation"""
    MARKDOWN = "markdown"
    ASCII = "ascii"
    CSV = "csv"

class TimelineDetailsEnum(str, Enum):
    """The level of detail to include for each timeline event"""
    MINIMAL = "minimal"
    MODERATE = "moderate"
    COMPREHENSIVE = "comprehensive"

class TimelineFormatEnum(str, Enum):
    """The presentation format for the timeline"""
    LIST = "list"
    NARRATIVE = "narrative"
    TABLE = "table"

class TimelineGranularityEnum(str, Enum):
    """The level of time detail to include in the timeline"""
    DAY = "day"
    MONTH = "month"
    YEAR = "year"
    DECADE = "decade"
    CENTURY = "century"
    ERA = "era"

class ToneStyleEnum(str, Enum):
    """The desired tone and style for the response"""
    FORMAL = "formal"
    CASUAL = "casual"
    FRIENDLY = "friendly"
    TECHNICAL = "technical"
    HUMOROUS = "humorous"

class UncertaintyFormatEnum(str, Enum):
    """How to format uncertainty indications in the response"""
    INLINE = "inline"
    SECTION = "section"
    CONFIDENCE = "confidence"

class UncertaintyThresholdEnum(str, Enum):
    """The threshold for flagging uncertain content"""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"