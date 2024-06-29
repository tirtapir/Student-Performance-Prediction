from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(filename:str)->list[str]:
    '''
    Get list of requirements from requirements.txt
    '''
    requirements = []
    with open(filename, 'r') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements
 
setup(
    name='studentPerformancePrediction',
    version='0.0.1',
    author='Tirta',
    author_email='tirtarumy14@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)