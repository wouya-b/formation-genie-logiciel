def calculer_moyenne(notes):
    return sum(notes)/len(notes)
def est_admis(note):
    if note >= 10:
        return True
    else:
        return False
def afficher_resultats(noms,notes):
    for i in range (len(notes)):
        nom_etudiant = noms[i]
        notes_etudiant = notes[i]
        if est_admis(notes_etudiant):
            statut = "Admis"
        else :
            statut = "Refus"
        print(f'{nom_etudiant} : {notes_etudiant} : {statut}')
noms = ["Mouctar","Ibrahima","Moussa", "Kadiatou", "Bereko"]
notes = [12,8,15,17,9] 
afficher_resultats(noms,notes) 
print(f'Moyenne : {calculer_moyenne(notes)}')  

