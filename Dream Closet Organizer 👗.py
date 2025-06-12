print("👗 Dream Closet Organizer")
closet = set()
closet.add("pink dress")
closet.add("vintage hoodie")
closet.add("chunky boots")

print(closet)

item = input("write an item u want to remove from close: ").lower()

if item in closet:
    closet.remove(item)
    print(closet)
else:
    print("it’s not in the closet.")

clear = input('type "yes" if u want to clear the closet: ').lower()
if clear == "yes":
     closet.clear()
     print(closet)
     
     
else:
    print(closet)
    print("te number of items in closet are",len(closet))


closet2 = set()
 
set2  = input('type "yes" if you want to create another closet').lower()

if set2 == "yes":
    a= input("enter a 1st item: ").lower()
    closet2.add(a)
    b= input("enter a 2nd item: ").lower()
    closet2.add(b)
    c= input("enter a 3rd item: ").lower()
    closet2.add(c)
    print(closet2)
else:
    print(closet)


    

union = input("type 'yes' if you want to combine both closets: ").lower()

if union =="yes":
    print(closet.union(closet2))
else:
    print(closet)
    print(closet2)
    
     
     
    

