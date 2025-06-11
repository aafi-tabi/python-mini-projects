marks = {
    "aafia" : 100,
    "maria" : 98,
    "annika" : 78

}

name = input("enter your name : " ).lower()

if name in marks:
    grade = marks[name]
    if grade >= 90:
        print("A")
    elif grade >= 80:
        print("B")
    elif grade >= 70:
        print("C")
    elif grade >= 60:
        print("D")
    else: 
        print("F")
        