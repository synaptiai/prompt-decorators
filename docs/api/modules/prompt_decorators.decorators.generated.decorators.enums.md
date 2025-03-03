# Module `prompt_decorators.decorators.generated.decorators.enums`

Decorator Enum Definitions.

This module provides enum types used by decorators.

## Classes

- [`AcademicFormatEnum`](#class-academicformatenum): The citation format to use for references.
- [`AcademicStyleEnum`](#class-academicstyleenum): The academic discipline style to follow.
- [`AlternativesDiversityEnum`](#class-alternativesdiversityenum): How different or varied the alternatives should be from each other.
- [`AnalogicalDepthEnum`](#class-analogicaldepthenum): Level of detail in developing the analogy.
- [`AsExpertExperienceEnum`](#class-asexpertexperienceenum): The experience level of the expert.
- [`AudienceLevelEnum`](#class-audiencelevelenum): The expertise level of the target audience.
- [`BalancedStructureEnum`](#class-balancedstructureenum): How to structure the different perspectives.
- [`BlindSpotsDepthEnum`](#class-blindspotsdepthenum): How thoroughly to analyze for blind spots.
- [`BlindSpotsPositionEnum`](#class-blindspotspositionenum): Where to place the blind spots analysis.
- [`BreakAndBuildBreakdownEnum`](#class-breakandbuildbreakdownenum): Primary approach for the critical breakdown phase.
- [`BreakAndBuildIntensityEnum`](#class-breakandbuildintensityenum): How thorough and challenging the breakdown phase should be.
- [`BuildOnApproachEnum`](#class-buildonapproachenum): How to build upon the referenced content.
- [`BuildOnReferenceEnum`](#class-buildonreferenceenum): What to build upon from the previous context.
- [`BulletStyleEnum`](#class-bulletstyleenum): The visual marker used for bullet points.
- [`CiteSourcesFormatEnum`](#class-citesourcesformatenum): The citation format to use.
- [`CiteSourcesStyleEnum`](#class-citesourcesstyleenum): The placement and format of citations within the response.
- [`ComparisonFormatEnum`](#class-comparisonformatenum): The presentation format for the comparison.
- [`ConciseLevelEnum`](#class-conciselevelenum): The degree of conciseness to apply.
- [`ConfidenceScaleEnum`](#class-confidencescaleenum): The method used to express confidence levels.
- [`ConstraintsVocabularyEnum`](#class-constraintsvocabularyenum): Constraints on vocabulary usage.
- [`ContextLevelEnum`](#class-contextlevelenum): The expertise level to target within the domain.
- [`ContextScopeEnum`](#class-contextscopeenum): Which aspects of decorators to contextualize.
- [`ContrarianApproachEnum`](#class-contrarianapproachenum): The specific contrarian approach to take.
- [`CreativeLevelEnum`](#class-creativelevelenum): The degree of creative thinking to apply.
- [`CustomPriorityEnum`](#class-custompriorityenum): How to prioritize custom rules relative to other decorators.
- [`DecisionMatrixScaleEnum`](#class-decisionmatrixscaleenum): Rating scale to use for evaluations.
- [`DetailedDepthEnum`](#class-detaileddepthenum): The level of detail and comprehensiveness.
- [`ExtremesVersionsEnum`](#class-extremesversionsenum): Which extreme versions to include.
- [`FactCheckStrictnessEnum`](#class-factcheckstrictnessenum): The threshold for considering information verified.
- [`FactCheckUncertainEnum`](#class-factcheckuncertainenum): How to handle uncertain information.
- [`FindGapsAspectsEnum`](#class-findgapsaspectsenum): The specific types of gaps to focus on finding.
- [`FindGapsDepthEnum`](#class-findgapsdepthenum): How thoroughly to analyze for gaps.
- [`ForcedAnalogyComprehensivenessEnum`](#class-forcedanalogycomprehensivenessenum): How comprehensively to map concepts between domains.
- [`InductiveStructureEnum`](#class-inductivestructureenum): The pattern of inductive reasoning to follow.
- [`LayeredLevelsEnum`](#class-layeredlevelsenum): The granularity of explanation levels to include.
- [`LayeredProgressionEnum`](#class-layeredprogressionenum): How to structure the progression between layers.
- [`LimitationsDetailEnum`](#class-limitationsdetailenum): The level of detail in the limitations statement.
- [`LimitationsFocusEnum`](#class-limitationsfocusenum): The primary aspect to focus on in the limitations.
- [`LimitationsPositionEnum`](#class-limitationspositionenum): Where to place the limitations statement in the response.
- [`MECEFrameworkEnum`](#class-meceframeworkenum): Optional predefined MECE framework to apply.
- [`MotivationalFocusEnum`](#class-motivationalfocusenum): The primary motivational approach to emphasize.
- [`MotivationalIntensityEnum`](#class-motivationalintensityenum): The level of motivational energy and enthusiasm.
- [`NarrativeLengthEnum`](#class-narrativelengthenum): The relative length of the narrative.
- [`NarrativeStructureEnum`](#class-narrativestructureenum): The narrative structure to employ.
- [`NegativeSpaceDepthEnum`](#class-negativespacedepthenum): How deeply to explore the negative space.
- [`NegativeSpaceFocusEnum`](#class-negativespacefocusenum): The specific aspect of negative space to emphasize.
- [`NegativeSpaceStructureEnum`](#class-negativespacestructureenum): How to present the negative space analysis.
- [`NestedStyleEnum`](#class-nestedstyleenum): Visual style for hierarchical levels.
- [`OutlineStyleEnum`](#class-outlinestyleenum): Numbering or bullet style for the outline.
- [`OutputFormatFormatEnum`](#class-outputformatformatenum): The format to use for the response.
- [`PeerReviewCriteriaEnum`](#class-peerreviewcriteriaenum): Primary criteria to focus on in the review.
- [`PeerReviewPositionEnum`](#class-peerreviewpositionenum): Where to place the peer review relative to the main content.
- [`PeerReviewStyleEnum`](#class-peerreviewstyleenum): The tone and approach of the peer review.
- [`PrecisionLevelEnum`](#class-precisionlevelenum): The degree of precision to apply.
- [`PriorityModeEnum`](#class-prioritymodeenum): How to handle conflicts between decorators.
- [`ProfessionalFormalityEnum`](#class-professionalformalityenum): The level of formality to maintain in the response.
- [`QualityMetricsScaleEnum`](#class-qualitymetricsscaleenum): Rating scale to use for evaluations.
- [`ReasoningDepthEnum`](#class-reasoningdepthenum): The level of detail in the reasoning process.
- [`RedTeamStrengthEnum`](#class-redteamstrengthenum): How aggressive or challenging the red team analysis should be.
- [`RemixPreserveEnum`](#class-remixpreserveenum): What aspects of the original content to prioritize preserving.
- [`RootCauseMethodEnum`](#class-rootcausemethodenum): The specific root cause analysis methodology to apply.
- [`StressTestSeverityEnum`](#class-stresstestseverityenum): The intensity level of the stress conditions.
- [`StyleShiftAspectEnum`](#class-styleshiftaspectenum): The specific style aspect to modify.
- [`SummaryLengthEnum`](#class-summarylengthenum): Relative length of the summary.
- [`SummaryPositionEnum`](#class-summarypositionenum): Where to position the summary in relation to any full content.
- [`TableFormatAlignmentEnum`](#class-tableformatalignmentenum): Text alignment within table cells.
- [`TableFormatFormatEnum`](#class-tableformatformatenum): Format style for the table representation.
- [`TimelineDetailsEnum`](#class-timelinedetailsenum): The level of detail to include for each timeline event.
- [`TimelineFormatEnum`](#class-timelineformatenum): The presentation format for the timeline.
- [`TimelineGranularityEnum`](#class-timelinegranularityenum): The level of time detail to include in the timeline.
- [`ToneStyleEnum`](#class-tonestyleenum): The desired tone and style for the response.
- [`UncertaintyFormatEnum`](#class-uncertaintyformatenum): How to format uncertainty indications in the response.
- [`UncertaintyThresholdEnum`](#class-uncertaintythresholdenum): The threshold for flagging uncertain content.

### Class `AcademicFormatEnum`

The citation format to use for references.

**Inherits from:** `Enum`


### Class `AcademicStyleEnum`

The academic discipline style to follow.

**Inherits from:** `Enum`


### Class `AlternativesDiversityEnum`

How different or varied the alternatives should be from each other.

**Inherits from:** `Enum`


### Class `AnalogicalDepthEnum`

Level of detail in developing the analogy.

**Inherits from:** `Enum`


### Class `AsExpertExperienceEnum`

The experience level of the expert.

**Inherits from:** `Enum`


### Class `AudienceLevelEnum`

The expertise level of the target audience.

**Inherits from:** `Enum`


### Class `BalancedStructureEnum`

How to structure the different perspectives.

**Inherits from:** `Enum`


### Class `BlindSpotsDepthEnum`

How thoroughly to analyze for blind spots.

**Inherits from:** `Enum`


### Class `BlindSpotsPositionEnum`

Where to place the blind spots analysis.

**Inherits from:** `Enum`


### Class `BreakAndBuildBreakdownEnum`

Primary approach for the critical breakdown phase.

**Inherits from:** `Enum`


### Class `BreakAndBuildIntensityEnum`

How thorough and challenging the breakdown phase should be.

**Inherits from:** `Enum`


### Class `BuildOnApproachEnum`

How to build upon the referenced content.

**Inherits from:** `Enum`


### Class `BuildOnReferenceEnum`

What to build upon from the previous context.

**Inherits from:** `Enum`


### Class `BulletStyleEnum`

The visual marker used for bullet points.

**Inherits from:** `Enum`


### Class `CiteSourcesFormatEnum`

The citation format to use.

**Inherits from:** `Enum`


### Class `CiteSourcesStyleEnum`

The placement and format of citations within the response.

**Inherits from:** `Enum`


### Class `ComparisonFormatEnum`

The presentation format for the comparison.

**Inherits from:** `Enum`


### Class `ConciseLevelEnum`

The degree of conciseness to apply.

**Inherits from:** `Enum`


### Class `ConfidenceScaleEnum`

The method used to express confidence levels.

**Inherits from:** `Enum`


### Class `ConstraintsVocabularyEnum`

Constraints on vocabulary usage.

**Inherits from:** `Enum`


### Class `ContextLevelEnum`

The expertise level to target within the domain.

**Inherits from:** `Enum`


### Class `ContextScopeEnum`

Which aspects of decorators to contextualize.

**Inherits from:** `Enum`


### Class `ContrarianApproachEnum`

The specific contrarian approach to take.

**Inherits from:** `Enum`


### Class `CreativeLevelEnum`

The degree of creative thinking to apply.

**Inherits from:** `Enum`


### Class `CustomPriorityEnum`

How to prioritize custom rules relative to other decorators.

**Inherits from:** `Enum`


### Class `DecisionMatrixScaleEnum`

Rating scale to use for evaluations.

**Inherits from:** `Enum`


### Class `DetailedDepthEnum`

The level of detail and comprehensiveness.

**Inherits from:** `Enum`


### Class `ExtremesVersionsEnum`

Which extreme versions to include.

**Inherits from:** `Enum`


### Class `FactCheckStrictnessEnum`

The threshold for considering information verified.

**Inherits from:** `Enum`


### Class `FactCheckUncertainEnum`

How to handle uncertain information.

**Inherits from:** `Enum`


### Class `FindGapsAspectsEnum`

The specific types of gaps to focus on finding.

**Inherits from:** `Enum`


### Class `FindGapsDepthEnum`

How thoroughly to analyze for gaps.

**Inherits from:** `Enum`


### Class `ForcedAnalogyComprehensivenessEnum`

How comprehensively to map concepts between domains.

**Inherits from:** `Enum`


### Class `InductiveStructureEnum`

The pattern of inductive reasoning to follow.

**Inherits from:** `Enum`


### Class `LayeredLevelsEnum`

The granularity of explanation levels to include.

**Inherits from:** `Enum`


### Class `LayeredProgressionEnum`

How to structure the progression between layers.

**Inherits from:** `Enum`


### Class `LimitationsDetailEnum`

The level of detail in the limitations statement.

**Inherits from:** `Enum`


### Class `LimitationsFocusEnum`

The primary aspect to focus on in the limitations.

**Inherits from:** `Enum`


### Class `LimitationsPositionEnum`

Where to place the limitations statement in the response.

**Inherits from:** `Enum`


### Class `MECEFrameworkEnum`

Optional predefined MECE framework to apply.

**Inherits from:** `Enum`


### Class `MotivationalFocusEnum`

The primary motivational approach to emphasize.

**Inherits from:** `Enum`


### Class `MotivationalIntensityEnum`

The level of motivational energy and enthusiasm.

**Inherits from:** `Enum`


### Class `NarrativeLengthEnum`

The relative length of the narrative.

**Inherits from:** `Enum`


### Class `NarrativeStructureEnum`

The narrative structure to employ.

**Inherits from:** `Enum`


### Class `NegativeSpaceDepthEnum`

How deeply to explore the negative space.

**Inherits from:** `Enum`


### Class `NegativeSpaceFocusEnum`

The specific aspect of negative space to emphasize.

**Inherits from:** `Enum`


### Class `NegativeSpaceStructureEnum`

How to present the negative space analysis.

**Inherits from:** `Enum`


### Class `NestedStyleEnum`

Visual style for hierarchical levels.

**Inherits from:** `Enum`


### Class `OutlineStyleEnum`

Numbering or bullet style for the outline.

**Inherits from:** `Enum`


### Class `OutputFormatFormatEnum`

The format to use for the response.

**Inherits from:** `Enum`


### Class `PeerReviewCriteriaEnum`

Primary criteria to focus on in the review.

**Inherits from:** `Enum`


### Class `PeerReviewPositionEnum`

Where to place the peer review relative to the main content.

**Inherits from:** `Enum`


### Class `PeerReviewStyleEnum`

The tone and approach of the peer review.

**Inherits from:** `Enum`


### Class `PrecisionLevelEnum`

The degree of precision to apply.

**Inherits from:** `Enum`


### Class `PriorityModeEnum`

How to handle conflicts between decorators.

**Inherits from:** `Enum`


### Class `ProfessionalFormalityEnum`

The level of formality to maintain in the response.

**Inherits from:** `Enum`


### Class `QualityMetricsScaleEnum`

Rating scale to use for evaluations.

**Inherits from:** `Enum`


### Class `ReasoningDepthEnum`

The level of detail in the reasoning process.

**Inherits from:** `Enum`


### Class `RedTeamStrengthEnum`

How aggressive or challenging the red team analysis should be.

**Inherits from:** `Enum`


### Class `RemixPreserveEnum`

What aspects of the original content to prioritize preserving.

**Inherits from:** `Enum`


### Class `RootCauseMethodEnum`

The specific root cause analysis methodology to apply.

**Inherits from:** `Enum`


### Class `StressTestSeverityEnum`

The intensity level of the stress conditions.

**Inherits from:** `Enum`


### Class `StyleShiftAspectEnum`

The specific style aspect to modify.

**Inherits from:** `Enum`


### Class `SummaryLengthEnum`

Relative length of the summary.

**Inherits from:** `Enum`


### Class `SummaryPositionEnum`

Where to position the summary in relation to any full content.

**Inherits from:** `Enum`


### Class `TableFormatAlignmentEnum`

Text alignment within table cells.

**Inherits from:** `Enum`


### Class `TableFormatFormatEnum`

Format style for the table representation.

**Inherits from:** `Enum`


### Class `TimelineDetailsEnum`

The level of detail to include for each timeline event.

**Inherits from:** `Enum`


### Class `TimelineFormatEnum`

The presentation format for the timeline.

**Inherits from:** `Enum`


### Class `TimelineGranularityEnum`

The level of time detail to include in the timeline.

**Inherits from:** `Enum`


### Class `ToneStyleEnum`

The desired tone and style for the response.

**Inherits from:** `Enum`


### Class `UncertaintyFormatEnum`

How to format uncertainty indications in the response.

**Inherits from:** `Enum`


### Class `UncertaintyThresholdEnum`

The threshold for flagging uncertain content.

**Inherits from:** `Enum`
