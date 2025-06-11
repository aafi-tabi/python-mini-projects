item_1= input("enter a item1 name: ")
a= float(input("enter a price 1: "))
item_2= input("enter a item2 name: ")
b= float(input("enter a price 2: "))
item_3= input("enter a item3 name: ")
c= float(input("enter a price 3: "))

add= a+b+c
if(add>500):
    dis= add/10
    discount=add-a
    print("total is =",discount)
    print("discount is applied")
else:
    print("total is =",add)
