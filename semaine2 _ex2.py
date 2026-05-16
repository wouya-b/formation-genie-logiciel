prenoms=["Mamadou", "Ibrahima", "Kadiatou", "Moussa", "Adama"]
print(prenoms[0])
print(prenoms[4])
prenoms.append("Sory")
print(prenoms)
del prenoms[1]
print(prenoms)
for i in range(len(prenoms)):
    print(f'{i}; {prenoms[i]}')