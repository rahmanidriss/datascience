
from typing import Callable

def decorator_add_func(function: Callable[[int, int], int])-> None:
    def wrapper(*arg):
        result=function(*arg)
        return result+1
    return wrapper

@decorator_add_func
def add_two_numberes(x: int, y: int ) -> int:
    return x+y

if __name__ == "__main__":
    print(add_two_numberes(4,4))
