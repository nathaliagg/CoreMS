import pathlib, os, sys

import setuptools
from setuptools import Command, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="corems",
    version="2.0.0-alpha",
    description="Object Oriented Mass Spectrometry ToolBox for Small Molecules",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://gitlab.pnnl.gov/corilo/corems/",
    author="Corilo, Yuri",
    author_email="corilo@pnnl.gov",
    license="Not decided yet",
    classifiers=[
        #"License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages= setuptools.find_packages(".", exclude= ["test", "*win_only"]),
    exclude_package_data={'.': ["test", "*.win_only"]},
    include_package_data=True,
    install_requires=["pandas", "numpy", "matplotlib", "scipy", 'IsoSpecPy', 'sqlalchemy'],
    # test are not yet implemented, will test dependences and syntax only for now
    test_suite='pytest',
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],

   
    #entry_points={
    #    "console_scripts": [
    #        "corems=cli.__main__:main",
    #    ]
    #},
)
