# CÓDIGO DO MÓDULO 1

# BIBLIOTECAS
from funcionalidades import valores_base, obter_impedancia, corrente_curto_trifasica_simetrica, corrente_curto_monofasica
from funcionalidades import potencia_de_curto_circuito, exibir_menu, tipo_transformador, impedancia_alimentadores
from time import sleep

# MAIN
while True:
    exibir_menu()
    opcao = input("Digite o número da opção desejada: ")
    escolha = opcao.strip()
    sleep(1)

    if escolha == "1":
        corrente_base = valores_base() # CORRENTE BASE DO SISTEMA
        print(corrente_base)

    elif escolha == "2":
    # IMPEDÂNCIAS 
        impedancia_reduzida_positiva = obter_impedancia() # IMPEDÂNCIA DE SEQUÊNCIA POSITIVA REDUZIDA DO SISTEMA
        impedancia_reduzida_negativa = obter_impedancia() # IMPEDÂNCIA DE SEQUÊNCIA NEGATIVA REDUZIDA DO SISTEMA
        impedancia_reduzida_zero = obter_impedancia() # IMPEDÂNCIA DE SEQUÊNCIA ZERO REDUZIDA DO SISTEMA
        impedancia_trafo_zero = obter_impedancia() # IMPEDÂNCIA DE SEQUÊNCIA ZERO DO TRANSFORMADOR
        impedancia_condutores_zero = obter_impedancia() # IMPEDÂNCIA DE SEQUÊNCIA ZERO DOS CONDUTORES

    elif escolha == "3":
        # CALCULANDO CURTO-CIRCUITO
        tri = corrente_curto_trifasica_simetrica(impedancia_reduzida_positiva) # ICC TRIFÁSICO
        print(tri)

    elif escolha == "4":
        mono = corrente_curto_monofasica(impedancia_reduzida_positiva, impedancia_reduzida_zero, impedancia_condutores_zero, impedancia_trafo_zero, corrente_base) # ICC MONO MÁX
        print(mono)

    elif escolha == "5":
        pot_cc = potencia_de_curto_circuito() # POTÊNCIA DE CURTO-CIRCUITO
        print(pot_cc)
    
    elif escolha == "6":
        trafo_escolhido = tipo_transformador() # MODELANDO TRANSFORMADOR
        print(trafo_escolhido)
    
    elif escolha == "7":
        corrente_base_secundaria = valores_base()
        impedancia_acumulada_positiva = impedancia_reduzida_positiva + trafo_escolhido
        corrente_curto_terminal_trafo = corrente_curto_trifasica_simetrica(impedancia_acumulada_positiva)
        print('*'*50)
        print(corrente_base_secundaria)
        print(corrente_curto_terminal_trafo)
    
    elif escolha == "8":

        mono_secundario = corrente_curto_monofasica(impedancia_reduzida_positiva, impedancia_reduzida_zero, impedancia_condutores_zero, trafo_escolhido, corrente_base_secundaria)
        print(mono_secundario)
    
    elif escolha == "9":

        comprimento = float(input('Qual o comprimento do alimentador: '))
        cabos_paralelos = float(input('Digite quantos cabos por fase tem no circuito: '))
        impedancia_alimentador = impedancia_alimentadores(comprimento, cabos_paralelos)
        print(impedancia_alimentador)

    elif escolha == "0":
        break
    
    else:
        print('Opção inválida.')
        sleep(1)
