from classes import Hello_world, Calculator

calc = Calculator()
def test_addiction():
	assert calc.addition(2, 4) ==  6

def test_substraction():
	assert calc.subtraction(2, 4) == -2  

def test_division():
	assert calc.division(2, 4) ==  0.5

def test_multiplication():
	assert calc.multiplication(2, 4) == 8

def test_sqrt():
	assert calc.sqrt(2) ==  1.4142135623730951

def test_power():
	assert calc.power(2, 4) ==  16
