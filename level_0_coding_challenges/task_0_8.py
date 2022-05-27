def change_to_time(number):
    hours = number // 60
    minutes = number % 60
    if minutes < 10:
        minutes = "0" + str(minutes)
    if hours == 1 and minutes == "01":
        print(f"the time is {hours} hour, {minutes} minute")
    elif hours == 1:
        print(f"the time is {hours} hour, {minutes} minutes")
    elif minutes == "01":
         print(f"the time is {hours} hours, {minutes} minute")
    else:
        print(f"the time is {hours} hours, {minutes} minutes")
    
change_to_time(61)

