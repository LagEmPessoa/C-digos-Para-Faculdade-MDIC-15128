def lucroDistribuidor(precoFabrica,percentualLucro):
    lucro = precoFabrica * (percentualLucro/100)
    return lucro
def valorImposto(precoFabrica,percentualImposto):
    imposto = precoFabrica * (percentualImposto/100)
    return imposto
def precoFinal(precoFabrica,percentualLucro,percentualImposto):
    p_final = precoFabrica + lucroDistribuidor(precoFabrica,percentualLucro) + valorImposto(precoFabrica,percentualImposto)
    return p_final

precoF1 = float(input("Qual o preço de fábrica desse modelo? "))
pLucro1 = float(input("Qual o percentual de lucro do distribuidor? "))
pImposto1 = float(input("Qual o percentual de imposto desse modelo? "))

print("O preço final do primeiro modelo é: ", precoFinal(precoF1,pLucro1,pImposto1))

precoF2 = float(input("Qual o preço de fábrica desse modelo? "))
pLucro2 = float(input("Qual o percentual de lucro do distribuidor? "))
pImposto2 = float(input("Qual o percentual de imposto desse modelo? "))

print("O preço final do segundo modelo é: ", precoFinal(precoF2,pLucro2,pImposto2))

precoF3 = float(input("Qual o preço de fábrica desse modelo? "))
pLucro3 = float(input("Qual o percentual de lucro do distribuidor? "))
pImposto3 = float(input("Qual o percentual de imposto desse modelo? "))

print("O preço final do terceiro modelo é: ", precoFinal(precoF3,pLucro3,pImposto3))
