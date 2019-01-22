somevar = 1
"""Documentation for this variable"""

class foo(object):
    """Some headers line

    :ivar somevar: some text for this instance variable

    some detailed docstring
    """

    def __init__(self, *a):
        """Initialize a new foo instance

        :param a: details of a
        """
        self.somevar = a
