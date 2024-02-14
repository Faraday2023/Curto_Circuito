# FUNCIONALIDADES

import math, numpy, cmath
from validacao import validar_valor_float, validar_valor_inteiro, verificar_argumentos_explicitos

# FUNÇÃO DE MENU
def exibir_menu():
    print('-'*100)
    print("Escolha uma opção:")
    print('-'*100)
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
    print("12. Impedância acumulada no CCM")
    print("13. Curto no CCM")
    print("14. Curto assimétrico")
    print("15. Impulso da corrente de curto_circuito")
    print("16. Curto bifásico")
    print("17. Calculo  curto fase terra máximo")
    print("18. Curto fase terra mínimo")
    print("0. Sair")
    print('-'*100)

# FUNÇÃO PARA DETERMINAÇÃO DE IMPEDÂNCIAS
    
def obter_impedancia():
    while True:
        try:
            parte_real = input('Digite a parte real da impedância: ').strip()
            parte_real = validar_valor_float(parte_real)
            
            while True:
                try:
                    parte_imaginaria = input('Digite a parte imaginária da impedância: ').strip()
                    parte_imaginaria = validar_valor_float(parte_imaginaria)
                    
                    if parte_imaginaria == 0:
                        print("Erro: A parte imaginária da impedância não pode ser zero. Por favor, insira um valor diferente.")
                    else:
                        break  # Sai do loop interno se a parte imaginária for diferente de zero
                except ValueError as ve:
                    print(f"{ve}")
            
            return complex(parte_real, parte_imaginaria)
        
        except KeyboardInterrupt:
            print("\nOperação interrompida pelo usuário.")
            raise
        except ValueError as ve:
            print(f"Erro: {ve}")

# FUNÇÃO PARA DETERMINAÇÃO DOS BASE
def valores_base():
    try:
        while True:
            # Solicita ao usuário que insira a potência base
            potencia = input('Defina a potência base (em números inteiros): ').strip()
            # Valida a entrada da potência base
            potencia = validar_valor_inteiro(potencia)
            
            # Solicita ao usuário que insira a tensão base primária
            tensao_base_primaria = input('Defina a tensão base primária (em números inteiros): ').strip()
            # Valida a entrada da tensão base primária
            tensao_base_primaria = validar_valor_float(tensao_base_primaria)
            
            # Solicita ao usuário que insira a tensão base secundária
            tensao_base_secundaria = input('Defina a tensão base secundária (em números inteiros): ').strip()
            # Valida a entrada da tensão base secundária
            tensao_base_secundaria = validar_valor_inteiro(tensao_base_secundaria)

            try:
                corrente_base_primaria = potencia / (tensao_base_primaria * math.sqrt(3))
                corrente_base_secundaria = potencia / (tensao_base_secundaria * math.sqrt(3))
                impedancia_base_primaria = (tensao_base_primaria**2) / potencia
                impedancia_base_secundaria = (tensao_base_secundaria**2) / potencia

            except ZeroDivisionError:
                print("Erro: A tensão base não pode ser zero.")
                return None

            return round(corrente_base_primaria, 2), round(corrente_base_secundaria, 2), tensao_base_primaria, tensao_base_secundaria, potencia, impedancia_base_primaria, impedancia_base_secundaria
    
    except KeyboardInterrupt:
        print("\nPrograma encerrado pelo usuário.")
        return None

def conversao_fisico_pu(valor_fisico = None, valor_base = None):

    argumentos = [(valor_fisico, "valor_fisico"), (valor_base, "valor_base")]

    # Verificar se todos os argumentos foram fornecidos
    for arg, nome in argumentos:
        if not verificar_argumentos_explicitos(arg, nome, 1): # Passo aqui precisa ser definido ainda
            return None

    valor_fisico = validar_valor_float(valor_fisico)
    valor_base = validar_valor_float(valor_base)

    if valor_fisico is not None and valor_base is not None:
        valor_pu = valor_fisico / valor_base
        return valor_pu
    else:
        print("Não foi possível calcular o valor por unidade (PU). Por favor defina o valor_fisico e o valor_base primeiro")

    return valor_pu

