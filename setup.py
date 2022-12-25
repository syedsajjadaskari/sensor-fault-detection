from setuptools import find_packages, setup #return a list of python items(modules/packages)
from typing import List

#helps to understand and install external file(requirements.txt)

def get_requirements()->List[str]:
    """This function will return list of requirements"""
    requirements_list:List[str] = []
    return requirements_list

setup(
    name = "sensor",
    version="0.0.1",
    author = "syed sajjad askari",
    author_email = "syedsajjad62@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements(),

)