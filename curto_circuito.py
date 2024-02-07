# CÓDIGO DO MÓDULO 1

# BIBLIOTECAS
from funcionalidades import valores_base, obter_impedancia, corrente_curto_trifasica_simetrica, corrente_curto_monofasica
from funcionalidades import potencia_de_curto_circuito, exibir_menu, tipo_transformador, impedancia_alimentadores, impedancia_barramento
from time import sleep

# MAIN
while True:
    exibir_menu()
    opcao = input("Digite o número da opção desejada: ")
    escolha = opcao.strip()
    sleep(1)

    if escolha == "1":
        corrente_base_primaria,corrente_base_secundaria,tensao_primaria_base,tensao_secundaria_base, potencia = valores_base() # VALORES BASE DO SISTEMA
        print(corrente_base_primaria,corrente_base_secundaria, tensao_primaria_base, tensao_secundaria_base, potencia)

    elif escolha == "2":
    # IMPEDÂNCIAS 
        impedancia_reduzida_positiva = obter_impedancia() # IMPEDÂNCIA DE SEQUÊNCIA POSITIVA REDUZIDA DO SISTEMA
        impedancia_reduzida_negativa = obter_impedancia() # IMPEDÂNCIA DE SEQUÊNCIA NEGATIVA REDUZIDA DO SISTEMA
        impedancia_reduzida_zero = obter_impedancia() # IMPEDÂNCIA DE SEQUÊNCIA ZERO REDUZIDA DO SISTEMA
        impedancia_trafo_zero = obter_impedancia() # IMPEDÂNCIA DE SEQUÊNCIA ZERO DO TRANSFORMADOR
        impedancia_condutores_zero = obter_impedancia() # IMPEDÂNCIA DE SEQUÊNCIA ZERO DOS CONDUTORES

    elif escolha == "3":
        # CALCULANDO CURTO-CIRCUITO
        tri = corrente_curto_trifasica_simetrica(impedancia_reduzida_positiva, corrente_base_primaria) # ICC TRIFÁSICO
        print(tri)

    elif escolha == "4":
        impedancia_acumulada = impedancia_reduzida_positiva + impedancia_trafo_zero
        mono = corrente_curto_monofasica(impedancia_acumulada, impedancia_reduzida_zero, impedancia_condutores_zero, impedancia_trafo_zero, corrente_base_primaria) # ICC MONO MÁX
        print(mono)

    elif escolha == "5":
        pot_cc = potencia_de_curto_circuito(tensao_primaria_base, corrente_base_primaria) # POTÊNCIA DE CURTO-CIRCUITO
        print(pot_cc)
    
    elif escolha == "6":
        trafo_escolhido = tipo_transformador(tensao_primaria_base, str(tensao_secundaria_base), potencia) # MODELANDO TRANSFORMADOR
        print(trafo_escolhido)
    
    elif escolha == "7":
        #corrente_base_primaria,corrente_base_secundaria_secundaria = valores_base()
        impedancia_acumulada_positiva = impedancia_reduzida_positiva + trafo_escolhido
        corrente_curto_terminal_trafo = corrente_curto_trifasica_simetrica(impedancia_acumulada_positiva, corrente_base_secundaria)
        print('*'*50)
        print(corrente_base_primaria, corrente_base_secundaria)
        print(corrente_curto_terminal_trafo)
    
    elif escolha == "8":

        impedancia_acumulada_2 = impedancia_reduzida_positiva + trafo_escolhido
        mono_secundario = corrente_curto_monofasica(impedancia_acumulada_2, impedancia_reduzida_zero, impedancia_condutores_zero, trafo_escolhido, corrente_base_secundaria)
        print(mono_secundario)
    
    elif escolha == "9":

        comprimento = float(input('Qual o comprimento do alimentador: '))
        cabos_paralelos = float(input('Digite quantos cabos por fase tem no circuito: '))
        impedancia_alimentador = impedancia_alimentadores(comprimento, cabos_paralelos, potencia, tensao_secundaria_base)
        print(impedancia_alimentador)
    
    elif escolha == "10":

        largura = str(input('Qual a largura do barramento: '))
        espessura = str(input('Digite a espessura do barramento: '))
        comprimento_bar = float(input('Digite o comprimento do barramento: '))
        quant_bar_por_fase = float(input('Digite quantas barras por fase: '))
        impedancia_barramento_modelado = impedancia_barramento(largura, espessura, comprimento_bar, quant_bar_por_fase, potencia, tensao_secundaria_base)

        print(impedancia_barramento_modelado)
    
    elif escolha == "11": 

        impedancia_qgf_positiva = impedancia_reduzida_positiva + trafo_escolhido + impedancia_alimentador + impedancia_barramento_modelado

        print(impedancia_qgf_positiva)

        curto_simetrico_barramento = corrente_curto_trifasica_simetrica(impedancia_qgf_positiva, corrente_base_secundaria) # ICC TRIFÁSICO
        curto_monofasico_barramento = corrente_curto_monofasica(impedancia_qgf_positiva, impedancia_reduzida_zero, impedancia_condutores_zero, trafo_escolhido, corrente_base_secundaria)
        print(curto_simetrico_barramento)
        print(curto_monofasico_barramento)
    
    elif escolha == "12":

        comprimento_circuito_QGF_CCM3 = float(input('Qual o comprimento do alimentador: '))
        cabos_paralelos_QGF_CCM3 = float(input('Digite quantos cabos por fase tem no circuito: '))

        impedancia_circuito_QGF_CCM3 = impedancia_alimentadores(comprimento_circuito_QGF_CCM3, cabos_paralelos_QGF_CCM3, potencia, tensao_secundaria_base)
        print(impedancia_circuito_QGF_CCM3)

    elif escolha == "0":
        break
    
    else:
        print('Opção inválida.')
        sleep(1)
