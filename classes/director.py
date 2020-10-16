from connection.conn import Conexion

class Director:
    def __init__(self):
        self.model = Conexion('directores')

    def guardar_director(self, director):
        return self.model.insert(director)

    def obtener_director(self, id_director):
        return self.model.get_by_id(id_director)

    def obtener_directores(self, order):
        return self.model.get_all(order)

    def buscar_directores(self, data_director):
        return self.model.get_by_column(data_director)

    def modificar_director(self, id_director, data_director):
        return self.model.update(id_director, data_director)

    def eliminar_director(self, id_director):
        return self.model.delete(id_director)
