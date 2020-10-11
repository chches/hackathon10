from psycopg2 import connect

class Conexion:
    def __init__(self, table_name):
        self.table_name = table_name
        self.db = connect(host='127.0.0.1', 
                    user='postgres', password='*********', database='sictema_colegio')
        self.cursor = self.db.cursor()


    def ejecutar_sentencia(self, query):
        self.cursor.execute(query)
        self.commit()

    def get_all(self, order):
        query = f'SELECT * FROM {self.table_name} ORDER BY {order}'
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_all_inner(self, fields_select, table_select, order):

        list_field_select = []
        for t, list_field in fields_select.items():
            for f in list_field.values():
                list_field_select.append(f'{t}.{f}')
                print(list_field_select)

        # print(list_field_select)
        list_table_inner = []
        tabla_principal = ""
        for t1, list_t2 in table_select.items():
            tabla_principal = t1
            for t2, list_f in list_t2.items():
                for f1, f2 in list_f.items():
                    list_table_inner.append(f'INNER JOIN {t2} ON {t1}.{f1} = {t2}.{f2}')

        inner_join = tabla_principal + " " + " ".join(list_table_inner)
        print(inner_join)
        query = f'''SELECT {", ".join(list_field_select)} FROM {inner_join} ORDER BY {self.table_name}.{order}'''
        print(query)
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_by_id(self, id_object):
        query = f'SELECT * FROM {self.table_name} WHERE {"".join(map(str, id_object.keys()))} = {"".join(map(str, id_object.values()))}'
        self.cursor.execute(query)
        return self.cursor.fetchone()

    def get_by_column(self, data):
        list_select_where = []
        for field_name, field_value in data.items():
            list_select_where.append(f"{field_name}='{field_value}'")
        query = f'SELECT * FROM {self.table_name} WHERE {" AND ".join(list_select_where)}'
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close_connection(self):
        self.db.close()

    def commit(self):
        self.db.commit()
        return True

    def rollback(self):
        self.db.rollback()
        return True

    def insert(self, data):
        values = "'" + "', '".join(map(str, data.values())) + "'"
        query = f'INSERT INTO {self.table_name} ({", ".join(data.keys())}) VALUES ({values})' #'Charly', 'Chinchay', 1989-09-20'
        self.ejecutar_sentencia(query)
        return True

    def update(self, id_object, data):
        list_update = []
        for field_name, field_value in data.items():
            list_update.append(f"{field_name} = '{field_value}'") # SET nombre = ''
        query = f'UPDATE {self.table_name} SET {", ".join(list_update)} WHERE {"".join(map(str, id_object.keys()))} = {"".join(map(str, id_object.values()))}'
        self.ejecutar_sentencia(query)
        return True

    def delete(self, id_object):
        query = f'DELETE FROM {self.table_name} WHERE {"".join(map(str, id_object.keys()))} = {"".join(map(str, id_object.values()))}'
        self.ejecutar_sentencia(query)
        return True