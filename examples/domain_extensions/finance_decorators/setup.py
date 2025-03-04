from setuptools import find_packages, setup

setup(
    name="finance-decorators",
    version="1.0.0",
    description="Domain-specific prompt decorators for financial applications",
    author="Finance AI Team",
    author_email="finance@example.com",
    packages=find_packages(),
    install_requires=[
        "prompt-decorators>=1.0.0",
    ],
    include_package_data=True,
    package_data={
        "finance_decorators": ["registry_extensions/*.json"],
    },
)
