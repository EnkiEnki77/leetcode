import pytest
from problems.concatenate_array import concatenate_array


@pytest.mark.parametrize("nums, expected_output", [([1,2,1], [1,2,1,1,2,1]), ([2,1,3], [2,1,3,2,1,3]), ])
def test_concatenate_array(nums, expected_output):
    result = concatenate_array(nums)
    assert result == expected_output