def main(a):
    """
    Given integer a,  check the following statement "The integer is two-digit number".
    Args:
        a: int
    Returns:
        True if a is two-digit number, False otherwise
    """
    return a//10>=1 and a//10<=9