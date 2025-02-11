# Program Name: functions.py
# Program Description:
#   This is the Fifth lab
#
#   In this program I make a progarm to count and do various things regarding a text file
# @Author: Akshay Rajendran
# @Date: 7/14/22

from datetime import datetime

current_time = datetime.now()
current_time_str = str(current_time)

print("Name         : CNET-142 Akshay Rajendran")
print("Lab          : Lab 5 - File and list")
print("Current Time :", current_time_str)
print()

lst = []
l = w = 0
c = -12

f = open("test.txt", "r")
for line in f:
    lst.append(line.strip())
    l += 1
    c += len(line)
    w += len(line.split())

sp = 12
up = lo = no = st = 0
z = 1

for l in lst:
    print(f"Line  {z}  : {l}")
    z += 1
z -= 1

chars = list(''.join(lst))
for ch in chars:
    if ch.isupper():
        up += 1
    elif ch.islower():
        lo += 1
    elif ch.isspace():
        sp += 1
    elif ch.isdigit():
        no += 1
    elif ch == '.' or ch == '!' or ch == '?':
        st += 1


print(f"Total number of lines: {z}")
print(f"Total number of words: {w}")
print(f"Total number of characters: {c}")
print(f"Total number of uppercase letters: {up}")
print(f"Total number of lowercase letters: {lo}")
print(f"Total number of spaces: {sp}")
print(f"Total number of digits: {no}")
print(f"Total number of sentences: {st}")

f.close()