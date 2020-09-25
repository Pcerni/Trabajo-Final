'''
Plantilla para el ramo de Programacion Basica (Python)
IPP, 2019

Desarrollada: Sebastian Teran.

Trabajo Individual M2.

Fecha: < 08-09-2019
Integrante :  Pamela Cerda
'''
#Los ejercicios piden datos de entrada, ya que no puse funciones.
#--------------------------------------------------------------------------------------------#

print ("SECUENCIA FIBONACCI")
print (("-")*100)
fib1 = 0    #Fibonacci 0
fib2 = 1    #Fibonacci 1
cont = 1    #Contador
fibo = int (input ("Introduzca el número a calcular... \n"))
while (cont < fibo):
    suma = fib1 + fib2 # Se suma 0 + 1 = 1/ 2/ 3 / 5 / 8 / 13 / 21...
    fib1 = fib2 # fib1 = 1 se iguala a fib2 y queda = 1/ 1 / 2 / 3 / 5 / 8 / 13...
    fib2 = suma # fib2 = 1 se iguala a suma y queda = 1/ 2 / 3 / 5 / 8 / 13 / 21...
    cont += 1   # agrega 1 al contador, hasta llegar al número introducido por el usuario.
    
#--------------------------------------------------------------------------------------------#

print ("MÍNIMO COMÚN MÚLTIPLO")
print (("-")*100)
def mcd (num1, num2):
    a = max(num1, num2) # Esta instrucción deja el número mayor en a
    b = min(num1, num2) # Esta instrucción deja el número menor en b
    while b != 0: # Mientras que b sea diferente de cero :
        mcd = b # mcd guarda el número divisor 
        b = a % b # b hace la división, y guarda el módulo (resto) para hacer una nueva división.
        a = mcd # a se iguala a mcd, y se devuelve al ciclo...       
    return mcd

num1 = int (input ("Ingrese el primer número\n"))
num2 = int (input ("Ingrese el segundo número\n"))

mcm = (num1 * num2)/ mcd (num1, num2) # Expresión para obtener el mínimo común múltiplo.

#--------------------------------------------------------------------------------------------#

print ("MÁXIMO COMÚN DIVISOR")
print (("-")*100)
def mcd (num3, num4):
    a = max(num3, num4) # Esta instrucción deja el número mayor en a
    b = min(num3, num4) # Esta instrucción deja el número menor en b
    while b != 0: # Mientras que b sea diferente de cero :
        mcd = b # mcd guarda el número divisor 
        b = a % b # b hace la división, y guarda el módulo (resto) para hacer una nueva división.
        a = mcd # a guarda el nuevo divisor (módulo o resto), y se devuelve al ciclo...
    return mcd

num3 = int (input ("Ingrese el primer número...\n"))
num4 = int (input ("Ingrese el segundo número...\n"))

#--------------------------------------------------------------------------------------------#

print ("NÚMERO AL REVÉS")
print (("-")*100)
rev = input ("Ingrese un número de dos o más dígitos para revertir\n")
largo = len(rev)
if (largo == 1) or (rev.isalpha() == True): # largo de la palabra es igual a 1 - isalpha (si la palabra contiene letras) es igual a verdadero
    print ("No es posible trabajar con esto.") #Ejecuta este mensaje y sale del programa.
    quit()
else:
    lista1 = list(rev) #convierte los números en lista.
    lista1.reverse() #pone la lista en reversa.
    
#--------------------------------------------------------------------------------------------#

print ("TEXTO AL REVÉS")
print (("-")*100)
reves = input ("Ingrese una palabra de dos o más letras para revertir\n")
largo = len(reves)
if (largo == 1) or (reves.isdigit() == True):# largo de la palabra es igual a 1 - isdigit (si la palabra contiene números) es igual a verdadero
    print ("No es posible trabajar con esto.") #Ejecuta este mensaje y sale del programa.  
    quit()
else:
    listilla = list(reves)#convierte los números en lista.
    listilla.reverse()#pone la lista en reversa.

#--------------------------------------------------------------------------------------------#

print ("PALÍNDROMO")
print (("-")*100)
pal = input ("Ingrese una palabra, y el programa reconocerá si es palíndroma o no\n")
pal1 = pal #asigna el input a una nueva variable.
listapal = list(pal) # convierte el input en lista.
listapal1 = list (pal1) # convierte la nueva variable en lista.
listapal1.reverse() # da vueltas la lista nueva.
listapal = [listapal.lower() for listapal in listapal] #Revisa mayúsculas. En caso de haber mayúsculas, las coloca en minúsculas.
listapal1 = [listapal1.lower() for listapal1 in listapal1]#Revisa mayúsculas. En caso de haber mayúsculas, las coloca en minúsculas.

#--------------------------------------------------------------------------------------------#

