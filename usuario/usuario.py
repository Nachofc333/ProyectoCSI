class Usuario():
    def __init__(self, nombre, contraseña, telefono):
        self.nombre = nombre
        self.contraseña = contraseña
        self.telefono = telefono

    def __dict__(self):
        return {"nombre": self.nombre, "contraseña": self.nombre, "telefono": self.telefono}


u = Usuario("pedro", "asdasd", "ASDAS")
print(u.__dict__())
