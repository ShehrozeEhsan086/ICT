# calculates the energy required to heat specific amount of water. 

amount_water = float(input("Enter the amount of water in kilograms: "))
ini_temp = float(input("Enter the initial temperature in celcius: "))
final_temp = float(input("Enter the final temperature in celcius: "))

energy_req = amount_water * (final_temp - ini_temp) * 4184

print(f"The energy required is {energy_req} joules")

# Shehroze Ehsan BSE-1B 086