import pytest

import pytest

def pytest_addoption(parser):
    parser.addoption("--key", action="store")

@pytest.fixture(scope='session')
def key(request):
    key = request.config.option.key
    return key
