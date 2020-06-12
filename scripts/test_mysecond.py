import allure
import pytest
class TestPeple:
    @allure.severity("critical")
    @allure.step(title="注册")
    def test_peple1(self):
        allure.attach("输入用户名",'输入了：1，无')
        print('22')

    def test_peple2(self):
        print('22')