from service.functionAss import *
from pytest import fixture
import pytest
import math, itertools




class Test_Formater:


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
    def roman(self):
        return "MCLXXVI"

    def test_addition(self, var1, var2):
        r = addition(var1, var2)
        add = var1 + var2
        re = f"The result of adding {var1} and {var2} is equal to {add}"
        assert (r == re), f'Failing to add {var1} and {var2}'


    def test_subtraction(self, var1, var2):
        r = subtraction(var1, var2)
        subs = var1 - var2
        re = f"The result of subtracting {var2} from {var1} is equal to {subs}"
        assert (r == re), f'Failing to subtract {var1} and {var2}'


    def test_multiplication(self, var1, var2):
        r = multiplication(var1, var2)
        mult = var1 * var2
        re = f"The result of multiplying {var1} and {var2} is equal to {mult}"
        assert(r == re), f'Failing to multiply {var1} and {var2}'


    def test_division(self, var1, var2):
        r = division(var1, var2)
        div = var1 / var2
        re = f"The result of dividing {var1} and {var2} is equal to {div}"
        assert (r == re), f'Failing to divide {var1} and {var2}'


    def test_evencheck_odd(self, var1):
        r = evenCheck(var1)
        re = f"{var1} is odd"
        assert (r == re), f'Failing to check if {var1} is even'


    def test_evencheck_even(self, var2):
        r = evenCheck(var2)
        re = f"{var2} is even"
        assert (r == re), f'Failing to check if {var2} is even'

    def test_isDiv_true(self):
        r = isDiv(10,2)
        re = f"{10} is dividable by {2}"
        assert (r == re), f'Failing to check if {10} is dividable by {2}'


    def test_isDiv_false(self):
        r = isDiv(10,3)
        re = f"{10} is not dividable by {3}"
        assert (r == re), f'Failing to check if {10} is dividable by {3}'


    def test_toPower(self, var1, var2):
        r = toPower(var1, var2)
        power = var1 ** var2
        re = f"The result of {var1} raised to the power of {var2} is equal to {power}"
        assert (r == re), f'Failing to get {var1} to the power of {var2}'

    def test_sqroot(self, var1):
        r = sqRoot(var1)
        root = math.sqrt(var1)
        re = f"The square root of {var1} is equal to {root}"
        assert (r == re), f'Failing to get square root of {var1}'

    def test_perm(self, tstring):
        r = perm(tstring)
        tperm = ([''.join(p) for p in itertools.permutations(tstring)])
        re = f"The permutations of test are : {tperm}"
        assert (r == re), f'Failing to get permutations of {tstring}'

    def test_sortlist(self):
        tlist = ["testing", "is", "quite", "challenging"]
        r = sortlist("testing", "is", "quite", "challenging")
        sortedlist = sorted(tlist)
        re = f"The list {tlist} have been sorted to: {sortedlist}"
        assert (r == re), f'Failing to sort {tlist}'

    def test_roman(self, roman):
        r = romantoint(roman)
        roman_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i, c in enumerate(roman):
            if (i + 1) == len(roman) or roman_num[c] >= roman_num[roman[i + 1]]:
                result += roman_num[c]
            else:
                result -= roman_num[c]
        re = f"The Roman numeral {roman} is equivalent to the number {result}"
        assert(r == re), f'Failing to convert roman number {roman} to int'

    def test_roman_int(self, var1):
        if(var1.isdigit() == True):
            assert f'Input is not a Roman number'
        else:

            r = romantoint(var1)
            roman_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
            result = 0
            for i, c in enumerate(var1):
                if (i + 1) == len(var1) or roman_num[c] >= roman_num[var1[i + 1]]:
                    result += roman_num[c]
                else:
                    result -= roman_num[c]
            re = f"The Roman numeral {var1} is equivalent to the number {result}"
            assert (r == re), f'Failing to convert roman number {var1} , input might not be a roman number'

        #Explanation in word file

    def test_roman_int(self, tstring):
        import re
        if((bool(re.search(r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$",tstring))) == True):
            r = romantoint(tstring)
            roman_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
            result = 0
            for i, c in enumerate(tstring):
                if (i + 1) == len(tstring) or roman_num[c] >= roman_num[tstring[i + 1]]:
                    result += roman_num[c]
                else:
                    result -= roman_num[c]
            re = f"The Roman numeral {tstring} is equivalent to the number {result}"
            assert (r == re), f'Failing to convert roman number {tstring} to int'
        else:
            assert f'Input is not valid roman number'
