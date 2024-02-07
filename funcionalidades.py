# FUNCIONALIDADES

import math
import numpy
import cmath

# VARIÁVEIS GLOBAIS
''''
corrente_base_primaria = None
tensao_base_primaria = 13800
tensao_base_secundaria = 380
potencia = 100000000'''

# FUNÇÃO DE MENU
def exibir_menu():
    print('-'*60)
    print("Escolha uma opção:")
    print('-'*60)
    print("1. Calcular corrente base")
    print("2. Cadastrar impedâncias")
    print("3. Calcular Curto-Circuito-Trifásico-Simétrico")
    print("4. Calcular Curto-Circuito-Monofásico")
    print("5. Calcular Potência de Curto-Circuito")
    print("6. Modelando transformador")
    print("7. Calcular curto trifásico nos terminais do trafo")
    print("8. Calcular curto monofásico nos terminais do trafo")
    print("9. Calcular impedância do alimentador")
    print("10. Calcular impedância do barramento")
    print("11. Curto simétrico e monofásico no barramento")
    print("0. Sair")
    print('-'*60)

# FUNÇÃO PARA DETERMINAÇÃO DE IMPEDÂNCIAS
def obter_impedancia():
    parte_real = float(input('Digite a parte real da impedância: '))
    parte_imaginaria = float(input('Digite a parte imaginária da impedância: '))
    return complex(parte_real, parte_imaginaria)

# CORRENTE BASE
def valores_base():
    #global potencia, tensao_base_primaria, corrente_base_primaria
    potencia = int(input('Defina a potência base: '))
    tensao_base_primaria = int(input('Defina a tensão base primaria: '))
    tensao_base_secundaria = int(input('Defina a tensão base secundaria: '))

    try:
        corrente_base_primaria = potencia / (tensao_base_primaria * math.sqrt(3))
        corrente_base_secundaria = potencia / (tensao_base_secundaria * math.sqrt(3))
        
    except ZeroDivisionError:
        print("Erro: A tensão base não pode ser zero.")
        return None
    
    return (round(corrente_base_primaria, 2)),(round(corrente_base_secundaria, 2)),tensao_base_primaria, tensao_base_secundaria, potencia

# CORRENTE DE CURTO TRIFÁSICA SIMÉTRICA 
def corrente_curto_trifasica_simetrica(impedancia_reduzida_sistema, corrente_base):

    if corrente_base is None:
        return None  # Lidar com a situação de erro na corrente base
    
    curto_trifasico_simetrico = (1/(impedancia_reduzida_sistema)) * corrente_base
    magnitude, angulo_radiano = cmath.polar(curto_trifasico_simetrico)
    angulo_graus = math.degrees(angulo_radiano)
    return magnitude, angulo_graus

# CORRENTE DE CURTO-CIRCUITO FASE/TERRA
def corrente_curto_monofasica(impedancia_reduzida,impedancia_zero, impedancia_condutores,impedancia_trafo,corrente_base):
    
    curto_fase_terra = (3 * corrente_base)/((2 *(impedancia_reduzida))+ impedancia_zero + impedancia_condutores+impedancia_trafo)
    magnitude, angulo_radiano = cmath.polar(curto_fase_terra)
    angulo_graus = math.degrees(angulo_radiano)
    return magnitude, angulo_graus

# POTÊNCIA DE CURTO-CIRCUITO

def potencia_de_curto_circuito(tensao_base_primaria, corrente_base_primaria):
    
    potência_cc = math.sqrt(3) * tensao_base_primaria * corrente_base_primaria
    
    return round(potência_cc,2)

