from datetime import datetime

usuarios = {}

mercancia = {}

proveedores = []

Roles = {}

#hola mundo me llamo por mi nombre y tambien por celular,

def registrar_usuario():
    print('--Xamiaa pijamas--')
    nombre = input('Ingrese su nombre de usuario: ')
    correo = input('Ingrese su correo electrónico: ')
    contraseña = input('Ingrese su contraseña: ')
    print("Rol")
    print("1. Administrador")
    print("2. Trabajador")
    Rol = int(input("Ingrese una opción: "))
    usuarios[nombre] = {"correo": correo, "contraseña": contraseña, "rol": Rol}
    print('¡Registro exitoso!')

    if Rol == 1:
        iniciar_sesion_administrador()
    elif Rol == 2:
        iniciar_sesion_trabajador()

def iniciar_sesion_administrador():
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    if usuario in usuarios and usuarios[usuario]["contraseña"] == contraseña and usuarios[usuario]["rol"] == 1:
        print("Inicio de sesión exitoso.")
        menu_principal_administrador()
    else:
        print("Credenciales incorrectas.")
        iniciar_sesion_administrador()

def iniciar_sesion_trabajador():
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    if usuario in usuarios and usuarios[usuario]["contraseña"] == contraseña and usuarios[usuario]["rol"] == 2:
        print("Inicio de sesión exitoso.")
        menu_principal_trabajador()
    else:
        print("Credenciales incorrectas.")
        iniciar_sesion_trabajador()

def menu_principal_administrador():
            print('--- Menú principal ---')
            print('1. Registrar mercancía')
            print('2. Ingresar infrormacion proveedor')
            print('3. Generar informe de entrada y salida de mercancía')
            print('4. Registrar devolución de mercancía')
            print('5. Cambiar contraseña')
            print('6. Salir')
            opcion = int(input('Ingrese una opción: '))
            if opcion == 1:
                ingresar_mercancia()
            elif opcion == 2:
                registrar_proveedor()
            elif opcion == 3:
                generar_informe()
            elif opcion == 4:
                registrar_devolucion()
            elif opcion == 5:
                cambiar_contraseña()
            elif opcion == 6:
                print('¡Hasta luego, vuelve pronto!')
            else:
                print('Opción inválida. Por favor, ingrese una opción válida.')
                menu_principal_administrador()
def cambiar_contraseña():
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    if  nombre_usuario in usuarios:
        nueva_contraseña = input("Ingrese la nueva contraseña: ")
        usuarios[nombre_usuario]["contraseña"] = nueva_contraseña
        print("Contraseña cambiada correctamente.")
        print ("iniciar sesion")
        iniciar_sesion_administrador()
        if nombre_usuario in usuarios and usuarios[nombre_usuario]["contraseña"] == nueva_contraseña:
            print("Inicio de sesión exitoso.")
        else:
            print("Usuario no encontrado.")
def registrar_proveedor():
    print("ingresar proveedor:")
    proveedor = input ("nombre de el proveedor:")
    numero_proveedor = int(input("Ingresar numero proveedor:."))
    direccion_proveedor= input("Ingresar direccion de proveedor:")
    mercancia_proveedor= input ("Ingresar mercancia del proveedor:")
    print("Guardado exitosamente")
    numero_proveedor
    direccion_proveedor
    mercancia_proveedor
    menu_principal_administrador ()
    proveedores.append (proveedor)
def ingresar_mercancia():
    print ("---Registrar mercancia---")
    nombre_m = input("Ingrese el nombre de la mercancía: ")
    cantidad = int(input("Ingrese la cantidad de la mercancía: "))
    valor_unitario = float(input("Ingrese el valor unitario de la mercancía: "))
    mercancia[nombre_m] = {"cantidad": cantidad, "valor_unitario": valor_unitario}
    print ("--Mercancia registrada--")
    menu_principal_administrador ()
def generar_informe ():
            print ("¿Que producto deseas generar el informe?")
            print('1. pijama franela')
            print('2. pijama camison')
            print('3. pijama sexy')
            print('4. Salir')
            opcion = int(input('Ingrese una opción: '))
            if opcion == 1:
                pijama_franela()
            elif opcion == 2:
                pijama_camison()
            elif opcion == 3:
                pijama_sexy()
            elif opcion == 4:
                print('¡Hasta luego!')
                menu_principal_administrador ()
            else:
                print('Opción inválida. Por favor, ingrese una opción válida.')
                generar_informe()
def pijama_franela():
    print("pijama franela")
    print("¿Tipo de movimiento que deseas el informe:")
    print("1. entrada")
    print("2. salida")
    print("3. cancelar")
    opcion = int(input('Ingrese una opción: '))
    if opcion == 1:
        print("entrada pijamas franela")
        print("las tallas disponibles son:s,m,l")
        print(" descripcion :es un tejido suave , de varios tipos de calidaes, apto para el invierno")
        print("colores : azul, morado, verde")
        print("fecha de entrada:20/06/2023")
        print("cantidad: 100")
        input("si desea imprimir el informe precione /Enter ")
        print("--Informe generado--")
        print ("nombre de el proovedor:",proveedores)
        generar_informe ()
    elif opcion == 2:
        print("salida pijama franela")
        print("las tallas disponibles son:s,m,l")
        print(" descripcion :es un tejido suave , de varios tipos de calidaes, apto para el invierno")
        print("colores : azul, morado, verde")
        print("fecha de salida:22/06/2023")
        print("cantidad: 90")
        print("Distribucion: Se distribuyo a los tres locales de ha 30 pijamas franela ")
        input("si desea imprimir el informe precione /Enter ")
        print("--Informe generado--")
        print ("nombre de el proovedor:",proveedores)
        generar_informe ()
    elif opcion == 3:
        print('¡Hasta luego!.')
        menu_principal_administrador ()
    else:
        print('Opción inválida. Por favor, ingrese una opción válida.')
        pijama_franela()
