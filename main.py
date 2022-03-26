import math
from os import system, name

def legA():
    system('cls')
    legb = float(input("Enter a value for Leg B: "))
    hypotenuse = float(input("Enter a value for the Hypotenuse: "))

    squareb = legb ** 2
    squarec = hypotenuse ** 2

    sum = (squarec) - (squareb)
    sum2 = math.sqrt(sum)

    system('cls')
    print("Method: ")
    print("1) Square the values of Leg B and the Hypotenuse")
    print(f"Leg B squared = {squareb} ")
    print(f"Hypotenuse squared = {squarec}")
    print("2) Subtract the value of leg B from the Hypotenuse")
    print(f"{squareb} - {squarec} = {sum}")
    print("3) Then find the square root of the previous sum")
    print("This will then give you the value of Leg A")
    print(f"Value of Leg A: {sum2}")
    system('pause')


def legB():
    system('cls')
    lega = float(input("Enter a value for Leg A: "))
    hypotenuse = float(input("Enter a value for the Hypotenuse: "))

    squarea = lega ** 2
    squarec = hypotenuse ** 2

    sum = (squarec) - (squarea)
    sum2 = math.sqrt(sum)

    system('cls')
    print("Method: ")
    print("1) Square the values of Leg A and the Hypotenuse")
    print(f"Leg A squared = {squarea} ")
    print(f"Hypotenuse squared = {squarec}")
    print("2) Subtract the value of Leg A from the Hypotenuse")
    print(f"{squarea} - {squarec} = {sum}")
    print("3) Then find the square root of the previous sum")
    print("This will then give you the value of Leg A")
    print(f"Value of Leg A: {sum2}")
    system('pause')

def Hypotenuse():
    system('cls')
    lega = float(input("Enter a value for Leg A: "))
    legb = float(input("Enter a value for Leg B: "))

    squarea = lega ** 2
    squareb = legb ** 2

    sum = (squarea) + (squareb)
    sum2 = math.sqrt(sum)

    system('cls')
    print("Method: ")
    print("1) Square the values of Leg B and the Hypotenuse")
    print(f"Leg A squared = {squarea} ")
    print(f"Leg B squared = {squareb}")
    print("2) Add those numbers together")
    print(f"{squarea} + {squareb} = {sum}")
    print("3) Then find the square root of the previous sum")
    print("This will then give you the value of the hypotenuse")
    print(f"Value of Leg A: {sum2}")
    system('pause')

def Menu():
    print("               Pythagoras Calculator: (V1) - Ben Archard 26/3/22")
    print("----------------------------------------------------------------------------------------")
    print("What would you like to work out?")
    print("1) Leg A")
    print("2) Leg B")
    print("3) Hypotenuse (C)")
    start = input("You: ")

    if start == "1":
        legA()
    elif start == "2":
        legB()
    elif start == "3":
        Hypotenuse()
    else:
        print("Invalid input!")
Menu()