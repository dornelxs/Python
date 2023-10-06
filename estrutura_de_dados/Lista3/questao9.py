def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Divisão por zero não é permitida."

print("Escolha a operação:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

opcao = input("Digite o número da operação desejada: ")

if opcao in ('1', '2', '3', '4'):
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    if opcao == '1':
        print(f"Resultado: {adicao(num1, num2)}")
    elif opcao == '2':
        print(f"Resultado: {subtracao(num1, num2)}")
    elif opcao == '3':
        print(f"Resultado: {multiplicacao(num1, num2)}")
    elif opcao == '4':
        print(f"Resultado: {divisao(num1, num2)}")
else:
    print("Opção inválida.")