def pijama_camison():
    print("pijama camison")
    print("¿Tipo de movimiento que deseas el informe:")
    print("1. entrada")
    print("2. salida")
    print("3. cancelar")
    opcion = int(input('Ingrese una opción: '))
    if opcion == 1:
        print("entrada pijamas camison")
        print("las tallas disponibles son:m,l,xl")
        print(" descripcion :es un tejido fluffy de tacto suave ideal para el frio")
        print("colores : Negro, Azul, rojo")
        print("fecha de entrada:15/06/2023")
        print("cantidad: 84")
        input("si desea imprimir el informe precione /Enter ")
        print("--Informe generado--")
        print ("nombre de el proovedor:",proveedores)
        generar_informe()
    elif opcion == 2:
        print("salida pijama camison")
        print("las tallas disponibles son:m,l,xl")
        print(" descripcion :es un tejido fluffy de tacto suave ideal para el frio")
        print("colores : Negro, Azul, rojo")
        print("fecha de salida:22/06/2023")
        print("cantidad: 84")
        print("Distribucion: Se distribuyo a los tres locales de ha 28 pijamas camison")
        input("si desea imprimir el informe precione /Enter ")
        print("--Informe generado--")
        print ("nombre de el proovedor:",proveedores)
        generar_informe ()
    elif opcion == 3:
        print('¡Hasta luego!.')
        menu_principal_administrador ()
    else:
        print('Opción inválida. Por favor, ingrese una opción válida.')
        pijama_camison()
def pijama_sexy():
    print("pijama sexy")
    print("¿Tipo de movimiento que deseas el informe:")
    print("1. entrada")
    print("2. salida")
    print("3. cancelar")
    opcion = int(input('Ingrese una opción: '))
    if opcion == 1:
        print("entrada pijamas sexy")
        print("las tallas disponibles son:xs,s,m,l,xl,xxl")
        print("descripcion :Tejido de seda o el raso convinado con el encaje")
        print("colores disponibles: azul, morado, verde")
        print("fecha de entrada:21/06/2023")
        print("cantidad: 90")
        input("si desea imprimir el informe precione /Enter ")
        print("--Informe generado--")
        print ("nombre de el proovedor:",proveedores)
        generar_informe ()
    elif opcion == 2:
        print("salida pijama sexy")
        print("las tallas disponibles son:xs,s,m,l,xl,xxl")
        print("descripcion :Tejido de seda o el raso convinado con el encaje")
        print("colores disponibles: azul, morado, verde")
        print("fecha de salida:22/06/2023")
        print("cantidad: 90")
        print("Distribucion: Se distribuyo a los tres locales de ha 30 pijamas sexy")
        input("si desea imprimir el informe precione /Enter ")
        print("--Informe generado--")
        print ("nombre de el proovedor:",proveedores)
        generar_informe ()
    elif opcion == 3:
        print('¡Hasta luego!.')
        menu_principal_administrador ()
    else:
        print('Opción inválida. Por favor, ingrese una opción válida.')
        pijama_sexy()
pijamafra = 80
pijamacami = 100
pijamasex = 95
def registrar_devolucion():
    print("¿Qué producto deseas realizar la devolución?")
    print('1. Pijama de franela')
    print('2. Pijama camisón')
    print('3. Pijama sexy')
    print('4. Salir')
    opcion = int(input('Ingrese una opción: '))
    if opcion == 1:
        print("Pijama de franela")
        print(f"Cantidad disponible de pijamas de franela: {pijamafra}")
        cantidad = int(input("Cantidad de la devolución: "))
        total = pijamafra + cantidad
        print("Devolución registrada correctamente.")
        print(f"Total de pijamas de franela: {total}")
        registrar_devolucion()
    elif opcion == 2:
        print("Pijama camisón")
        print(f"Cantidad disponible de pijamas camisón: {pijamacami}")
        cantidad = int(input("Cantidad de la devolución: "))
        total = pijamacami + cantidad
        print("Devolución registrada correctamente.")
        print(f"Total de pijamas camisón: {total}")
        registrar_devolucion()
    elif opcion == 3:
        print("Pijama sexy")
        print(f"Cantidad disponible de pijamas sexy: {pijamasex}")
        cantidad = int(input("Cantidad de la devolución: "))
        total = pijamasex + cantidad
        print("Devolución registrada correctamente.")
        print(f"Total de pijamas sexy: {total}")
        registrar_devolucion()
    elif opcion == 4:
        print('¡Hasta luego!')
        menu_principal_administrador()
    else:
        print('Opción inválida. Por favor, ingrese una opción válida.')
        registrar_devolucion()
print("----- REGISTRO -----")
registrar_usuario()
print("\n----- INICIO DE SESIÓN -----")
iniciar_sesion_administrador()



