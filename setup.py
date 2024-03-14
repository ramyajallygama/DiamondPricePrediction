from setuptools import find_packages,setup
from typing import List

def get_Requirementstxtfile(filename:str)->List[str]:
    requirements=[]
    with open(filename) as filename:
        requirements=filename.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        return requirements


setup(
    name='DiamondpricePrediction',
    description="This will predict price for diamond based on the features",
    author='Ramya Jallygama',
    author_email="ramya.jallygama@gmail.com",
    version='1.0.0',
    install_requires=get_Requirementstxtfile('Requirements.txt'),
    packages=find_packages()
)