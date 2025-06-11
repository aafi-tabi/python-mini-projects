a= float(input("enter a 1st number "))
b= float(input("enter a 2nd number "))
c= float(input("enter a 3rd number ")) 
d= float(input("enter a 4th number "))
if(a>b and a>c and a>d):
        print(a,"is greater")
elif(b>a and b>c and b>d):
        print(b,"is greater")
elif(c>a and c>b and c>d):
        print(c," is greater")
elif(d>a and d>b and d>c):
        print(d," is greater")
else:
        print("invalid")