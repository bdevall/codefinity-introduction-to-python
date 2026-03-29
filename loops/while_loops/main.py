# Task: Create a discount countdown timer that collects all countdown values in a list using a while loop.

start_number = 5
countdown_values = []

# Countdown using while loop
current = start_number
while current >= 1:
    countdown_values.append(current)
    current -= 1

# Print results
print("Discount countdown complete!")
print(countdown_values)