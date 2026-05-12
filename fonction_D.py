def maximum(a,b):
    if a>b:
        return a
    else:
        return b
print(maximum(12,22)) 
def maximum_trois(a,b,c):
    premier_max= maximum(a,b)
    return maximum(premier_max,c)
print(maximum_trois(12,25,2))  