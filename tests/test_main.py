from main import sort_area,sort_population
import pytest

def test_sort_area():
    data = [('a', '-3'), ('b', '1'), ('c', '-2')]
    assert sort_area(data) == [('b', '1'), ('c', '-2'), ('a', '-3')]

def test_sort_population():
    data = [('a', '1','1'), ('b', '1','100'), ('c', '1','20')]
    assert sort_population(data) == [('b', '1','100'), ('c', '1','20'), ('a', '1','1')]

# @pytest.mark.parametrize("data, res", [
#     (
#             [('a', '3'), ('b', '1'), ('c', '2')],
#             [('a', '3'), ('c', '2'), ('b', '1')]
#     ),
# ])
# def test_sort_area(data, res):
#     assert sort_area(data) == res



