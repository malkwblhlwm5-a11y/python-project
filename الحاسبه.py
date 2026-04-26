"""turtledemo/yinyang.py

Another drawing suitable as a beginner's
programming example.

The small circles are drawn by the circle
command.

"""

from turtle import *

def yin(radius, color1, color2):
    width(3)
    color("red", color1)
    begin_fill()
    circle(radius/2., 180)
    circle(radius, 180)
    left(180)
    circle(-radius/2., 180)
    end_fill()
    left(90)
    up()
    forward(radius*0.35)
    right(90)
    down()
    color(color1, color2)
    begin_fill()
    circle(radius*0.15)
    end_fill()
    left(90)
    up()
    backward(radius*0.35)
    down()
    left(90)

def main():
    reset()
    yin(200, "blue", "red")
    yin(200, "red", "blue")
    ht()
    return "Done!"

if __name__ == '__main__':
    main()
    mainloop()

#user name
user_name = input("enter user name")
#password
password = input("enter password")
#if login
if user_name == "admin" and password == "admin123":
    print("login succsesful")
else:
    print("currect password or user name")
    print()
#calculator
number1 = float(input("enter number: "))
operator = input("enter operator: ")
number2 = float(input("enter number: "))
if operator == "+":
    print(number1 + number2)
elif operator == "-":
    print(number1 - number2)
elif operator == "*":
    print(number1 * number2)  
elif operator == "/":
    print(number1 / number2)
else:
    print("error in operator")
input("press enter to exit")    
if input("press enter to exit") == "":
    print("april fools")
user_name = input("enter user name")
#password
password = input("enter password")
#if login
if user_name == "admin" and password == "admin123":
    print("login succsesful")
else:
    print("currect password or user name")
    print()
#calculator
number1 = float(input("enter number: "))
operator = input("enter operator: ")
number2 = float(input("enter number: "))
if operator == "+":
    print(number1 + number2)
elif operator == "-":
    print(number1 - number2)
elif operator == "*":
    print(number1 * number2)  
elif operator == "/":
    print(number1 / number2)
else:
    print("error in operator")
input("press enter to exit ")
























