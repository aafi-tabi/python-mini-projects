a= float(input("enter your marks: "))
if(a>=90 and a<=100):
    print("A")
elif(a>=80 and a<=89):
    print("A+")
elif(a>=70 and a<=79):
    print("B")
elif(a>=60 and a<=69):
    print("C")
elif(a>=50 and a<=59):
    print("D")
elif(a>=0 and a<=49):
    print("F")
else:
    print("invalid")