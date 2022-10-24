import pytest

from sample_components.example import hello, hello_world


@pytest.mark.parametrize(
    ("name", "expected"),
    [
        ("Jeanette", "Hello Jeanette."),
        ("Raven", "Hello Raven."),
        ("Maxine", "Hello Maxine."),
        ("Matteo", "Hello Matteo."),
        ("Destinee", "Hello Destinee."),
        ("Alden", "Hello Alden."),
        ("Mariah", "Hello Mariah."),
        ("Anika", "Hello Anika."),
        ("Isabella", "Hello Isabella."),
    ],
)
def test_hello_world(name, expected):
    assert hello_world(name) == expected


@pytest.mark.parametrize(
    ("name", "expected"),
    [
        ("Jeanette", "Hello Jeanette!"),
        ("Raven", "Hello Raven!"),
        ("Maxine", "Hello Maxine!"),
        ("Matteo", "Hello Matteo!"),
        ("Destinee", "Hello Destinee!"),
        ("Alden", "Hello Alden!"),
        ("Mariah", "Hello Mariah!"),
        ("Anika", "Hello Anika!"),
        ("Isabella", "Hello Isabella!"),
    ],
)
def test_hello(name, expected):
    """Example test with parametrization."""
    assert hello(name) == expected
