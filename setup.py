from setuptools import find_packages, setup

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='pytectonic',
    packages=find_packages(include=['tectonic']),
    version='0.3.0',
    description='Real Estate modeling and evaluation.',
    long_description_content_type='text/markdown',
    long_description=long_description,
    author='Greg James',
    license='MIT',
    install_requires=['numpy==1.24.1'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==7.2.1'],
    test_suite='tests',
)
