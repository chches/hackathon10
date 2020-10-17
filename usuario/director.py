from helpers.menu import Menu
from helpers.helper import input_data, print_table, pregunta
from controllers.directores_controller import Directores_controller
from controllers.profesores_controller import Profesores_controller
from controllers.alumno_controller import Alumno_controller
from controllers.cursos_controller import Cursos_controller
from controllers.salon_controller import Salon_controller
from controllers.malla_controller import Malla_controller
from controllers.periodo_controller import Periodo_controller

users = {}

def menu_director():
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

def director():
    try:
        print('''
        ================
            Colegio 
        ================
        ''')
        menu_principal = ['director', 'profesor', 'alumno', 'malla', 'salon', 'curso', 'periodo', 'salir' ]
        respuesta = Menu(menu_principal).show()
        if respuesta == 1:
            director = Directores_controller()
            director()
            if director.salir:
                menu_director()
        elif respuesta == 2:
            profesor = Profesores_controller()
            profesor()
            if profesor.salir:
                menu_director()
        elif respuesta == 3:
            alumno = Alumno_controller()
            alumno()
            if alumno.salir:
                menu_director()
        elif respuesta == 4:
            malla = Malla_controller()
            malla()
            if malla.salir:
                menu_director()
        elif respuesta == 5:
            salon = Salon_controller()
            salon()
            if salon.salir:
                menu_director()
        elif respuesta == 6:
            curso = Cursos_controller()
            curso()
            if curso.salir:
                menu_director()
        elif respuesta == 7:
            periodo = Periodo_controller()
            periodo()
            if periodo.salir:
                menu_director()

        print("\nGracias por utilizar el sistema\n")
    except KeyboardInterrupt:
        print('\n Se interrumpio la aplicación')
    except Exception as e:
        print(f'{str(e)}')