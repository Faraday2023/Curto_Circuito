# FUNÇÕES PARA VALIDAÇÃO DE DADOS

import re

def validar_valor_float(valor):
    if not re.match(r'^-?\d*[\.,]?\d+$', valor):
        raise ValueError("Erro: Por favor, digite um valor válido de ponto flutuante.")
    valor = valor.replace(',', '.')  # Substituir vírgula por ponto, se presente
    return float(valor)
'''
def validar_valor_float(valor):
    try:
        valor_float = float(valor.replace(',', '.'))
        return valor_float
    except ValueError:
        raise ValueError("Erro: Por favor, digite um valor válido de ponto flutuante.")'''