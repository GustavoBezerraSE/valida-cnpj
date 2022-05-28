import re
"""
Essa função remove os caracteres diferente de numeros e gera um novo cnpj
sem os ultimos dois números
"""
def remover_caracteres(cnpj):
    cnpj = cnpj[:-2]                            #remove os ultimo dois digitos
    novo_cnpj = re.sub(r'[^ 0-9]', '', cnpj)    #remove os . - / (tudo que é diferente de 0,1,2,3,4,5,6,7,8,9)
    return novo_cnpj

"""
Essa função faz a soma da multiplicação de cada numero do cnpj pelo respectivo
número da lista (lista1 para o primeiro digito) e (lista 2 para o segundo digito)
"""
def contador_soma(novo_cnpj):
    total = 0
    if len(novo_cnpj) <= 12:                                #verifica se está somando para o primeiro digito
        lista1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        for i in range(len(novo_cnpj)):
            total += int(novo_cnpj[i])*lista1[i]
    else:                                                   #verifica se está somando para o segundo digito
        lista2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        for i in range(len(novo_cnpj)):
            total += int(novo_cnpj[i]) * lista2[i]
    return total

"""
Essa função receberá o retorno da função contador_soma e realizará o calculo da fórmula
para definir qual será o digito a ser retornado 
"""
def calcula_digitos(contador):
    x = 11 - (contador % 11)
    if x <= 9:                  #se o resultado for <= 9 deve ser retornado o resultado da formula
        digito = x
        return digito
    else:                       #se for maior que 9 deve retornar 0
        digito = 0
        return digito
"""
Aqui formara um novo cnpj já com os digitos calculados
"""
def add_digitos(cnpj):
    novo_cnpj = remover_caracteres(cnpj)             # cnpj sem caracteres e sem os dois ultimos digitos
    x = calcula_digitos(contador_soma(novo_cnpj))    # primeiro digito
    novo_cnpj = novo_cnpj + str(x)                   # cnpj com o penultimo digito
    x = calcula_digitos(contador_soma(novo_cnpj))
    novo_cnpj = novo_cnpj + str(x)                   # cnpj com o ultimo digito
    return novo_cnpj

def valida(cnpj_do_input):
    # esssa linha se refere ao cnpj que o usuario colocou sem os caracteres diferentes de numeros
    cnpj_do_input = re.sub(r'[^ 0-9]', '', cnpj_do_input)
    #aqui será comparado o cnpj que o usuário colocou com o cnpj que foi calculado
    if cnpj_do_input == add_digitos(cnpj_do_input):
        return True
    else:
        return False
