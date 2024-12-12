import math

square_length = float(input("What is the length of the square? "))
square_area = square_length ** 2
print(f"The area of the square is {square_area:.2f}\n")

rectangle_length = float(input("What is the length of the rectangle? "))
rectangle_width = float(input("What is the width of the rectangle? "))
rectangle_area = rectangle_length * rectangle_width
print(f"The area of the rectangle is {rectangle_area:.2f}\n")

circle_radius = float(input("What is the radius of the circle? "))
circle_area = math.pi * circle_radius ** 2
print(f"The area of the circle is {circle_area:.2f}\n")

length = float(input("Enter a single length: \n"))

square_area_length = length ** 2
circle_area_length = math.pi * length ** 2
cube_volume_length = length ** 3
sphere_volume_length = (4 / 3) * math.pi * length ** 3

print(f"The area of the square with side {length} is {square_area_length:.2f}")
print(f"The area of a circle with radius {length} is {circle_area_length:.2f}")
print(f"The volume of a cube with side {length} is {cube_volume_length:.2f}")
print(f"The volume of a sphere with radius {length} is {sphere_volume_length:.2f}")