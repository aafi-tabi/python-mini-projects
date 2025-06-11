num1= float(input("enter a 1st number: "))
num2= float(input("enter a 2nd number: "))
operator= input("enter a operator(+,-,*,/): ")
if(operator=="+"):
        print(num1+num2)
elif(operator=="-"):
        print(num1-num2)
elif(operator=="*"):
        print(num1*num2)
elif(operator=="/"):
        print(num1/num2)
else:
        print("invalid")              
