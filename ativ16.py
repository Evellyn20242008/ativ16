# Crie um programa que receba o peso e a altura de uma pessoa e calcule o Índice de Massa Corporal (IMC). O programa deve classificar o IMC da pessoa de acordo com a tabela a seguir:
# Abaixo do peso: IMC < 18.5
# Peso normal: 18.5 ≤ IMC < 25
# Sobrepeso: 25 ≤ IMC < 30
# Obesidade: IMC ≥ 30

peso = float(input("digite o peso em KG"))
altura = float(input("digite a altura em M"))

# calcule o IMC

IMC = (peso / altura) * altura 
print(IMC)

# verificar se esta com IMC ideal 

if IMC  < 18.5:
print ("voce esta abaixo do peso")
elif 18.5 <= IMC <25:
  print("voce esta com o peso normal")
elif 25 <= IMC <30:
  print("voce esta sobrepeso")
elif IMC >=30:
  print("voce esta com obsidade")