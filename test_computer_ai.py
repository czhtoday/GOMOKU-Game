import pytest
from computer_ai import AI
from unittest.mock import Mock

def test_movement():
    # Mocking the Intersections object and its properties for testing movement
    intersections_mock = Mock()
    intersections_mock.board = [[0 for _ in range(15)] for _ in range(15)]

    ai = AI(intersections_mock)
    try:
        ai.movement()
        # Pass the test if the method executes without error
        assert True  
    except Exception as e:
        assert False, f"Movement method failed with exception: {e}"
