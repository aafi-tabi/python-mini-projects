mood_ring ={
     "blue": "Calm & Peaceful",
    "red": "Energetic & Bold",
    "green": "Balanced & Fresh",
    "black": "Stressed or Overwhelmed",
    "pink": "Romantic & Soft"
    
}

color= input("enter your fav color: " ).lower()

if color in mood_ring:
    print("your are",mood_ring.get(color))
else:
    print("aura is undetected")

