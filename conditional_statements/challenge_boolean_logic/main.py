seasonal = True
on_sale = False
selling_well = False
current_stock = 150
high_stock_threshold = 100

overstock_risk = True
status = seasonal and current_stock >= high_stock_threshold
print(status)

discount_eligible = True
sales_performance = not selling_well and not on_sale
print(sales_performance)

make_discount = True
stock_level = overstock_risk or discount_eligible
print(stock_level)

print("Should the item be discounted?", make_discount )








