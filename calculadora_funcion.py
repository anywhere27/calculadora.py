import sys

n1 = 0
n2 = 0

menu = """
1.- Sumar
2.- Restar
3.- Multiplicar
4.- Dividir
5.- Potencia
6.- Raiz
7.- Salir
"""
def Sumar():
   print("Ingresa la cantidad que quieres sumar: ")
   n1 = float(input())
   print("ingresa la segunda cantidad: ")
   n2 = float(input())
   print("el resultado es: ", n1 + n2)
   
def Restar():
   print("ingresa una cantidad: ")
   n1 = float(input())
   print("menos: ")
   n2 = float (input())
   print("el resultado de la Resta es: ", n1 - n2)
   
def Multiplicar():
   print("ingresa una cantidad: ")
   n1 = float(input())
   print("Multiplicado por: ")
   n2 = float(input())
   print("Es igual a: ", n1 * n2 )
   
def Dividir():
   print("ingresa un número: ")
   n1 = float(input())
   print("Dividido entre: ")
   n2 = float(input())
   print("La division es igual a: ", n1 / n2)
   
def Potencia():
   print("ingresa la base: ")
   n1 = float(input())
   print("ingresa el exponente: ")
   n2 = float(input())
   print("El resultado es: ", n1 ** n2)
   
def Raiz():
   print("Ingresa el radicando: ")
   n1 = float(input())
   print("ingresa el Indice: ")
   n2 = float(input())
   print("El resultado es: ", n1 ** (1/n2))
    
print("Ésta es tu primer calculadora con python")
print("Bienvenida")

while True:
   print (menu)
   opcion = int(input())
   if opcion == 1:
      Sumar()
   elif opcion == 2:
      Restar()
   elif opcion == 3:
      Multiplicar()
   elif opcion ==4:
      Dividir()
   elif opcion ==5:
      Potencia()
   elif opcion==6:
      Raiz()
   elif opcion==7:
      sys.exit()
      



print(menu)