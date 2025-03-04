"""Finance domain-specific decorators implementation."""

from typing import Any, Dict, List, Optional, Union

from prompt_decorators.core.base import BaseDecorator


class RiskDisclosure(BaseDecorator):
    """Decorator that ensures financial risk disclosures are included in responses.

    This decorator modifies prompts to request appropriate risk disclosures
    based on the financial product or service being discussed.

    Args:
        product_type: The type of financial product (investment, loan, insurance, etc.)
        jurisdiction: The regulatory jurisdiction (us, eu, uk, international)
        risk_level: The level of risk disclosure detail (basic, standard, comprehensive)
    """

    def __init__(
        self,
        product_type: str = "investment",
        jurisdiction: str = "us",
        risk_level: str = "standard",
    ) -> None:
        super().__init__()
        self.product_type = product_type
        self.jurisdiction = jurisdiction
        self.risk_level = risk_level

        # Validate parameters
        valid_product_types = ["investment", "loan", "insurance", "banking", "crypto"]
        if self.product_type not in valid_product_types:
            raise ValueError(f"product_type must be one of {valid_product_types}")

        valid_jurisdictions = ["us", "eu", "uk", "international"]
        if self.jurisdiction not in valid_jurisdictions:
            raise ValueError(f"jurisdiction must be one of {valid_jurisdictions}")

        valid_risk_levels = ["basic", "standard", "comprehensive"]
        if self.risk_level not in valid_risk_levels:
            raise ValueError(f"risk_level must be one of {valid_risk_levels}")

    def __call__(self, text: str) -> str:
        """Apply the risk disclosure decorator to the prompt.

        Args:
            text: The original prompt text

        Returns:
            The modified prompt text with risk disclosure instructions
        """
        disclosure_text = self._get_disclosure_text()
        return f"{text}\n\n{disclosure_text}"

    def _get_disclosure_text(self) -> str:
        """Generate the appropriate risk disclosure text based on parameters.

        Returns:
            The risk disclosure instruction text
        """
        base_text = "Include appropriate risk disclosures"

        if self.product_type == "investment":
            product_text = (
                "for investment products, including potential loss of principal"
            )
        elif self.product_type == "loan":
            product_text = "for loan products, including interest rate risks and repayment obligations"
        elif self.product_type == "insurance":
            product_text = (
                "for insurance products, including coverage limitations and exclusions"
            )
        elif self.product_type == "banking":
            product_text = "for banking products, including fees, terms, and conditions"
        elif self.product_type == "crypto":
            product_text = "for cryptocurrency, including volatility, regulatory uncertainty, and potential total loss"
        else:
            product_text = "for this financial product"

        if self.jurisdiction == "us":
            jurisdiction_text = "compliant with SEC and FINRA regulations"
        elif self.jurisdiction == "eu":
            jurisdiction_text = "compliant with MiFID II and EU financial regulations"
        elif self.jurisdiction == "uk":
            jurisdiction_text = "compliant with FCA regulations"
        elif self.jurisdiction == "international":
            jurisdiction_text = "following international best practices"
        else:
            jurisdiction_text = "following applicable regulations"

        if self.risk_level == "basic":
            level_text = "at a basic level"
        elif self.risk_level == "standard":
            level_text = "with standard detail"
        elif self.risk_level == "comprehensive":
            level_text = "with comprehensive explanations of all potential risks"
        else:
            level_text = ""

        return f"{base_text} {product_text}, {jurisdiction_text}, {level_text}."

    @classmethod
    def us_investment(cls) -> "RiskDisclosure":
        """Factory method for US investment risk disclosures.

        Returns:
            A RiskDisclosure instance configured for US investments
        """
        return cls(product_type="investment", jurisdiction="us", risk_level="standard")

    @classmethod
    def crypto(cls) -> "RiskDisclosure":
        """Factory method for cryptocurrency risk disclosures.

        Returns:
            A RiskDisclosure instance configured for cryptocurrency
        """
        return cls(
            product_type="crypto",
            jurisdiction="international",
            risk_level="comprehensive",
        )


