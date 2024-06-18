import math

cat1 = float(input('digite o valor do primeiro cateto: '))
cat2 = float(input('digite o valor do segundo cateto: '))

hip = math.pow(cat1,2) + math.pow(cat2,2)
print('a hipotenusa é {:.2f} cm'.format(math.sqrt(hip)))

#math.hypot(co,ca) = hipotenusa