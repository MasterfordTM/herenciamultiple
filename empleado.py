from persona import Persona

class Empleado:
    def __init__(Persona):
        super().__init__()
        self._fecha_contratacion = ""
        self._email = ""
        self._id_empleado = ""

    def get_fecha_contratacion(self):
        return self.fecha_contratacion
    def set_fecha_contratacion(self, fecha):
        self.fecha_contratacion = fecha
    def get_email(self):
        return self.email
    def set_email(self, email):
        self.email = email
    def get_id_empleado(self):
        return self._id_empleado
    def set_id_empleado(self, id_empleado):
        self._id_empleado = id_empleado
    def mostrar_informacion(self):
        base_info= super().mostrar


