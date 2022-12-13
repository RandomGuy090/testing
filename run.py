from classes import Hello_world, Calculator


Hello_world()

calc = Calculator()



print(f" 2 + 4 = {calc.addition(2, 4)}")
print(f" 2 - 4 = {calc.subtraction(2, 4)}")
print(f" 2 / 4 = {calc.division(2, 4)}")
print(f" 2 * 4 = {calc.multiplication(2, 4)}")
print(f" sqrt(2) = {calc.sqrt(2)}")
print(f" 2 ** 4 = {calc.power(2, 4)}")


