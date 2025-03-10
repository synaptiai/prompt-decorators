# Backup Decorator

Designs backup and recovery strategies.

**Category**: Devops And Infrastructure

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `criticality` | `enum` | Data importance level | `high` |
| `rpo` | `enum` | Recovery Point Objective | `hours` |
| `rto` | `enum` | Recovery Time Objective | `hours` |

## Criticality Options

- `low`: The data has low criticality. Basic backup measures are sufficient.
- `medium`: The data has medium criticality. Standard backup practices should be implemented.
- `high`: The data has high criticality. Robust backup solutions are required.
- `mission-critical`: The data is mission-critical. Implement enterprise-grade backup and recovery solutions with redundancy.

## Rpo Options

- `minutes`: Recovery Point Objective (RPO): Minutes - Data loss must be limited to minutes or less.
- `hours`: Recovery Point Objective (RPO): Hours - Data loss of up to a few hours is acceptable.
- `days`: Recovery Point Objective (RPO): Days - Data loss of up to a few days is acceptable.
- `custom`: Recovery Point Objective (RPO): Custom - Consider specific business requirements for acceptable data loss.

## Rto Options

- `minutes`: Recovery Time Objective (RTO): Minutes - Systems must be restored within minutes after failure.
- `hours`: Recovery Time Objective (RTO): Hours - Systems can be down for a few hours during recovery.
- `days`: Recovery Time Objective (RTO): Days - Systems can be down for a few days during recovery.
- `custom`: Recovery Time Objective (RTO): Custom - Consider specific business requirements for acceptable downtime.

## Examples

### Mission-critical financial system backup strategy

```
+++Backup(criticality=mission-critical, rpo=minutes, rto=minutes)
Design a backup and disaster recovery strategy for our financial transaction database.
```

Produces a comprehensive backup strategy for financial data with zero data loss tolerance and immediate recovery capabilities.

### Standard backup for development environment

```
+++Backup(criticality=low, rpo=days, rto=days)
What backup strategy should we use for our development environment?
```

Provides a cost-effective backup approach for non-critical development systems.

## Model-Specific Implementations

### gpt-4-turbo

**Instruction:** Create a detailed backup and recovery strategy considering these requirements:

**Notes:** For smaller models, more explicit instructions about backup components may be needed.


## Implementation Guidance

### Financial database backup planning

**Original Prompt:**
```
Design a backup and disaster recovery strategy for our financial transaction database.
```

**Transformed Prompt:**
```
Design a backup and recovery strategy with the following requirements:

The data is mission-critical. Implement enterprise-grade backup and recovery solutions with redundancy.
Recovery Point Objective (RPO): Minutes - Data loss must be limited to minutes or less.
Recovery Time Objective (RTO): Minutes - Systems must be restored within minutes after failure.

Design a backup and disaster recovery strategy for our financial transaction database.
```

**Notes:** For financial systems, the decorator automatically applies the highest levels of protection and fastest recovery times.

## Transformation Details

**Base Instruction:** Design a backup and recovery strategy with the following requirements:

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `criticality`:
  - When set to `low`: The data has low criticality. Basic backup measures are sufficient.
  - When set to `medium`: The data has medium criticality. Standard backup practices should be implemented.
  - When set to `high`: The data has high criticality. Robust backup solutions are required.
  - When set to `mission-critical`: The data is mission-critical. Implement enterprise-grade backup and recovery solutions with redundancy.

- `rpo`:
  - When set to `minutes`: Recovery Point Objective (RPO): Minutes - Data loss must be limited to minutes or less.
  - When set to `hours`: Recovery Point Objective (RPO): Hours - Data loss of up to a few hours is acceptable.
  - When set to `days`: Recovery Point Objective (RPO): Days - Data loss of up to a few days is acceptable.
  - When set to `custom`: Recovery Point Objective (RPO): Custom - Consider specific business requirements for acceptable data loss.

- `rto`:
  - When set to `minutes`: Recovery Time Objective (RTO): Minutes - Systems must be restored within minutes after failure.
  - When set to `hours`: Recovery Time Objective (RTO): Hours - Systems can be down for a few hours during recovery.
  - When set to `days`: Recovery Time Objective (RTO): Days - Systems can be down for a few days during recovery.
  - When set to `custom`: Recovery Time Objective (RTO): Custom - Consider specific business requirements for acceptable downtime.

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4-turbo, gpt-4o, claude-3-7-sonnet-latest, llama-3.2
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **DisasterRecovery**: Enhances Backup The Backup decorator works well with DisasterRecovery to create comprehensive data protection strategies.
- **CloudMigration**: Enhances Backup Can be used to ensure proper backup strategies are included in cloud migration plans.
