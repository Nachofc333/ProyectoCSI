from almacen.jsonAlmacen import JsonAlmacen

a = JsonAlmacen()
match = a.find_name("Luis")
if match:
    print("Y")
print(match["nombre"])