def mudanca_base(valor_antigo = None, potencia_nova = None, potencia_antiga = None, tensao_antiga = None, tensao_nova = None ):

    argumentos = [(valor_antigo, "valor_antigo"), (potencia_nova, "potencia_nova"), (potencia_antiga, "potencia_antiga"), (tensao_antiga, "tensao_antiga"), (tensao_nova, "tensao_nova")]

    # Verificar se todos os argumentos foram fornecidos
    for arg, nome in argumentos:
        if not verificar_argumentos_explicitos(arg, nome, 1): # Passo aqui precisa ser definido ainda
            return None

    valor_antigo = validar_valor_float(valor_antigo)
    potencia_nova = validar_valor_float(potencia_nova)
    potencia_antiga = validar_valor_float(potencia_antiga)
    tensao_antiga = validar_valor_float(tensao_antiga)
    tensao_nova = validar_valor_float(tensao_nova)

    valor_novo = valor_antigo*(potencia_nova/potencia_antiga)*(tensao_antiga/tensao_nova)**2

    return valor_novo

# CORRENTE DE CURTO TRIFÁSICA SIMÉTRICA 

def corrente_curto_trifasica_simetrica(impedancia_reduzida_sistema = None, corrente_base = None):

    argumentos = [(impedancia_reduzida_sistema, "impedancia_reduzida_sistema"), (corrente_base, "corrente_base")]

    # Verificar se todos os argumentos foram fornecidos
    for arg, nome in argumentos:
        if not verificar_argumentos_explicitos(arg, nome, 1): # Passo aqui precisa ser definido ainda
            return None
    
    curto_trifasico_simetrico = (1/(impedancia_reduzida_sistema)) * corrente_base
    magnitude, angulo_radiano = cmath.polar(curto_trifasico_simetrico)
    angulo_graus = math.degrees(angulo_radiano)
    return magnitude, angulo_graus

# CORRENTE DE CURTO-CIRCUITO FASE/TERRA
def corrente_curto_monofasica(impedancia_reduzida,impedancia_zero,impedancia_trafo,corrente_base):
    
    curto_fase_terra = (3 * corrente_base)/((2 *(impedancia_reduzida))+ impedancia_zero +impedancia_trafo)
    magnitude, angulo_radiano = cmath.polar(curto_fase_terra)
    angulo_graus = math.degrees(angulo_radiano)
    return magnitude, angulo_graus

# POTÊNCIA DE CURTO-CIRCUITO

def potencia_de_curto_circuito(tensao_base_primaria, corrente_base_primaria):
    
    potência_cc = math.sqrt(3) * tensao_base_primaria * corrente_base_primaria
    
    return round(potência_cc,2)

