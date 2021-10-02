
import sys

sys.setrecursionlimit(1500)

factorial_dict = {}

def factorial_memo(input_value):
    if input_value < 2: 
        return 1
    if input_value not in factorial_dict:
        factorial_dict[input_value] = input_value * factorial_memo(input_value-1)
    return factorial_dict[input_value]

def Factorial(num_factorial):        
    for i in range(1, num_factorial):
        resultado=factorial_memo(i)

    return resultado