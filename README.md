# Note on the Distance Formula: 
The Euclidean distance formula calculates the straight-line distance between two points on a 2D plane. It uses the Pythagorean theorem (a² + b² = c²), where the horizontal change is (x2 - x1) and the vertical change is (y2 - y1). Taking the square root gives us the final distance.

# Prompting the user for coordinates
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Calculating the horizontal and vertical differences
delta_x = x2 - x1
delta_y = y2 - y1

# Calculating the distance using math.pow() for squaring and math.sqrt() for the square root
distance = math.sqrt(math.pow(delta_x, 2) + math.pow(delta_y, 2))

# Displaying the final result clearly
print(f"The distance between the two points is: {distance:.2f}")


# REFLECTION:
Using a library is more practical because it provides pre-tested, optimized functions like sqrt() and pow(), saving time and reducing the risk of errors. 
Instead of writing complex algorithms from scratch to approximate a square root manually, I could solve the formula in a single, readable line of code. 
Without the math library, the program would be much longer and harder to write, as computing square roots manually requires implementing advanced mathematical loops.


# WHAT I CHANGED AND WHY?
WHAT: Added an explanatory comment about the Pythagorean theorem at the top of the script and introduced intermediate variables `delta_x` and `delta_y`.
WHY: This makes the mathematical logic behind the Euclidean distance formula easier to understand and improves code readability by simplifying the expression inside `math.sqrt()`.
