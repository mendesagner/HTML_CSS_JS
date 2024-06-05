#faça um programa que leia um numero inteiro e mostre o seu antecessor e sucessor tbm
n1 = int(input("digite um numero: "))
print("{} < antecessor {} sucessor > {}".format(n1-1,n1,n1+1) )

#Crie um algoritimo que leia um numero e mostre seu dobro,triplo, e raiz quadrada
valor = int(input("digite um valor: "))
print("valor incial: {} \nseu dobro:{} \nseu triplo:{} \nsua raiz quarada:{} ".format(valor,valor*2,valor*3,valor**(1/2)))

#Desenvolva um programa que leia duas notas de um aluno e mostre sua media

nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))
print("media é: {}".format((nota1 + nota2)/2))


#Desenvolva um programa leia um volar em metros e converta seu valor para centimetros e milimetros
dis = float(input("digite um numero: "))
print("{} metros, {} centimetros e {} milimetros".format(dis,dis*100,dis*1000))


#faça um programa que leia um numero inteiro e mostre sua tabuada

tab= int(input("digite um numero: "))
print("tabuada de {}".format(tab))
print("{} x 0 = {}\n{} x 1 = {}\n{} x 2 = {}\n{} x 3 = {}\n{} x 4 = {}\n{} x 5 = {}\n{} x 6 = {}\n{} x 7 = {}\n{} x 8 = {}\n{} x 9 = {}\n{} x 10 = {}".format(tab,tab*0,tab,tab*1,tab,tab*2,tab,tab*3,tab,tab*4,tab,tab*5,tab,tab*6,tab,tab*7,tab,tab*8,tab,tab*9,tab,tab*10))

#Crie um programa que leia quantos reais tem em uma carteira e quantos dolares esta mesma pode comprar r$ 1.00 = $3.27

reais = float(input("digite  valor da carteira: "))
print("reais = {}\nDolares = {}".format(reais,reais*3.27))

#Faça um programa que leia a largura e a altura de uma parede em metros e calcule a sua área e a quantidade de tinta nescessaria para pinta-la, sabendo que cada litro de tinta cobre 2m^2.

lar = float(input("digite a largura: "))
alt = float(input("digite a altura "))
print("a area do espaço é {}".format(lar*alt))
print("litros de tinta necessarios {}".format((lar*alt)/2))

#faça um programa que mostre o desconto de um produto baseado no seu preço e subtraindo 5% do mesmo.

prod = float(input("digite o valor do produto: "))
print(" o valor do produto é {}, mas com desconto de 5 por cento fica {}".format(prod,prod - (prod*0.05)))

#faça um programa que leia um salário e depois com 15% de aumento

salario = float(input("digite o salario: "))
print(" o valor do salario é {}, mas com aumento de 15 por cento fica {}".format(salario,salario + (salario*0.15)))