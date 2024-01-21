# FUNCIONALIDADES

import math
import numpy
import cmath

# VARIÁVEIS GLOBAIS

corrente_base = None
tensao = 13800
tensao_secundaria = 380
potencia = 100000000

# FUNÇÃO DE MENU
def exibir_menu():
    print('-'*40)
    print("Escolha uma opção:")
    print('-'*40)
    print("1. Calcular corrente base")
    print("2. Cadastrar impedâncias")
    print("3. Calcular Curto-Circuito-Trifásico-Simétrico")
    print("4. Calcular Curto-Circuito-Monofásico")
    print("5. Calcular Potência de Curto-Circuito")
    print("6. Modelando transformador")
    print("7. Calcular curto trifásico nos terminais do trafo")
    print("8. Calcular curto monofásico nos terminais do trafo")
    print("9. Calcular impedancia do alimentador")
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
def corrente_curto_monofasica(impedancia_reduzida,impedancia_zero, impedancia_condutores,impedancia_trafo,corrente_base):
    
    curto_fase_terra = (3 * corrente_base)/((2 *(impedancia_reduzida+impedancia_trafo))+ impedancia_zero + impedancia_condutores+impedancia_trafo)
    magnitude, angulo_radiano = cmath.polar(curto_fase_terra)
    angulo_graus = math.degrees(angulo_radiano)
    return magnitude, angulo_graus

# POTÊNCIA DE CURTO-CIRCUITO

def potencia_de_curto_circuito():
    global tensao, corrente_base

    potência_cc = math.sqrt(3) * tensao * corrente_base
    
    return round(potência_cc,2)

# MODELANDO TRANSFORMADOR
def tipo_transformador():

    global tensao, potencia
    print('*'*50)
    seleçao = str(input('1) Dados obtidos por ensaio\n2) Dados obtidos por tabela\n'))
    if seleçao == '1':
        corrente_ensaio_cc = float(input(('Digite o valor da corrente de curto-circuito: ')))
        #Impedância de sequência positiva/negativa
        impedancia_cc_primario = tensao/(math.sqrt(3)*corrente_ensaio_cc)
        #Tipos de ligação das bobinas do transformador
        tipo = str(input('O transformador é núcleo envolvente ou núcleo envolvido: '))
        ligação = str(input('1) Y-Y aterrado,2) Y aterrado-DELTA, 3) Y-DELTA, 4) DELTA-DELTA): '))

        if ligação == '1':
            sequência_positiva = sequência_negativa = sequência_zero = tensao/corrente_ensaio_cc
        elif ligação == '2':
            sequência_positiva_lado_y = sequência_negativa = sequência_zero = tensao/corrente_ensaio_cc
            sequência_positiva_lado_delta = sequência_negativa = sequência_zero = math.inf
        elif ligação == '3':
            sequência_zero = math.inf
        elif ligação == '4':
            sequência_zero = math.inf
        else:
            print('Opção inválida.')

    elif seleçao == '2':
        print('*'*50)
        pot_trafo = str(input('Digite a potência do transformador em kVA: '))
        tensao_primaria = str(input('Digite a tensão nominal primária: '))
        impedancia_de_placa = str(input('Digite a impedância percentual de placa do transformador: '))
        
        if pot_trafo == '15':
            perdas_no_cobre = 300
        elif pot_trafo == '30':
            perdas_no_cobre = 570
        elif pot_trafo == '45':
            perdas_no_cobre = 750
        elif pot_trafo == '75':
            perdas_no_cobre = 1200
        elif pot_trafo == '112.5':
            perdas_no_cobre = 1650
        elif pot_trafo == '150':
            perdas_no_cobre = 2050
        elif pot_trafo == '225':
            perdas_no_cobre = 2800
        elif pot_trafo == '300':
            tensao_op = str(input('Digite a tensão nominal do trafo: 1) 220\n2) 380 ou 440'))
            if tensao_op == '1':
                perdas_no_cobre = 3900
            elif tensao_op == '2':
                perdas_no_cobre = 3700
            else:
                print('Opção inválida')
        elif pot_trafo == '500':
            tensao_op = str(input('Digite a tensão nominal do trafo: 1) 220\n2) 380 ou 440'))
            if tensao_op == '1':
                perdas_no_cobre = 6400
            elif tensao_op == '2':
                perdas_no_cobre = 6000
            else:
                print('Opção inválida')
        elif pot_trafo == '750':
            tensao_op = str(input('Digite a tensão nominal do trafo: 1) 220\n2) 380 ou 440'))
            if tensao_op == '1':
                perdas_no_cobre = 10000
            elif tensao_op == '2':
                perdas_no_cobre = 8500
            else:
                print('Opção inválida')
        elif pot_trafo == '1000':
            print('*'*50)
            tensao_op = str(input('Digite a tensão nominal do trafo:\n1) 220\n2) 380 ou 440\n'))
            if tensao_op == '1':
                perdas_no_cobre = 12500
            elif tensao_op == '2':
                perdas_no_cobre = 11000
            else:
                print('Opção inválida')
        elif pot_trafo == '1500':
            print('*'*50)
            tensao_op = str(input('Digite a tensão nominal do trafo: 1) 220\n2) 380 ou 440'))
            if tensao_op == '1':
                perdas_no_cobre = 18000
            elif tensao_op == '2':
                perdas_no_cobre = 16000
            else:
                print('Opção inválida')
        else:
            print('Opção inválida')

        resistencia_percentual = perdas_no_cobre/(10*int(pot_trafo))
        resistencia_percentual_base = (resistencia_percentual/100)*((potencia/(int(pot_trafo)*1000))*(float(tensao_primaria)/tensao))
        impedancia_percentual_base = (float(impedancia_de_placa)/100)*((potencia/(int(pot_trafo)*1000))*(float(tensao_primaria)/tensao))
        reatancia_percentual_base = math.sqrt((math.pow(impedancia_percentual_base,2)-math.pow(resistencia_percentual_base,2)))

        return complex(resistencia_percentual_base, reatancia_percentual_base)
    
