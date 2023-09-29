class Usuario():
    def __init__(self, nombre, contraseña, telefono, salt):
        self.nombre = nombre
        self.contraseña = contraseña.decode('latin-1')
        self.telefono = telefono
        self.salt = salt.decode('latin-1')

    def __dict__(self):
        return {"nombre": self.nombre, "password": self.contraseña, "telefono": self.telefono, "salt":self.salt}


