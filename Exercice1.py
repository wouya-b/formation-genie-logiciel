prenom = input("entrez votre prenom :" )
age = int(input("entrez votre age :" ))
annee_de_naissance = 2026-age
if age >= 18 :
    print(f'Bonjour {prenom} ! tu as {age} ans. tu es ne(e) en {annee_de_naissance}. ')
    print(f'Tu es majeur(e)')
else :
    print(f'Bonjour {prenom}! tu as {age}ans. Tu es ne(e) en {annee_de_naissance}. ')
    print(f'Tu es mineur(e)')