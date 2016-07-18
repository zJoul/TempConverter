# Converters functions


def celsius_to_fahrenheit(temp):
    """
    Convert Celsius to Fahrenheit
    :param temp:
    :return:
    """
    try:
        return (9 / 5) * temp + 32
    except TypeError:
        print 'Not an number'
        return False


def fahrenheit_to_celsius(temp):
    """
    Convert Fahrenheit to Celsius
    :param temp:
    :return:
    """
    try:
        return (5 / 9) * (temp - 32)
    except TypeError:
        print 'Not a number'
        return False
