import math, itertools



def addition(var1,var2):
    result = var1 + var2
    resultStr = f"The result of adding {var1} and {var2} is equal to {result}"
    return resultStr


def subtraction(var1,var2):
    result = var1 - var2
    resultStr = f"The result of subtracting {var2} from {var1} is equal to {result}"
    return resultStr


def multiplication(var1,var2):
    result = var1 * var2
    resultStr = f"The result of multiplying {var1} and {var2} is equal to {result}"
    return resultStr


def division(var1,var2):
    result = var1 / var2
    resultStr = f"The result of dividing {var1} and {var2} is equal to {result}"
    return resultStr


def evenCheck(var1):
    if (var1 % 2) == 0:
       return f"{var1} is even"
    else:
        return f"{var1} is odd"


def isDiv(var1,var2):
    if( var1 % var2) == 0:
        return f"{var1} is dividable by {var2}"
    else:
        return f"{var1} is not dividable by {var2}"

def toPower(var1,var2):
    result = var1 ** var2
    return f"The result of {var1} raised to the power of {var2} is equal to {result}"


def sqRoot(var1):
    result = math.sqrt(var1)
    return f"The square root of {var1} is equal to {result}"


def perm(str):
    result = ([''.join(p) for p in itertools.permutations(str)])
    return f"The permutations of {str} are : {result}"


def sortlist(a,b,c,d):
    list = [a,b,c,d]
    result = sorted(list, key=None)
    return f"The list {list} have been sorted to: {result}"


def romantoint(num):
    roman_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i, c in enumerate(num):
        if (i + 1) == len(num) or roman_num[c] >= roman_num[num[i + 1]]:
            result += roman_num[c]
        else:
            result -= roman_num[c]
    return f"The Roman numeral {num} is equivalent to the number {result}"


