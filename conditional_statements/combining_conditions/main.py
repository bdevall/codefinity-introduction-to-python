# The item's discount and stock status have been defined
discounted = False
lowStock = True

#define a variable
movingProduct = True
promotion = True

promotion_status = discounted or lowStock
print(promotion_status)

movingProduct = discounted or lowStock
promotion = not movingProduct

print("Is the item eligible for promotion?", promotion)





