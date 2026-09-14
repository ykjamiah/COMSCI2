import math

# Prompting the user for coordinates
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Calculating the distance using math.pow() and math.sqrt()
# Formula: d = sqrt((x2 - x1)^2 + (y2 - y1)^2)
distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

# Displaying the final result clearly
print(f"The distance between the two points is: {distance:.2f}")

"""
REFLECTION:
Using a library is more practical because it provides pre-tested, optimized functions like sqrt() and pow(), saving time and reducing the risk of errors. 
Instead of writing complex algorithms from scratch to approximate a square root manually, I could solve the formula in a single, readable line of code. 
Without the math library, the program would be much longer and harder to write, as computing square roots manually requires implementing advanced mathematical loops.
"""
