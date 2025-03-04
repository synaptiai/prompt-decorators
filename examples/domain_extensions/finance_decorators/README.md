# Finance Domain-Specific Decorators

This package provides domain-specific decorators for financial applications, including risk disclosures and financial analysis structures.

## Installation

```bash
# From the repository root
pip install -e examples/domain_extensions/finance_decorators
```

## Usage

```python
from prompt_decorators.registry import DecoratorRegistry
from finance_decorators import register_extensions

# Initialize registry and register finance extensions
registry = DecoratorRegistry()
register_extensions(registry)

# Create a prompt with finance decorators
prompt = """
+++RiskDisclosure(product_type=investment, jurisdiction=us, risk_level=standard)
+++FinancialAnalysis(analysis_type=fundamental, timeframe=long_term)
Analyze Tesla (TSLA) as a potential long-term investment.
"""

# Process the prompt
processed_prompt = registry.process_prompt(prompt)

# Send to LLM API
response = llm_api.generate(processed_prompt)
```

## Available Decorators

### RiskDisclosure

Ensures financial risk disclosures are included in responses based on product type and jurisdiction.

**Parameters:**
- `product_type`: The type of financial product (investment, loan, insurance, banking, crypto)
- `jurisdiction`: The regulatory jurisdiction (us, eu, uk, international)
- `risk_level`: The level of risk disclosure detail (basic, standard, comprehensive)

**Factory Methods:**
- `RiskDisclosure.us_investment()`: Standard US investment risk disclosures
- `RiskDisclosure.crypto()`: Comprehensive cryptocurrency risk disclosures

### FinancialAnalysis

Structures responses as financial analysis following industry standards and methodologies.

**Parameters:**
- `analysis_type`: The type of financial analysis (fundamental, technical, quantitative, esg, risk)
- `timeframe`: The analysis timeframe (short_term, medium_term, long_term)
- `metrics`: List of specific financial metrics to include

**Factory Methods:**
- `FinancialAnalysis.long_term_fundamental()`: Long-term fundamental analysis with key metrics
- `FinancialAnalysis.technical_trading()`: Short-term technical analysis for trading

## Examples

### Investment Analysis with Risk Disclosure

```
+++RiskDisclosure.us_investment()
+++FinancialAnalysis.long_term_fundamental()
Analyze Microsoft (MSFT) as a potential addition to a retirement portfolio.
```

### Cryptocurrency Trading Analysis

```
+++RiskDisclosure.crypto()
+++FinancialAnalysis.technical_trading()
Analyze the current market conditions for Ethereum (ETH).
```

## Development

To add new finance-specific decorators:

1. Add new decorator classes to `decorators.py`
2. Update the registry entries in `registry_extensions/finance_decorators.json`
3. Register the new decorators in `__init__.py`
4. Add tests for the new decorators

## License

MIT
