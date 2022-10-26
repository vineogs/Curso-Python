from math import radians, sin, cos, tan
angulo = float(input("Informe o ângulo: "))
seno = sin(radians(angulo))
coseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print("o seno de {} é {:.2f}, o cosseno {:.2f} e a tangente {:.2f}".format(angulo, seno, coseno, tangente))
