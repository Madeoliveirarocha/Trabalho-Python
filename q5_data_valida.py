# Questão 5 - Validação de data (considerando anos bissextos)
dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))

def bissexto(y):
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

dias_mes = {
    1: 31, 2: 29 if bissexto(ano) else 28, 3: 31, 4: 30,
    5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}

if mes in dias_mes and 1 <= dia <= dias_mes[mes]:
    print("Data válida.")
else:
    print("Data inválida.")
