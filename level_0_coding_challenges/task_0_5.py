def area_of_triangle(side_1,side_2,side_3):
    sides = side_1 + side_2 + side_3
    sides = 1/2*(sides)
    sides_perimeter = sides*(sides - side_1)*(sides - side_2)*(sides - side_3)
    area = (sides_perimeter) ** 0.5 
    return area

print(area_of_triangle(3, 4, 5), "metres squared")
    
