# Task setup
vegetables = ["tomatoes", "potatoes", "onions"]

# Remove "onions"
vegetables.remove("onions")

# Add "carrots" if missing
if "carrots" not in vegetables:
    vegetables.append("carrots")
else:
    print("Carrots are already in the list.")

# Add "cucumbers" if missing
if "cucumbers" not in vegetables:
    vegetables.append("cucumbers")
else:
    print("Cucumbers are already in the list.")

# Sort and print result
vegetables.sort()
print("Updated Vegetable Inventory:", vegetables)