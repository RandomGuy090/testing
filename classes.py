import math

class Hello_world:
	def __init__(self):
		print("Hello_world class initialized")

class Simple_calculator():
	
	def addition(self, x, y):
		return x+y

	def subtraction(self, x, y):
		return x-y

	def division(self, x, y):
		return x/y

	def multiplication(self, x, y):
		return x*y

class Calculator(Simple_calculator):
	def __init__(self):
		super().__init__()

	def sqrt(self, x):
		return math.sqrt(x)

	def power(self, x, y):
		# for i in range(0, y-1):
		x = x**y
		return x




