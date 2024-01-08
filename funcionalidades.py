# FUNCIONALIDADES

import math
import numpy
import cmath

def obter_impedância():
    parte_real = float(input('Digite a parte real da impedância: '))
    parte_imaginaria = float(input('Digite a parte imaginária da impedância: '))
    return complex(parte_real, parte_imaginaria)

# CORRENTE BASE
def valores_base():
    global corrente_base
    potência = int(input('Defina a potência base: '))
    tensão = int(input('Defina a tensão base: '))

    try:
        corrente_base = potência / (tensão * math.sqrt(3))
    except ZeroDivisionError:
        print("Erro: A tensão base não pode ser zero.")
        return None
    
    return round(corrente_base, 2)

# CORRENTE DE CURTO TRIFÁSICA SIMÉTRICA 
def corrente_curto_trifásica_simétrica(impedância_reduzida_sistema):

    if corrente_base is None:
        return None  # Lidar com a situação de erro na corrente base
    
    curto_trifásico_simétrico = (1/(impedância_reduzida_sistema)) * corrente_base
    magnitude, angulo_radiano = cmath.polar(curto_trifásico_simétrico)
    angulo_graus = math.degrees(angulo_radiano)
    return magnitude, angulo_graus

# CORRENTE DE CURTO-CIRCUITO FASE/TERRA
def corrente_curto_monofásica(impedância_reduzida,impedância_condutores,impedância_trafo):
    
    curto_fase_terra = (3 * corrente_base)/(2 *impedância_reduzida+impedância_condutores+impedância_trafo)
    return curto_fase_terra
