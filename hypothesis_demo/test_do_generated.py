# This test code was written by the `hypothesis.extra.ghostwriter` module
# and is provided under the Creative Commons Zero public domain dedication.

import calculate_devision
from hypothesis import given, strategies as st

do_devision_operands = st.integers()


@given(a=do_devision_operands, b=do_devision_operands, c=do_devision_operands)
def test_associative_binary_operation_do_devision(a: int, b: int, c) -> None:
    left = calculate_devision.do_devision(
        a=a, b=calculate_devision.do_devision(a=b, b=c)
    )
    right = calculate_devision.do_devision(
        a=calculate_devision.do_devision(a=a, b=b), b=c
    )
    assert left == right, (left, right)


@given(a=do_devision_operands, b=do_devision_operands)
def test_commutative_binary_operation_do_devision(a: int, b: int) -> None:
    left = calculate_devision.do_devision(a=a, b=b)
    right = calculate_devision.do_devision(a=b, b=a)
    assert left == right, (left, right)


@given(a=do_devision_operands)
def test_identity_binary_operation_do_devision(a: int) -> None:
    assert a == calculate_devision.do_devision(a=a, b=0)

