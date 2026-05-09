nombre = int(input("Veuillez entrez le nombre que vous voulez la table de multiplication : " ))
for i in range(1,11):
    resultat = nombre * i
    print(f'{nombre} * {i} = {resultat}')