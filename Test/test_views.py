import pytest
from service.views import app
from service.functionAss import *

class Test_Flask_Views:
    @classmethod
    def setup_class(cls):
        app.config['TESTING'] = True
        cls.app = app.test_client()

    @pytest.fixture
    def var1(self):
        return 5

    @pytest.fixture
    def var2(self):
        return 44

    @pytest.fixture
    def tstring(self):
        return "test"

    @pytest.fixture
    def tstring1(self):
        return "is"

    @pytest.fixture
    def tstring2(self):
        return "quite"

    @pytest.fixture
    def tstring3(self):
        return "fun"

    @pytest.fixture
    def roman(self):
        return "MCLXXVI"

    def test_add(self, var1, var2):
        rv = self.app.get(f'/{var1}add{var2}')
        r = rv.data.decode('utf-8')
        res = addition(var1, var2)
        assert r == res

    def test_sub(self, var1, var2):
        rv = self.app.get(f'/{var1}sub{var2}')
        r = rv.data.decode('utf-8')
        res = subtraction(var1, var2)
        assert r == res

    def test_mult(self, var1, var2):
        rv = self.app.get(f'/{var1}mult{var2}')
        r = rv.data.decode('utf-8')
        res = multiplication(var1, var2)
        assert r == res

    def test_div(self, var1, var2):
        rv = self.app.get(f'/{var1}div{var2}')
        r = rv.data.decode('utf-8')
        res = division(var1, var2)
        assert r == res

    def test_div(self, var1, var2):
        rv = self.app.get(f'/{var1}isDiv{var2}')
        r = rv.data.decode('utf-8')
        res = isDiv(var1, var2)
        assert r == res

    def test_pow(self, var1, var2):
        rv = self.app.get(f'/pow{var1},{var2}')
        r = rv.data.decode('utf-8')
        res = toPower(var1, var2)
        assert r == res

    def test_sqroot(self, var1):
        rv = self.app.get(f'/sqroot{var1}')
        r = rv.data.decode('utf-8')
        res = sqRoot(var1)
        assert r == res

    def test_perm(self, tstring):
        rv = self.app.get(f'/perm({tstring})')
        r = rv.data.decode('utf-8')
        res = perm(tstring)
        assert r == res

    def test_list(self, tstring, tstring1, tstring2, tstring3):
        rv = self.app.get(f'/list({tstring},{tstring1},{tstring2},{tstring3})')
        r = rv.data.decode('utf-8')
        res = sortlist(tstring, tstring1, tstring2, tstring3)
        assert  r == res

    def test_roman(self, roman):
        rv = self.app.get(f'/roman({roman})')
        r = rv.data.decode('utf-8')
        res = romantoint(roman)
        assert r == res