print ("NÚMEROS PARES")
print (("-")*100)
par = int (input ("Ingrese un número\n"))
cont = 0 # Contador
if (par % 2 !=0): # Si el resto del input es diferente a 0 (si es número impar)
    par1 = par+1 # Crea una variable y le suma 1 a esa variable(de forma que quede en número par).
    lista = [] # Crea una lista sin items dentro de ella.
    while cont < 10: # Mientras el contador sea menor a 10:       
        par1 += 2 #Se suman 2 a la variable
        lista.append (par1) #Se le agrega la última variable sumada, hasta que el contador llegue a 10.
        cont = cont +1 #Se le suma 1 al contador.

else:
    par1 = par #Se crea una variable y se iguala a la variable de input.
    lista = []# Se crea una lista vacía.
    while cont < 10: # Mientras el contador sea menor a 10.       
        par1 += 2 # se agrega 2 a la nueva variable.
        lista.append (par1) #Se le agrega la última variable sumada, hasta que el contador llegue a 10. 
        cont = cont +1 #Se agrega 1 al contador.
        
#--------------------------------------------------------------------------------------------#

print ("FACTORIAL")
print (("-")*100)
facto = int (input ("Ingrese un número\n"))
contador = 0
n = 1 # multiplicador factorial.
while (contador < facto): # Mientras el contador sea menor que el número ingresado:
    for i in range(1, int (facto+1)): # Se itera entre el rango 1 y el número ingresado.
        n = (n*i)    # n se multiplica por todas las veces que se itera, hasta llegar al número ingresado.
        contador = (contador +1) # se agrega un contador.
        
#--------------------------------------------------------------------------------------------#
               
print ("NÚMEROS PRIMOS")
print (("-")*100)
primo = int (input ("Ingrese un número\n"))
primobool = True #variable booleana verdadera
if primo < 2: # Si el input es menor a 2, entonces el número no es primo
    primobool = False # variable booleana pasa a ser falsa
elif primo == 2: # Si el input es igual a 2, entonces el número  es primo
    primobool = True # variable se mantiene verdadera
else:
    if (primo % 2 == 0): #Si el módulo entre el input y 2 es igual a 0
        primobool = False  #variable booleana falsa.      
    else:  #de lo contrario
        primobool = True #variable booleana verdadera.
        
#--------------------------------------------------------------------------------------------#

print ("BALANCE DE PARÉNTESIS")
print (("-")*100)
texto = input ("Escriba paréntesis\n")
contar = texto.count("(") #Cuenta cuántos paréntesis abiertos hay.
contar1 = texto.count (")")#Cuenta cuántos paréntesis cerrados hay.
if ")" in texto[0]:#Si hay un paréntesis cerrado al principio, dirá que el paréntesis está al revés.
    print ("Paréntesis al revés")
else:
    contar != contar1 #Si la suma de paréntesis abiertos y cerrados no concuerda, muestra el print al final.

#--------------------------------------------------------------------------------------------#

print ("FECHA")
print (("-")*100)
fecha = input ("Ingrese fecha en formato DDMMAAAA\n")
fecha1 = [] #Lista vacía para para agregar datos
for i in fecha: #i itera en cada caracter de fecha
    fecha1.append(i) #agrega a fecha1 cada caracter por separado, en una lista
fecha1.insert(2,"/") #Se agrega el caracter / en la posición 2 de la lista
fecha1.insert(5,"/") #Se agrega el caracter / en la posición 5 de la lista

#--------------------------------------------------------------------------------------------#

print ("CALCULA TUS MINUTOS DE VIDA")
print (("-")*100)
# Cálculo de la edad con los datos ingresados#
fechacont = 1 #Contador para el isalpha
while fechacont == 1:
    fechanac = input("Ingrese fecha nacimiento en formato DDMMAAAA\n")
    if fechanac.isalpha() == True: #Si escribes letras dará error
        print ("Sólo debes escribir números")
    else:
        fechaactual = input ("Ingrese fecha actual en formato DDMMAAAA\n")
        if fechaactual.isalpha() == True: #Si escribes letras, dará error
            print ("Sólo debes escribir números")
        else:
            fechacont = fechacont -1 #Se resta el contador para terminar el bucle y seguir con el programa.        
fechanac1 = [] #Lista vacía para agregar los datos de fecha de nacimiento
fechaactual1 = []#Lista vacía para agregar los daros de fecha actuales
for i in fechanac:# i iterará dentro de la variable por cada caracter en ella
    fechanac1.append(i) #por cada iteración, se agregará el numero iterado a la lista de fechanac1
for e in fechaactual:# e iterará dentro de la variable por cada caracter en ella
    fechaactual1.append(e)#por cada iteración, se agregará el numero iterado a la lista de fechaactual1
