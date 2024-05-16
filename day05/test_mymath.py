import mymath
import pytest

def test_add():
    result = mymath.add(2, 3)
    assert(result == 5)

    result = mymath.add(-1, 1)
    assert(result == 0)

# def test_area():
#     result = mymath.area(2, 2)
#     assert(result == 4)

def test_area2():
    result = mymath.area(2, 3)
    assert(result == 6)

    result = mymath.area(2, 2)
    assert(result == 4)


@pytest.mark.parametrize("x, y, expected", [
    (2, 3,   5),
    (-1, 1,  0),
    (1, 1,  3),
])
def test_add_parametrize(x, y, expected):
    result = mymath.add(x, y)
    assert(result == expected)


# research_a  f, g, h
# research_b  f, g, h'