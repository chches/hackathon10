from helpers.menu import Menu
from usuario.alumno import menu_alumno
from usuario.director import menu_director
from usuario.profesor import menu_profesor

def iniciar_app():
    try:
        print('''
        ==========================
            Sistema de Colegio
        ==========================
        ''')
        menu_principal = ["Director", "Profesore", "Alumno", "Salir"]
        respuesta = Menu(menu_principal).show()
        if respuesta == 1:
            menu_director()
        elif respuesta == 2:
            menu_profesor()
        elif respuesta == 3:
            menu_alumno()

        print("\nGracias por utilizar el sistema\n")
    except KeyboardInterrupt:
        print('\n Se interrumpio la aplicación')
    except Exception as e:
        print(f'{str(e)}')

iniciar_app()