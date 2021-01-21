from setuptools import setup

with open("README", "r") as fh:
    long_description=fh.read()

# This call to setup() does all the work
setup(
    name="ckstats",
    version="1.0.0",
    description="A simple Python package for generating charts.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/chiraag-kakar/ckstats",
    author="Chiraag Kakar",
    author_email="ck2222@cse.jgec.ac.in",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7.7",
    ],
    packages= setuptools.find_packages(),
    include_package_data=True,
    install_requires=["Pillow", "reportlab"],
)