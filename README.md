# pytest-adaptivistreport
This is a pytest plugin that aims to report test cases results to Jira's plugin Adaptivist Test Management.


## Requirements

1. You will need to name the pytest test case with the Adaptivist test case number at the end preceded by an under score "_". ex. "test_T1111".

2. Unless "adaptivisit_test_run_key" and "adaptivist_test_cases_project_key" are test in pytest_namespace(), repoting to Adaptivist will be skipped.

3. This plugin assumes that the given test case is already added to the given test run.

## Installation

To install pytest-adaptivistreport, you can use the following command:

```
$ pip install https://github.com/mabouelfadl/pytest-adaptivistreport/archive/master.zip
```
