somme = int(input("entrez le montant déposé dans le compte : "))
interet = 4
montantint1 = (somme * interet )/100
montant1 = somme + montantint1
print("le montant dans le compte épargne après un an est : %.2f"%montant1)
montantint2 = (montant1 * interet )/100
montant2 = montant1 + montantint2
print("le montant dans le compte épargne après deux ans est : %.2f"%montant2)
montantint3 = (montant2 * interet)/100
montant3 = montant2 + montantint3
print("le montant dans le compte épargne après trois ans est : %.2f"%montant3)
