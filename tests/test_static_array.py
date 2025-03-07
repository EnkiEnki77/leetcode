import pytest


@pytest.mark.parametrize("create_static_array, expected_output", [([], False), ([1], True), ([1,2,3], True), ([1,-1], False),([1,2,3,-1,-1], False),], indirect=["create_static_array"])
def test_at_max_capacity(create_static_array, expected_output):
    assert create_static_array.at_max_capacity() == expected_output