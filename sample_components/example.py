def hello_world(name: str) -> str:
    return f"Hello {name}."


def hello(name: str) -> str:
    """Just an greetings example.
    Args:
        name (str): Name to greet.
    Returns:
        str: greeting message
    Examples:
        >>> hello("Roman")
        'Hello Roman!'
    """
    return f"Hello {name}!"


def sample_docstring                                                      (name: str) -> str:
    """This is a sample docstring

    Args:
        name (str): this is the arg which says who has created this docstring

    Returns:
        str: this is echo who has created the docstring


    Examples:
        >>> sample_docstring("Roman")
        'This is a docstring create by - Roman!'
    """
    return f"This is a docstring create by - f{name}."
