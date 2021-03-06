"""setuptools install script"""

from pathlib import Path

from setuptools import find_packages
from setuptools import setup

MODULE_NAME = "innanzi"

INIT_FILE = "__init__.py"
VERSION_INDICATOR = "__version__"  # This sets the version in INIT_FILE

with open(
    (Path(MODULE_NAME) / INIT_FILE).expanduser().resolve(),
    encoding="utf-8",
    errors="surrogateescape",
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
        "black ~= 22.6.0",
        "coverage[toml] ~= 6.4.1",
        "flake8 ~= 4.0.1",
        "flake8-bugbear ~= 22.7.1",
        "flake8-comprehensions ~= 3.10.0",
        "flake8-executable ~= 2.1.1",
        "flake8-isort ~= 4.1.1",
        "flake8-logging-format ~= 0.6.0",
        "flake8-print ~= 4.0.1",
        "flake8-pytest ~= 1.3",
        "flake8-pytest-style ~= 1.6.0",
        "flake8-quotes ~= 3.3.0",
        "flake8-return ~= 1.1.3",
        "flake8-slots ~= 0.1.5",
        "flake8-type-checking ~= 2.1.0",
        "flake8-typing-imports ~= 1.12.0",
        "flynt ~= 0.76",
        "isort ~= 5.10.1",
        "mypy==0.971",
        "pandas-vet ~= 0.2.3",
        "pep8-naming ~= 0.13.0",
        "pylint ~= 2.14.1",
        "pytest ~= 7.1.2",
        "pytest-bandit ~= 0.6.1",
        "pytest-black ~= 0.3.12",
        "pytest-cov ~= 3.0.0",
        "pytest-dependency ~= 0.5.1",
        "pytest-flake8 ~= 1.1.1",
        "pytest-mypy ~= 0.9.1",
        "pytest-pylint ~= 0.18.0",
        "pytest-randomly ~= 3.12.0",
        "pytest-xdist ~= 2.5.0",
        "pyupgrade-directories ~= 0.2.0",
        "semgrep ~= 0.107.0",
        "sphinx ~= 5.1.1",
        "tryceratops ~= 1.1.0",
        "vulture ~= 2.5",
        "yesqa ~= 1.4.0",
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
        "pandas ~= 1.4.2",
        "pandas-stubs==1.4.3.220718",
        "toml ~= 0.10.2",
        "setuptools >= 60.0.5",
        "types-setuptools==63.2.0",  # Bump types-* only with mypy
        "types-toml==0.10.7",  # For (temp) infrastructure stuff of some packages
        "wheel >= 0.37.0",
    ],
    extras_require=EXTRAS,
    python_requires=">= 3.10",
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
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development :: Testing",
        "Topic :: Utilities",
    ],
)
