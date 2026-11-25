#nombre = input("Ingrese el nombre del producto: ")
#cantidad = int(input("Ingrese la cantidad del producto: "))
#precio = int(input("Ingrese el precio del producto: "))

#resultado = cantidad * precio
#print(f"El total de {cantidad} {nombre} es: {resultado}") 

#while True:
    #nota = float(input("Ingrese la nota: "))
    #if nota < 1.0:
        #print("La nota no es valida, vuelva a ingresarla")
    #elif nota > 7.0:
        #print("La nota no es valida, vuelva a ingresarla")
    #else:
        #if nota >= 4.0:
            #print("Aprobaste!")
            #break
        #else:
            #print("Reprobaste!")
            #break


#temp = ["18", "22", "25", "30", "17", "21", "28"]

#for days in temp:
    #if int(days) >= 25:
        #print(days)
    #else:
        #print("No es mayor a 25")


#import random

#ent = random.randint(1, 5)

#while True:
    #num = int(input("Ingrese un numero del One al V:"))
    #if num < 1: #Si
        #print("El numero no es valido w, vuelve a ingresarlo p")
    #elif num > 5: #SI NO, SI
    #    print("El numero no es valido w, vuelve a ingresarlo p")
    #else: #SINO
    #    if num == ent:
            #print(f"Haz ganado el numero era {ent}")
            #break
        #elif num > ent:
            #print("El numero en menor, intentalo otra vez")
        #else:
            #print("El numero es mayor, intentalo otra vez")



name = input("Ingresa tu nombre: ")

while True: #bucle
    try: #Prueba antes de enviarlo a la consola
        age = int(input("Ingrese su edad: "))
    except ValueError: #Agarra el error en este caso un error de valor(ValueError)
        print("El valor que ingreso es incorrecto, vuelva a ingresarlo")
    else:
        print(f"Su nombre es {name} y su edad {age}")
        break