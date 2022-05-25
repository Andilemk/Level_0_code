def maximum_value(num1, num2, num3, num4):
    largest_num = 0 
    for i in num1,num2,num3,num4:
        if i > largest_num:
            largest_num = i
    return largest_num
    
print(maximum_value(29,4,25,29))
    
