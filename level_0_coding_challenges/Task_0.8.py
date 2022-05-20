from lib2to3.pytree import convert


def convert_time(number):
    hours = number // 60
    minutes = number % 60
    print(f"the time is {hours} hours and {minutes} minutes")
    
convert_time(1000)