import pytest,allure
class Test_001:
    @allure.step(title="测试步骤01")
    @pytest.mark.parametrize("a",[1,2,3])
    def test_a(self,a):
        assert  a == 2
    @allure.step(title="测试步骤02")
    @pytest.mark.parametrize("b",[4,5,6])
    def test_b(self,b):
        assert b !=5
