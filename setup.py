from setuptools import setup, find_packages

setup(
    name="doctor_perrito_bot",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "pydantic"
    ],
)
