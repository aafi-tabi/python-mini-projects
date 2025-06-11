menu = {
     "burger": 300,
    "fries": 150,
    "pizza": 500,
    "drink": 100
}

food = input("enter a food: ").lower()

if food in menu:
    print(food,"price is",menu.get(food))
else:
    print("not found")