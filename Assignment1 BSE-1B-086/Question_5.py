# Calculates minimum length required for runway in view to aeroplane's velocity and acceleration.

vel_ , accel_ = eval(input("Enter speed (m/s) and acceleration (m/s^2)[seperate by comma]: "))

min_length = ( vel_ ** 2 ) / ( 2 * accel_ )

print(f"The minimum runway length for this aeroplane is {format(min_length,'.3f')} meters")

# Shehroze Ehsan BSE-1B 086