def contagem(opcao,lista):
    r = 0
    l= []
    for i in range(len(lista)):
        if lista[i] == opcao:
            r+=1
            l.append(i)
    return r, l
def maisU(a,b,c,posa,posb,posc,x,y,z):
    r = 0
    elevador = []
    posf = []
    lista = [a,b,c]
    for i in range(len(lista)):
        if r < int(lista[i]):
            r = int(lista[i])
        elif r == int(lista[i]):
            pass
    if r == lista[0]:
        elevador.append(x)
        posf = posa
    elif r == lista[1]:
        elevador.append(y)
        posf = posb
    else:
        elevador.append(z)
        posf = posc
    return elevador, r, posf
def periodoMaisUsado(posf, lista):
    listaf = []
    for i in range(len(lista)):
        if i in posf:
            listaf.append(lista[i])
    return listaf
def menosU(a,b,c,posa,posb,posc,x,y,z):
    elevador = []
    posf = []
    lista = [a,b,c]
    r = lista[0]
    for i in range(len(lista)):
        if r > int(lista[i]):
            r = int(lista[i])
        elif r == int(lista[i]):
            pass
    if r == lista[0]:
        elevador.append(x)
        posf = posa
    elif r == lista[1]:
        elevador.append(y)
        posf = posb
    else:
        elevador.append(z)
        posf = posc
    return elevador, r, posf
def porcentagem(valor, total):
    m = (valor/len(total))*100
    return m

class RespostaInvalida(Exception):
    pass
liel = []
lipe = []
r1 = r2 = r3 = False
while True:
    if r1 == True and r2 == True and r3 == True:
        r1 = r2 = r3 = False
    try:
        if r1 == False:
            el = input("Qual o elevador você utiliza com mais frequência?(A/B/C): ").upper()
            if el != "A" and el != "B" and el != "C":
                raise RespostaInvalida
            else:
                liel.append(el)
                r1 = True
        if r2 == False:
            pe = input("Em qual período você mais usa o elevador?(M/V/N):").upper()
            if pe != "M" and pe != "V" and pe != "N":
                raise RespostaInvalida
            else:
                lipe.append(pe)
                r2 = True
        if r3 == False:
            loop = input("Deseja Continuar?(S/N): ").upper()
            if loop == "N":
                break
            elif loop == "S":
                r3 = True
            else:
                raise RespostaInvalida
    except ValueError:
        print("Resposta inválida")
    except RespostaInvalida:
        print("Resposta inválida")
A,posA = contagem("A", liel)
B,posB = contagem("B", liel)
C,posC = contagem("C", liel)
maisusado, quantidadeE, posF  = maisU(A,B,C,posA,posB,posC,"A","B","C")
pemu = periodoMaisUsado(posF, lipe)
M,posM = contagem("M", pemu)
V,posV = contagem("V", pemu)
N,posN = contagem("N", pemu)
pemuF, quantidadeP, irrelevante = maisU(M,V,N,posM,posV,posN,"M","V","N")
print("Elevador mais usado:", maisusado,"quantidade:",quantidadeE,"/ Período que mais usam esse elevador:",pemuF,"quantidade:",quantidadeP)
M,posM = contagem("M", lipe)
V,posV = contagem("V", lipe)
N,posN = contagem("N", lipe)
pemuAll, quantidadePALL, irrelevante2 = maisU(M,V,N,posM,posV,posN,"M","V","N")
print("Perído em que os elevadores são mais usados:",pemuAll,"quantidade:", quantidadePALL)
pormaisu = porcentagem(quantidadePALL,lipe)
print("Hórario mais usado:",pemuAll,f". {pormaisu:.2f}%")
pemuAll, quantidadePALL, irrelevante2 = menosU(M,V,N,posM,posV,posN,"M","V","N")
pormenosu = porcentagem(quantidadePALL,lipe)
print("Horário menos usado:",pemuAll,f". {pormenosu:.2f}%")




