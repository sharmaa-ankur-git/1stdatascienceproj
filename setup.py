from setuptools import find_packages,setup

def get_requirements(requirements_file:str)->list[str]:
    requirements_list=[]
    with open(requirements_file) as file_obj:
        requirements_file=file_obj.readlines()
        requirements_file=[req.replace("\n","") for req in requirements_file] 

        if "-e ." in requirements_file:
            requirements_file.remove("-e .")
    return requirements_file
setup(
    name='1stdatascienceporj',
    version='0.0.1',
    author='Ankur Kumar Sharma',
    author_email='sharmaankur69851@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
