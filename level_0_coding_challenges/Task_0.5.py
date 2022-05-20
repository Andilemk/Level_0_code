import math

# Herons formula used the length of the sides of a triangle to calculate it's area

def area_of_triangle(a,b,c):
    sides = a + b + c
    sides = 1/2*(sides)
    sides_perimeter = sides*(sides - a)*(sides - b)*(sides - c)
    Area = math.sqrt(sides_perimeter)
    return Area

print(area_of_triangle(3, 4, 5), "metres squared")
    
