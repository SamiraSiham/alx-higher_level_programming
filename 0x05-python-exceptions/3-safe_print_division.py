#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = x / y
    except ZeroDivisionError:
        None
    finally:
        print("Inside result: {}".format(result))
        return result
