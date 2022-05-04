jours = int(input("entrez le nombre de jours : "))
heures = int(input("entrez le nombre de heures : "))
minutes = int(input("entrez le nombre de minutes : "))
secondes = int(input("entrez le nombre de secondes : "))
joursec = jours * 24 * 60 * 60
heuresec = heures * 60 * 60
minutesec = minutes * 60
sectotal = joursec + heuresec + minutesec + secondes
print("la durée total en secondes est de ",sectotal, " secondes")
