from setuptools import setup, find_namespace_packages

with open("README.md", "r") as fh:
    page_description = fh.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="pacote-modelo",
    version="0.0.1",
    author="AllianceTechSolutions/Thiago",
    description="my short description",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AllianceTechSolutions",
    packages=find_namespace_packages(),
    install_requires=requirements,
    python_requires='>=3.6',
)
