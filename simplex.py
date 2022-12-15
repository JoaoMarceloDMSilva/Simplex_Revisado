import numpy as np

indexValueToEnter: int = None
minValue: float = None
auxMemoryDiv: float = None
auxMemoryIndex: float = None

aux1, aux2, aux3, aux4 = None, None, None, None

def numBellowZero(num: list) -> bool:
    for i in num:
        if i < 0:
            return True

# R --> fora da base
outBase = [ [3, 6], 
            [4, 2]]
#outBaseInv = np.linalg.inv(outBase) #   Mariz inversa

# B --> na base
inBase = [  [1, 0],
            [0, 1]]

# Cr --> FO fora da basae
of_out = [-20, -24]


#Cb --> FO na base
of_in = [0, 0]


# b --> coeficinete
b = [ [60],
      [32]]
bNP = np.array(b)

#Verifica se há valor NEGATIVO fora da base
if numBellowZero(of_out):
    minValue  = min(of_out)
    indexValueToEnter = of_out.index(min(of_out))

#Acha a coluna 
#for i in range(len(outBase)):
#     print( b[i][0] / outBase[i][indexValueToEnter])
aux = 100000000000000000000000000000
for i in range(len(outBase)):
    #print(b[i][0] / outBase[i][indexValueToEnter])
    aux_temp = b[i][0] / outBase[i][indexValueToEnter]
    aux_index = i

    if aux_temp < aux:
        auxMemoryDiv = aux_temp # Pega o menor número
        #print(auxMemoryDiv)
        auxMemoryIndex = aux_index #  Quem foi dividido
        aux = aux_temp

# alterar bases:
for i in range(len(outBase)):
    aux1 = inBase[i][auxMemoryIndex]
    aux2 = outBase[i][indexValueToEnter]
    #print(f"{aux1}\t{aux2}")
    outBase[i][indexValueToEnter] = aux1
    inBase[i][auxMemoryIndex] = aux2
    #print(f"{inBase[i][auxMemoryIndex]}\t{outBase[i][indexValueToEnter]}")

#troca na FOs
aux3 = of_out[indexValueToEnter]
aux4 = of_in[auxMemoryIndex]
of_out[indexValueToEnter] = aux4
of_in[auxMemoryIndex] = aux3

#print(f"\naux3: [{aux3}]\taux4: [{aux4}]")

#Converte em array após alterar

#print(f"{outBase}\n")
#print(f"{inBase}\n")
#
outBaseNP = np.array(outBase) # B
inBaseNP = np.array(inBase) # R
outBaseInvNP = np.linalg.inv(outBaseNP) # B^-1
of_inNP = np.array(of_in)
of_outNP = np.array(of_out)

print(f"outBaseNP: \n{outBaseNP}\n")
print(f"inBaseNP:\n{inBaseNP}\n")

print(f"of_inNP:\n{of_inNP}\n")
print(f"of_outNP:\n{of_outNP}\n")
#atualizar o Cr (of_outNP)
#of_outNP = of_outNP - of_inNP.dot(outBaseInvNP.dot(inBaseNP) )
#print(of_outNP)

bNP = outBaseInvNP.dot(bNP)
print(bNP)

#bNP = outBaseInvNP.dot(bNP)
