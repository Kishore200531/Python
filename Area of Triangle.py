#When all the length of the sides is known - a,b,c
#Semi perimeter = (a+b+c)/2
#Area = square root of (s*(s-a)*(s-b)*(s-c))

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))
s = (a + b + c)/2
area = (s*(s+a)*(s+b)*(s+c))**0.5
print("Area of Triangle:", area)
print("Area of Triangle:", round(area,2)) #Round fun'n is used to round off the decimal digits


#When base and height is known - b,h
#Area = (1/2)*b*h

b = float(input("Enter base value b: "))
h = float(input("Enter height value h: "))
area = (b*h)/2
print("Area of Triangle:", area)