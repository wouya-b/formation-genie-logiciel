def est_pair(nombre):
    return nombre%2==0
print(f'{est_pair(2)}')
def compter_pairs(debut,fin):
    compteur = 0
    for i in range(debut, fin+1):
        if est_pair(i):
            compteur +=1
    return compteur
print(f'{compter_pairs(1,20)}')