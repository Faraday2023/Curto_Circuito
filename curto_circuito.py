# CÓDIGO DO MÓDULO 1

# BIBLIOTECAS
from funcionalidades import valores_base, obter_impedancia, corrente_curto_trifasica_simetrica, corrente_curto_monofasica
from funcionalidades import potencia_de_curto_circuito, exibir_menu, tipo_transformador, impedancia_alimentadores, impedancia_barramento
from funcionalidades import curto_assimétrico, impulso_da_corrente_de_curto_circuito, curto_bifasico, corrente_curto_monofasica_minima
from funcionalidades import conversao_fisico_pu, mudanca_base, impedancia_acumulada_positiva, impedancia_acumulada_zero
from validacao import executar_funcao_com_validacao, imprimir_resultado, executar_variavel_com_validacao
from time import sleep

# MAIN
while True:
    exibir_menu()
    opcao = input("Digite o número da opção desejada: ")
    escolha = opcao.strip()
    sleep(1)

    if escolha == "1":
        corrente_base_primaria,corrente_base_secundaria,tensao_primaria_base,tensao_secundaria_base, potencia, impedancia_base_primaria, impedancia_base_secundaria = valores_base() # VALORES BASE DO SISTEMA
        print(corrente_base_primaria,corrente_base_secundaria, tensao_primaria_base, tensao_secundaria_base, potencia)

    elif escolha == "2":
    # IMPEDÂNCIAS 
        impedancia_reduzida_positiva = obter_impedancia() # IMPEDÂNCIA DE SEQUÊNCIA POSITIVA REDUZIDA DO SISTEMA
        impedancia_reduzida_negativa = obter_impedancia() # IMPEDÂNCIA DE SEQUÊNCIA NEGATIVA REDUZIDA DO SISTEMA
        impedancia_reduzida_zero = obter_impedancia() # IMPEDÂNCIA DE SEQUÊNCIA ZERO REDUZIDA DO SISTEMA
        impedancia_trafo_zero = obter_impedancia() # IMPEDÂNCIA DE SEQUÊNCIA ZERO DO TRANSFORMADOR
        impedancia_condutores_zero = obter_impedancia() # IMPEDÂNCIA DE SEQUÊNCIA ZERO DOS CONDUTORES
        impedancia_acumulada_positiva_trecho_01 = executar_funcao_com_validacao(lambda: impedancia_acumulada_positiva(impedancia_reduzida_positiva,0))
        impedancia_acumulada_zero_trecho_01 = executar_funcao_com_validacao(lambda: impedancia_acumulada_zero(impedancia_condutores_zero, 0))
        
    elif escolha == "3":

        tri = executar_funcao_com_validacao(lambda:corrente_curto_trifasica_simetrica(impedancia_reduzida_positiva, corrente_base_primaria))
        imprimir_resultado(tri)

    elif escolha == "4":
        #impedancia_acumulada = impedancia_reduzida_positiva + impedancia_trafo_zero
        
        mono = executar_funcao_com_validacao(lambda:corrente_curto_monofasica(impedancia_acumulada_positiva_trecho_01, impedancia_reduzida_zero + impedancia_condutores_zero, impedancia_trafo_zero, corrente_base_primaria)) # ICC MONO MÁX
        imprimir_resultado(mono)

    elif escolha == "5":
        pot_cc = executar_funcao_com_validacao(lambda:potencia_de_curto_circuito(tensao_primaria_base, corrente_base_primaria)) # POTÊNCIA DE CURTO-CIRCUITO
        print(pot_cc)
    
    elif escolha == "6":
        trafo_escolhido = executar_funcao_com_validacao(lambda:tipo_transformador(tensao_primaria_base, str(tensao_secundaria_base), potencia)) # MODELANDO TRANSFORMADOR
        print(trafo_escolhido)
    
    elif escolha == "7":
        #corrente_base_primaria,corrente_base_secundaria_secundaria = valores_base()
        #impedancia_acumulada_positiva = impedancia_reduzida_positiva + trafo_escolhido
        impedancia_acumulada_positiva_trecho_02 = executar_funcao_com_validacao(lambda: impedancia_acumulada_positiva(trafo_escolhido, impedancia_acumulada_positiva_trecho_01))
        corrente_curto_terminal_trafo = executar_funcao_com_validacao(lambda: corrente_curto_trifasica_simetrica(impedancia_acumulada_positiva_trecho_02, corrente_base_secundaria))
        print('*'*50)
        print(corrente_base_primaria, corrente_base_secundaria)
        print(corrente_curto_terminal_trafo)
    
    elif escolha == "8":

        mono_secundario = executar_funcao_com_validacao(lambda: corrente_curto_monofasica(impedancia_acumulada_positiva_trecho_02, impedancia_reduzida_zero + impedancia_condutores_zero, trafo_escolhido, corrente_base_secundaria))
        print(mono_secundario)
    
    elif escolha == "9":

        comprimento = float(input('Qual o comprimento do alimentador: '))
        cabos_paralelos = float(input('Digite quantos cabos por fase tem no circuito: '))
        impedancia_alimentador_positiva,impedancia_alimentador_zero = executar_funcao_com_validacao(lambda:impedancia_alimentadores(comprimento, cabos_paralelos, potencia, tensao_secundaria_base))
        impedancia_acumulada_positiva_trecho_03 = executar_funcao_com_validacao(lambda: impedancia_acumulada_positiva(impedancia_alimentador_positiva, impedancia_acumulada_positiva_trecho_02))
        impedancia_acumulada_zero_trecho_02 = executar_funcao_com_validacao(lambda: impedancia_acumulada_zero(impedancia_alimentador_zero, impedancia_acumulada_zero_trecho_01))
        print(impedancia_alimentador_positiva)
    
    elif escolha == "10":

        largura = str(input('Qual a largura do barramento: '))
        espessura = str(input('Digite a espessura do barramento: '))
        comprimento_bar = float(input('Digite o comprimento do barramento: '))
        quant_bar_por_fase = float(input('Digite quantas barras por fase: '))
        impedancia_barramento_modelado = executar_funcao_com_validacao(lambda: impedancia_barramento(largura, espessura, comprimento_bar, quant_bar_por_fase, potencia, tensao_secundaria_base))
        impedancia_acumulada_positiva_trecho_04 = executar_funcao_com_validacao(lambda: impedancia_acumulada_positiva(impedancia_barramento_modelado, impedancia_acumulada_positiva_trecho_03))

        print(impedancia_barramento_modelado)
    
    elif escolha == "11": 

        curto_simetrico_barramento = executar_funcao_com_validacao(lambda: corrente_curto_trifasica_simetrica(impedancia_acumulada_positiva_trecho_04, corrente_base_secundaria)) # ICC TRIFÁSICO
        curto_monofasico_barramento = executar_funcao_com_validacao(lambda: corrente_curto_monofasica(impedancia_acumulada_positiva_trecho_04, impedancia_reduzida_zero + impedancia_condutores_zero, trafo_escolhido, corrente_base_secundaria))
        print(curto_simetrico_barramento)
        print(curto_monofasico_barramento)
    
    elif escolha == "12":

        comprimento_circuito_QGF_CCM3 = float(input('Qual o comprimento do alimentador: '))
        cabos_paralelos_QGF_CCM3 = float(input('Digite quantos cabos por fase tem no circuito: '))
        impedancia_circuito_QGF_CCM3_positiva, impedancia_circuito_QGF_CCM3_zero = executar_funcao_com_validacao(lambda: impedancia_alimentadores(comprimento_circuito_QGF_CCM3, cabos_paralelos_QGF_CCM3, potencia, tensao_secundaria_base))
        impedancia_acumulada_positiva_trecho_05 = executar_funcao_com_validacao(lambda: impedancia_acumulada_positiva(impedancia_circuito_QGF_CCM3_positiva, impedancia_acumulada_positiva_trecho_04))
        impedancia_acumulada_zero_trecho_03 = executar_funcao_com_validacao(lambda: impedancia_acumulada_zero(impedancia_circuito_QGF_CCM3_zero, impedancia_acumulada_zero_trecho_02))
        print(impedancia_circuito_QGF_CCM3_positiva)
    
    elif escolha == "13":

        curto_no_ccm = corrente_curto_trifasica_simetrica(impedancia_acumulada_positiva_trecho_05, corrente_base_secundaria) # ICC TRIFÁSICO
        print(curto_no_ccm)
    
    elif escolha == "14":

        real = impedancia_acumulada_positiva_trecho_05.real
        imag = impedancia_acumulada_positiva_trecho_05.imag

        curto_assimetrico = curto_assimétrico(real, imag, curto_no_ccm)
        print(curto_assimetrico)
    
    elif escolha == "15":

        impulso = impulso_da_corrente_de_curto_circuito(curto_assimetrico)
        print(impulso)
    
    elif escolha == "16":

        curto_bif = curto_bifasico(curto_assimetrico)
        print(curto_bif)
    
    elif escolha == "17":

        #impedancia_acumulada_zero = impedancia_alimentador_zero + impedancia_circuito_QGF_CCM3_zero
        mono_max = corrente_curto_monofasica(impedancia_acumulada_positiva_trecho_05, impedancia_acumulada_zero_trecho_03, trafo_escolhido, corrente_base_secundaria) # ICC MONO MÁX
        print(mono_max)
    
    elif escolha == "18":

        re_contato = int(input('Digite a resistência de contato: '))
        re_contato_pu = conversao_fisico_pu(re_contato, impedancia_base_secundaria)
        re_malha = int(input('Digite a resistencia da malha de aterramento: '))
        re_malha_pu = conversao_fisico_pu(re_malha, impedancia_base_secundaria)
        re_resistor = int(input('Digite o valor do resistor de aterramento: '))
        re_resistor_pu = conversao_fisico_pu(re_resistor, impedancia_base_secundaria)

        curto_minimo = corrente_curto_monofasica_minima(impedancia_acumulada_positiva_trecho_05, impedancia_acumulada_zero_trecho_03, impedancia_trafo_zero, corrente_base_secundaria, re_contato_pu, re_malha_pu, re_resistor_pu)
        print(impedancia_acumulada_positiva_trecho_05, impedancia_acumulada_zero_trecho_02, trafo_escolhido, re_contato_pu, re_malha_pu, re_resistor_pu)
        print(curto_minimo)
        
    elif escolha == "0":
        break
    
    else:
        print('Opção inválida.')
        sleep(1)
