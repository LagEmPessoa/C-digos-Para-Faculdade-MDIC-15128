def horasParaSegundos(horas):
    h_s = horas*3600
    return h_s
def minutosParaSegundos(minutos):
    m_s = minutos * 60
    return m_s

h_viagem = int(input("A viagem foi de quantas horas? "))
m_viagem = int(input("A viagem foi de quantos minutos? "))
s_viagem = int(input("A viagem foi de quantos segundos? "))

t_total = horasParaSegundos(h_viagem) + minutosParaSegundos(m_viagem) + s_viagem
print("O tempo total gasto,em segundos, foi de: ",t_total)
