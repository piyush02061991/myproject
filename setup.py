from setuptools import setup, find_packages
from typing import List
HYPEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    """Read the requirements from a file and return them as a list."""
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
setup(
    name="myproject",  # Replace with your package name
    version="0.0.1",
    author="piyush",
    author_email="wanherepiyush.com",
    packages=find_packages(),  # Automatically find packages in your source folder
    install_requires=get_requirements("requirements.txt")

)