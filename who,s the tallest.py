name1= input("enter your  1st person name: ")
a= float(input("enter a your height:"))
name2= input("enter your  2nd person name: ")
b= float(input("enter a your height:"))
name3= input("enter your  3rd person name: ")
c= float(input("enter a your height:"))
if(a>b and a>c):
    print(name1, "is tallest")
elif(b>a and b>c):
    print(name2,"is tallest")
elif(c>a and c>b):
    print(name3, "is tallest")
else:
    print("invalid")
    
