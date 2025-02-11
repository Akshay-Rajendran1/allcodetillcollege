import random
greeting = ["hi hi", "good morning", "hello", "hi"]
print(random.choice(greeting))
x = ["first", "second", "third", "fourth"]
x[0]="fart"
y = int(input())
print (x[y-1])
numbers = [1,2,4,53,5,7,8,5]
numbers.sort (reverse = True)
print(numbers)
v = 0
while (v <= 100):
    v = v + 1
    if (v <= 100):
        print (v)
    else :
        print("hi")
print(round(3.6))
from math import *
print(floor(8.7))
print(ceil(4.5))
print(sqrt(25))
name = input("enter your name :")
age = input("enter your age :")
print("hello " + name + "! " "you are " + age + " years old")
numb1 = input("enter your number:")
numb2 = input ("enter the number you want to add:")
result = float(numb1) + float(numb2)
print(result)
print(x[0])
b=[3,4,5]
x.extend(b)
print(x)
x.append("muhahahaha")
print(x)
x.insert(0,"no")
print(x)
x.remove(3)
print(x)
c=["q"]
c.clear()
print(c)
def say_hi (no ,bag):
    print("hello " + no + ",you are " + str(bag))
say_hi("mike" , 90001)
def cube (num):
    return num*num*num
print(cube(3))
is_male=True
is_tall=True
if is_male and is_tall :
    print("you are male and tall")
elif is_male and not(is_tall):
    print("you are male and short")
elif not(is_male) and is_tall:
    print("you are not male and tall")
else:
    print("you are not male or you are not tall")
def max_num(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
print(max_num(1,3,2))
number1 = float(input("enter first number: "))
op = input("enter the operator you want to use: ")
number2 = float(input("enter second number: "))

if op == "+":
    print(number1 + number2)
elif op == "-":
    print(number1 - number2)
elif op == "*":
    print(number1 * number2)
elif op == "/":
    print(number1 / number2)
else:
    print("invalid operator")
month_conversion={
    "jan":"January",
}
print(month_conversion.get("jan", "not a valid name"))
secret_word="pig"
guess=""
while guess != secret_word:
    guess = input("enter guess: ")
print("you win!!!")

name1=input("who is player one: ")

name2=input("who is player two: ")

person1=input(name1 + " enter rock, paper or scissors: ")

person2=input(name2 + " enter rock, paper or scissors: ")

if person2 == "rock" and person1 == "paper":
    print(name1 + " wins")

elif person1 == "rock" and person2 == "rock":
    print("tie game")

elif person2 == "rock" and person1 == "paper":
    print(name1 + " wins")

elif person2 == "rock" and person1 == "scissors":
    print(name2 + " wins")

elif person1 == "scissors" and person2 == "paper":
    print(name1 + " wins")

elif person1 == "scissors" and person2 == "scissors":
    print("tie game")

elif person2 == "scissors" and person1 == "rock":
    print(name1 + " wins")

elif person2 == "scissors" and person1 == "paper":
    print(name2 + " wins")

elif person1 == "paper" and person2 == "paper":
    print("tie game")

else:
    print("invalid input by a player")

lower = 100
upper = 1000

for num in range(lower, upper + 1):


   order = len(str(num))


   sum = 0

   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       print(num)
sum = 0
n = 5
x = 1
print(x)
while x != n:
    sum = sum + x
    x = x+1
    print(x,sum)
    if x == n:
        sum = sum + x
        print(sum)