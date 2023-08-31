## 2.1.0 (2023-08-30)

1. Make sure `sphinx` tries to generate docs first, then fail on CI when docs contain sphinx errors
1. Switch `ruff` to select all rules automatically to run, instead of manually specifying each category
1. Revert `python_files` setting to the default and add `--strict-markers` to `addopts`
1. Switch back to `pytest-instafail` and add `--instafail` to `pytest` run command
1. Bump `pyright` to 1.1.324, `ruff` to 0.0.286, `semgrep` to 1.37.0, `sphinx` to 7.2.4 and `vulture` to 2.9.1

## 2.0.4 (2023-08-20)

1. Bump `pandas` to 2.0.3 and `pandas-stubs` to 2.0.2.230605

## 2.0.3 (2023-08-20)

1. Remove obsolete vulture ignore line

## 2.0.2 (2023-08-20)

1. Bump number of known ignore lines on CI

## 2.0.1 (2023-08-20)

1. Fix all outstanding CI issues
1. Bump vulture to 2.9

## 2.0.0 (2023-08-20)

1. General Python package structure updated
1. Switch entirely to `pyproject.toml` and use `setuptools-scm`
1. Switch entirely to `ruff` from `flake8`
1. `.gitignore` template updated
1. Stop using `pytype`, as its development has slowed immensely, also `mypy` and `pyright` seem sufficient

## 1.0.1 (2023-08-20)

1. The names parameter for the `read_csv` function has to accept a numpy array, after stubs were added upstream
1. Use `.str.contains` when checking if a dataframe contains a string in each row
1. Set country-less entries to `False` instead of throwing an error
1. Try using `on_bad_lines="warn"` instead of the now-deprecated `error_bad_lines=False`
1. Download data separately using requests
1. Improve logging code and add tests
1. Run on more operating systems on CI
1. Add more tools and linters

## 1.0.0 (2021-10-07)

1. First release.
