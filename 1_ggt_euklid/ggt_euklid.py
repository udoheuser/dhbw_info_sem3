"""
Modul ggt_euklid
Enthält die beiden Funktionen (Implementierungs-Varianten) des ggT:
1. euklid_recursive()
2. euklid()
"""


def euklid_recursive(a, b):
    """Calculate HCF (ggT) using recursive Euklidian algorithm.

    Keyword arguments:
    a -- first integer number (no default)
    b -- second integer number (no default)
    Return value:
    ggt -- ggt as integer number
    Error return value:
    False -- if either of the two params are not integer values
    """

    # checking for integer first
    if not isinstance(a, int) or not isinstance(b, int):
        return False

    # main algorithm
    if b == 0:
        return a
    else:
        return euklid_recursive(b, a % b)

def euklid(a, b):
    """Calculate HCF (ggT) using linear Euklidian algorithm.

    Keyword arguments:
    a -- first integer number (no default)
    b -- second integer number (no default)
    Return value:
    ggt (as integer number)
    Error return value:
    False -- if either of the two params are not integer values
    """

    # checking for integer first
    if not isinstance(a, int) or not isinstance(b, int):
        return False

    # main algorithm
    if a == 0:
        return b
    else:
        while b != 0:
            if a > b:
                a = a - b
            else:
                b = b - a
        return a

