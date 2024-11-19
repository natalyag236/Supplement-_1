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

def upsert(dictionary, key , value):
    """ Inserts or updates a key value in a dicrionary

   

    Args:
        dictionary: the dictionary to pefroms the upsert .
        key: the key insert in the dictionary 
        value: the value add to existing value

    Returns:
       int: the numenr of key value pairs in the dictionary after the operation
    """
    if key in dictionary.keys():
        # dictionary contains key, update
        dictionary[key] = dictionary[key] + value
    else:
        # dictionary does not contain key, set
        dictionary[key] = value

def test_should_insert_new_key():
    dictionary = {}
    key = "test"
    upsert(dictionary , key, 5)
    assert dictionary[key ] == 5

def test_should_append_new_key():
    dictionary = {}
    key = "test"
    upsert(dictionary , key, 5)
    upsert(dictionary , key, 2)
    assert dictionary[key ] == 7