def celsius_converter(fahrenheit_temp):
    celsius = (fahrenheit_temp - 32) * 5 / 9
    return round(celsius, 1)


if __name__ == '__main__':
    print(celsius_converter(50))
