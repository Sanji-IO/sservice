import os
import setuptools


def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()


setuptools.setup(
    name="sservice",
    version="0.1.0",
    author="Sanji Team",
    author_email="sanji@moxa.com",
    description="Systemd Service Wrapper",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/Sanji-IO/sservice",
    packages=setuptools.find_packages(),
    install_requires=["sh"],
    classifiers=(
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries :: Python Modules"
    )
)
