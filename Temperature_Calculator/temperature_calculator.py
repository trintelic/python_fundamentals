print("Temperature Calculator")
print("Program calculates the Fahrenheit version for a Celcius value.")

import math

while True:
    try:
        Celcius = float(input("Please enter Celcius temperature value:").strip())

        if not math.isfinite(Celcius):
            print("Enter a finite number! Please try again.")
        elif Celcius < -273.15:
            print("Temperature cannot be below -271.15!")
        else:
            break

    except ValueError:
        print("Invalid input! Please enter a numerical value!")

Fahrenheit = (Celcius * 9 / 5) + 32

print("Celcius:", Celcius)
print("Fahrenheit:", Fahrenheit)

label = input("Please enter a label: ").strip()

if label == "":
    label = "Temperature"
elif len(label) > 20:
    label = label[:20]
    print("Label is now shortened to 20 characters.")

print("Label:", label)
print("Uppercase Label:", label.upper())
print("Lowercase Label:", label.lower())
print("Number of characters:", len(label))
