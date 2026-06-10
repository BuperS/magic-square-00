"""Boundary: Mom Test Red-T1 / Green-T1."""

from src.validate_lines import validate_lines

# Green-T1: 10선 모두 sum == 34
GREEN_T1_GRID = [
    [16, 3, 2, 13],
    [5, 10, 11, 8],
    [9, 6, 7, 12],
    [4, 15, 14, 1],
]

# Red-T1: D2(부대각선) sum == 38 — Mom Test 증거 3
RED_T1_GRID = [
    [16, 3, 2, 13],
    [5, 10, 11, 8],
    [9, 6, 7, 12],
    [8, 15, 14, 1],
]


def test_red_t1_d2_fail():
    result = validate_lines(RED_T1_GRID)
    assert result["status"] == "fail"
    assert "D2" in result["failed_lines"]


def test_green_t1_all_pass():
    result = validate_lines(GREEN_T1_GRID)
    assert result["status"] == "pass"
    assert result["failed_lines"] == []
