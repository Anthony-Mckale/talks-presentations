import os
from unittest import mock

def some_func():
    return os.environ.get("HELLO")

@mock.patch.dict(os.environ, {"HELLO": "WORLD"})
def test_os_mocking():
    # Given
    expected_output = "WORLD"
    # When
    output = some_func()
    assert output == expected_output


