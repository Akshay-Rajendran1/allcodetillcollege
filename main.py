# Program Name: Decision Logic
# Program Description:
#   This is the second lab in which I will check the aspects of a car
#
#   This program will calculate the efficiency of a car and other aspects of it
# @Author: Akshay Rajendran
# @Date: 6/21/22

from datetime import datetime

current_time = datetime.now()
current_time_str = str(current_time)
print("Name         : CNET-142 Akshay Rajendran")
print("Lab          : Lab 2 - Decision Logic")
print("Current Time :", current_time_str)

capacity = float(input("Enter the capacity of the car's gas tank (in gallons): "))
miles_per_gallon = int(input("Enter car's miles per gallon: "))
price_per_gallon = float(input("Enter price per gallon: "))

cost = 100 / miles_per_gallon * price_per_gallon
distance = capacity * miles_per_gallon

print(f"cost for driving 100 miles is ${cost: .2f}")
print(f"distance on a tank of gas is: {distance: .2f}")

if miles_per_gallon < 30:
    print(f"Your car MPG is {miles_per_gallon: .1f} it is not a fuel efficient car")
elif miles_per_gallon < 40:
    print(f"Your car MPG is {miles_per_gallon: .1f} it is a average fuel efficient car")
elif miles_per_gallon <50:
    print(f"Your car MPG is {miles_per_gallon: .1f} it is a fuel efficient car")
else:
    print(f"Your car MPG is {miles_per_gallon: .1f} it is a very fuel efficient car")

