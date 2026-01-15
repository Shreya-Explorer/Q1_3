def temperature_convert(celsius):
    return (celsius * 9/5) + 32


if __name__ == "__main__":
    celsius = 25
    print("Temperature in Fahrenheit:", temperature_convert(celsius))
