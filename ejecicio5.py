#Función ValidarFecha: Recibe un día, mes y año correspondiente a una fecha y devuelve si la fecha es correcta o no. Simplemente miramos si el día indicado es mayor que 1 y menor que los días del mes. Si introducimos un mes incorrecto, la función DiasDelMes devuelve 0 por lo tanto la fecha va a ser incorrecta. Parámetros de entrada: día, mes y año
#Dato devuelto: Valor lógico indicando si es correcta (Verdadero) o no (Falso)




Mesdelaño = { 1:"Enero", 2:"Febrero", 3:"Marzo", 4:"Abril", 5:"Mayo", 6:"Junio", 7:"Julio", 8:"Agosto", 9:"Septiembre", 10:"Octubre", 11:"Noviembre", 12:"Diciembre"}

def Anio (A):
   if A%4 == 0:
      Diamax = 29 
      return Diamax
   else:
      Diamax = 28
      return Diamax
   
def ValidarFecha (D,Diamax,M,A):
   if (M >=1 and M <=12):
      if (D <=Diamax) and (M==2):
         print("\t Fecha: ", D, "de", Mesdelaño[M], "del año",A)
      elif (D <= 30) and (M==4 or M==6 or M==9 or M==11):
         print("\t Fecha: ", D, "de", Mesdelaño[M], "del año",A)
      elif (D <= 31 and (M != 2)):
         print("\t Fecha: ", D,"de",Mesdelaño[M],"del año",A)
      else:
         print ("ERROR, FECHA INVALIDA")
   else:
      print("ERROR, FECHA INVALIDA")
   
   
while True:
   print("\n INTRUDUZCA UNA FECHA")
   D = int(input("Dia: "))
   M = int(input("mes: "))
   A = int(input("Año: "))
   Diamax = Anio(A) 
   ValidarFecha(D,Diamax,M,A)
   
   print ("\n ¿desea introducir otra fecha?")
   
   Op = input(" S = Sí / N = No ")
   if Op == 'S' or Op == 's':
      pass
   else:
      break
   
   print("!\n FIN") 