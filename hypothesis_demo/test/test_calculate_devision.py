from  ..calculate_devision import do_devision
from hypothesis import given
from hypothesis.strategies import integers

@given(integers(min_value=1,max_value=20),integers(min_value=3,max_value=3))
def test_do_som_devision(a: int, b: int):
    do=do_devision(a,b)
    assert do> 0

def second_test_do_devision():
    assert(3 >1)