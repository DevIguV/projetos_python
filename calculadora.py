def quadrado (numero):
    resultado = numero ** 2
    return resultado

while True:
    print("\nCalculadora para elevar um numero ao quadrado:")
    print("Insira 1 para calcular o quadrado de um numero")
    print("Insira 2 para sair da aplicação")
    escolha = input ("Digite sua opção:")
    resultado_quadrado = quadrado(int (input("O quadrado de ")))
    print("Resultado é =", resultado_quadrado)
    if escolha == "1":
        resultado_quadrado == ""
    elif escolha == "2":
        break
print("Programa finalizado!!")
        
        
