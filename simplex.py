import numpy as np

indexMenorValor: int = None
valorMin: float = None
menorValorDiv: float = None
indexMenorValorDiv: int = None

r_ForaBase = [  [3, 6], #outBase
                [4, 2]]

b_NaBase = [    [1, 0], #inBase
                [0, 1]]

cr_ForaBase = [-20, -24] #of_out

cb_NaBase = [0, 0] #of_in

b_coef = [  [60], # b
            [32]]

def numBellowZero(num: list) -> bool:
    for i in num:
        if i < 0:
            return True

if numBellowZero(cr_ForaBase):
    valorMin  = min(cr_ForaBase)
    indexMenorValor = cr_ForaBase.index(min(cr_ForaBase))

#   Selecionar variável que sai da base
valorGrande = 100000000000000000000000000000
for linha in range(len(r_ForaBase)):
    auxValorDiv = b_coef[linha][0] / r_ForaBase[linha][indexMenorValor]
    auxGetLinha = linha
    if auxValorDiv < valorGrande:
        menorValorDiv = auxValorDiv
        indexMenorValorDiv = auxGetLinha
        valorGrande = auxValorDiv

for linha in range(len(r_ForaBase)):
    getValorNaBase = b_NaBase[linha][indexMenorValorDiv]
    getValorForaBase = r_ForaBase[linha][indexMenorValor]
    b_NaBase[linha][indexMenorValorDiv] = getValorForaBase
    r_ForaBase[linha][indexMenorValor] = getValorNaBase

get_cr_ForaBase = cr_ForaBase[indexMenorValor]
get_cb_NaBase = cb_NaBase[indexMenorValorDiv]
cr_ForaBase[indexMenorValor] = get_cb_NaBase
cb_NaBase[indexMenorValorDiv] = get_cr_ForaBase

r_ForaBaseArray = np.array(r_ForaBase)
b_NaBaseArray = np.array(b_NaBase)
b_NaBaseInv = np.linalg.inv(b_NaBaseArray)
cr_ForaBaseArray = np.array(cr_ForaBase)
cb_NaBaseArray = np.array(cb_NaBase)
b_coefArray = np.array(b_coef)

print("-"*30)
print(f"r_ForaBaseArray: \n{r_ForaBaseArray}\n")
print(f"b_NaBaseArray:\n{b_NaBaseArray}\n")
print(f"b_NaBaseInv:\n{b_NaBaseInv}\n")
print(f"cr_ForaBaseArray:\n{cr_ForaBaseArray}\n")
print(f"cb_NaBaseArray:\n{cb_NaBaseArray}\n\n")
print(F"b_coefArray: \n{b_coefArray}\n")
print("-"*30)

print("_"*30)
cr_ForaBaseArray = cr_ForaBaseArray - (np.dot(cb_NaBaseArray, np.dot(b_NaBaseInv, r_ForaBaseArray)))
print(f"cr_ForaBaseArray:\n{cr_ForaBaseArray}\n")

b_coefArray = np.dot(b_NaBaseInv, b_coefArray)
print(F"b_coefArray: \n{b_coefArray}\n")

r_ForaBaseArray = np.dot(b_NaBaseInv, r_ForaBaseArray)
print(f"r_ForaBaseArray: \n{r_ForaBaseArray}\n")

print(f"FO: {np.dot(cb_NaBaseArray, np.dot(b_NaBaseInv, b_coefArray))} ")
