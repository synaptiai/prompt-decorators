"""Tests for finance domain-specific decorators."""

import pytest
from finance_decorators.decorators import FinancialAnalysis, RiskDisclosure

from prompt_decorators.utils.discovery import DecoratorRegistry


def test_risk_disclosure_basic() -> None:
    """Test basic functionality of RiskDisclosure decorator."""
    decorator = RiskDisclosure(
        product_type="investment", jurisdiction="us", risk_level="standard"
    )
    result = decorator("Analyze Tesla stock")

    assert "Include appropriate risk disclosures" in result
    assert "investment products" in result
    assert "SEC and FINRA regulations" in result
    assert "standard detail" in result


def test_risk_disclosure_factory_methods() -> None:
    """Test factory methods of RiskDisclosure decorator."""
    # Test us_investment factory method
    us_investment = RiskDisclosure.us_investment()
    assert us_investment.product_type == "investment"
    assert us_investment.jurisdiction == "us"
    assert us_investment.risk_level == "standard"

    # Test crypto factory method
    crypto = RiskDisclosure.crypto()
    assert crypto.product_type == "crypto"
    assert crypto.jurisdiction == "international"
    assert crypto.risk_level == "comprehensive"

    # Test output of factory method
    result = RiskDisclosure.crypto()("Explain DeFi investments")
    assert "cryptocurrency" in result
    assert "international best practices" in result
    assert "comprehensive explanations" in result


def test_risk_disclosure_parameter_validation() -> None:
    """Test parameter validation in RiskDisclosure decorator."""
    # Valid parameters should not raise exceptions
    RiskDisclosure(product_type="investment", jurisdiction="us", risk_level="standard")

    # Invalid product_type should raise ValueError
    with pytest.raises(ValueError):
        RiskDisclosure(product_type="invalid_product")

    # Invalid jurisdiction should raise ValueError
    with pytest.raises(ValueError):
        RiskDisclosure(jurisdiction="invalid_jurisdiction")

    # Invalid risk_level should raise ValueError
    with pytest.raises(ValueError):
        RiskDisclosure(risk_level="invalid_level")


def test_financial_analysis_basic() -> None:
    """Test basic functionality of FinancialAnalysis decorator."""
    decorator = FinancialAnalysis(
        analysis_type="fundamental",
        timeframe="long_term",
        metrics=["P/E ratio", "EPS growth"],
    )
    result = decorator("Analyze Microsoft stock")

    assert "Structure your response as a financial analysis" in result
    assert "fundamental analysis principles" in result
    assert "long-term outlook" in result
    assert "P/E ratio, EPS growth" in result


def test_financial_analysis_factory_methods() -> None:
    """Test factory methods of FinancialAnalysis decorator."""
    # Test long_term_fundamental factory method
    long_term = FinancialAnalysis.long_term_fundamental()
    assert long_term.analysis_type == "fundamental"
    assert long_term.timeframe == "long_term"
    assert "P/E ratio" in long_term.metrics
    assert "EPS growth" in long_term.metrics

    # Test with custom metrics
    custom_metrics = ["Revenue growth", "Free cash flow"]
    custom_long_term = FinancialAnalysis.long_term_fundamental(metrics=custom_metrics)
    assert custom_long_term.metrics == custom_metrics

    # Test technical_trading factory method
    technical = FinancialAnalysis.technical_trading()
    assert technical.analysis_type == "technical"
    assert technical.timeframe == "short_term"
    assert "RSI" in technical.metrics
    assert "MACD" in technical.metrics


def test_financial_analysis_parameter_validation() -> None:
    """Test parameter validation in FinancialAnalysis decorator."""
    # Valid parameters should not raise exceptions
    FinancialAnalysis(analysis_type="fundamental", timeframe="long_term")

    # Invalid analysis_type should raise ValueError
    with pytest.raises(ValueError):
        FinancialAnalysis(analysis_type="invalid_type")

    # Invalid timeframe should raise ValueError
    with pytest.raises(ValueError):
        FinancialAnalysis(timeframe="invalid_timeframe")

    # Empty metrics list should be valid
    fa = FinancialAnalysis(metrics=[])
    assert fa.metrics == []


def test_decorator_composition() -> None:
    """Test composition of finance decorators."""
    risk = RiskDisclosure.us_investment()
    analysis = FinancialAnalysis.long_term_fundamental()

    # Apply decorators in sequence
    prompt = "Analyze Apple stock"
    result = analysis(risk(prompt))

    # Check that both decorators' effects are present
    assert "Include appropriate risk disclosures" in result
    assert "investment products" in result
    assert "Structure your response as a financial analysis" in result
    assert "fundamental analysis principles" in result
