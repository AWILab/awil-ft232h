from setuptools import setup, find_packages

setup(
    name='awil_ft232h',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pyftdi'
    ]
)