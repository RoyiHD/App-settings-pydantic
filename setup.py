from setuptools import find_packages, setup


setup(
    name="Application Settings",
    version="0.0.1",
    description="Managing environment variables using Pydantic",
    packages = find_packages(exclude=["*.tests"]),
    include_packages_data = True,
    install_requires = [
        "Flask==3.0.0",
        "pydantic==2.4.2",
        "pydantic-settings==2.0.3"
    ]
)