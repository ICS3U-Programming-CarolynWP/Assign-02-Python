#!/usr/bin/env python3
# Created by: Carolyn Webster Pless
# Created on: 2022/10/01
# Takes user input for the length, width, base,
# height, and side of the arrow and
# displays the area and perimeter back to
# the user


import math


def main():
    # title
    print(">>>>>>>_____________________\`-._")
    print(">>>>>>>                     /.-'")
    print("Area and Perimeter of an Arrow")

    # arrow base image
    print(" _________")
    print("|         |")
    print("|_________|\n")

    # arrow base user input
    length = int(input("Enter the length: "))
    width = int(input("Enter the width: "))
    print("\n")

    # arrow tip image
    print("    _")
    print(".-'` |")
    print("`'-._|")

    # arrow tip user input
    base = int(input("Enter the base: "))
    height = int(input("Enter the height: "))
    side = int(input("Enter the sides: "))
    print("\n")

    # units user input
    units = input("What are the units for your arrow? :")
    print("\n")

    # calculations
    area = (length * width) + (base * height / 2)
    perimeter = (2 * (length + width)) + (2 * side + base)

    # output
    print("The area of your arrow is {:,.2f}".format(area), units, "^2")
    print("The perimeter of your arrow {:,.2f}".format(perimeter), units)
    print("    _ ")
    print(".-'` |------.")
    print("`'-._|------'")


if __name__ == "__main__":
    main()
