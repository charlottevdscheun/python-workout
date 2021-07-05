import setuptools

with open("README.md") as f:
    readme = f.read()

setuptools.setup(
    name="WPE",
    version="0.0.1",
    author="Charlotte van der Scheun",
    description="Python weekly exercises",
    packages=['src'],
    python_requires=">=3.6",
)