# MODELANDO TRANSFORMADOR
def tipo_transformador(tensao_base_primaria,tensao_base_secundaria, potencia):
    print('-' * 100)
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
        print('-' * 100)
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
        '1.5': {'resistencia_positiva': 14.8137, 'reatancia_positiva': 0.1378,'resistencia_zero': 16.6137, 'reatancia_zero': 2.9262}, 
        '2.5': {'resistencia_positiva': 8.8882, 'reatancia_positiva': 0.1345,'resistencia_zero': 10.6882, 'reatancia_zero': 2.8755},
        '4': {'resistencia_positiva': 5.5518, 'reatancia_positiva': 0.1279, 'resistencia_zero': 7.3552, 'reatancia_zero': 2.8349},
        '6': {'resistencia_positiva': 3.7045, 'reatancia_positiva': 0.1225, 'resistencia_zero': 5.5035, 'reatancia_zero': 2.8},
        '10': {'resistencia_positiva': 2.221, 'reatancia_positiva': 0.1207, 'resistencia_zero': 4.0222, 'reatancia_zero': 2.7639},
        '16': {'resistencia_positiva': 1.3899, 'reatancia_positiva': 0.1173, 'resistencia_zero': 3.1890, 'reatancia_zero': 2.7173},
        '25': {'resistencia_positiva': 0.8891, 'reatancia_positiva': 0.1164, 'resistencia_zero': 2.6891, 'reatancia_zero': 2.6692},
        '35': {'resistencia_positiva': 0.6353, 'reatancia_positiva': 0.1128, 'resistencia_zero': 2.4355, 'reatancia_zero': 2.6382},
        '50': {'resistencia_positiva': 0.445, 'reatancia_positiva': 0.1127, 'resistencia_zero': 2.2450, 'reatancia_zero': 2.5991},
        '70': {'resistencia_positiva': 0.3184, 'reatancia_positiva': 0.1096, 'resistencia_zero': 2.1184, 'reatancia_zero': 2.5681},
        '95': {'resistencia_positiva': 0.2352, 'reatancia_positiva': 0.1090, 'resistencia_zero': 2.0352, 'reatancia_zero': 2.5325},
        '120': {'resistencia_positiva': 0.1868, 'reatancia_positiva': 0.1076, 'resistencia_zero': 1.9868, 'reatancia_zero': 2.5104},
        '150': {'resistencia_positiva': 0.1502, 'reatancia_positiva': 0.1076, 'resistencia_zero': 1.9502, 'reatancia_zero': 2.4843},
        '185': {'resistencia_positiva': 0.1226, 'reatancia_positiva': 0.1073, 'resistencia_zero': 1.9226, 'reatancia_zero': 2.4594},
        '240': {'resistencia_positiva': 0.0958, 'reatancia_positiva': 0.1070, 'resistencia_zero': 1.8958, 'reatancia_zero': 2.4312},
        '300': {'resistencia_positiva': 0.0781, 'reatancia_positiva': 0.1068, 'resistencia_zero': 1.8781, 'reatancia_zero': 2.4067},
        '400': {'resistencia_positiva': 0.0608, 'reatancia_positiva': 0.1058, 'resistencia_zero': 1.8608, 'reatancia_zero': 2.3757},
        '500': {'resistencia_positiva': 0.0507, 'reatancia_positiva': 0.1051, 'resistencia_zero': 1.8550, 'reatancia_zero': 2.3491},
        '630': {'resistencia_positiva': 0.0292, 'reatancia_positiva': 0.1042, 'resistencia_zero': 1.8376, 'reatancia_zero': 2.3001}
    }

    secao_cabo = input('Digite a seção nominal do cabo: ')
    
    if secao_cabo in dados_cabos:
        dados = dados_cabos[secao_cabo]

        resistencia_do_circuito_positiva = (dados['resistencia_positiva'] * comprimento_alimentador) / (1000 * cabos_por_fase)
        reatancia_do_circuito_positiva = (dados['reatancia_positiva'] * comprimento_alimentador) / (1000 * cabos_por_fase)
        resistencia_do_circuito_zero = (dados['resistencia_zero'] * comprimento_alimentador) / (1000 * cabos_por_fase)
        reatancia_do_circuito_zero = (dados['reatancia_zero'] * comprimento_alimentador) / (1000 * cabos_por_fase)

        resistencia_circuito_base_nova_positiva = (resistencia_do_circuito_positiva * 1000) * (potencia / (1000 * (tensao_base_secundaria ** 2)))
        reatancia_circuito_base_nova_positiva = (reatancia_do_circuito_positiva * 1000) * (potencia / (1000 * (tensao_base_secundaria ** 2)))
        resistencia_circuito_base_nova_zero = (resistencia_do_circuito_zero * 1000) * (potencia / (1000 * (tensao_base_secundaria ** 2)))
        reatancia_circuito_base_nova_zero = (reatancia_do_circuito_zero * 1000) * (potencia / (1000 * (tensao_base_secundaria ** 2)))

        impedancia_circuito_positiva = complex(resistencia_circuito_base_nova_positiva, reatancia_circuito_base_nova_positiva)
        impedancia_circuito_zero = complex(resistencia_circuito_base_nova_zero, reatancia_circuito_base_nova_zero)

        return impedancia_circuito_positiva, impedancia_circuito_zero
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

