def ordenamientoBurbuja(unaLista):
    for numPasada in range(len(unaLista)-1,0,-1):
        for i in range(numPasada):
            if unaLista[i]>unaLista[i+1]:
                temp = unaLista[i]
                unaLista[i] = unaLista[i+1]
                unaLista[i+1] = temp

unaLista = [54,26,93,17,77,31,44,55,20]
ordenamientoBurbuja(unaLista)
print(unaLista)


def ordenamientoBurbujaCorto(unaLista):
    intercambios = True
    numPasada = len(unaLista)-1
    while numPasada > 0 and intercambios:
       intercambios = False
       for i in range(numPasada):
           if unaLista[i]>unaLista[i+1]:
               intercambios = True
               temp = unaLista[i]
               unaLista[i] = unaLista[i+1]
               unaLista[i+1] = temp
       numPasada = numPasada-1

unaLista=[20,30,40,90,50,60,70,80,100,110]
ordenamientoBurbujaCorto(unaLista)
print(unaLista)