from setuptools import setup, find_packages

setup(
    name="EliteSalesIA",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pandas>=1.2.3",
        "pickle5>=0.0.11",
        "streamlit>=1.0.0",
        "matplotlib>=3.3.4",
        "pyodbc>=4.0.0",
    ],
    entry_points={
        "console_scripts": [
            "comando=app_database"
        ],
    },
    author="Cgenius",
    author_email="rm98214@fiap.com.br",
    description="Descrição do pacote",
    #long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/gabrielmendesoficial/cgenius-devops-sprint-4",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
