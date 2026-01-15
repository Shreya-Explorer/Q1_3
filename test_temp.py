from temp import temperature_convert

def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


if __name__ == "__main__":
    temp_c = 25.0   # default Celsius value
    temp_f = celsius_to_fahrenheit(temp_c)
    print("Temperature in Fahrenheit:", temp_f)
