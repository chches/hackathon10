from helpers.menu import Menu
from helpers.helper import input_data, print_table, pregunta
from controllers.nota_controller import Notas_controller
from controllers.alumno_controller import Alumno_controller
from controllers.malla_controller import Malla_controller

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
        menu_principal = ['buscar alumno', 'listar alumnos', 'notas', 'malla', 'salir' ]
        respuesta = Menu(menu_principal).show()
        if respuesta == 1:
            alumno = Alumno_controller()
            alumno.buscar_alumno()
            if alumno.salir:
                menu_profesor()
        elif respuesta == 2:
            alumno = Alumno_controller()
            alumno.listar_alumnos()
            if alumno.salir:
                menu_profesor()
        elif respuesta == 3:
            nota = Notas_controller()
            nota()
            if nota.salir:
                menu_profesor()
        elif respuesta == 4:
            malla = Malla_controller()
            malla.buscar_malla()
            if malla.salir:
                menu_profesor()

        print("\nGracias por utilizar el sistema\n")
    except KeyboardInterrupt:
        print('\n Se interrumpio la aplicación')
    except Exception as e:
        print(f'{str(e)}')