arr=[2,5,1,8,0,4,9,6,7,3]

def Menor(m):
    menor = m[0]
    index = 0
    for i in range(1,len(m)):
        if m[i]<menor:
            menor=m[i]
            index=i
    return index

def Sort(a):
    copia = a
    novo=[]
    for i in range(len(copia)):
        novo.append(copia.pop(Menor(copia)))
    return novo

print(Sort(arr))