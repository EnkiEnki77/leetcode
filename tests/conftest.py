import pytest
from ds_and_a.static_array import StaticArray

@pytest.fixture
def create_static_array(request):
    # print(request.param)
    return StaticArray(request.param)