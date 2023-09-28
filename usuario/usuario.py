class Usuario():
    def __init__(self, nombre, contraseña, telefono, salt):
        self.nombre = nombre
        self.contraseña = contraseña
        self.telefono = telefono
        self.salt = str(salt)

    def __dict__(self):
        return {"nombre": self.nombre, "password": self.nombre, "telefono": self.telefono, "salt":self.salt}


