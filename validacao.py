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

def verificar_argumentos_explicitos(valor, nome_argumento):

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
        return False
    return True

def imprimir_resultado(resultado):
    if resultado is not None:
        print('-'*100)
        print(resultado)

def executar_funcao_com_validacao(funcao, *args, **kwargs):
    try:
        return funcao(*args, **kwargs)
    except NameError as e:
        print(f"Erro: Uma variável não está definida. Detalhes: {e}")
        return None
    except TypeError as e:
        print(f"Erro: Tipo de argumento inválido para a função. Detalhes: {e}")
        return None
    except Exception as e:
        print(f"Erro: {e}")
        return None

# Verifica se a variável está vazia
def executar_variavel_com_validacao(variavel):
    try:
        if not variavel:
            print("Erro: A variável está vazia.")
            return None
        return variavel
    except NameError as e:
        print(f"Erro: A variável não está definida. Detalhes: {e}")
        return None
    
# Verifica se a variável está declarada
def verificar_variavel(variavel):
    if variavel in globals():
        return globals()[variavel]
    else:
        print(f"Erro: Variável '{variavel}' não está definida.")
        return None
    
# Verifica se a variável está declarada e vazia
def verificar_variavel_completa(variavel, global_vars):
    '''globals_copy = global_vars.copy()
    for var_name, var_value in globals_copy.items():
        print(f"Variável '{var_name}': {var_value}")'''

    if variavel in global_vars:
        valor = global_vars[variavel]
        #print(f'O valor é: {valor}')
        if valor:
            return valor
        else:
            print(f"Erro: Variável '{variavel}' está definida, mas está vazia.")
            return None
    else:
        print('O problema está aqui')
        print(f"Erro: Variável '{variavel}' não está definida.")
        return None

'''def verificar_variavel_completa(variavel):
    if variavel is None:
        print(f"Erro: Variável '{variavel}' não está definida.")
        return None
    
    if variavel:
        return variavel
    else:
        print(f"Erro: Variável '{variavel}' está definida, mas está vazia.")
        return None'''

# Função para verificar dependências
def verificar_dependencias(escolha, opcoes_escolhidas):

    dependencias = {

    "0": [], # Não depende de outras escolhas
    "1": [],  # Não depende de outras escolhas
    "2": [],  # Não depende de outras escolhas
    "3":["1", "2"], # Opção 3 depende da opção 1 e 2
    "4":["1", "2"], # Opção 4 depende da opção 1 e 2
    "5": ["1"], # Opção 5 depende da opção 1
    "6": ["1"], # Opção 6 depende da opção 1
    "7": ["1", "2","6"], # Opção 7 depende de 1,2 e 6
    "8": ["1", "2", "6", "7"], # Opção 8 depende da 1,2,6 e 7
    "9": ["1", "2", "7"], # Opção 9 depende da 1,2,7
   "10": ["1", "9"], # Opção 10 depende da 1 e 9
   "11": ["1", "2", "10"], # Opção 11 depende da 1,2 e 10
   "12": ["1", "9", "10"], # Opção 12 depende da 1, 9 e 10
   "13": ["1", "12"], # Opção 13 depende da 1 e 12
   "14": ["12", "13"], # Opção 14 depende da 12 e 13
   "15": ["14"], # Opção 15 depende da 14
   "16": ["14"], # Opção 16 depende da 14
   "17": ["1", "6","12"], # Opção 1, 6 e 12
   "18": ["1", "6","12"] # Opção 1, 6 e 12
}
    
    dependencias_nao_atendidas = []
    for dependencia in dependencias[escolha]:
        if dependencia not in opcoes_escolhidas:
            dependencias_nao_atendidas.append(dependencia)
    if dependencias_nao_atendidas:
        return dependencias_nao_atendidas
    return None
