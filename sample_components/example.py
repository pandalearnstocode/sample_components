def hello_world(name: str) -> str:
    return f"Hello {name}."


def hello(name: str) -> str:
    """Just an greetings example.
    Args:
        name (str): Name to greet.
    Returns:
        str: greeting message
    Examples:
        .. code:: python
            >>> hello("Roman")
            'Hello Roman!'
    """
    return f"Hello {name}!"
