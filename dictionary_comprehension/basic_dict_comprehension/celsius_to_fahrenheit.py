# formula to convert Celsius to fahrenheit is (12*9/5)+32

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24, }
print({day: (temp_c * 1.8) + 32 for (day, temp_c) in weather_c.items()})
