# pytest-adaptavistreport
This is a pytest plugin that aims to report test cases results to Jira's plugin Adaptavist Test Management.


## Requirements

1. You will need to name the pytest test case with the Adaptavist test case number at the end preceded by an under score "_". ex. "test_T1111".

2. Unless "adaptivisit_test_run_key" and "adaptavist_test_cases_project_key" are test in pytest_namespace(), repoting to Adaptavist will be skipped.

3. This plugin assumes that the given test case is already added to the given test run.

## Installation

To install pytest-adaptavistreport, you can use the following command:

```
$ pip install https://github.com/mabouelfadl/pytest-adaptavistreport/archive/master.zip
```
