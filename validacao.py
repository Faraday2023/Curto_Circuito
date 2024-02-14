# FUNÇÕES PARA VALIDAÇÃO DE DADOS

import re, inspect

def validar_valor_float(valor):
    while True:
        try:
            # Convertendo a entrada para float
            valor = str(valor)
            valor_float = float(valor.replace(',','.'))
            # Verificação de valores não negativos
            if valor_float < 0:
                raise ValueError("Erro: O valor não pode ser negativo.")
            return valor_float
        except ValueError:
            print("Erro: Por favor, insira um valor válido de número.")
            # Se a entrada não for um número ou for negativa, solicita ao usuário que insira novamente
            valor = input('Digite novamente: ').strip()
        except Exception as e:
            print(f"Erro inesperado: {e}")
        except KeyboardInterrupt:
            print("\nPrograma encerrado pelo usuário.")
            return None
        
def validar_valor_inteiro(valor):
    while True:
        try:
            # Convertendo a entrada para inteiro
            valor_inteiro = int(valor)
            # Verificando se o valor convertido tem no máximo 6 dígitos
            if len(str(valor_inteiro)) <= 12:
                return valor_inteiro
            else:
                print('Erro: Por favor, insira um número de até 6 dígitos.')
                # Se o valor tiver mais de 6 dígitos, solicita ao usuário para inserir novamente
                valor = input('Digite novamente: ').strip()
        except ValueError:
            print("Erro: Por favor, insira um valor válido de número inteiro.")
            # Se a entrada não puder ser convertida para inteiro, solicita ao usuário para inserir novamente
            valor = input('Digite novamente: ').strip()
        except Exception as e:
            print(f"Erro inesperado: {e}")
        except KeyboardInterrupt:
            print("\nPrograma encerrado pelo usuário.")
            return None

def verificar_varios_argumentos(*args, passo):
    
    '''Mais genérica: Esta abordagem permite lidar com um número variável de argumentos sem precisar listar explicitamente todos eles na chamada da função.
Menos explícita: A chamada da função não indica diretamente quais argumentos estão sendo verificados, o que pode tornar menos claro para alguém lendo o código pela primeira vez.'''

    f_frame = inspect.currentframe().f_back
    f_args = inspect.getargvalues(f_frame).args
    argumentos_faltando = []
    for arg_name in f_args:
        arg_value = f_frame.f_locals[arg_name]
        if arg_value is None:
            argumentos_faltando.append(arg_name)
    if argumentos_faltando:
        print("Erro: Os seguintes argumentos não foram fornecidos:")
        for arg_name in argumentos_faltando:
            print(f"- '{arg_name}'")
        print(f"Por favor, volte ao passo n° {passo} e forneça os argumentos indicados.")
        return False
    return True

def verificar_argumentos_explicitos(valor, nome_argumento, passo):

    '''Mais explícita: Ao listar explicitamente os argumentos na chamada da função verificar_argumento, fica claro para quem lê o código quais argumentos estão sendo verificados.
Menos flexível: Se você adicionar ou remover argumentos na função, precisará atualizar a chamada da função verificar_argumento manualmente.'''

    f_frame = inspect.currentframe().f_back
    f_args = inspect.getargvalues(f_frame).args
    argumentos_faltando = []
    for arg_name in f_args:
        arg_value = f_frame.f_locals[arg_name]
        if arg_value is None:
            argumentos_faltando.append(arg_name)
    if argumentos_faltando:
        print("Erro: Os seguintes argumentos não foram fornecidos:")
        for arg_name in argumentos_faltando:
            print(f"- '{arg_name}'")
        print(f"Por favor, volte ao passo n° {passo} e forneça os argumentos indicados.")
        return False
    return True

def executar_funcao_com_validacao(funcao):
    try:
        return funcao()
    except NameError as e:
        print(f"Erro: Uma variável não está definida. Detalhes: {e}")
        return None
def imprimir_resultado(resultado):
    if resultado is not None:
        print(resultado)

def executar_variavel_com_validacao(variavel):
    try:
        if not variavel:
            print("Erro: A variável está vazia.")
            return None
        return variavel
    except NameError as e:
        print(f"Erro: A variável não está definida. Detalhes: {e}")
        return None
