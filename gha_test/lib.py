def count_ones(arr: list[int]) -> int:
    ''' Returns the number of ones in a list.

    This function uses the `builtins.list` type hint introduced in
    Python 3.9. It should fail to run on earlier releases of Python.
    '''

    count = 0
    for x in arr:
        if x == 1:
            count += 1
    return count
