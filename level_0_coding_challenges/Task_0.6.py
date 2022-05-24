def maximum_value(numbers):
    largest_num = 0
    for number in numbers:
        if number > largest_num:
            largest_num = number
    print(f"The largest number is in the list is: {largest_num}")
    
    count = 0
            
    for number in numbers:
        if number == largest_num:
            count += 1
    print(f"The number of largest numbers there are in the list is: {count}")
             
maximum_value([12,4,25,29])
    
