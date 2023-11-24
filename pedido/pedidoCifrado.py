class PedidoCifrado():
    def __init__(self, pedido, modo):
        print(pedido)
        self.pedido = []
        if modo == 0:
            for i in pedido:
                self.pedido.append(i.encode("latin-1"))
        if modo == 1:
            for i in pedido:
                self.pedido.append(i.decode("latin-1"))

    def __dict__(self):
        return {"Pedido" : self.pedido}