def curto_assimétrico(resistencia_total, reatancia_total, curto_simetrico_tri):

    a = round(reatancia_total/resistencia_total,1)

    relacao_X_R = {

        '0.4': {'fator_de_assimetria': 1.0}, '0.6': {'fator_de_assimetria': 1.0}, '0.8': {'fator_de_assimetria': 1.02},
        '1.0': {'fator_de_assimetria': 1.04}, '1.2': {'fator_de_assimetria': 1.07}, '1.4': {'fator_de_assimetria': 1.10},
        '1.6': {'fator_de_assimetria': 1.13}, '1.8': {'fator_de_assimetria': 1.16}, '2.0': {'fator_de_assimetria': 1.19},
        '2.2': {'fator_de_assimetria': 1.21}, '2.4': {'fator_de_assimetria': 1.24}, '2.6': {'fator_de_assimetria': 1.26},
        '2.8': {'fator_de_assimetria': 1.28}, '3.0': {'fator_de_assimetria': 1.30}, '3.2': {'fator_de_assimetria': 1.32},
        '3.4': {'fator_de_assimetria': 1.34}, '3.6': {'fator_de_assimetria': 1.35}, '3.8': {'fator_de_assimetria': 1.37},
        '4.0': {'fator_de_assimetria': 1.38}, '4.2': {'fator_de_assimetria': 1.39}, '4.4': {'fator_de_assimetria': 1.40},
        '4.6': {'fator_de_assimetria': 1.41}, '4.8': {'fator_de_assimetria': 1.42}, '5.0': {'fator_de_assimetria': 1.43},
        '5.5': {'fator_de_assimetria': 1.46}, '6.0': {'fator_de_assimetria': 1.47}, '6.5': {'fator_de_assimetria': 1.49},
        '7.0': {'fator_de_assimetria': 1.51}, '7.5': {'fator_de_assimetria': 1.52}, '8.0': {'fator_de_assimetria': 1.53},
        '8.5': {'fator_de_assimetria': 1.54}, '9.0': {'fator_de_assimetria': 1.55}, '9.5': {'fator_de_assimetria': 1.56},
        '10.0': {'fator_de_assimetria': 1.57},'11.0': {'fator_de_assimetria': 1.58}, '12.0': {'fator_de_assimetria': 1.59},
        '13.0': {'fator_de_assimetria': 1.60},'14.0': {'fator_de_assimetria': 1.61},'15.0': {'fator_de_assimetria': 1.62},
        '20.0': {'fator_de_assimetria': 1.64},'30.0': {'fator_de_assimetria': 1.67},'40.0': {'fator_de_assimetria': 1.68},
        '50.0': {'fator_de_assimetria': 1.69},'60.0': {'fator_de_assimetria': 1.70},'70.0': {'fator_de_assimetria': 1.71},
        '80.0': {'fator_de_assimetria': 1.71},'100.0': {'fator_de_assimetria': 1.71},'200.0': {'fator_de_assimetria': 1.72},
        '400.0': {'fator_de_assimetria': 1.72},'600.0': {'fator_de_assimetria': 1.73},'1000.0': {'fator_de_assimetria': 1.73}

        # ADICIONAR CONFORME NECESSÁRIO

    }

    chave_mais_proxima = None
    minima_diferenca = float('inf')  # Inicializa a diferença mínima como infinito

    for chave in relacao_X_R.keys():
        diferenca_atual = float(chave) - a
        if diferenca_atual >= 0 and diferenca_atual < minima_diferenca:
            minima_diferenca = diferenca_atual
            chave_mais_proxima = chave

    if chave_mais_proxima is not None:
        real, ang = curto_simetrico_tri
        curto_assimetrico = relacao_X_R[chave_mais_proxima]['fator_de_assimetria'] * real
    else:
        # Tratar caso especial se nenhuma chave adequada for encontrada
        print("Nenhuma chave adequada encontrada no dicionário para o valor arredondado de 'a'")
    
    return curto_assimetrico

def impulso_da_corrente_de_curto_circuito(curto_assim): 
    
    impulso = curto_assim*math.sqrt(2)

    return impulso

def curto_bifasico(curto_assimetrico_trifasico):

    curto_bif = curto_assimetrico_trifasico*(math.sqrt(3)/2)
    return curto_bif

def corrente_curto_monofasica_minima(impedancia_reduzida,impedancia_zero,impedancia_trafo,corrente_base, r_contato, r_malha, r_resistor):
    
    curto_fase_terra_minimo = (3 * corrente_base)/((2 *(impedancia_reduzida))+ impedancia_zero + impedancia_trafo + 3*(r_contato + r_malha + r_resistor))
    magnitude, angulo_radiano = cmath.polar(curto_fase_terra_minimo)
    angulo_graus = math.degrees(angulo_radiano)
    return magnitude, angulo_graus

def impedancia_acumulada_positiva(impedancia_atual, acumulada):
    acumulada = impedancia_atual + acumulada
    return acumulada

def impedancia_acumulada_zero(impedancia_atual, acumulada):
    acumulada = impedancia_atual + acumulada
    return acumulada
