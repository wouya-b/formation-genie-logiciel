note=[12, 8, 15, 9, 17, 11, 14, 6, 18, 10]
print(max(note))
print(min(note))
moyenne= sum(note)/len(note)
print(moyenne)
note.sort()
print(note)
compteur=0
for i in note :
    if i >= 10:
        compteur +=1
print(compteur)      