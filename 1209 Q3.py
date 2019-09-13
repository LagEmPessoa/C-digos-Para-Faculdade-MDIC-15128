def consumoMedio(distancia, combustivel):
    a = distancia/combustivel 
    return a

dcarro1 = float(input("Informe o valor da distância que percorre o CARRO 01 em km: "))
ccarro1 = float(input("Informe o qauanto de gasolina o CARRO 01 consome em litros: "))
print("O cosumo médio do CARRO 01 é: ", consumoMedio(dcarro1, ccarro1),"km/l")

dcarro2 = float(input("Informe o valor da distância que percorre o CARRO 02 em km: "))
ccarro2 = float(input("Informe o qauanto de gasolina o CARRO 02 consome em litros: "))
print("O cosumo médio do CARRO 02 é: ", consumoMedio(dcarro2, ccarro2),"km/l")

dcarro3 = float(input("Informe o valor da distância que percorre o CARRO 03 em km: "))
ccarro3 = float(input("Informe o qauanto de gasolina o CARRO 03 consome em litros: "))
print("O cosumo médio do CARRO 03 é: ", consumoMedio(dcarro3, ccarro3),"km/l")
