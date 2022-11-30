from setuptools import setup,find_packages
from typing import List

#Declaring Global Variables 
PROJECT_NAME = "housing_price_project"
VERSION = "0.0.1"
AUTHOR = "your ass"
DESCRIPTION = "To predict house price you dumbass"
PACKAGES = ["housing"]

FILENAME = "requirements.txt"
#creating a function to read my requirements.txt file
def get_requirements_data()->List[str]:
    """You already forgotted this ,ooooh my goddddddddd!!!
    this is will return content of the requirements.txt into list
    """
    with open(FILENAME,'r') as contents:
        return contents.readlines().remove("-e .")

setup(name=PROJECT_NAME,
version=VERSION,
description=DESCRIPTION,
packages=find_packages(),
install_requires=get_requirements_data())


#if you want to run only this module :) -> python setup.py install 
# if __name__ == "__main__":
#     print(get_requirements_data())
