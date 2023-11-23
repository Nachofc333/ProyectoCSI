class PedidoCifrado():
    def __init__(self, pedido, modo):
        self.pedido = []
        if modo == 0:
            for i in pedido:
                self.pedido.append(i.decode("latin-1"))
        if modo == 1:
            self.pedido.append(pedido.decode("latin-1"))

    def __dict__(self):
        return {"Pedido" : self.pedido}