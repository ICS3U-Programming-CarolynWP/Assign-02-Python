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
    length = int(input("Enter the length (cm): "))
    width = int(input("Enter the width (cm): "))
    print("\n")
    # arrow tip image
    print("    _")
    print(".-'` |")
    print("`'-._|")
    # arrow tip user input
    base = int(input("Enter the base (cm): "))
    height = int(input("Enter the height (cm): "))
    side = int(input("Enter the sides (cm): "))
    print("\n")
    # calculations
    area = (length * width) + (base * height / 2)
    perimeter = (2 * (length + width)) + (2 * side + base)
    # output
    print("The area of your arrow is : {:,.2f}cm^2".format(area))
    print("The perimeter of your arrow : {:,.2f}cm".format(perimeter))
    print("    _ ")
    print(".-'` |------.")
    print("`'-._|------'")


if __name__ == "__main__":
    main()
