# CÓDIGO DO MÓDULO 1

from funcionalidades import valores_base, obter_impedancia, corrente_curto_trifasica_simetrica,corrente_curto_monofasica
from funcionalidades import potencia_de_curto_circuito

corrente_base = valores_base() # CORRENTE BASE DO SISTEMA

# IMPEDÂNCIAS 
impedancia_reduzida_positiva = obter_impedancia() # IMPEDÂNCIA DE SEQUÊNCIA POSITIVA REDUZIDA DO SISTEMA
'''impedancia_reduzida_negativa = obter_impedancia() # IMPEDÂNCIA DE SEQUÊNCIA POSITIVA REDUZIDA DO SISTEMA
impedancia_reduzida_zero = obter_impedancia() # IMPEDÂNCIA DE SEQUÊNCIA ZERO REDUZIDA DO SISTEMA
impedancia_trafo_zero = obter_impedancia() # IMPEDÂNCIA DE SEQUÊNCIA ZERO DO TRANSFORMADOR
impedancia_condutores_zero = obter_impedancia() # IMPEDÂNCIA DE SEQUÊNCIA ZERO DOS CONDUTORES'''

# CALCULANDO CURTO-CIRCUITO
#tri = corrente_curto_trifasica_simetrica(impedancia_reduzida_positiva) # ICC TRIFÁSICO
#print(tri)
#mono = corrente_curto_monofásica(impedancia_reduzida_zero, impedancia_condutores_zero, impedancia_trafo_zero) # ICC MONO MÁX
pot_cc = potencia_de_curto_circuito() # POTÊNCIA DE CURTO-CIRCUITO
