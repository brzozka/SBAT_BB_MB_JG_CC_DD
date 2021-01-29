from .functionAss import *
from flask import Flask
#Comment BB

app = Flask(__name__)

@app.route('/<int:a>add<int:b>')
def add(a,b):
    return addition(a,b)

@app.route('/<int:a>sub<int:b>')
def sub(a,b):
    return subtraction(a,b)

@app.route('/<int:a>mult<int:b>')
def mult(a,b):
    return multiplication(a,b)

@app.route('/<int:a>div<int:b>')
def div(a,b):
    return division(a,b)

@app.route('/isEven<int:a>')
def isEven(a):
    return evenCheck(a)

@app.route('/<int:a>isDiv<int:b>')
def isdiv(a,b):
    return isDiv(a,b)

@app.route('/pow<int:a>,<int:b>')
def pow(a,b):
    return toPower(a,b)

@app.route('/sqroot<int:a>')
def  root(a):
    return sqRoot(a)

@app.route('/perm(<str>)')
def permstr(str):
    return (perm(str))

@app.route('/list(<a>,<b>,<c>,<d>)')
def list(a,b,c,d):
    return sortlist(a,b,c,d)

@app.route('/roman(<a>)')
def roman(a):
    return romantoint(a)