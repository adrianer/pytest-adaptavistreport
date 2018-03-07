import logging
import pytest
from _pytest.runner import runtestprotocol

logger = logging.getLogger("Apadtivist report plugin")

def pytest_runtest_protocol(item, nextitem):
    reports = runtestprotocol(item, nextitem=nextitem)
    should_execute_reporting = True
      
    try:
        test_run_key = getattr(pytest, 'adaptivisit_test_run_key')
    except AttributeError:
        logger.warning("Adaptivist Jira's test management plugin reporting is not available for this test case! The test run key wasn't set in pytest namespace!")
        should_execute_reporting = False
    else:
        if test_run_key == None:
            logger.warning("Adaptivist Jira's test management plugin reporting is not available for this test case! The test run key is set to null!")
            should_execute_reporting = False
    
    try:
        test_project_key = getattr(pytest, 'adaptivist_test_cases_project_key')
    except AttributeError:
        logger.warning("Adaptivist Jira's test management plugin reporting is not available for this test case! The project key wasn't set in pytest namespace!")
        should_execute_reporting = False
    else:
        if test_project_key == None:
            logger.warning("Adaptivist Jira's test management plugin reporting is not available for this test case! The test project key is set to null!")
            should_execute_reporting = False
        
    try:
        adaptivist_instance =getattr(pytest, 'adaptivist_instance')
    except AttributeError:
        logger.warning("Adaptivist Jira's test management plugin reporting is not available for this test case! The adaptivist instance wasn't set in pytest namespace!")
        should_execute_reporting = False
    else:
        if adaptivist_instance == None:
            logger.warning("Adaptivist Jira's test management plugin reporting is not available for this test case! The adaptivist instance is set to null!")
            should_execute_reporting = False    

    if should_execute_reporting:
        for report in reports:
            if report.when == 'call':
                test_name = item.name
                test_case_key = pytest.adaptivist_test_cases_project_key + "-" + test_name.split('_')[1]
                logger.info(test_case_key)
                logger.info(report.outcome)
                if report.passed:
                    adaptivist_instance.edit_test_result_status(test_run_key, test_case_key, "Pass")
                elif report.failed:
                    adaptivist_instance.edit_test_result_status(test_run_key, test_case_key, "Fail")

    return True
