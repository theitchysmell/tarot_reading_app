from setuptools import setup, find_packages

setup(
    name="tarot_reading_app",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "openpyxl",
    ],
)
