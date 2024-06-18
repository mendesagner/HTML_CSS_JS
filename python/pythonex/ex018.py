import math

ang = float(input('Digite um angulo: '))
angr = math.radians(ang)

sen = math.sin(angr) 
cos = math.cos(angr) 
tan = math.tan(angr) 

print('{}° tem seno de {:.5f}°, cosseno de {:.5f}° e tangente {:.5f}°'.format(ang,sen,cos,tan))

#print(math.cos(ang))
#print(angr)