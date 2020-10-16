from classes.director import Director
# from classes.director_director import director_director
from helpers.menu import Menu
from helpers.helper import print_table, input_data, pregunta

class Directores_controller:
    def __init__(self):
        self.director = Director()
        # self.director_director = director_director()
        self.salir = False

    def menu(self):
        while True:
            try:
                print('''
                ===================
                    directores
                ===================
                ''')
                menu = ['Listar directores', 'Buscar director', "Nuevo director", "Salir"]
                respuesta = Menu(menu).show()
                
                if respuesta == 1:
                    self.listar_directores()
                elif respuesta == 2:
                    self.buscar_director()
                elif respuesta == 3:
                    self.insertar_director()
                else:
                    self.salir = True
                    break
            except Exception as e:
                print(f'{str(e)}')

    def listar_directores(self):
        print('''
        ===========================
            Lista de directores
        ===========================
        ''')
        directores = self.director.obtener_directores('director_id')
        print(print_table(directores, ['ID', 'Nombre', 'Edad', 'Correo']))
        input("\nPresione una tecla para continuar...")

    def buscar_director(self):
        print('''
        ===========================
            Buscar director
        ===========================
        ''')
        try:
            id_director = input_data("Ingrese el ID del director >> ", "int")
            director = self.director.obtener_director({'director_id': id_director})
            print(print_table(director, ['ID', 'Nombre', 'Edad', 'Correo']))

            if director:
                if pregunta("¿Deseas dar mantenimiento al director?"):
                    opciones = ['Asignar director', 'Editar director', 'Eliminar director', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        self.asignar_director(id_director, director)
                    elif respuesta == 2:
                        self.editar_director(id_director)
                    elif respuesta == 3:
                        self.eliminar_director(id_director)
        except Exception as e:
            print(f'{str(e)}')
        input("\nPresione una tecla para continuar...")

    def insertar_director(self):
        nombre = input_data("Ingrese el nombre del director >> ")
        edad = input_data("Ingrese la edad del director >> ")
        correo = input_data("Ingrese el correo del director >> ")
        self.director.guardar_director({
            'nombres': nombre,
            'edad': edad,
            'correo': correo
        })
        print('''
        =================================
            Nuevo director agregado !
        =================================
        ''')
        self.listar_directores()

    def editar_director(self, id_director):
        nombre = input_data("Ingrese el nuevo nombre del director >> ")
        edad = input_data("Ingrese la nueva edad del director >> ")
        correo = input_data("Ingrese el nuevo correo del director >> ")
        self.director.modificar_director({
            'director_id': id_director
        }, {
            'nombres': nombre,
            'edad': edad,
            'correo': correo
        })
        print('''
        ==========================
            director Editado !
        ==========================
        ''')

    def eliminar_director(self, id_director):
        self.director.eliminar_director({
            'director_id': id_director
        })
        print('''
        ===========================
            director Eliminado !
        ===========================
        ''')

    def asignar_director(self, id_director, director):
        print(f'\n Asignación de directors para el director : {director[1]}')
        print('''
            ============================
                directors disponibles
            ============================
        ''')
        directors = self.director.obtener_directors('director_id')
        directors_disponibles = []
        if directors:
            for director in directors:
                id_director = director[0]
                nombre_director = director[1]
                directors_director = self.director_director.buscar_director_directors({
                    'id_director': id_director,
                    'id_director': id_director
                })
                if not directors_director:
                    directors_disponibles.append({
                        'id': id_director,
                        'directors disponibles': nombre_director
                    })

            print(print_table(directors_disponibles))
            director_seleccionado = input_data(f'\nSeleccione el ID del director a asignar al director: {director[1]} >> ', 'int')
            buscar_director = self.director.obtener_director({'director_id': director_seleccionado})
            if not buscar_director:
                print('\nEste director no existe !')
                return
            directors_director = self.director_director.buscar_director_directors({
                'id_director': id_director,
                'id_director': director_seleccionado
            })
            if directors_director:
                print('\nEste director ya esta asignado al director !')
                return
            self.director_director.guardar_director_director({
                'id_director': id_director,
                'id_director': director_seleccionado
            })
            print('''
                ==============================
                    Nuevo director asignado !
                ==============================
            ''')
        