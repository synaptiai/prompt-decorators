# SecurityAudit Decorator

Performs security-focused analysis following industry standards.

**Category**: Testing And Debugging

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `standard` | enum | Security standard to follow | owasp-top10 |
| `risk-level` | enum | Sensitivity for flagging issues | medium |
| `scope` | enum | Areas to evaluate | all |

## Standard Options

- `owasp-top10`: Follow OWASP Top 10 guidelines to identify common web application security risks.
- `sans-top25`: Use SANS Top 25 Most Dangerous Software Errors as a reference framework.
- `cwe`: Reference the Common Weakness Enumeration (CWE) database for vulnerability identification.
- `nist`: Apply NIST Cybersecurity Framework standards for the security assessment.
- `gdpr`: Evaluate compliance with GDPR data protection and privacy requirements.
- `hipaa`: Assess against HIPAA security and privacy standards for healthcare information.

## Risk-Level Options

- `low`: Flag only critical and high-severity security issues.
- `medium`: Identify critical, high, and medium-severity security concerns.
- `high`: Report all security issues including low-severity and potential future concerns.

## Scope Options

- `input-validation`: Focus on input validation vulnerabilities such as injection attacks, XSS, and input sanitization.
- `authentication`: Concentrate on authentication mechanisms, credential management, and session handling.
- `authorization`: Examine authorization controls, access rights, and privilege escalation risks.
- `data-protection`: Analyze data encryption, storage practices, and sensitive information handling.
- `all`: Conduct a comprehensive security review across all potential vulnerability categories.

## Examples

### Basic security audit of a web API endpoint

```
+++SecurityAudit(standard=owasp-top10, risk-level=medium, scope=input-validation)
Audit this express.js API endpoint for security vulnerabilities.
```

Performs a security audit focused on input validation vulnerabilities according to OWASP Top 10, with medium risk sensitivity.

### Comprehensive HIPAA compliance check

```
+++SecurityAudit(standard=hipaa, risk-level=high, scope=all)
Review this patient data handling code for security issues.
```

Conducts a thorough security assessment against HIPAA standards across all security domains with high sensitivity to potential issues.

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** Analyze the following for security vulnerabilities according to industry standards. Identify risks and suggest fixes.

**Notes:** Simplified instruction for models with less security expertise.


## Implementation Guidance

### Code review for a web application

**Original Prompt:**
```
Review this login function for issues:

function login(username, password) {
  const user = db.findUser(username);
  if (user && user.password === password) {
    return generateToken(user);
  }
  return null;
}
```

**Transformed Prompt:**
```
Perform a security audit on the following content. Identify potential security vulnerabilities and provide recommendations for remediation. Follow OWASP Top 10 guidelines to identify common web application security risks. Identify critical, high, and medium-severity security concerns. Conduct a comprehensive security review across all potential vulnerability categories.

Review this login function for issues:

function login(username, password) {
  const user = db.findUser(username);
  if (user && user.password === password) {
    return generateToken(user);
  }
  return null;
}
```

**Notes:** The security audit decorator adds specific instructions to evaluate the code against security standards with appropriate risk sensitivity.

## Transformation Details

**Base Instruction:** Perform a security audit on the following content. Identify potential security vulnerabilities and provide recommendations for remediation.

**Placement:** prepend

**Composition Behavior:** override

**Parameter Effects:**

- `standard`:
  - When set to `owasp-top10`: Follow OWASP Top 10 guidelines to identify common web application security risks.
  - When set to `sans-top25`: Use SANS Top 25 Most Dangerous Software Errors as a reference framework.
  - When set to `cwe`: Reference the Common Weakness Enumeration (CWE) database for vulnerability identification.
  - When set to `nist`: Apply NIST Cybersecurity Framework standards for the security assessment.
  - When set to `gdpr`: Evaluate compliance with GDPR data protection and privacy requirements.
  - When set to `hipaa`: Assess against HIPAA security and privacy standards for healthcare information.

- `risk-level`:
  - When set to `low`: Flag only critical and high-severity security issues.
  - When set to `medium`: Identify critical, high, and medium-severity security concerns.
  - When set to `high`: Report all security issues including low-severity and potential future concerns.

- `scope`:
  - When set to `input-validation`: Focus on input validation vulnerabilities such as injection attacks, XSS, and input sanitization.
  - When set to `authentication`: Concentrate on authentication mechanisms, credential management, and session handling.
  - When set to `authorization`: Examine authorization controls, access rights, and privilege escalation risks.
  - When set to `data-protection`: Analyze data encryption, storage practices, and sensitive information handling.
  - When set to `all`: Conduct a comprehensive security review across all potential vulnerability categories.

## Compatibility

- **Requires**: None
- **Conflicts**: Simplify, CreativeWriting
- **Compatible Models**: gpt-4, gpt-3.5-turbo, claude-2, llama-2
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **CodeReview**: Enhances SecurityAudit SecurityAudit adds security-specific analysis to general code reviews.
- **Simplify**: Conflicts with SecurityAudit Security audits require detailed analysis which conflicts with simplification.
