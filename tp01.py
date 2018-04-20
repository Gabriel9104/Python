def exo01():
    nb = "Je dois faire des sauvegardes régulières de mes fichiers."
    i = 0
    while i < 500:
        print(nb)
        i = i + 1

exo01()




def exo02():
    o = 0
    nb = 1
    while o < 1000:
        print(nb * o)
        o = o + 2

exo02()




def exo03():

    compteur = 1
    while compteur <= 10:
        print(compteur, '* 13 =', compteur * 13)
        compteur += 1

exo03()




def exo04():

    valeur = input("Ecrire un mot :")
    print(len(valeur))

exo04()




def exo05():

    valeur = int(input("Ecrire un chiffre :"))
    if (valeur % 2  == 0):
        print("pair")
    else:
        print("impair")


exo05()




def exo06():
    nombre = int(input("Ecrire un nombre entre 10 et 20 :"))
    if (nombre > 20):
        print ("Plus petit!")
    elif (nombre < 10):
        print ("Plus grand!")

exo06()




def exo07():
    nombre = int(input("Ecrire un nombre :"))
    print(nombre + 1)
    print(nombre + 2)
    print(nombre + 3)
    print(nombre + 4)
    print(nombre + 5)
    print(nombre + 6)
    print(nombre + 7)
    print(nombre + 8)
    print(nombre + 9)
    print(nombre + 10)

exo07()




def exo08():
    nombre = int(input("Ecrire un nombre :"))
    print(nombre * 1)
    print(nombre * 2)
    print(nombre * 3)
    print(nombre * 4)
    print(nombre * 5)
    print(nombre * 6)
    print(nombre * 7)
    print(nombre * 8)
    print(nombre * 9)
    print(nombre * 10)

exo08()




def exo09():
    age = int(input("Quel est l'âge de votre enfant?"))








def exo10():
    age = int(input("Quel est l'âge de votre enfant?:"))
    if(age == 6 or age == 7):
        print("Poussin")
    elif(age == 8 or age == 9):
        print("Pupille")
    elif (age == 10 or age == 11):
        print("Minime")
    elif (age > 12):
        print("Cadet")
exo10()




def exo11():
    nbr_article = int(input("Combien d'articles avez-vous?:"))
    prix_article = float(input("Quel est le prix HT unitaire de vos articles?:"))
    prixht = prix_article * nbr_article
    print ("nombres d'articles : ",nbr_article)
    print ("prix HT : ", prixht)
    TVA = (prixht * 1.2)
    print ("prix TTC:", TVA)

exo11()


