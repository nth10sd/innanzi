"""setuptools install script"""

from pathlib import Path

from setuptools import find_packages
from setuptools import setup

MODULE_NAME = "innanzi"

INIT_FILE = "__init__.py"
VERSION_INDICATOR = "__version__"  # This sets the version in INIT_FILE

with open(
    (Path(MODULE_NAME) / INIT_FILE).expanduser().resolve(),
) as f:  # Look in module's __init__ for __version__
    for line in f:
        if line.startswith(VERSION_INDICATOR):
            MODULE_VER = line.split("=", 1)[1].strip()[1:-1]
            break
    if not MODULE_VER:
        raise ValueError(
            f"{VERSION_INDICATOR} is not defined in {MODULE_NAME}/{INIT_FILE}",
        )

EXTRAS = {
    "test": [
        "bandit ~= 1.7.0",
        "black ~= 21.6b0",
        "coverage[toml] ~= 5.5",
        "flake8 ~= 3.9.2",
        "flake8-bugbear ~= 21.4.3",
        "flake8-commas ~= 2.0.0",
        "flake8-comprehensions ~= 3.5.0",
        "flake8-isort ~= 4.0.0",
        "flake8-print ~= 4.0.0",
        "flake8-quotes ~= 3.2.0",
        "isort ~= 5.8.0",
        "mypy==0.902",
        "pep8-naming ~= 0.11.1",
        "pylint ~= 2.9.0.dev1",
        "pytest ~= 6.2.4",
        "pytest-bandit ~= 0.6.1",
        "pytest-black ~= 0.3.12",
        "pytest-cov ~= 2.12.1",
        "pytest-dependency ~= 0.5.1",
        "pytest-flake8 ~= 1.0.7",
        "pytest-mypy ~= 0.8.1",
        "pytest-pylint ~= 0.18.0",
        "sphinx ~= 4.0.2",
        "vulture ~= 2.3",
    ],
}

setup(
    name=MODULE_NAME,
    version=MODULE_VER,
    url="https://github.com/nth10sd/innanzi",
    license="MIT",
    author="Gary Kwong",
    author_email="nth10sd@gmail.com",
    description="Bootstrap a project easily",
    # long_description=read("README.rst"),
    # entry_points={
    #     "console_scripts": [f"{MODULE_NAME} = {MODULE_NAME}.start:main"],
    # },
    packages=find_packages(exclude=("tests",)),
    package_data={
        MODULE_NAME: [
            "py.typed",
        ],
    },
    install_requires=[  # Include relevant types-* package, e.g. types-toml & toml
        "pandas ~= 1.2.4",
        "toml ~= 0.10.2",
        "types-toml ~= 0.1.1",
    ],
    extras_require=EXTRAS,
    python_requires=">= 3.9",
    zip_safe=False,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Programming Language :: Python",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development :: Testing",
        "Topic :: Utilities",
    ],
)
