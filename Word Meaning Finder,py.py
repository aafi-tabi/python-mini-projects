word = {
     "python": "A powerful programming language.",
    "aesthetic": "Concerned with beauty or the appreciation of beauty.",
    "tuple": "An immutable collection of items in Python.",
    "loop": "A sequence of instructions that is continually repeated.",
    "debug": "To fix errors in a program."
}
name = input("enter a word: ").lower()

if name in word:
    print(name,":",word.get(name))
else:
    print("not found")

