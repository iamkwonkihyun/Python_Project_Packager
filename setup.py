from setuptools import setup, find_packages

setup(
    name="ppb",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["pipreqs", "pyinstaller", "jinja2"],
    entry_points={
        "console_scripts": [
            "ppb=ppb.cli:main"
        ]
    },
)
