from setuptools import find_packages, setup
setup(
    name='tectonic',
    packages=find_packages(include=['tectonic']),
    version='0.1.0',
    description='A python library for real estate modeling and evaluation',
    author='Greg James',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==7.2.1'],
    test_suite='tests',
)