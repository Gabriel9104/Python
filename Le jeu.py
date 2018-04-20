from random import randrange

nombrePropose = 0

print("\t\t\t\t=== LE JEU DU PLUS OU MOINS ===\n\n")

nombreMystere = randrange(1, 100)

while nombrePropose != nombreMystere:

    print("Quel est le nombre ?")

    nombrePropose = input()
    nombrePropose = int(nombrePropose)

    if nombrePropose < nombreMystere:
        print("C'est trop petit !\n")

    elif nombrePropose > nombreMystere:
        print("C'est trop grand !\n")

    else:
        print("Bravo")