# MODELANDO TRANSFORMADOR
def tipo_transformador(tensao_base_primaria,tensao_base_secundaria, potencia):
    print('*' * 50)
    selecao = str(input('1) Dados obtidos por ensaio\n2) Dados obtidos por tabela\n'))

    if selecao == '1':
        corrente_ensaio_cc = float(input('Digite o valor da corrente de curto-circuito: '))
        impedancia_cc_primario = tensao_base_primaria / (math.sqrt(3) * corrente_ensaio_cc)
        tipo = str(input('O transformador é núcleo envolvente ou núcleo envolvido: '))
        ligacao = str(input('1) Y-Y aterrado, 2) Y aterrado-DELTA, 3) Y-DELTA, 4) DELTA-DELTA: '))

        if ligacao == '1':
            sequencia_positiva = sequencia_negativa = sequencia_zero = tensao_base_primaria / corrente_ensaio_cc
        elif ligacao == '2':
            sequencia_positiva_lado_y = sequencia_negativa = sequencia_zero = tensao_base_primaria / corrente_ensaio_cc
            sequencia_positiva_lado_delta = sequencia_negativa = sequencia_zero = math.inf
        elif ligacao in ['3', '4']:
            sequencia_zero = math.inf
        else:
            print('Opção inválida.')

    elif selecao == '2':
        print('*' * 50)
        pot_trafo = str(input('Digite a potência do transformador em kVA: '))
        #tensao_base_primaria = str(input('Digite a tensão nominal primária: '))
        impedancia_de_placa = str(input('Digite a impedância percentual de placa do transformador: '))

        perdas_no_cobre = {
            '15': 300, '30': 570, '45': 750, '75': 1200,
            '112.5': 1650, '150': 2050, '225': 2800, '300': {'220': 3900, '380': 3700},
            '500': {'220': 6400, '380': 6000}, '750': {'220': 10000, '380': 8500},
            '1000': {'220': 12500, '380': 11000}, '1500': {'220': 18000, '380': 16000}
        }

        if pot_trafo == '300' or pot_trafo == '500' or pot_trafo == '750' or pot_trafo == '1000' or pot_trafo == '1500':
            #tensao_base_secundaria = str(input('Digite a tensão nominal do trafo: 1) 220\n2) 380 ou 440'))
            perdas_no_cobre = perdas_no_cobre[pot_trafo][tensao_base_secundaria]

        resistencia_percentual = perdas_no_cobre / (10 * int(pot_trafo))
        resistencia_percentual_base = (resistencia_percentual / 100) * (
                    (potencia / (int(pot_trafo) * 1000)) * (float(tensao_base_primaria) / tensao_base_primaria))
        impedancia_percentual_base = (float(impedancia_de_placa) / 100) * (
                    (potencia / (int(pot_trafo) * 1000)) * (float(tensao_base_primaria) / tensao_base_primaria))
        reatancia_percentual_base = math.sqrt(
            (math.pow(impedancia_percentual_base, 2) - math.pow(resistencia_percentual_base, 2)))

        return complex(resistencia_percentual_base, reatancia_percentual_base)

def impedancia_alimentadores(comprimento_alimentador, cabos_por_fase, potencia, tensao_base_secundaria):
    #global potencia, tensao_base_secundaria

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

        resistencia_circuito_base_nova = (resistencia_do_circuito * 1000) * (potencia / (1000 * (tensao_base_secundaria ** 2)))
        reatancia_circuito_base_nova = (reatancia_do_circuito * 1000) * (potencia / (1000 * (tensao_base_secundaria ** 2)))
        impedancia_circuito = complex(resistencia_circuito_base_nova, reatancia_circuito_base_nova)

        return impedancia_circuito
    else:
        print('Opção de cabo inválida')

def impedancia_barramento(largura, espessura,comprimento_bar, barra_por_fase, potencia, tensao_base_secundaria):
    #global potencia, tensao_base_secundaria

    dados_barramento = {

        '12': {'2': {'resistencia_positiva': 0.9297, 'reatancia_positiva': 0.2859}},
        '15': {'2': {'resistencia_positiva': 0.7406, 'reatancia_positiva': 0.2774},'3':{'resistencia_positiva': 0.4909, 'reatancia_positiva': 0.2619}},
        '20': {'2': {'resistencia_positiva': 0.5531, 'reatancia_positiva': 0.2664},'3':{'resistencia_positiva': 0.3672, 'reatancia_positiva': 0.2509},'5':{'resistencia_positiva': 0.2205, 'reatancia_positiva': 0.2317}, '10':{'resistencia_positiva': 0.1098, 'reatancia_positiva': 0.2054}},
        '25': {'3': {'resistencia_positiva': 0.2932, 'reatancia_positiva': 0.2424},'5':{'resistencia_positiva': 0.1748, 'reatancia_positiva': 0.2229}},
        '30': {'3': {'resistencia_positiva': 0.2441, 'reatancia_positiva': 0.2355},'5':{'resistencia_positiva': 0.1561, 'reatancia_positiva': 0.2187},'10':{'resistencia_positiva': 0.0731, 'reatancia_positiva': 0.19}},
        '40': {'3': {'resistencia_positiva': 0.1836, 'reatancia_positiva': 0.2248},'5':{'resistencia_positiva': 0.1098, 'reatancia_positiva': 0.2054}, '10':{'resistencia_positiva': 0.0548, 'reatancia_positiva': 0.1792}},
        '50': {'5': {'resistencia_positiva': 0.0877, 'reatancia_positiva': 0.1969},'10':{'resistencia_positiva': 0.0438, 'reatancia_positiva': 0.1707}},
        '60': {'5': {'resistencia_positiva': 0.0731, 'reatancia_positiva': 0.19},'10':{'resistencia_positiva': 0.0365, 'reatancia_positiva': 0.1639}},
        '80': {'5': {'resistencia_positiva': 0.0548, 'reatancia_positiva': 0.1792},'10':{'resistencia_positiva': 0.0273, 'reatancia_positiva': 0.1530}},
        '100': {'5':{'resistencia_positiva': 0.0438, 'reatancia_positiva': 0.1707},'10':{'resistencia_positiva': 0.0221, 'reatancia_positiva': 0.1450}},
        '120': {'10':{'resistencia_positiva': 0.0182, 'reatancia_positiva': 0.1377}},
        '160': {'10':{'resistencia_positiva': 0.0137, 'reatancia_positiva': 0.1268}},
        '200': {'10':{'resistencia_positiva': 0.0109, 'reatancia_positiva': 0.1184}}

        # Adicionar mais dados conforme necessário
        
    }

    dados = dados_barramento.get(largura, {}).get(espessura, {})

    if dados:

        resistencia_do_barramento = (dados['resistencia_positiva'] * comprimento_bar) / (1000 * barra_por_fase)
        print(dados['resistencia_positiva'])
        reatancia_do_barramento = (dados['reatancia_positiva'] * comprimento_bar) / (1000 * barra_por_fase)
    
        resistencia_barramento_base_nova = (resistencia_do_barramento * 1000) * (potencia / (1000 * (tensao_base_secundaria ** 2)))
        reatancia_barramento_base_nova = (reatancia_do_barramento * 1000) * (potencia / (1000 * (tensao_base_secundaria ** 2)))
        impedancia_barramento = complex(resistencia_barramento_base_nova, reatancia_barramento_base_nova)

        return impedancia_barramento
    else:
        print('Combinação de largura, espessura e seção do barramento inválida')

