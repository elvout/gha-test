from gha_test import lib


def test_count_ones():
    arr = [5, 8, 6, 2, 1, 1, 8, 7, 1, 4, 2]
    assert lib.count_ones(arr) == 3
