#!/usr/bin/env python3

def islower(c):
    return ord('a') <= ord(c) <= ord('z')

if __name__ == "__main__":
    # Sample test cases
    print(islower("a"))  # True
    print(islower("H"))  # False
    print(islower("A"))  # False
    print(islower("3"))  # False
    print(islower("g"))  # True
