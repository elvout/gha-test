from typing import List


def count_ones(arr: List[int]) -> int:
    ''' Returns the number of ones in a list. '''

    count = 0
    for x in arr:
        if x == 1:
            count += 1
    return count
