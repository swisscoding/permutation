#!/usr/local/bin/python3
# Made by @swisscoding on Instagram
# Follow now and share!

from colored import stylize, fg
import math

# decoration
print(stylize("\n---- | Calculate possible permutations | ----\n", fg("red")))

# user interaction
list = input("Enter a list of UNIQUE digits: ").split(", ")

# main program
list = [int(i) for i in list]

# check if every digit is unique
count = 0
for i in list:
    if list.count(i) > 1:
        count += 1

if count != 0:
    print("\nThis list does not meet the requirements!\n")

else:
    print(f"\nList of digits:\n{list}\n")
    permutations_count = stylize(str(math.factorial(len(list))), fg("red"))
    print(f"Possible permutations with {len(list)} digit/s: {permutations_count}\n")
