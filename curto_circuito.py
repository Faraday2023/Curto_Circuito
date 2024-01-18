# CÓDIGO DO MÓDULO 1

# BIBLIOTECAS
from funcionalidades import valores_base, obter_impedancia, corrente_curto_trifasica_simetrica, corrente_curto_monofasica
from funcionalidades import potencia_de_curto_circuito, exibir_menu, tipo_transformador
from time import sleep

# MAIN
while True:
    exibir_menu()
    opcao = input("Digite o número da opção desejada: ")
    escolha = opcao.strip()
    sleep(1)

    if escolha == "1":
        corrente_base = valores_base() # CORRENTE BASE DO SISTEMA

    elif escolha == "2":
    # IMPEDÂNCIAS 
        impedancia_reduzida_positiva = obter_impedancia() # IMPEDÂNCIA DE SEQUÊNCIA POSITIVA REDUZIDA DO SISTEMA
        impedancia_reduzida_negativa = obter_impedancia() # IMPEDÂNCIA DE SEQUÊNCIA POSITIVA REDUZIDA DO SISTEMA
        impedancia_reduzida_zero = obter_impedancia() # IMPEDÂNCIA DE SEQUÊNCIA ZERO REDUZIDA DO SISTEMA
        impedancia_trafo_zero = obter_impedancia() # IMPEDÂNCIA DE SEQUÊNCIA ZERO DO TRANSFORMADOR
        impedancia_condutores_zero = obter_impedancia() # IMPEDÂNCIA DE SEQUÊNCIA ZERO DOS CONDUTORES

    elif escolha == "3":
        # CALCULANDO CURTO-CIRCUITO
        tri = corrente_curto_trifasica_simetrica(impedancia_reduzida_positiva) # ICC TRIFÁSICO
        print(tri)

    elif escolha == "4":
        mono = corrente_curto_monofasica(impedancia_reduzida_zero, impedancia_condutores_zero, impedancia_trafo_zero) # ICC MONO MÁX
        print(mono)

    elif escolha == "5":
        pot_cc = potencia_de_curto_circuito() # POTÊNCIA DE CURTO-CIRCUITO
        print(pot_cc)
    
    elif escolha == "6":
        trafo_escolhido = tipo_transformador()
        print(trafo_escolhido)

    elif escolha == "0":
        break
    
    else:
        print('Opção inválida.')
        sleep(1)
