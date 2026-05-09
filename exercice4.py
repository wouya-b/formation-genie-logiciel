def annee_de_naissance(age):
    return 2026-age
def mageur(age):
    return age>= 18
def afficher_profil(prenom, age):
    annee =annee_de_naissance(age)
    est_grand = mageur(age)
    print(f'Bonjour {prenom} !. Tu as {age}. Tu es ne en {annee}')
    if est_grand:
        print("Tu es mageur")
    else: 
        print("Tu es mineur") 
prenom = input("Entrez-votre prenom : ") 
age = int(input("Entrez-votre age : "))
afficher_profil(prenom, age)  