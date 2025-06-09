from setuptools import setup, find_packages

setup(
    name="p3",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["pipreqs", "pyinstaller", "jinja2"],
    entry_points={
        "console_scripts": [
            "p3=p3.cli:main"
        ]
    },
)
