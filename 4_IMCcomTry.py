try:

  for c in range(1, 11):

    print('\n\n{} Pessoa'.format(c))

    peso = float(input('Digite o Peso: '))
    altura = float(input('Digite a  em Metros: '))

  imc = peso / altura**2
  print("Seu IMC é: %.4f" % imc)
  if imc < 18.5:
    print("Abaixo do peso")
  elif imc < 24:
   print("Peso normal")
  elif imc < 25:
    print("Saudável")
  elif imc < 30:
   print("Sobrepeso")
  elif imc < 35:
   print("Obesidade Grau I")
  elif imc < 40:
   print("Obesidade Grau II (severa)")
  else:
   print("Obesidade Grau III (mórbida)")

except ValueError:
  print('\n\n Digite apenas números!')

input('Tecle ENTER para sair...')
