def pagamento(dias, precoDiaria):
    liq = (dias * precoDiaria)*0.92
    return liq

qnt_dias1 = int(input("Informe a quantidade de dias de trabalho para o Eletricista: "))
prc_dia1 = float(input("Imprima o preço da diária do Eletricista: "))

print("Pagamento do Eletricista: ", pagamento(qnt_dias1, prc_dia1))

qnt_dias2 = int(input("Informe a quantidade de dias de trabalho para o Pintor: "))
prc_dia2 = float(input("Imprima o preço da diária do Pintor: "))

print("Pagamento do Pintor: ",pagamento(qnt_dias2, prc_dia2))

qnt_dias3 = int(input("Informe a quantidade de dias de trablho para o Encanador: "))
prc_dia3 = float(input("Imprima o preço da diária do Encanador: "))

print("Pagamento do Encanador: ",pagamento(qnt_dias3, prc_dia3))

somaSal = pagamento(qnt_dias1, prc_dia1) + pagamento(qnt_dias2, prc_dia2) + pagamento(qnt_dias3, prc_dia3)
print("Você vai embolçar: ", somaSal, "R$")