def curto_assimétrico(resistencia_total, reatancia_total):

    a = reatancia_total/resistencia_total

    dados_cabos = {
        '0.4': {'fator_de_assimetria': 1.0},
        '0.6': {'fator_de_assimetria': 1.0},
        '0.8': {'fator_de_assimetria': 1.02},
        '1.0': {'fator_de_assimetria': 1.04},
        '1.2': {'fator_de_assimetria': 1.07},
        '1.4': {'fator_de_assimetria': 1.10},
        '1.6': {'fator_de_assimetria': 1.13},
        '1.8': {'fator_de_assimetria': 1.16},
        '2.0': {'fator_de_assimetria': 1.19},
        '2.2': {'fator_de_assimetria': 1.21},
        '2.4': {'fator_de_assimetria': 1.24},
        '2.6': {'fator_de_assimetria': 1.26},
        '2.8': {'fator_de_assimetria': 1.28},
        '3.0': {'fator_de_assimetria': 1.30},
        '3.2': {'fator_de_assimetria': 0.0958},
        '3.4': {'fator_de_assimetria': 0.0781},
        '3.6': {'fator_de_assimetria': 0.0608},
        '3.8': {'fator_de_assimetria': 0.0507},
        '4.0': {'fator_de_assimetria': 0.0292},
        '4.2': {'fator_de_assimetria': 14.8137},
        '4.4': {'fator_de_assimetria': 8.8882},
        '4.6': {'fator_de_assimetria': 5.5518},
        '4.8': {'fator_de_assimetria': 3.7045},
        '5.0': {'fator_de_assimetria': 2.221},
        '5.5': {'fator_de_assimetria': 1.3899},
        '6.0': {'fator_de_assimetria': 0.8891},
        '6.5': {'fator_de_assimetria': 0.6353},
        '7.0': {'fator_de_assimetria': 0.445},
        '7.5': {'fator_de_assimetria': 0.3184},
        '8.0': {'fator_de_assimetria': 0.2352},
        '8.5': {'fator_de_assimetria': 0.1868},
        '9.0': {'fator_de_assimetria': 0.1502},
        '9.5': {'fator_de_assimetria': 0.1226},
        '10.0': {'fator_de_assimetria': 0.0958},
        '11.0': {'fator_de_assimetria': 0.0781},
        '12.0': {'fator_de_assimetria': 0.0608},
        '13.0': {'fator_de_assimetria': 0.0507},
        '14.0': {'fator_de_assimetria': 0.0292},
        '15.0': {'fator_de_assimetria': 0.1226},
        '20.0': {'fator_de_assimetria': 0.0958},
        '30.0': {'fator_de_assimetria': 0.0781},
        '40.0': {'fator_de_assimetria': 0.0608},
        '50.0': {'fator_de_assimetria': 0.0507},
        '60.0': {'fator_de_assimetria': 0.0292},
        '70.0': {'fator_de_assimetria': 14.8137},
        '80.0': {'fator_de_assimetria': 8.8882},
        '100.0': {'fator_de_assimetria': 5.5518},
        '200.0': {'fator_de_assimetria': 3.7045},
        '400.0': {'fator_de_assimetria': 2.221},
        '600.0': {'fator_de_assimetria': 1.3899},
        '1000.0': {'fator_de_assimetria': 0.8891},

    }
