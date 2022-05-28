from cnpj import valida, remover_caracteres, contador_soma, calcula_digitos
#importação do modulo criado com as funções
from time import sleep

while True:  #looping infinito
    cnpj = input("Digite um CNPJ: ")
    while len(cnpj) != 18:
        print("CNPJ deve conter todos os pontos (.) traços (-) e barras (/)")
        print("Ou ser menor que 18 caracteres!")
        cnpj = input("Digite um CNPJ: ")

    print("VALIDANDO:")

    x = 0
    for numero in cnpj:
        if x == 17:
            print(f"{numero} validação completa!", end="")
        else:
            print(f"{numero} ", end="")
        x += 1
        sleep(0.25)

    print()

    if valida(cnpj):
        print("CNPJ é válido!!!")
    else:
        print("CNPJ é inválido tente novamente!")