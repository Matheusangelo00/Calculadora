from time import sleep

print(40*"=")
print("Bem vindo ao meu primeiro projeto...")
print(40*"=")

nome = input("Digite seu nome:")
print("Iniciando calculadora...")
sleep(3)

print(f"E aí {nome} vamos começar? ")

continua = "s"
while(continua =="s"):
    num1 = float(input("Digite o primeiro número:"))
    op = input("Digite a operação (+, -, *, /):")
    num2 = float(input("Digite o segundo número:"))

    if(op == "+"):
        resultado = num1 + num2
    elif(op == "-"):
        resultado = num1 - num2
    elif(op == "*"):
        resultado = num1 * num2
    elif(op == "/"):
        resultado = num1 / num2
    else:
        resultado = 0

    print(f"Resultado: {resultado}")

    continua = input("Deseja continuar? (s/n):")         
               