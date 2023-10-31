#printing out the menu
print("here is the food menu of things you can buy")
print("pizza = £7.30")
print("pie = £3.45")
print("burger = £4.50")
print("chips = £2.00")
print("onion rings = £2.30")
print("drink = £1.50")
#creating the order and total variable
order = []
total = 0.00
ordering = True
while ordering == True:
    print("What would you like? type in the word finish when you are done ordering")
    item = input().lower()
    if item == "finish":
        break
    if item == "pizza":
        order.append("pizza 7.30")
        total += 7.30
    if item == "pie":
        order.append("pie 3.45")
        total += 3.45
    if item == "burger":
        order.append("burger 4.50")
        total += 4.50
    if item == "chips":
        order.append("chips 2.00")
        total += 2.00
    if item == "onion rings":
        order.append("onion rings 2.30")
        total += 2.30
    if item == "drink":
        order.append("drink 1.50")
        total += 1.50
print("the items you ordered are")
for x in order:
    print(x)
print(f"your total price is {total}")
#using commands to make the program calculate the total price of the foods and drink

