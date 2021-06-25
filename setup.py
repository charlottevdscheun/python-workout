import setuptools

with open("README.md") as f:
    readme = f.read()

setuptools.setup(
    name="python-workout",
    version="0.0.1",
    author="Charlotte van der Scheun",
    description="Python weekly exercises",
    url="https://github.com/pypa/sampleproject",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)