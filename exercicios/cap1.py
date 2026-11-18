
#exercício 1.2

'''
Quantos segundos há em 42 minutos e 42 segundos
'''

minutos:int = 42
segundos:int = 42

def calcular_segundos(minutos:int, segundos:int) -> float:
    minuto_em_segundos = minutos * 60
    
    tempo_convertido:int = minuto_em_segundos + segundos
    
    return tempo_convertido    


def calcular_horas(minutos:float) -> float:
    minuto_em_horas = minutos /  3600
    
    return minuto_em_horas  

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
    
    tempo_segundos = calcular_segundos(minutos, segundos)
    
    hora= calcular_horas(tempo_segundos)
    
    velodicade_media = milhas / hora
    
    result = round(velodicade_media,2)
    
    return result

print(calcular_velocidade_media_em_milha(10.0,42,42))