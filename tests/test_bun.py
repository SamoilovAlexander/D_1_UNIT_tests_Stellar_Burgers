import pytest

from datahelper import BUNS
from praktikum.bun import Bun


class TestBun:

    @pytest.mark.parametrize('name, price', BUNS)
    def test_get_name(self, name, price):
        bun = Bun(name, float(price))
        assert bun.get_name() == name

    @pytest.mark.parametrize('name, price', BUNS)
    def test_get_price(self, name, price):
        bun = Bun(str(name), float(price))
        assert bun.get_price() == float(price)
