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

def count(string):
    """ returns the lenght of the string passed

    Args:
         string: the string the count or return the lenght of.
    Returns:
        the length of the string.
    """
    return len(string)

def test_return_lenght_five_for_hello():
    assert count("hello") == 5

def test_should_insert_new_key():
    dictionary = {}
    key = "test"
    upsert(dictionary , key, 5)
    assert dictionary[key ] == 5