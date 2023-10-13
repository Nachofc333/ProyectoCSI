class PedidoCifrado():
    def __init__(self, pedido):
        self.pedido = pedido.decode("latin-1")

    def __dict__(self):
        return {"Pedido" : self.pedido}