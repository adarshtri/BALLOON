import pytest
from balloon.main import welcome

def test_welcome():
    assert welcome("Adarsh") == "Hello Adarsh, Welcome to BALLOON !!"
