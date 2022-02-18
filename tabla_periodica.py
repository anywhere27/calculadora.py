
from re import A
from sqlalchemy import false


Elementos = ["H","P","Na","O","Li","C","Br","Cl","Mg","Rb","Ti","Al","Sr","Te","He","Kr","Xe","I","Ga","V"]


def Orden(arreglo):
   
      for i in range(len(arreglo)):
         least = i
         for k in range(i+1, len(arreglo)):
            if arreglo[k] < arreglo[least]:
               least = k  
         
         temp = arreglo[least]
         arreglo[least] = arreglo[i]
         arreglo[i] = temp
        
            
         #swap(arreglo, least, i)      
         
#def swap(A, x, y):             
         # temp = A[x]
         # A[x] = A[y]
         # A[y] = temp         

Num_Atomico = [1, 15, 11, 8, 3, 6, 35, 17, 12, 37, 81, 13, 38, 52, 2, 36, 54, 53, 31, 23]

Orden(Num_Atomico)
print (Num_Atomico)


