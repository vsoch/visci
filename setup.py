from setuptools import setup, find_packages

setup(
    # Application name:
    name="visci",

    # Version number (initial):
    version="0.0.2",

    # Application author details:
    author="Vanessa Sochat",
    author_email="vsochat@stanford.edu",

    # Packages
    packages=find_packages(),

    # Data
    package_data = {'visci.templates':['*.html']},

    # Details
    url="http://www.github.com/vsoch/visualization-ci",

    license="LICENSE.txt",
    description="visualization standard file structure for continuous integration",

)