def impedancia_alimentadores(comprimento_alimentador, cabos_por_fase):
    global potencia, tensao_secundaria

    dados_cabos = {
        '1.5': {'resistencia_positiva': 14.8137, 'reatancia_positiva': 0.1378},
        '2.5': {'resistencia_positiva': 8.8882, 'reatancia_positiva': 0.1345},
        '4': {'resistencia_positiva': 5.5518, 'reatancia_positiva': 0.1279},
        '6': {'resistencia_positiva': 3.7045, 'reatancia_positiva': 0.1225},
        '10': {'resistencia_positiva': 2.221, 'reatancia_positiva': 0.1207},
        '16': {'resistencia_positiva': 1.3899, 'reatancia_positiva': 0.1173},
        '25': {'resistencia_positiva': 0.8891, 'reatancia_positiva': 0.1164},
        '35': {'resistencia_positiva': 0.6353, 'reatancia_positiva': 0.1128},
        '50': {'resistencia_positiva': 0.445, 'reatancia_positiva': 0.1127},
        '70': {'resistencia_positiva': 0.3184, 'reatancia_positiva': 0.1096},
        '95': {'resistencia_positiva': 0.2352, 'reatancia_positiva': 0.1090},
        '120': {'resistencia_positiva': 0.1868, 'reatancia_positiva': 0.1076},
        '150': {'resistencia_positiva': 0.1502, 'reatancia_positiva': 0.1076},
        '185': {'resistencia_positiva': 0.1226, 'reatancia_positiva': 0.1073},
        '240': {'resistencia_positiva': 0.0958, 'reatancia_positiva': 0.1070},
        '300': {'resistencia_positiva': 0.0781, 'reatancia_positiva': 0.1068},
        '400': {'resistencia_positiva': 0.0608, 'reatancia_positiva': 0.1058},
        '500': {'resistencia_positiva': 0.0507, 'reatancia_positiva': 0.1051},
        '630': {'resistencia_positiva': 0.0292, 'reatancia_positiva': 0.1042}
    }

    secao_cabo = input('Digite a seção nominal do cabo: ')
    
    if secao_cabo in dados_cabos:
        dados = dados_cabos[secao_cabo]
        resistencia_do_circuito = (dados['resistencia_positiva'] * comprimento_alimentador) / (1000 * cabos_por_fase)
        reatancia_do_circuito = (dados['reatancia_positiva'] * comprimento_alimentador) / (1000 * cabos_por_fase)

        resistencia_circuito_base_nova = (resistencia_do_circuito * 1000) * (potencia / (1000 * (tensao_secundaria ** 2)))
        reatancia_circuito_base_nova = (reatancia_do_circuito * 1000) * (potencia / (1000 * (tensao_secundaria ** 2)))
        impedancia_circuito = complex(resistencia_circuito_base_nova, reatancia_circuito_base_nova)

        return resistencia_circuito_base_nova, reatancia_circuito_base_nova, impedancia_circuito
    else:
        print('Opção de cabo inválida')
