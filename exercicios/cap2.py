#Exercício 2.2

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

print(custo_total_atacado(60))