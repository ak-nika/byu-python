"""
Author: Akingbayi Ojo
Purpose: To calculate the wind chill of a given temperature
"""


def calculate_wind_chill(temp, speed):
    wind_chill = (
        35.74 + 0.6215 * temp - 35.75 * speed**0.16 + 0.4275 * temp * speed**0.16
    )
    return wind_chill


def celsius_to_fahrenheit(temp):
    return temp * 9 / 5 + 32


temperature = float(input("What is the temperature? "))
unit = input("Fahrenheit or Celsius (F/C)? ")

if unit.lower() == "c":
    temperature = celsius_to_fahrenheit(temperature)
speed = 5

while speed <= 60:
    wind_chill = calculate_wind_chill(temperature, speed)

    print(
        f"At temperature {temperature:.1f}F, and wind speed {speed}mph, the wind chill is {wind_chill:.2f}F"
    )
    speed += 5