fechanio = fechanac1 [4:] #Selecciona los números desde la 4ta posición en adelante (En este caso, el año de nacimiento)
fechanioact = fechaactual1 [4:] #Selecciona los números desde la 4ta posición en adelante (En este caso, el año actual)
fechames = fechanac1 [2:4] #Selecciona los números desde la 2nda posición hasta la tercera (mes de nacimiento)
fechamesact = fechaactual1 [2:4]#Selecciona los números desde la 2nda posición hasta la tercera (mes actual)
fechadia = fechanac1 [:2]#Selecciona los últimos números (día de nacimiento)
fechadiact = fechaactual1 [:2]#Selecciona los últimos números(día actual)
listanio = int(''.join (str(i) for i in fechanio)) #Ocupa .join para unir la cadena sin ningún ('')caracter de por medio. itera en la lista, transforma cada uno de los caracteres en un número entero - Cambia de ["1","2","3","4"] a [1,2,3,4] y luego a 1234)
listanio1 = int(''.join (str(i)for i in fechanioact))#Ocupa .join para unir la cadena sin ningún ('')caracter de por medio. itera en la lista, transforma cada uno de los caracteres en un número entero - Cambia de ["1","2","3","4"] a [1,2,3,4] y luego a 1234)
listames = int(''.join (str(i)for i in fechames))
listames1 = int(''.join (str(i)for i in fechamesact))
listadia = int(''.join (str(i)for i in fechadia))
listadia1 = int(''.join (str(i)for i in fechadiact))
#Operación para obtener años, de acuerdo a datos ingresados
anios = (listanio1 - listanio) #Resultado del año actual MENOS el año de nacimiento (edad de la persona)
meses = (listames1 - listames)#Resultado de los meses sin calcular el mes real. 
dias = (listadia1 - listadia)#Resultado de los días sin calcular el día real.
diasenmes = 30 #Días por cada mes. 
mesesenanio = 12 #Meses en 1 año.
#Minutos en 365 días
Mins = 525600
#Horas en 365 días
Hrs = 8760
#Días en 1 año (sin contar años bisiestos)
Dias = 365
#Promedio de vida de Mujer Chilena, según Instituto de políticas públicas de salud
PromM = 85
if listadia1 < listadia: #Si el día de nacimiento, es mayor que el día actual:
    meses = meses - 1 # Se resta un mes
    dias = diasenmes + listadia1 - listadia #Se suma 30(dias en mes), a listadia1 (dia actual), y se resta dia de nacimiento.
elif listames1 < listames:#Si el mes de nacimiento, es mayor al mes actual:
        anios = anios -1 # Se resta 1 año
        meses = mesesenanio + listames1 - listames#Se suma 12 (meses en año), al mes actual, y se resta el mes de nacimiento.
promediominsM = PromM*Mins # Promedio de vida * Mins en 1 año
promediominsM1 = (anios*Mins)+(meses*Mins)+(dias*Mins) # Promedio de minutos en años, meses y días.
promediohrsM = PromM*Hrs # Promedio de vida * Horas en 1 año
promediohrsM1 = (anios*Hrs)+(meses*Hrs)+(dias*Hrs)# Promedio de horas en años, meses y días
promediodiasM = PromM*Dias #Promedio de vida * días en 1 año
promediodiasM1 = (anios*Dias)+(meses*Dias)+(dias*Dias)# Promedio de días en años, meses y días
promtotalmins = promediominsM - promediominsM1 #Promedio total de minutos restantes
promtotalhrs = promediohrsM - promediohrsM1 #Promedio total de horas restantes
promtotaldias = promediodiasM - promediodiasM1 #Promedio total de días restantes

#--------------------------------------------------------------------------------------------#
print (("\n")*100)
print ("RESULTADOS")
print (("-")*100)
print("El número %i, de acuerdo a la secuencia Fibonacci es: "%(fibo), end="")
print(suma)
print (("*")*100)
print("El Mínimo Común Múltiplo entre %i y %i es : "%(num1, num2), end="")
print(+int(mcm))
print (("*")*100)
print("El Máximo Común Divisor entre %i y %i es : "%(num3, num4), end="")
print(mcd(num3, num4)) # Se llama a función mcd y se aplica a num1 y num2
print (("*")*100)
print("El numero ingresado al revés es: ", end="")
print (lista1)
print (("*")*100)
print("La palabra ingresada al revés es: ", end="")
print (listilla)
print (("*")*100)
print ("La palabra '%s' ingresada por ud, para comprobar si es palíndroma, da el resultado de :"%(pal), listapal == listapal1)
print (("*")*100)
if (par % 2 !=0):
    print ("Ingresaste %i, y es impar. Redondearemos a %i,y los siguientes pares son: "%(par, par+1), lista)
    print ("El último número de la secuencia es:", lista [9])
else:
    print ("Los numéros pares siguientes a %i, son: "%(par), lista)
    print ("El último número de la secuencia es:", lista [9])
print (("*")*100)
print ("La factorización de %i es : %i"%(facto,n))
print (("*")*100)
print("El resultado del numero si es primo es: ", end="")
print (primobool)
print (("*")*100)
if contar != contar1:
    print ("No está balanceado")
    print ("Colocaste",contar, "( y ", contar1, "). Inténtalo de nuevo")
else:
    print ("Está balanceado")        
print (("*")*100)
print ("Su fecha es: {","".join(fecha1),"}") #Une todos los datos, incluyendo los caracteres / en una sola lista
print (("*")*100)
print ("Te quedan:",promtotaldias,"días, o",promtotalhrs,"horas, o",promtotalmins,"minutos")
print (("*")*100)
