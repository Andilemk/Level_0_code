



def area_of_triangle(a,b,c):
    sides = a + b + c
    sides = 1/2*(sides)
    sides_perimeter = sides*(sides - a)*(sides - b)*(sides - c)
    Area = (sides_perimeter) ** 0.5 
    return Area

print(area_of_triangle(3, 4, 5), "metres squared")
    
