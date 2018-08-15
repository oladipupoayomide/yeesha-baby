"""
this program is meant to compute the area of a sector
enter value for pie
enter value for theta
enter value for radius
display  area
"""
print("this program is meant to calculate area of a sector")
pie = float(input("enter the value of pie:"))
radius = float(input("enter the value of radius:"))
theta= float(input("enter the value of theta:"))
area= (theta/360)*pie*radius*radius
print ("area","of","a","sector","is")
print (area)

"""
this program is meant to calculate area of a square
enter value for length
display area
"""
print("this program is meant to calculate area of a square")
#ask for length
length = float(input("enter the length:"))
#multiply to get area
area =length*length
#print area
print ("area","of","a","square","is")
print (area)

"""
this program is expected to calculate the area of a cylinder
enter the value of radius
enter the value of height
enter the value of pie
display area
"""
print("this is expected to calculate the area of a cylinder")
pie = float(input("enter the value for pie:"))
radius = float(input("enter the value for radius:"))
height = float(input("enter the value for height:"))
area = (pie*radius*radius*height)
print ("area","of","a","cylinder","is")
print(area)

"""
this program is meant to calculate the area of a triangle
you are required to
enter value for base
enter value for height
display area
"""
print("this program is meant to calculate area of a triangle")
base = int(input("enter value for base:"))
height = int(input("enter value for height:"))
area =(1/2)*base*height
print ("area","of","a","triangle","is")
print (area)

"""
this program is meant to compute area of a trapezoid
you are required to
enter the value for base 1
enter the value for base 2
enter the value for height
display area
"""
print("this program is meant to calculate area of a trapezoid")
base1=float(input("enter the value for base 1:"))
base2=float(input("enter the value for base 2:"))
height=float(input("enter the value for height:"))
area=((base1+base2)*height)/2
print("area","of","a","trapezoid","is")
print(area)

        
               

