def change_to_time(number):
    hours = number // 60
    minutes = number % 60
    if minutes < 10:
        minutes = "0" + str(minutes)
    if hours =< 1:
        print(f"the time is {hours} hour and {minutes} minutes")
    else:
        print(f"the time is {hours} hours and {minutes} minutes")
        
    
change_to_time(60)
