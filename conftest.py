import logging
import pytest
from _pytest.runner import CallInfo

def pytest_exception_interact(node,call: CallInfo, report):
    logger = logging.getLogger(__name__)
    if report.failed:
        logger.error(call.excinfo)

@pytest.fixture(scope='function', autouse=True)
def test_log(request):
    logging.info("Test '{}' STARTED".format(request.node.nodeid)) # Here logging is used, you can use whatever you want to use for logs
    yield test_log
    logging.info("Test '{}' COMPLETED".format(request.node.nodeid))
