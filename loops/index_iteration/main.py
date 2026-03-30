prices = [29.99, 45.50, 12.75, 38.20]
discounts = [0.10, 0.20, 0.15, 0.05]

for i in range(len(prices)):
    # Apply the correct discount for this index
    prices[i] = prices[i] * (1 - discounts[i])
    # Print with two decimal places
    print(f"Updated price for item {i}: ${prices[i]:.2f}")