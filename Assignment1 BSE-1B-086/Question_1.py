# Calculates the average speed of a runner in Miles/Hour.

distance_kms = 14
time_minutes = 45
time_sec = 30

distance_miles = distance_kms / 1.6
time_hours = ( time_minutes + ( time_sec / 60) ) / 60  
avg_speed = distance_miles / time_hours

print(f"Average Speed is {format(avg_speed,'.2f')} miles/hour.")

# Shehroze Ehsan BSE-1B 086