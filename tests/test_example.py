from sample_components.example import hello_world
import pytest

def test_hello_world():
    assert hello_world("aritra") == "Hello aritra."