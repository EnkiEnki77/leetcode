import pytest

@pytest.mark.skip
@pytest.mark.parametrize("create_static_array, expected_output", [([], False), ([1], True), ([1,2,3], True), ([1,-1], False),([1,2,3,-1,-1], False),], indirect=["create_static_array"])
def test_at_max_capacity(create_static_array, expected_output):
    assert create_static_array.at_max_capacity() == expected_output

@pytest.mark.parametrize("create_static_array, index, expected_output", [([1], 0, 1), ([1,2,3], 1, 2)], indirect=["create_static_array"])
def test_read_index(create_static_array, index, expected_output):
    assert create_static_array.read_index(index) == expected_output

