import pytest
class Test_001:
    @pytest.mark.parametrize("a",[1,2,3])
    def test_a(self,a):
        assert  a == 2