import numpy as np

indexMenorValor: int = None
valorMin = None
menorValorDiv: float = None
indexMenorValorDiv: int = None

cr_ForaBaseArrayCopy, b_coefArrayCopy = None, None

r_ForaBaseArray = None
b_NaBaseArray = None
b_NaBaseInv = None
cr_ForaBaseArray = None
cb_NaBaseArray = None
b_coefArray = None

# Deve-se adicionar as matrizes manualmente nos respectivos campos

r_ForaBase = [  [1, 2, 1], # R
                [2, 0, 0],
                [0, 1, 1]]

b_NaBase = [    [1, 0, 0], # B
                [0, 1, 0],
                [0, 0, 1]]

cr_ForaBase = [-2, 0, -4] # Cr

cb_NaBase = [0, 0, 0] #Cb

b_coef = [  [8000], # b
            [6000],
            [620]]

def numBellowZero(num: list) -> bool:
    for i in num:
        if i < 0:
            return True

def get_VariavelSaiBase(indexMenorValor):#   Selecionar variável que sai da base
    global r_ForaBase
    global b_coef
    global menorValorDiv
    global cr_ForaBase
    global cb_NaBase
    global indexMenorValorDiv

    valorGrande = 100000000000000000000000000000
    for linha in range(len(r_ForaBase)):
        if r_ForaBase[linha][indexMenorValor] > 0:
            auxValorDiv = b_coef[linha][0] / r_ForaBase[linha][indexMenorValor]
            auxGetLinha = linha
            if (auxValorDiv < valorGrande) and (auxValorDiv >= 0):
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

def transformaArray(): # Transforma em Array para efetuar os cálculos no numpy
    global r_ForaBaseArray
    global b_NaBaseArray
    global b_NaBaseInv 
    global cr_ForaBaseArray 
    global cb_NaBaseArray 
    global b_coefArray

    r_ForaBaseArray = np.array(r_ForaBase)
    b_NaBaseArray = np.array(b_NaBase)
    b_NaBaseInv = np.linalg.inv(b_NaBaseArray)
    cr_ForaBaseArray = np.array(cr_ForaBase)
    cb_NaBaseArray = np.array(cb_NaBase)
    b_coefArray = np.array(b_coef)

def imprimeValores():
    global r_ForaBaseArray
    global b_NaBaseArray
    global b_NaBaseInv 
    global cr_ForaBaseArray 
    global cb_NaBaseArray 
    global b_coefArray

    print("-"*30)
    print(f"R: \n{r_ForaBaseArray}\n")
    print(f"B:\n{b_NaBaseArray}\n")
    print(f"B^-:\n{b_NaBaseInv}\n")
    print(f"Cr:\n{cr_ForaBaseArray}\n")
    print(f"Cb:\n{cb_NaBaseArray}\n\n")
    print(F"b: \n{b_coefArray}\n")
    print("-"*30)

def calculaAtualiza():
    global cr_ForaBaseArrayCopy 
    global b_coefArrayCopy
    global r_ForaBaseArray
    global b_NaBaseArray
    global b_NaBaseInv 
    global cr_ForaBaseArray 
    global cb_NaBaseArray 
    global b_coefArray
    global cr_ForaBaseVerif

    
    cr_ForaBaseArrayCopy = cr_ForaBaseArray - (np.dot(cb_NaBaseArray, np.dot(b_NaBaseInv, r_ForaBaseArray)))
    print(f"Cr:\n{cr_ForaBaseArrayCopy}\n")

    b_coefArrayCopy = np.dot(b_NaBaseInv, b_coefArray)
    print(F"b: \n{b_coefArrayCopy}\n")

    r_ForaBaseArray = np.dot(b_NaBaseInv, r_ForaBaseArray)
    print(f"R: \n{r_ForaBaseArray}\n")

    cr_ForaBaseVerif = cr_ForaBaseArrayCopy # Atualiza para verificar no while

def calcularFO():
    global cr_ForaBaseArray 
    global cb_NaBaseArray 
    global b_coefArray

    print(f"FO: {np.dot(cb_NaBaseArray, np.dot(b_NaBaseInv, b_coefArray))} ")


# Executa

cr_ForaBaseVerif = cr_ForaBase # Faz uma cópia inicialmente -->  "goto" linha 119
contador = 0
while numBellowZero(cr_ForaBaseVerif):
    print('¨'*25)
    print(f"\nExecução {contador + 1}")
    print('¨'*25)
    valorMin  = min(cr_ForaBase)
    indexMenorValor = cr_ForaBase.index(min(cr_ForaBase))

    get_VariavelSaiBase(indexMenorValor)
    transformaArray()
    imprimeValores()
    calculaAtualiza()
    calcularFO()

    contador += 1
