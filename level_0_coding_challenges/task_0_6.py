def maximum_value(num1, num2, num3):
    largest_num = None
    for i in num1,num2,num3:
        if largest_num ==  None:
              largest_num = i
        elif i > largest_num:
              largest_num = i
    print(largest_num)      
    
maximum_value(-25, -1,-3)
    
