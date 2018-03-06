import pytest
from _pytest.runner import runtestprotocol

def pytest_runtest_protocol(item, nextitem):
    reports = runtestprotocol(item, nextitem=nextitem)
    try:
        pytest.adaptivisit_test_run_key
    except AttributeError:
        logging.info("Adaptivist Jira's test management plugin test run key wasn't set in the pytest namespace!")
        test_run_set = False
    else:
        test_run_set = True

    if test_run_set and pytest.adaptivisit_test_run_key != None:
        for report in reports:
            if report.when == 'teardown':
                test_run_key = pytest.adaptivisit_test_run_key
                test_name = item.name
                test_case_key = pytest.adaptivist_test_cases_project_key + "-" + test_name.split('_')[1]
                logger.info(test_case_key)
                logger.info(report.outcome)
                if report.passed:
                    adaptivist_instance.edit_test_result_status(test_run_key, test_case_key, "Pass")
                elif report.failed:
                    adaptivist_instance.edit_test_result_status(test_run_key, test_case_key, "Fail")

    return True
