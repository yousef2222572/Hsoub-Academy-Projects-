from setuptools import setup # type: ignore

setup(
    name='taskaty',
    version='0.1.0',
    description='A simple command-line Task-app written in python3',
    author='Yousef',
    install_requires=['tabulate'],
    entry_points={
        'console_scripts':[
            'taskaty=taskaty:main',
        ]
    }
)