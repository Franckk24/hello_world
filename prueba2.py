import math 
import random 

def suma_dos_valores (sumando1, sumando2):
    global resultado
    resultado = sumando1 + sumando2
    return resultado

#suma_dos_valores (4,5)
#print ("primera suma")
#print ( resultado )
#suma_dos_valores (1,2)
#print ("segunda suma")
#print ( resultado )
def calculadora_dos_valores (numero1 , numero2, operador):
    global resultado
    if operador == ("suma"): # si el operadores 1 es suma
        resultado = numero1 + numero2
        return resultado
    elif operador == ("resta"): # si el operador 2 es resta
        resultado = numero1 - numero2
        return resultado
    elif operador == ("multiplicacion"): # si el operador 3 es multiplicación
        resultado = numero1 * numero2
        return resultado
    elif operador == ("diviision"): # si el operador 4 es division
        if numero2 == 0:
            return "Error: División por cero"
        else:
            resultado = numero1 / numero2
            return resultado
#calculadora_dos_valores (1,2,"suma")
#print ("suma = ", resultado)
#calculadora_dos_valores (10,5,"resta")
#print ("resta = ", resultado)
#calculadora_dos_valores (10,5,"multiplicaion")
#print ("multiplicacion = ", resultado)
#calculadora_dos_valores (10,4,"division")
#print ("division = " ,resultado)


#def teorema_de_pitagoras (a,b):
    global c
    c = (a**2+b**2)**0.5
    return c

#teorema_de_pitagoras = (3,4)
#print ("teorema_de_pitagoras", c)


#def despeje_X():
    global x
    b = int (input ("ingrese el valor de B "))
    c = int (input ("ingrese el valor de C "))
    x = (c-b)/2
    print ("el valor de x es = ", x)
    return x

#despeje_X()

#def compuerta_and ():
    #global resultado
    a = bool (input ("ingrese el valor de A (True/False) "))
    b = bool (input ("ingrese el valor de B (True/False) "))
    c = bool (input ("ingrese el valor de C (True/False) "))
    #resultado = a and b and c
    #print ("resultado", resultado)
    #return resultado

#compuerta_and()

#def pitagoras_funcion_suma ():
    #global resul_pitagoras
    #a = int (input ("ingrese el valor de A "))
    #b = int (input ("ingrese el valor de B "))
    #a2 = a**2
    #b2 = b**2
    #suma = suma_dos_valores (a2,b2)
    #resul_pitagoras = suma**0.5
    #print ("el valor de la pitagoras es = ", resul_pitagoras)
    #return resul_pitagoras

#pitagoras_funcion_suma()

#def contador_letra ():
    global contador
    palabra = str(input ("ingrese una palabra "))
    letra = str(input ("ingrese la letra que quiere contar "))
    contador = palabra.count(letra)
    print ("la letra", letra, "aparece", contador, "veces en la palabra", palabra)
    x = len (palabra)
    print ("la longitud de la palabra es", x)
    s = list (palabra)
    print ("la lista de caracteres de la palabra es", s)
    return contador

#contador_letra()


#def juego_piedra_papel_tijera():
    #global resultado
    #jugador1 = random.choice(["piedra", "papel", "tijera"])
    #jugador2 = random.choice(["piedra", "papel", "tijera"])
    #if jugador1 == jugador2:
    #    resultado = "empate"
    #elif (jugador1 == "piedra" and jugador2 == "tijera") or (jugador1 == "papel" and jugador2 == "piedra") or (jugador1 == "tijera" and jugador2 == "papel"):
    #    resultado = "gana jugador 1"
    ##else:
    #    resultado = "gana jugador 2"
    #print ("el jugador 1 escogió", jugador1)
    #print ("el jugador 2 escogió", jugador2)
    #print ("El resultado es:", resultado)

#juego_piedra_papel_tijera ()


#def descubrir_contraseña():
    contraseña = "123456789"
    contraseña_ingresada = ""
    intento_ingresado = int(input("por favor ingrese un numero de intentos"))
    intento = 1
    while contraseña_ingresada != contraseña:
        contraseña_ingresada = str(input("Ingrese la contraseña: "))

        if contraseña_ingresada != contraseña:
            print ("la contraseña no coinciden")
        if contraseña_ingresada == contraseña:
            print ("Contraseña correcta")
            break
        if intento == intento_ingresado:
            print ("se llego al limite de intentos")
            break
        intento = intento + 1


#descubrir_contraseña()

def ingresar_frase_y_cuenta_la_letra_que_elija():
    frase = str(input("Ingrese una frase: "))
    letra = str(input("Ingrese una letra: "))
    contador = 0 
    for i in frase:
        if i == letra:
            contador = contador +1
            print ("La letra", letra "se encuentra", contador "veces en la frase")