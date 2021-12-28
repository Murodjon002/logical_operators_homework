def main(a,b,c):
    """
    Given three integers a, b, c,  check the following statement "The number b is between a and c".
    Args:
        a: int
        b: int
        c: int
    Returns:
        True if b is between a and c, False otherwise
    """
    return (a>b and b>c) or (c>b and b>a)