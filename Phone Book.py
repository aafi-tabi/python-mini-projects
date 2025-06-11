phone_numbers = {
    "aafia" : 123456789,
    "maria" : 238745895,
    "annika" : 497794385
}


name= input("enter your name").lower()

if name in phone_numbers:
    print(name,":",phone_numbers[name])
else:
    print("name not found")
 