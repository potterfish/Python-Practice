# 1. Criar três variáveis: nome (texto), idade (número) e altura (número decimal) 
# capturadas pelo input(). Depois, imprimir essas informações formatadas. 
# nome: str = input("Qual o seu nome? ")
# idade: int = int(input("Qual a sua idade? "))
# altura = float(input("Qual a sua altura? "))
# print(f"seu nome é {nome}, você tem {idade} anos e sua altura é {altura:.3}m")

# 2. Solicitar dois números, exibir a soma, subtração, multiplicação e divisão entre 
# eles. (Não é necessário tratar erros por enquanto)
# numero1= float(input("Digite um número: "))
# numero2= float(input("Digite outro número: "))
# soma= numero1 + numero2
# subtracao= numero1 - numero2
# multiplicacao= numero1 * numero2
# divisao= numero1 / numero2
# print(f'A soma é {soma}, a subtração é {subtracao}, a multiplicação é {multiplicacao} e n\
# a divisão é {divisao:.2f}')

# 3. Solicitar um número para exibir o dobro, o triplo e a raiz quadrada dele.
# numero= float(input("Digite um número: "))
# dobro= numero * 2
# triplo= numero * 3
# raiz= numero ** (1/2)
# print(f"O dobro é {dobro}, o triplo é {triplo} e a raiz quadrada é {raiz:.2f}")

# 4. Solicitar dois números e mostrar a média aritmética entre eles.
# numero1= float(input("Digite um número: "))
# numero2= float(input("Digite outro número: "))
# media= (numero1 + numero2) / 2
# print(f"A média entre {numero1} e {numero2} é {media}")

# 5. Solicitar a quantidade de quilômetros percorridos e o tempo gasto em minutos 
# (distância / tempo).
km= float(input("Quantos quilômetros foram percorridos? "))
minutos= float(input("Quantos minutos foram gastos? "))
tempo= minutos / 60
velocidade= km / tempo
print(f"A velocidade média foi de {velocidade:.3f} km/h")

