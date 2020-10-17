from helpers.menu import Menu
from helpers.helper import input_data, print_table, pregunta

users = {}

def menu_profesor():
    menu_principal = ['Nuevo Usuario', 'Iniciar Sesion']
    respuesta = Menu(menu_principal).show()
    if respuesta == 1:
        nuevo_usuario()
    elif respuesta == 2:
        iniciar_sesion()

def nuevo_usuario():
    print('''
    ============================
        Registrar Usuario
    ============================
    ''')
    crearusuario = input("Ingresar Nombre de Usuario: ")
    if crearusuario in users:
        print("\nEl Nombre de Usuario existe !\n")
    else:
        createpassword = input("\nIngrese su Contraseña: ")
        users[crearusuario] = createpassword
        print("\nUsuario Creado\n")
        iniciar_sesion()

def iniciar_sesion():
    print('''
    =========================
        Iniciar Sesion
    =========================
    ''')
    usuario = input("Ingrese el Nombre de Usuario: ")
    password = input("Ingrese la Contraseña: ")

    if usuario in users and users[usuario] == password:
        print("\nSesion Iniciada")
        administrador()
    else:
        print("\nNo Existe el Usuario o Error de Contraseña")

def profesor():
    try:
        print('''
        ================
            Colegio 
        ================
        ''')
        menu_principal = ['salir' ]
        respuesta = Menu(menu_principal).show()
        if respuesta == 1:
            pass
        elif respuesta == 2:
            pass
        elif respuesta == 3:
            pass
        elif respuesta == 4:
            pass

        print("\nGracias por utilizar el sistema\n")
    except KeyboardInterrupt:
        print('\n Se interrumpio la aplicación')
    except Exception as e:
        print(f'{str(e)}')