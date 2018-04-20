import random
n = random.randint(0,100)
vies = 9
appreciation = "?"

print("\t\t\t\t=== LE JEU DU PLUS OU MOINS ===\n\n")
print("Vous devez trouver un nombre aléatoire entre 0 et 100, vous avez 9 chances!!!")


while vies > 0:
    var = input("Entrez un nombre: ")
    var = int(var)
    if var < n :
        appreciation = "trop bas"
        print ("Nombre de chances:", vies)
        print(appreciation)
    elif var > n :
        appreciation = "trop haut"
        print("Nombre de chances:", vies)
        print(appreciation)

    elif var == n:
        print("BRAVO!!!")
        break

    vies -= 1
