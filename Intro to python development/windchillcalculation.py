def calculate_wind_chill(temp, speed):
   
    wind_chill = 35.74 + 0.6215 * temp - 35.75 * speed ** 0.16 + 0.4275 * temp * speed ** 0.16
    return wind_chill

def convert_to_fahrenheit(temp):
    return temp * (9/5) + 32

temp = float(input("What is the temperature? "))
unit = input("Fahrenheit or Celsius (F/C)? ")

if unit.upper() == "C":
    temp = convert_to_fahrenheit(temp)

print(f"At temperature {temp:.1f}F:")
for speed in range(5, 61, 5):
    wind_chill = calculate_wind_chill(temp, speed)
    print(f"and wind speed {speed} mph, the windchill is: {wind_chill:.2f}F")
