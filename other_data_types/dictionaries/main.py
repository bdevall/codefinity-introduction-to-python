grocery_inventory = {
    "Milk" : (113, "Dairy"),
    "Eggs" : (116, "Dairy"),
    "Bread" : (117, "Bakery"),
    "Apples" : (141, "produce")
}

bread_details = grocery_inventory.get("Bread")
#bread_details = grocery_inventory.["Bread"] -- this is aslo another way to get the or fetch the info
print("Details of Bread:", bread_details)

grocery_inventory["Cookies"] = (143, "Bakery")
# grocery_inventory.update({"Cookies": (143, "Bakery")}) --another way of writing
print("Inventory after adding Cookies:", grocery_inventory)

grocery_inventory.pop("Eggs")
print("Inventory after removing Eggs:", grocery_inventory)