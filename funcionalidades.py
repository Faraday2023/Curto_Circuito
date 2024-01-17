# FUNCIONALIDADES

import math
import numpy
import cmath

# VARIÁVEIS GLOBAIS

corrente_base = None
tensao = None
potencia = None

# Função de menu
def exibir_menu():
    print('-'*40)
    print("Escolha uma opção:")
    print('-'*40)
    print("1. Calcular corrente base")
    print("2. Cadastrar impedâncias")
    print("3. Calcular Curto-Circuito-Trifásico-Simétrico")
    print("4. Calcular Curto-Circuito-Monofásico")
    print("5. Calcular Potência de Curto-Circuito")
    print("0. Sair")
    print('-'*40)

# FUNÇÃO PARA DETERMINAÇÃO DE IMPEDÂNCIAS
def obter_impedancia():
    parte_real = float(input('Digite a parte real da impedância: '))
    parte_imaginaria = float(input('Digite a parte imaginária da impedância: '))
    return complex(parte_real, parte_imaginaria)

# CORRENTE BASE
def valores_base():
    global potencia, tensao, corrente_base
    potencia = int(input('Defina a potência base: '))
    tensao = int(input('Defina a tensão base: '))

    try:
        corrente_base = potencia / (tensao * math.sqrt(3))
    except ZeroDivisionError:
        print("Erro: A tensão base não pode ser zero.")
        return None
    
    return round(corrente_base, 2)

# CORRENTE DE CURTO TRIFÁSICA SIMÉTRICA 
def corrente_curto_trifasica_simetrica(impedancia_reduzida_sistema):

    if corrente_base is None:
        return None  # Lidar com a situação de erro na corrente base
    
    curto_trifasico_simetrico = (1/(impedancia_reduzida_sistema)) * corrente_base
    magnitude, angulo_radiano = cmath.polar(curto_trifasico_simetrico)
    angulo_graus = math.degrees(angulo_radiano)
    return magnitude, angulo_graus

# CORRENTE DE CURTO-CIRCUITO FASE/TERRA
def corrente_curto_monofasica(impedancia_reduzida,impedancia_condutores,impedancia_trafo):
    
    curto_fase_terra = (3 * corrente_base)/((2 *impedancia_reduzida)+impedancia_condutores+impedancia_trafo)
    magnitude, angulo_radiano = cmath.polar(curto_fase_terra)
    angulo_graus = math.degrees(angulo_radiano)
    return magnitude, angulo_graus

# POTÊNCIA DE CURTO-CIRCUITO

def potencia_de_curto_circuito():
    global tensao, corrente_base

    potência_cc = math.sqrt(3) * tensao * corrente_base
    
    return round(potência_cc,2)
