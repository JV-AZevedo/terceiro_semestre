def calculo(horas, turno, categoria):
    salariomin = 1621
    if categoria == "G":
        if turno == "N":
            valorhr = salariomin*0.10
        else:
            valorhr = salariomin*0.15
    elif categoria == "O":
        if turno == "N":
            valorhr = salariomin*0.09
        else:
            valorhr = salariomin*0.14
    salario = valorhr*horas
    return salario
class RespostaInvalida(Exception):
    pass
nomes = []
horas = []
turno = []
categoria = []
r1 = r2 = r3 = r4 = r5 = False
while True:

    try:
        if r1 == False:
            n = input("Nome: ").title()
            if n == "":
                raise RespostaInvalida
            else:
                nomes.append(n)
                r1 = True
        if r2 == False:
            h = float(input("Horas trabalhadas no mês: "))
            horas.append(h)
            r2 = True
        if r3 == False:
            t = input("Turno de trabalho(M/V/N): ").upper()
            if t not in "MVN" or t == "":
                raise RespostaInvalida
            else:
                turno.append(t)
                r3 = True
        if r4 == False:
            c = input("Categoria(O/G): ").upper()
            if c not in "OG" or c == "":
                raise RespostaInvalida
            else:
                categoria.append(c)
                r4 = True
        if r5 == False:
            loop = input("Deseja continuar?(S/N): ").upper()
            if loop == "N":
                break
            elif loop == "S":
                r1 = r2 = r3 = r4 = r5 = False
            else:
                raise RespostaInvalida
    except (ValueError, RespostaInvalida):
        print("Resposta Inválida!")
for i in range(len(nomes)):
    print(f"{nomes[i]}, Salário: {calculo(horas[i],turno[i],categoria[i]):.2f}")

        