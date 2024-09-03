from setuptools import find_packages, setup


HYPEN_E_DOT = "-e ."

def get_requirements(file_path):
     '''
     Function to retrieve requirements from  requirements.txt
     '''

     with open(file= file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]
        if HYPEN_E_DOT in requirements:
               requirements.remove(HYPEN_E_DOT)
     return(requirements)

setup(
    name = "mlproject",
    version= "0.0.1",
    author= "hammad",
    author_email="hammadfaheem5@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements("requirements.txt")
)