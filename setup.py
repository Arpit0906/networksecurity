'''The setup.py file is an essential part of packaging and distributing python projects. It is used by setuptools to 
define the configuration of your project such as metadata, dependancies and more.'''

from setuptools import find_packages,setup
from typing import List

def get_requirements()-> List[str]:
    """This function will return list of requirements."""
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as f:
            #Read lines from the file
            lines=f.readlines()
            ## Process the line
            for line in lines:
                requirement=line.strip()
                ## Ignore emptylines and .e
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print('requirements.txt file is not available ')

    return requirement_lst

setup(
    name="Networksecurity",
    version='0.0.1',
    author='Arpit',
    author_email='arpitgangwani090@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()

)
                