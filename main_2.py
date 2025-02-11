# Program Name: Functions
# Program Description:
#   This is the fourth lab in which I will make an interest and mortgage calculator
#
#   This program will calculate the total earned and the interest earned and the mortgage payment
# @Author: Akshay Rajendran
# @Date: 6/30/22

from mortgage import mortgage
from simple_interest import interest
from datetime import datetime
current_time = datetime.now()

current_time_str = str(current_time)
print("Name         : CNET-142 Akshay Rajendran")
print("Lab          : Lab 4 - Functions")
print("Current Time :", current_time_str)
print()
print()

x = 0
def options():
    x = int(input("Select one of the command numbers above: "))
    if x == 1:
        interest()
        return
    elif x == 2:
        mortgage()
        return
    elif x == 99:
        print("Have a nice day...")
        global z
        z = 0
    else:
        print("Error: command not recognized")
        options()

z = 1
while z == 1:
    print()
    print("---" * 10)
    print("1    Calculate Simple Interest")
    print("2    Calculate Mortgage Payment")
    print("99   Quit the program")
    print("---" * 10)
    print()
    options()





