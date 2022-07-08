#Defino las variables
selector = input("Elija una operacion (Cualquier otra opcion lo sacara del programa): a)Suma b)Resta c)Multiplicacion d)Division: ")
n1 = int(input("Ingrese un numero: "))
n2 = int(input("Ingrese otro numero: "))

def suma(n1, n2):
    print("La suma de los numeros es de", (n1 + n2))

def resta(n1, n2):
    print("La resta de los numeros es de", (n1 - n2))

def multiplicacion(n1, n2):
    print("La multiplicacion de los numeros es de", (n1 * n2))

def division(n1, n2):
    while n2 == 0:
        n2 = int(input("No se puede dividir por 0, ingrese otro numero"))

    print("La division de los numeros es de", (n1 / n2))

#La funcion Seleccion sera la que ejecute las funciones acorde a la seleccion del usuario
def seleccion(selector, n1, n2):
    while selector != 'salir' or selector != 'e':

        if selector == 'suma' or selector == 'a':
            return suma(n1, n2)
        elif selector == 'resta' or selector == 'b':
            return resta(n1, n2)
        elif selector == 'multiplicacion' or selector == 'c':
            return multiplicacion(n1, n2)
        elif selector == "division" or selector == 'd':
            return division(n1, n2)
        else:
            print("Ha salido del programa")
            break