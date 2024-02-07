"""
__post_init__
"""
from dataclasses import dataclass
import os


if os.getenv('base'):
    print('Using Virtualenv')
else:
    print('Not using Virtualenv')
@dataclass
class Test:
     car_number: int
     marque: str
     model: str
    
     def firs_method(self)->str:
        return "test data class"

def get_test(car: Test)->str:
    print(car.firs_method())

if __name__=="__main__":
    get_test(Test(1,2,3))


