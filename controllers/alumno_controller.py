from classes.alumno import Alumno
from helpers.menu import Menu
from helpers.helper import print_table, input_data, pregunta

class Alumno_controller:

    def __init__(self):
        self.alumno = Alumno()
        self.salir = False

    def menu(self):
        while True:
            try:
                print('''
                ===============
                    Alumno
                ===============
                ''')
                menu = ['Lista alumnos', 'Buscar Alumno', 'Nuevo Alumno', 'Salir']
                respuesta = Menu(menu).show()

                if respuesta == 1:
                    pass
                elif respuesta == 2:
                    pass
                elif respuesta == 3:
                    pass
                elif respuesta == 4:
                    self.salir = True
                    break
                
            except Exception as e:
                print(f'{str(e)}')

    def listar_alumnos(self):
        print('''
        ========================
            Lista de Alumnos
        ========================
        ''')
        alumnos = self.alumno.listar_alumnos('')