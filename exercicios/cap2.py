#Exercício 2.2
from cap1 import calcular_horas, calcular_segundos

'''
qual o volume de uma esfera com raio 5?
'''
def calcular_volume_esfera(raio:float) -> float:
    pi:float = 3.14

    volume = (4/3) * pi * raio**3

    volume_final = round(volume,2)
    return volume_final


'''
custo toal de  venda no atacado para 60 cópias
'''

def custo_total_atacado(copias:int)->float:
    preco_livro:float = 24.95
    desconto: float = 40/100
    preco_desconto:float = preco_livro * desconto

    preco_livro_com_desconto = preco_livro - preco_desconto

    frete:float = 0
    for c in range(copias):
        if c == 0:
            frete += 3.00
        else:
            frete +=0.75

    preco_total_livros:float = round(preco_livro_com_desconto * copias,2)


    custo_total_atacado:float = preco_total_livros + frete

    return custo_total_atacado 


'''
Se eu sair da minha casa às 6:52 e correr 1 quilômetro a um certo passo (8min15s por quilômetro), então 3 quilômetros a um passo mais rápido (7min12s por quilômetro) 
e 1 quilômetro no mesmo passo usado em primeiro lugar, que horas chego em casa para o café da manhã?
'''

tempos_minutos_caminhadas:list[float] = [8.,7,8]
tempo_segundos_caminhados:list[float] = [15,12,15]
def calcular_chegada_casa(tempo_minutos_caminhado:list[float],tempo_segundos_caminhado:list[float])->float:
    hora_saida_casa:float = 6
    minuto_saida_casa:float = 52

    hora_inicial_segundos = calcular_segundos(hora_saida_casa,minuto_saida_casa,0)


    primeira_caminhada = calcular_segundos(0,tempo_minutos_caminhado[0],tempo_segundos_caminhado[0])
    segunda_caminhada = calcular_segundos(0,tempo_minutos_caminhado[1],tempo_segundos_caminhado[1])*3
    terceira_caminhada = calcular_segundos(0,tempo_minutos_caminhado[2],tempo_segundos_caminhado[2])

    soma_minutos = primeira_caminhada + segunda_caminhada + terceira_caminhada +hora_inicial_segundos
    horas, minutos, segundos = calcular_horas(soma_minutos)

    print(f"Hora da chegada: {horas:02d}:{minutos:02d}:{segundos:02d}")


calcular_chegada_casa(tempos_minutos_caminhadas,tempo_segundos_caminhados)
    