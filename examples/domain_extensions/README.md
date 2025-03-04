# Domain-Specific Extension Examples

This directory contains examples of domain-specific extensions for the Prompt Decorators framework.

## Available Examples

### Finance Decorators

The [finance_decorators](./finance_decorators) package demonstrates how to create domain-specific decorators for financial applications, including:

- `RiskDisclosure`: Ensures financial risk disclosures are included in responses
- `FinancialAnalysis`: Structures responses as financial analysis following industry standards

## Creating Your Own Domain-Specific Extensions

For a comprehensive guide on creating your own domain-specific extensions, see the [Domain-Specific Extensions Guide](../../docs/guides/domain_specific_extensions.md).

## Structure of a Domain-Specific Extension

A typical domain-specific extension package includes:

```
your_domain_extension/
├── __init__.py              # Registration code
├── decorators.py            # Decorator class implementations
├── registry_extensions/     # JSON metadata for registry
│   └── your_extension.json
├── tests/                   # Unit tests
│   ├── __init__.py
│   └── test_decorators.py
├── README.md                # Documentation
├── setup.py                 # Package setup
└── pyproject.toml           # Project metadata
```

## Contributing

If you've created a domain-specific extension that might be useful to others, consider:

1. Adding it to this examples directory
2. Creating a standalone package and publishing it to PyPI
3. Sharing it in the Prompt Decorators community

## License

All examples in this directory are licensed under the MIT License.