class FinancialAnalysis(BaseDecorator):
    """Decorator that structures responses as financial analysis.

    This decorator modifies prompts to request structured financial analysis
    following industry standards and methodologies.

    Args:
        analysis_type: The type of financial analysis (fundamental, technical, quantitative)
        timeframe: The analysis timeframe (short_term, medium_term, long_term)
        metrics: List of specific financial metrics to include
    """

    def __init__(
        self,
        analysis_type: str = "fundamental",
        timeframe: str = "medium_term",
        metrics: Optional[List[str]] = None,
    ) -> None:
        super().__init__()
        self.analysis_type = analysis_type
        self.timeframe = timeframe
        self.metrics = metrics or []

        # Validate parameters
        valid_analysis_types = [
            "fundamental",
            "technical",
            "quantitative",
            "esg",
            "risk",
        ]
        if self.analysis_type not in valid_analysis_types:
            raise ValueError(f"analysis_type must be one of {valid_analysis_types}")

        valid_timeframes = ["short_term", "medium_term", "long_term"]
        if self.timeframe not in valid_timeframes:
            raise ValueError(f"timeframe must be one of {valid_timeframes}")

    def __call__(self, text: str) -> str:
        """Apply the financial analysis decorator to the prompt.

        Args:
            text: The original prompt text

        Returns:
            The modified prompt text with financial analysis instructions
        """
        analysis_text = self._get_analysis_text()
        return f"{text}\n\n{analysis_text}"

    def _get_analysis_text(self) -> str:
        """Generate the appropriate financial analysis text based on parameters.

        Returns:
            The financial analysis instruction text
        """
        base_text = "Structure your response as a financial analysis"

        if self.analysis_type == "fundamental":
            type_text = "using fundamental analysis principles, including financial statements, economic indicators, and industry trends"
        elif self.analysis_type == "technical":
            type_text = "using technical analysis, including price patterns, volume, and momentum indicators"
        elif self.analysis_type == "quantitative":
            type_text = "using quantitative methods, including statistical models and data-driven approaches"
        elif self.analysis_type == "esg":
            type_text = "with emphasis on environmental, social, and governance factors"
        elif self.analysis_type == "risk":
            type_text = "focusing on risk assessment, including volatility, drawdown potential, and risk-adjusted returns"
        else:
            type_text = ""

        if self.timeframe == "short_term":
            timeframe_text = "with a short-term outlook (0-6 months)"
        elif self.timeframe == "medium_term":
            timeframe_text = "with a medium-term outlook (6-24 months)"
        elif self.timeframe == "long_term":
            timeframe_text = "with a long-term outlook (2+ years)"
        else:
            timeframe_text = ""

        metrics_text = ""
        if self.metrics:
            metrics_list = ", ".join(self.metrics)
            metrics_text = f" Include the following specific metrics: {metrics_list}."

        return f"{base_text} {type_text}, {timeframe_text}.{metrics_text}"

    @classmethod
    def long_term_fundamental(
        cls, metrics: Optional[List[str]] = None
    ) -> "FinancialAnalysis":
        """Factory method for long-term fundamental analysis.

        Args:
            metrics: Optional list of specific metrics to include

        Returns:
            A FinancialAnalysis instance configured for long-term fundamental analysis
        """
        default_metrics = [
            "P/E ratio",
            "EPS growth",
            "ROE",
            "Debt-to-Equity",
            "Dividend yield",
        ]
        return cls(
            analysis_type="fundamental",
            timeframe="long_term",
            metrics=metrics or default_metrics,
        )

    @classmethod
    def technical_trading(cls) -> "FinancialAnalysis":
        """Factory method for short-term technical analysis for trading.

        Returns:
            A FinancialAnalysis instance configured for short-term technical analysis
        """
        return cls(
            analysis_type="technical",
            timeframe="short_term",
            metrics=["RSI", "MACD", "Moving Averages", "Volume", "Support/Resistance"],
        )
