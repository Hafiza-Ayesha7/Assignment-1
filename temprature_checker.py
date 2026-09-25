# Step 1: Read temperature
temp = float(input("Enter today's temperature in Celsius: "))

# Step 2: Check weather condition
if temp > 35:
    print("It's a hot day")
elif temp < 15:
    print("It's a cold day")
else:
    print("The weather is pleasant")