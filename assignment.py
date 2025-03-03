#Author Theis Noordhof
#Date Modified 2/24/2025
#Description Different types of variables 

#integer
print("Integers are whole numbers that are positive or negative")
x=5
print("For example:")
print(x)


#Floats
print("Floats are numbers with decimal points")
x=133.5
print("For example:")
print(x)

#Double
print("Double is more acurate numbers with decimal points")
x=3.14
print("For example:")
print(x)

#Char
print("Char is single characters")
x
print("For example:")
print(x)

#Booleans
print("Booleans are True or False")
logged_in = True
print("For example:")
print(logged_in)

#Strings
print("Strings are combination of characters")
print("For example")
print("Hello World")

#Calculating with different math operations
import math 

#Addition
print("Addition is the sum of two numbers")
sum_add=5+2
print("For example 5+2 is equal to")
print(sum_add)

#Subtraction
print("Subtraction is the difference between two numbers")
difference = 10-5
print("For example 10-5 is equal to")
print(difference)

#Product
print("Product is the multiplication of numbers")
prod=2*2*5
print("For example the product of 2*2*5 is equal to")
print(prod)

#Quotient Integer 
print("Quotient integer is the division two numbers")
quot = 25/5
print("For example 25/5 is equal to")
print(quot)

#Quotient Float
quot_float = 24.0/7
print(quot_float)

#Square Root
print("Square root of a number")
square = math.sqrt(144)
print("For example the square root of 144 is equal to")
print(square)

#Exponents 
nth_power = 3**4
print(nth_power)

#Modulus 
rem_1 = 30%7
print(rem_1)


#Finding the discriminant(the part of the quadratic formula that tells you the number of roots a quadratic function has)
print("The formula for finding the discriminant is b squared - 4ac.")
a=int(input("Please type in the a value and press enter "))
b=int(input("Please type in the b value and press enter "))
c=int(input("Please type in the c value and press enter "))
#The formula for the discriminant 
d=b^2-4^a^c
print("The discriminant is",d)

#Calculating the volume of 3 dimensional shapes

#Volume of a cube
print("The formula to find the volume of a cube is *Side length* cubed")
side_length = float(input("Enter the side length of the cube: "))
volume = side_length ** 3
print(f"The volume of the cube is: {volume} cubic units.")

#Volume of a sphere
shape = "sphere"
radius = float(input("Enter the radius of the sphere: "))
volume = (4/3) * math.pi * radius**3
print(f"The volume of the sphere is: {volume} cubic units.")

#Volume of a cone
shape = "cone"
radius = float(input("Input the radius of the cone's base: "))
height = float(input("Enter the height of the cone: "))
volume = (1/3) * math.pi * radius**2 * height
print(f"The volume of the cone is: {volume} cubic units. ")

#Volume of a cylinder 
shape = "cylinder"
radius = float(input("Enter the radius of the cylinders base: "))
height = float(input("Enter the height of the cylinder: "))
volume = math.pi * radius**2 * height
print(f"The volume of the cylinder is: {volume} cubic units. ")
