numero = int(input("Digite um número para caucularmos o fatorial: "))

fatorial = 1

for n in range(1, numero + 1):
    fatorial *= n

print(f'O fatorial do número: {numero}!, é: {fatorial}.')