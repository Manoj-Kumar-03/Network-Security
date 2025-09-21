from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    '''
        This function will return list of requirements
    '''
    requirements = []
    try:
        with open('requirements.txt','r') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()

                if requirement and requirement != '-e .':
                    requirements.append(requirement)
    except FileNotFoundError:
        print("requirements.txt not found")

    return requirements

setup(
    name="Network Security",
    author="Manoj Kumar",
    version='0.0.1',
    author_email="lingala.manoj3@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements()
)