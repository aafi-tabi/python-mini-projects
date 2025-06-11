print(" 🛍️ Welcome to Blush Boutique 🌸")

catalog = {
      "dress": "Flowy chiffon dress with pearl straps",
    "bag": "Heart-shaped pastel mini bag",
    "shoes": "Lace-up platform boots",
    "lip gloss": "Strawberry shimmer gloss",
    "bow": "Satin baby pink hair bow"
    
}
boutique = input("What item are you looking for? ").lower()

if boutique in catalog:
    print(boutique.title(),":",catalog.get(boutique))
else:
    print("Oops! That item isn’t in the boutique 🕊️")