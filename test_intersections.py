import pytest
from intersections import Intersections

def test_init():
    # Test initialization with different parameters
    intersections = Intersections(15, 15, 35, 35)
    assert intersections.ROW_NUM == 15
    assert intersections.COL_NUM == 15
    assert intersections.X == 35
    assert intersections.Y == 35
    assert intersections.board == [[0 for _ in range(15)] for _ in range(15)]

    # Test with different sizes
    small_intersections = Intersections(0, 0, 0, 0)
    assert small_intersections.board == []

    large_intersections = Intersections(20, 20, 50, 50)
    assert large_intersections.board == [[0 for _ in range(20)] for _ in range(20)]
