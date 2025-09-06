from setuptools import setup, find_packages

setup(
    name="signal_DhruviBhudiya_183",
    version="1.0.0",
    author="Dhruvi Bhudiya",
    author_email="dhruvibhudiya07@gmail.com",
    description="Python package for signal generation and operations",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "matplotlib"
    ],
    license="MIT",  
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)