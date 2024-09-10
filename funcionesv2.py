print("mas sobre funciones")
#Aqui se esvriben las funciones
def suma_ab(a,b):
    s=a+b
    return s,

def resta_ab(a,b):
    n=a-b
    return n,

def multi_ab(a,b):
    r=a*b
    return r,

def div_ab(a,b):
    d=a/b
    return d,

#Llamadas a funciones
n1=int(input("Ingresa el primer numero"))
n2=int(input("ingresa el segundo numero"))
suma=suma_ab(n1,n2)
resta=resta_ab(n1,n2)
div=div_ab(n1,n2)
multi=multi_ab(n1,n2)
print(f"la suma de {n1} + {n2} es {suma}")
print(f"la resta de {n1} - {n2} es {resta}")
print(f"la division de {n1} / {n2} es {div}")
print(f"la multiplicacion de {n1} * {n2} es {multi}")
