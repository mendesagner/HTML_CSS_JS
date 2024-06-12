dias = int(input('quantos dias alugados?'))
km = float(input('quantos KM rodados ?'))

preco = (dias * 60) + (km * 0.15)
print('o preço a pagar é de R${}'.format(preco))