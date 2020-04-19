num = c = soma = menor = maior = cont = quant = 0
while c < 11:
num=int(input('digite o valor {} : '.format(c)))
c += 1
cont += 1
quant += 1
if quant == 1:
maior = menor = num
else:
if num > maior:
maior = num
if num < menor:
menor = num
print('o valor {} é o menor de todos informados'.format(menor))
