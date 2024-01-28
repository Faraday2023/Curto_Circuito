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
    selecao = input('1) Dados obtidos por ensaio\n2) Dados obtidos por tabela\n')

    if selecao == '1':
        corrente_ensaio_cc = float(input('Digite o valor da corrente de curto-circuito: '))
        impedancia_cc_primario = tensao / (math.sqrt(3) * corrente_ensaio_cc)

        tipo = input('O transformador é núcleo envolvente ou núcleo envolvido: ')
        ligacao = input('1) Y-Y aterrado, 2) Y aterrado-DELTA, 3) Y-DELTA, 4) DELTA-DELTA): ')

        if ligacao in ['1', '2']:
            sequencia_positiva = sequencia_negativa = sequencia_zero = tensao / corrente_ensaio_cc
        elif ligacao in ['3', '4']:
            sequencia_zero = math.inf
        else:
            print('Opção inválida.')

    elif selecao == '2':
        print('*'*50)
        pot_trafo = input('Digite a potência do transformador em kVA: ')
        tensao_primaria = input('Digite a tensão nominal primária: ')
        impedancia_de_placa = input('Digite a impedância percentual de placa do transformador: ')

        perdas_no_cobre = {
            '15': 300, '30': 570, '45': 750, '75': 1200, '112.5': 1650,
            '150': 2050, '225': 2800, '300': 3900, '500': 6400, '750': 10000,
            '1000': 12500, '1500': 18000
        }

        try:
            perdas = perdas_no_cobre[pot_trafo]
            tensao_op = input('Digite a tensão nominal do trafo: 1) 220\n2) 380 ou 440\n')

            if tensao_op in ['1', '2']:
                perdas_no_cobre = perdas
                resistencia_percentual = perdas_no_cobre / (10 * int(pot_trafo))
                resistencia_percentual_base = (resistencia_percentual / 100) * (
                        (potencia / (int(pot_trafo) * 1000)) * (float(tensao_primaria) / tensao))
                impedancia_percentual_base = (float(impedancia_de_placa) / 100) * (
                        (potencia / (int(pot_trafo) * 1000)) * (float(tensao_primaria) / tensao))
                reatancia_percentual_base = math.sqrt(
                    (math.pow(impedancia_percentual_base, 2) - math.pow(resistencia_percentual_base, 2)))

                return complex(resistencia_percentual_base, reatancia_percentual_base)

            else:
                print('Opção inválida')

        except KeyError:
            print('Potência do transformador inválida.')

    else:
        print('Opção inválida.')
    
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
