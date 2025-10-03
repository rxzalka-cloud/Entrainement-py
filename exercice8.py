prenom = input("Quel est ton prenom ?")
age = int(input("Quel age a tu ? "))

if age <= 12:
    print("Bonjour",prenom,"tu es un enfants et dans 10 ans tu auras ",(age + 10),"ans")
elif age <= 17:
    print("Bonjour",prenom,"tu es un adolescent et dans 10 ans tu auras ",(age + 10),"ans")
else:
    print("Bonjour",prenom,"tu es un adulte et dans 10 ans tu auras ",(age + 10),"ans")
