# 1.0.1 (2023-08-20)

* The names parameter for the `read_csv` function has to accept a numpy array, after stubs were added upstream
* Use `.str.contains` when checking if a dataframe contains a string in each row
* Set country-less entries to `False` instead of throwing an error
* Try using `on_bad_lines="warn"` instead of the now-deprecated `error_bad_lines=False`
* Download data separately using requests
* Improve logging code and add tests
* Run on more operating systems on CI
* Add more tools and linters

# 1.0.0 (2021-10-07)

* First release.
