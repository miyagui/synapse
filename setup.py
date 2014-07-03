import os
from setuptools import setup, find_packages


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="SynapseHomeServer",
    version="0.1",
    packages=find_packages(exclude=["tests"]),
    description="Reference Synapse Home Server",
    install_requires=["Twisted", "twistar"],
    setup_requires=["setuptools_trial", "sphinx", "sphinxcontrib-napoleon", "mock"],
    include_package_data=True,
    long_description=read("README"),
    entry_points="""
    [console_scripts]
    synapse-homeserver=synapse.app.homeserver:run
    """
)
