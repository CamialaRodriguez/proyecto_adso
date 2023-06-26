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



