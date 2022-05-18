#f(x)=4x**2
#f'(x)=8x
#f'(3)=8*3=24
import math

def funktion(x):
    number = 3*math.sqrt(x) + (2/x**2) #stoppar in funktionen
    return number


h = 1e-11
"""
derivatans definition.
"""
answer = funktion(1+h) - funktion(1) #stoppa in vad x ska vara inuti paranteserna.

answer1 = answer/h

print(answer1)



