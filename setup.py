from setuptools import setup, find_packages

setup(
    name="Topsis-Kashish-102316021",
    version="1.0.0",
    author="Kashish",
    description="TOPSIS implementation in Python",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas"
    ],
    entry_points={
        'console_scripts': [
            'topsis=topsis.topsis:main',
        ],
    },
)
