n = int(input("saisir un entier à quatre chiffres : "))
nb1 = n//1000
nb2 = (n//100)%10
nb3 = (n//10)%10
nb4 = n%10
somme = nb1 + nb2 + nb3 + nb4
print("la somme vaut : ",somme)
