"""My first exercise in COMP110"""

from random import random

random()

__author__ = "730745570"

print("Hello, world!")


def greet(name: str) -> str:
    """A welcoming first function definition"""
    return "Hello, " + name + "!"


if __name__ == "__main__":
    print(greet(name=input("What is your name? ")))

