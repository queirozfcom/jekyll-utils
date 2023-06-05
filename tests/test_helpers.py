import pytest


# inside my_test.py
def test_raises_index_error():
    with pytest.raises(IndexError):
        arr = [1, 2, 3]
        print(arr[1])
