pares = 0
impares = 0

while True:
    try:
        entrada = input("Digite um número inteiro ou 'sair' para encerrar: ")
        
        if entrada.lower() == 'sair':
            break
        numero = int(entrada)
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    except ValueError:
        print("Por favor, insira um número inteiro.")