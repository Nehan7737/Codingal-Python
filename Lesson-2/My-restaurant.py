snack_name="Burger"
price=2.5
quantity=3
availibility=True

print(type(snack_name))

print(type(price))

print(type(quantity))

print(type(availibility))



print("The snack's name is",snack_name)
print("The price of the",snack_name ,"is",price)
print("The quantity of the",snack_name,"is",quantity)
print("is",snack_name,"available?:",availibility)

total=price*quantity
print("The total price of",snack_name,"will be",total)

sale_price=price-0.35
print("The total sale price will be",sale_price)

double_stock=quantity*quantity
print("the double stock will be",double_stock)

print("is the price under $2",price<2)

print("more than five in stock?",quantity>5)

print("is the price exactly 2.5?",price==2.5)

shop_name="Nehan's"+" "+"Cafe"

print("The shop's name is",shop_name)

print(len(shop_name))
print(shop_name[4])
x=4
y=5

temp=x
x=y
y=temp

print(x)
print(y)

