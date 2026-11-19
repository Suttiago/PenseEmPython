#Exercício 1.2

'''
Quantos segundos há em 42 minutos e 42 segundos
'''

minutos:int = 42
segundos:int = 42

def calcular_segundos(horas: int ,minutos:int, segundos:int) -> float:
    horas_em_minutos = horas *60

    minutos_totais = horas_em_minutos + minutos
    
    minuto_em_segundos:float = minutos_totais * 60
    
    tempo_convertido:int = minuto_em_segundos + segundos
    
    return tempo_convertido    


def calcular_horas(total_segundos: int) -> tuple[int, int, int]:
    horas = total_segundos // 3600
    minutos = (total_segundos % 3600) // 60
    segundos = total_segundos % 60

    return int(horas), int(minutos), int(segundos)

'''
Quantas milhas há em 10km?
'''

def calcular_milhas(quilometros:float) ->float:
    converter = quilometros / 1.61
    
    milhas = round(converter,2)
    return milhas
    
    
'''
Se você percorrer 10km em 42,42 minutos, qual o passo médio? quaala a velocidade média em milhas por hora?
'''

def calcular_passo_medio(quilometro:float, minutos:int, segundos:int) -> float:
    
    tempo:float = calcular_segundos(minutos, segundos)
    passo_medio:float = tempo / quilometro
    
    result = round(passo_medio,2)
    print(result)
    

def calcular_velocidade_media_em_milha(quilometro:float, minutos:int, segundos:int) ->float:
    
    milhas = calcular_milhas(quilometro)
    
    #tempo_segundos = calcular_segundos(0,minutos, segundos)
    
#    hora= calcular_horas(tempo_segundos)
    
#    velodicade_media = milhas / hora
    
    #result = round(velodicade_media,2)
    
    #return result

print(calcular_velocidade_media_em_milha(10.0,42,42))