# CÓDIGO DO MÓDULO 1

# BIBLIOTECAS
from funcionalidades import *
from validacao import *
from time import sleep

opcoes_escolhidas = []

# MAIN
while True:
    exibir_menu()
    opcao = input("Digite o número da opção desejada: ")
    escolha = opcao.strip()
    sleep(1)

    dependencias_nao_atendidas = verificar_dependencias(escolha, opcoes_escolhidas)

    if dependencias_nao_atendidas is not None:
        print(f"Erro: Para escolher a opção {escolha}, você precisa primeiro escolher as opções {', '.join(dependencias_nao_atendidas)}.")
    
    else:
        print(f"Opção {escolha} selecionada com sucesso.")
        opcoes_escolhidas.append(escolha)
        
        if escolha == "1":

            corrente_base_primaria,corrente_base_secundaria,tensao_primaria_base,tensao_secundaria_base, potencia, impedancia_base_primaria, impedancia_base_secundaria = valores_base() # VALORES BASE DO SISTEMA

        elif escolha == "2":
        # IMPEDÂNCIAS 
            impedancia_reduzida_positiva = obter_impedancia() # IMPEDÂNCIA DE SEQUÊNCIA POSITIVA REDUZIDA DO SISTEMA
            impedancia_reduzida_negativa = obter_impedancia() # IMPEDÂNCIA DE SEQUÊNCIA NEGATIVA REDUZIDA DO SISTEMA
            impedancia_reduzida_zero = obter_impedancia() # IMPEDÂNCIA DE SEQUÊNCIA ZERO REDUZIDA DO SISTEMA
            impedancia_trafo_zero = obter_impedancia() # IMPEDÂNCIA DE SEQUÊNCIA ZERO DO TRANSFORMADOR
            impedancia_condutores_zero = obter_impedancia() # IMPEDÂNCIA DE SEQUÊNCIA ZERO DOS CONDUTORES
            impedancia_acumulada_positiva_trecho_01 = executar_funcao_com_validacao(impedancia_acumulada_positiva,impedancia_reduzida_positiva,0)
            impedancia_acumulada_zero_trecho_01 = executar_funcao_com_validacao(impedancia_acumulada_zero,impedancia_condutores_zero,0)
            
        elif escolha == "3":

            impedancia_reduzida_positiva = verificar_variavel_completa('impedancia_reduzida_positiva', globals())
            corrente_base_primaria = verificar_variavel_completa('corrente_base_primaria', globals())

            tri = executar_funcao_com_validacao(corrente_curto_trifasica_simetrica, impedancia_reduzida_positiva, corrente_base_primaria)
            imprimir_resultado(tri)

        elif escolha == "4":
          
            impedancia_acumulada_positiva_trecho_01 = verificar_variavel_completa('impedancia_acumulada_positiva_trecho_01', globals())
            impedancia_reduzida_zero = verificar_variavel_completa('impedancia_reduzida_zero', globals())
            impedancia_condutores_zero = verificar_variavel_completa('impedancia_condutores_zero', globals())
            impedancia_trafo_zero = verificar_variavel_completa('impedancia_trafo_zero', globals())
            corrente_base_primaria = verificar_variavel_completa('corrente_base_primaria', globals())

            mono = executar_funcao_com_validacao(corrente_curto_monofasica, impedancia_acumulada_positiva_trecho_01, impedancia_reduzida_zero, impedancia_trafo_zero, corrente_base_primaria) # Tirada impedancia do ramal de entrada (impedancia_condutores_zero), mais tarde irá ser acrescentada
            imprimir_resultado(mono)

        elif escolha == "5":

            tensao_primaria_base = verificar_variavel_completa('tensao_primaria_base', globals())
            corrente_base_primaria = verificar_variavel_completa('corrente_base_primaria', globals())
            
            pot_cc = executar_funcao_com_validacao(potencia_de_curto_circuito, tensao_primaria_base, corrente_base_primaria) # POTÊNCIA DE CURTO-CIRCUITO
            imprimir_resultado(pot_cc)
           
        elif escolha == "6":

            tensao_primaria_base = verificar_variavel_completa('tensao_primaria_base', globals())
            tensao_secundaria_base = verificar_variavel_completa('tensao_secundaria_base', globals())
            potencia = verificar_variavel_completa('potencia', globals())
            
            trafo_escolhido = executar_funcao_com_validacao(tipo_transformador, tensao_primaria_base, str(tensao_secundaria_base), potencia) # MODELANDO TRANSFORMADOR
            imprimir_resultado(trafo_escolhido)
        
        elif escolha == "7":

            trafo_escolhido = verificar_variavel_completa('trafo_escolhido', globals())
            impedancia_acumulada_positiva_trecho_01 = verificar_variavel_completa('impedancia_acumulada_positiva_trecho_01', globals())
            
            impedancia_acumulada_positiva_trecho_02 = executar_funcao_com_validacao(impedancia_acumulada_positiva,trafo_escolhido, impedancia_acumulada_positiva_trecho_01)
            corrente_curto_terminal_trafo = executar_funcao_com_validacao(corrente_curto_trifasica_simetrica, impedancia_acumulada_positiva_trecho_02, corrente_base_secundaria)
            imprimir_resultado(impedancia_acumulada_positiva_trecho_02)
            imprimir_resultado(corrente_curto_terminal_trafo)
        
        elif escolha == "8":

            impedancia_acumulada_positiva_trecho_02 = verificar_variavel_completa('impedancia_acumulada_positiva_trecho_02', globals())
            impedancia_reduzida_zero = verificar_variavel_completa('impedancia_reduzida_zero', globals())
            impedancia_condutores_zero = verificar_variavel_completa('impedancia_condutores_zero', globals())
            trafo_escolhido = verificar_variavel_completa('trafo_escolhido', globals())
            corrente_base_secundaria = verificar_variavel_completa('corrente_base_secundaria', globals())

            mono_secundario = executar_funcao_com_validacao(corrente_curto_monofasica, impedancia_acumulada_positiva_trecho_02, impedancia_reduzida_zero + impedancia_condutores_zero, trafo_escolhido, corrente_base_secundaria)
            imprimir_resultado(mono_secundario)
        
        elif escolha == "9":

            comprimento_alimentador, cabos_paralelos_alimentador = definir_alimentador()
            comprimento_alimentador = verificar_variavel_completa('comprimento_alimentador', globals())
            cabos_paralelos_alimentador = verificar_variavel_completa('cabos_paralelos_alimentador', globals())
            potencia = verificar_variavel_completa('potencia', globals())
            tensao_secundaria_base = verificar_variavel_completa('tensao_secundaria_base', globals())
            impedancia_alimentador_positiva,impedancia_alimentador_zero = executar_funcao_com_validacao(impedancia_alimentadores,comprimento_alimentador, cabos_paralelos_alimentador, potencia, tensao_secundaria_base)

            impedancia_alimentador_positiva = verificar_variavel_completa('impedancia_alimentador_positiva', globals())
            impedancia_acumulada_positiva_trecho_02 = verificar_variavel_completa('impedancia_acumulada_positiva_trecho_02', globals())
            impedancia_acumulada_positiva_trecho_03 = executar_funcao_com_validacao(impedancia_acumulada_positiva, impedancia_alimentador_positiva, impedancia_acumulada_positiva_trecho_02)
            imprimir_resultado(impedancia_acumulada_positiva_trecho_03)

            impedancia_alimentador_zero = verificar_variavel_completa('impedancia_alimentador_zero', globals())
            impedancia_acumulada_zero_trecho_01 = verificar_variavel_completa('impedancia_acumulada_positiva_trecho_01', globals())
            impedancia_acumulada_zero_trecho_02 = executar_funcao_com_validacao(impedancia_acumulada_zero, impedancia_alimentador_zero, impedancia_acumulada_zero_trecho_01)
            imprimir_resultado(impedancia_acumulada_zero_trecho_02)
        
        elif escolha == "10":

            largura, espessura,comprimento_bar, quant_bar_por_fase = definir_barramento()
            largura = verificar_variavel_completa('largura', globals())
            espessura = verificar_variavel_completa('espessura', globals())
            comprimento_bar = verificar_variavel_completa('comprimento_bar', globals())
            quant_bar_por_fase = verificar_variavel_completa('quant_bar_por_fase', globals())

            impedancia_barramento_modelado = executar_funcao_com_validacao(impedancia_barramento, largura, espessura, comprimento_bar, quant_bar_por_fase, potencia, tensao_secundaria_base)
            imprimir_resultado(impedancia_barramento_modelado)

            impedancia_barramento_modelado = verificar_variavel_completa('impedancia_barramento_modelado', globals())
            impedancia_acumulada_positiva_trecho_03 = verificar_variavel_completa('impedancia_acumulada_positiva_trecho_03', globals())

            impedancia_acumulada_positiva_trecho_04 = executar_funcao_com_validacao(impedancia_acumulada_positiva, impedancia_barramento_modelado, impedancia_acumulada_positiva_trecho_03)
            imprimir_resultado(impedancia_acumulada_positiva_trecho_04)
        
        elif escolha == "11": 

            impedancia_acumulada_positiva_trecho_04 = verificar_variavel_completa('impedancia_acumulada_positiva_trecho_04', globals())
            corrente_base_secundaria = verificar_variavel_completa('corrente_base_secundaria', globals())
            curto_simetrico_barramento = executar_funcao_com_validacao(corrente_curto_trifasica_simetrica, impedancia_acumulada_positiva_trecho_04, corrente_base_secundaria) # ICC TRIFÁSICO
            imprimir_resultado(curto_simetrico_barramento)

            impedancia_reduzida_zero = verificar_variavel_completa('impedancia_reduzida_zero', globals())
            impedancia_condutores_zero = verificar_variavel_completa('impedancia_condutores_zero', globals())
            trafo_escolhido = verificar_variavel_completa('trafo_escolhido', globals())
            curto_monofasico_barramento = executar_funcao_com_validacao(corrente_curto_monofasica, impedancia_acumulada_positiva_trecho_04, impedancia_reduzida_zero + impedancia_condutores_zero, trafo_escolhido, corrente_base_secundaria)
            imprimir_resultado(curto_monofasico_barramento)
        
        elif escolha == "12":

            comprimento_circuito_QGF_CCM3, cabos_paralelos_QGF_CCM3 = definir_alimentador()
            comprimento_circuito_QGF_CCM3 = verificar_variavel_completa('comprimento_circuito_QGF_CCM3', globals())
            cabos_paralelos_QGF_CCM3 = verificar_variavel_completa('cabos_paralelos_QGF_CCM3', globals())

            impedancia_circuito_QGF_CCM3_positiva, impedancia_circuito_QGF_CCM3_zero = executar_funcao_com_validacao(impedancia_alimentadores, comprimento_circuito_QGF_CCM3, cabos_paralelos_QGF_CCM3, potencia, tensao_secundaria_base)
            impedancia_circuito_QGF_CCM3_positiva = verificar_variavel_completa('impedancia_circuito_QGF_CCM3_positiva', globals())
            impedancia_acumulada_positiva_trecho_05 = executar_funcao_com_validacao(impedancia_acumulada_positiva, impedancia_circuito_QGF_CCM3_positiva, impedancia_acumulada_positiva_trecho_04)
            imprimir_resultado(impedancia_circuito_QGF_CCM3_positiva)

            impedancia_circuito_QGF_CCM3_zero = verificar_variavel_completa('impedancia_circuito_QGF_CCM3_zero', globals())
            impedancia_acumulada_zero_trecho_02 = verificar_variavel_completa('impedancia_acumulada_zero_trecho_02', globals())
            impedancia_acumulada_zero_trecho_03 = executar_funcao_com_validacao(impedancia_acumulada_zero, impedancia_circuito_QGF_CCM3_zero, impedancia_acumulada_zero_trecho_02)
            imprimir_resultado(impedancia_circuito_QGF_CCM3_zero)
        
        elif escolha == "13":

            impedancia_acumulada_positiva_trecho_05 = verificar_variavel_completa('impedancia_acumulada_positiva_trecho_05', globals())
            corrente_base_secundaria = verificar_variavel_completa('corrente_base_secundaria', globals())
            curto_no_ccm = executar_funcao_com_validacao(corrente_curto_trifasica_simetrica, impedancia_acumulada_positiva_trecho_05, corrente_base_secundaria) # ICC TRIFÁSICO
            imprimir_resultado(curto_no_ccm)
        
        elif escolha == "14":

            real, imag = extrair_impedancia(impedancia_acumulada_positiva_trecho_05)

            real = verificar_variavel_completa('real', globals())
            imag = verificar_variavel_completa('imag', globals())
            curto_no_ccm = verificar_variavel_completa('curto_no_ccm', globals())
            curto_assimetrico = executar_funcao_com_validacao(curto_assimétrico, real, imag, curto_no_ccm)
            imprimir_resultado(curto_assimetrico)
        
        elif escolha == "15":

            curto_assimetrico = verificar_variavel_completa('curto_assimetrico', globals())
            impulso = executar_funcao_com_validacao(impulso_da_corrente_de_curto_circuito, curto_assimetrico)
            imprimir_resultado(impulso)
        
        elif escolha == "16":

            curto_assimetrico = verificar_variavel_completa('curto_assimetrico', globals())
            curto_bif = executar_funcao_com_validacao(curto_bifasico, curto_assimetrico)
            imprimir_resultado(curto_bif)
        
        elif escolha == "17":

            impedancia_acumulada_positiva_trecho_05 = verificar_variavel_completa('impedancia_acumulada_positiva_trecho_05', globals())
            impedancia_acumulada_zero_trecho_03 = verificar_variavel_completa('impedancia_acumulada_zero_trecho_03')
            trafo_escolhido = verificar_variavel_completa('trafo_escolhido', globals())
            corrente_base_secundaria = verificar_variavel_completa('corrente_base_secundaria', globals())
 
            mono_max = executar_funcao_com_validacao(corrente_curto_monofasica, impedancia_acumulada_positiva_trecho_05, impedancia_acumulada_zero_trecho_03, trafo_escolhido, corrente_base_secundaria) # ICC MONO MÁX
            imprimir_resultado(mono_max)
            
        
        elif escolha == "18":

            re_contato, re_malha, re_resistor = resistencias_aterramento()

            re_contato = verificar_variavel_completa('re_contato', globals())
            re_malha = verificar_variavel_completa('re_malha', globals())
            re_resistor = verificar_variavel_completa('re_resistor', globals())

            re_contato_pu = conversao_fisico_pu(re_contato, impedancia_base_secundaria)
            re_malha_pu = conversao_fisico_pu(re_malha, impedancia_base_secundaria)
            re_resistor_pu = conversao_fisico_pu(re_resistor, impedancia_base_secundaria)

            re_contato_pu = verificar_variavel_completa('re_contato_pu', globals())
            re_malha_pu = verificar_variavel_completa('re_malha_pu', globals())
            re_resistor_pu = verificar_variavel_completa('re_resistor_pu', globals())

            impedancia_acumulada_positiva_trecho_05 = verificar_variavel_completa('impedancia_acumulada_positiva_trecho_05', globals())
            impedancia_acumulada_zero_trecho_03 = verificar_variavel_completa('impedancia_acumulada_zero_trecho_03')
            impedancia_trafo_zero = verificar_variavel_completa('impedancia_trafo_zero', globals())
            corrente_base_secundaria = verificar_variavel_completa('corrente_base_secundaria', globals())

            curto_minimo = executar_funcao_com_validacao(corrente_curto_monofasica_minima, impedancia_acumulada_positiva_trecho_05, impedancia_acumulada_zero_trecho_03, impedancia_trafo_zero, corrente_base_secundaria, re_contato_pu, re_malha_pu, re_resistor_pu)
            imprimir_resultado(curto_minimo)

        elif escolha == "0":
            break

        else:
            print('Opção inválida')
