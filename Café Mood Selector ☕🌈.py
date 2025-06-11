moods = (input("enter your mood: "))
mood= moods.lower()


if(mood=="cozy"):
    print("Hot Chocolate")
elif(mood=="energetic"):
    print("Espresso")
elif(mood=="romantic"):
    print("Rose Latte")
elif(mood=="sad"):
    print("Mocha with extra whipped cream")
elif(mood=="productive"):
    print("Iced Americano")
else:
    print("Oops! Mood not found. Try cozy, energetic, romantic, sad, or productive 🌈")
