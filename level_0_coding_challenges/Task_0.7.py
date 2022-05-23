
def convert_to_farenheit(celsius_degrees):
    farenheit = (celsius_degrees * 1.8) + 32
    return farenheit
def convert_to_celsius(farenheit_degrees):
    celsius_degrees = (farenheit_degrees - 32) * (5/9)
    return celsius_degrees


print(f"The degrees converted from farenheit to celcius are: {convert_to_celsius(77)}")

print(f"The degrees converted from celcius to farenheit are: {convert_to_farenheit(25)}")
