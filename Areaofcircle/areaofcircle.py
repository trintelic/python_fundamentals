print("Coding to Calculate the Area of a Circle")
print("Requests radius from user and calculates circle area. Detects incorrect input.")

import math

while True:
    try:
        radius = float(input("Please enter the circle radius:").strip())

        if not math.isfinite(radius):
            print("Enter a finite number! Please try again.")
            continue
        elif radius < 0:
            print("Must have a positive number! Please try again.")
            continue
        else:
            break
    except ValueError:
        print("Invalid input. Please ender a numerical value!")

area = 3.14 * radius**2

print("Radius:", radius)
print("Area:", area)
