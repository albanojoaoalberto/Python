import math

a=int(input("Digite o Valor de A? "));
b=int(input("Digite o Valor de B? "));
c=int(input("Digite o Valor de C? "));

delta = math.pow(b,2)- 4*a-c;

print("Valor de Delta é ", delta);
print("Raiz de ",delta," é ", math.sqrt(delta));

x1 = -(b + (math.Sqrt(delta) ))/ (2 * a);
x2 = -(b - (math.Sqrt(delta) ))/ (2 * a);

print("X1 = ",x1);
print("X2 = ",x2);