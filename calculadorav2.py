#### imports
import datetime



### variables globales
opcion=None



### funciones historial & time


def registro():
    hora_modificacion=datetime.datetime.now()
    return hora_modificacion

def historial(a,b,resultado):
    with open ('historial.txt','a') as historial:
        historial.write(f'{registro()}\n el resultado es: {a}+{b}: {resultado}\n')

def leer_historial():
    with open('historial.txt','r') as historial:
        x=historial.read()
        print(x)

def borrar_historial():
    open('historial.txt','w').close()



def confirmacion():
    input('\n enter para continuar \n')



### funciones calculadora
def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def multiplicacion(a,b):
    return a*b

def division(a,b):
    return a/b

def porcentaje(a,b):
    return a*b/100

def cuadratica (a):
    return a*a

def guardar_historial(resultado, registro):
    with open('historial.txt','a') as historia:
        historia.write(f'fecha:{registro}\nresultado:{resultado}\n')




####menu

while opcion !=0:
    try:
        opcion=int(input("""selecione su opcion: \n 0.salir \n 1.suma \n 2.resta \n 3.multiplicacion \n 4.division \n 5.porcentaje \n 6.cuadratica \n 7. mostrar historial \n 8.borrar historial \n """))
    except:
        print('opcion invalida')
        confirmacion()
        continue

###opciones calculadora

    if opcion in [1,2,3,4]:
        while True:
            try:
                a=float(input('ingrese el primer numero: '))
                b=float(input('ingrese el segundo numero: '))
                break
            except:
                print('numero invalido ')

        if opcion==1:
            resultado=suma(a,b)
            print( registro() ,f'\n el resultado es: {a}+{b}: {resultado}\n')
            guardar_historial(resultado,registro())
            confirmacion()

        elif opcion==2:
            resultado=resta(a,b)
            print(registro() ,f'el resultado es: {a}-{b}: {resultado}\n')
            guardar_historial(resultado,registro())
            confirmacion()

        elif opcion==3:
            resultado=multiplicacion(a,b)
            print(f'el resultado es: {a}*{b}: {resultado}\n')
            guardar_historial(resultado,registro())
            confirmacion()


        elif opcion==4:
            while b==0:
                try:
                    b=float(input('no se puede dividir por 0  o letras ingrese un valor valido:'))
                    continue
                except:
                    pass
            resultado=division(a,b)
            print(f'el resultado es: {a}/{b}: {resultado}\n')
            guardar_historial(resultado,registro())
            confirmacion()

    elif opcion==5:
        while True:
            try:
                a=float(input('ingrese el primer numero: '))
                b=float(input('ingrese el segundo numero: '))
                break
            except:
                print('numero invalido ')

        resultado=porcentaje(a,b)
        print(registro(),f'\n el resultado es: {a}*{b}/100={resultado} ')
        guardar_historial(resultado,registro())
        confirmacion()

    elif opcion==6:
        while True:
            try:
                a=float(input('ingrese el numero deseado: '))
                break
            except:
                print('numero invalido ')
        resultado=cuadratica(a)
        print(registro(),f'\n el cuadrado del numero es: {a}^2={resultado}')
        guardar_historial(resultado,registro())
        confirmacion()

### opciones historial

    elif opcion==7:
        leer_historial()
        confirmacion()

    elif opcion==8:
        borrar_historial()
        print('historial borrado con exito')
        confirmacion()

    else:
        print('comando invalido')
        confirmacion()