class foo(object):
    """Some headers line

    :ivar somevar: some text

    some detailed docstring
    """

    __slots__ = (
        "somevar", # make this object more memory efficient
    )

    def __init__(self, *a):
        """Initialize a new foo instance

        :param a: details of a
        """
        self.somevar = a