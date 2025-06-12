print("🌟✨ Welcome to the Concert Vibes Filter ✨🌟")
print("Are you ready to vibe with your favorite fans?\n")
kpop = set()

print("enter the name of your kpop stans: ")

a= input("bias # 1 :").lower()
kpop.add(a)
b= input("bias # 2: ").lower()
kpop.add(b)
c= input("bias # 3: ").lower()
kpop.add(c)


aesthetic = set()

print("🌸 Enter names of your Aesthetic Music lovers 🎧")
d = input("Muse # 1:").lower() 
aesthetic.add(d)
e = input("Muse # 2:").lower() 
aesthetic.add(e)
f = input("Muse # 3:").lower() 
aesthetic.add(f)

aesthetic = {d,e,f}

print(kpop)
print(aesthetic)

print("fans who love both",kpop.intersection(aesthetic))
print("total fans to invite",kpop.union(aesthetic))

print("only kpop fans",kpop.difference(aesthetic))
print("only aesthetic lovers",aesthetic.difference(kpop))