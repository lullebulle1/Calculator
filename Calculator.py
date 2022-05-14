# Imports

import math
# behöver för att kuna använd api korrekt samt eulers numer (e)
import sympy as sp  # för derivering.
import time  # time.sleep
import os


# clearconsol.
# Global variables

# Classes
class Name:
    def __init__(self, name) -> None:
        self.name = name


# Functions
def cs():
    time.sleep(2)
    os.system('Clear')


def name():
    name = input("write your name and klick ENTER to start. ")
    user = Name(name)
    main(user)


def main(user):
    print(f"\n\nwelcome {user.name}\n")
    while True:
        print("""how would you like to calculate?
            [1] Addition
            [2] Subbtrakton
            [3] Multiplikation
            [4] Divitions
            [5] percantage
            [6] Square
            [7] Derivaties
            [8] e^x
            [9] pi
            """)
        number = input("Chose a number: ")
        if "1" == number:
            addition(user)
            cs()
        elif "2" == number:
            subbtraktion(user)
            cs()
        elif "3" == number:
            multiplikation(user)
            cs()
        elif "4" == number:
            divition(user)
            cs()
        elif "5" == number:
            percentage(user)
            cs()
        elif "6" == number:
            square(user)
            cs()
        elif "7" == number:
            derivaties(user)
            cs()
        elif "8" == number:
            e(user)
            cs()
        elif "29" == number:
            pi(user)
            cs()
            break
        else:
            print("sir/ma'ma, please insurt a number")


def addition(user):
    with open("saveeverything.txt", "a", encoding="utf-8") as sav:
        number_choice = int(input("insurt a number: "))
        number_yes = int(input("insurt a nother number: "))
        number_addition = number_choice + number_yes
        number_combine = (f"{number_choice} + {number_yes} = {number_addition}")
        print(number_combine)
        sav.write(str(number_combine) + "\n\n")
        sav.close()
        cs()
        main(user)


def subbtraktion(user):
    with open("saveeverything.txt", "a", encoding="utf-8") as sav:
        number_Choice = int(input("insurt a number: "))
        number_yes = int(input("insurt a nother number: "))
        number_subbtraktion = number_Choice - number_yes
        number_combine = (f"{number_Choice} - {number_yes} = {number_subbtraktion}")
        print(number_combine)
        sav.write(number_combine + "\n\n"  )
        sav.close()
        cs()
        main(user)


def multiplikation(user):
    with open("saveeverything.txt", "a", encoding="utf-8") as sav:
        number_choice = int(input("insurt a number: "))
        number_yes = int(input("insurt a nother number: "))
        number_multiplikation = number_choice * number_yes
        number_combine = (f"{number_choice} * {number_yes} = {number_multiplikation}")
        print(number_combine)
        sav.write(number_combine + "\n\n")
        sav.close()
        cs()
        main(user)

def divition(user):
    with open("saveeverything.txt", "a", encoding="utf-8") as sav:
        number_choice = int(input("insurt a number: "))
        number_yes = int(input("insurt a nother number: "))
        number_divition = number_choice / number_yes
        number_divition1 = number_choice // number_yes
        number_combine = (f"{number_choice} / {number_yes} = {number_divition}")
        number_combine1 = (f"Rounded down: {number_choice} // {number_yes} = {number_divition1}")
        print(number_combine)
        print(number_combine1)
        sav.write(number_combine + "\n\n", number_combine1 + "\n\n")
        sav.close()
        cs()
        main(user)



def percentage(user):
    with open("saveeverything.txt", "a", encoding="utf-8") as sav:
        print("how much is x percent of y")
        x = int(input("insurt x: "))
        y = int(input("insurt y: "))
        xy = x / y
        times=xy
        percent = (f"{x} is {times}% out of {y}")
        print(percent)
        sav.write(percent + "\n\n")
        sav.close()
        cs()
        main(user)


def square(user):
    number_square = int(input("insurt a number to Square root OBS x > 0: "))
    print(math.sqrt(number_square))
    main(user)


def derivaties(user):
    x = sp.Symbol('x')
    y = 3 * x ** 2 + 1
    print(sp.diff(y, x))
    main(user)


def e(user):
    number_x = input("write what you want in x (e^x): ")
    number_e = float(math.e ** number_x)
    print(f"e^{number_x} = {number_e}")
    main(user)


def pi():
    print("""
    [1] pi^
    [2] ^pi
    [3] /pi
    [4] pi/
    [5] *pi
    [6] +pi
    [7] -pi
    [8] pi-
    """)
    number_x = int(input("write what you want to to with pi"))
    if "1" in number_x:
        pass
    elif "2" in number_x:
        pass


# fil som sparar allt man har räknat ut. och som kan hämta tillbak datan.
#
# Main-caller
if __name__ == "__main__":
    name()
