def add(num1, num2):
    """
    Adds two numbers and returns the result.

    Args :
        num1: the first summond
        num2: the second summond
    Returns: 
        the sum of the two numbers.
    """
    return num1 + num2

def test_return_four_for_two_and_two():
    assert add(2, 2) == 4
