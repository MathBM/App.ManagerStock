import zmq

class ClienteLeitorCB:
    def __init__(self):
        self.context = None
        self.socket = None

    def conectar(self): #como cliente
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REQ)
        self.socket.connect("tcp://localhost:5555")

    def requisitarLeitura(self):
        self.socket.send(b"1") #comando para ler codigo de barras
        #  Get the reply.
        self.message = self.socket.recv()
        #print(f"Received reply [ {message} ]")
        return self.message

if __name__=='__main__':
    try:
        cliente = ClienteLeitorCB()
        cliente.conectar()
        print(f"{cliente.requisitarLeitura()}")
    except:
        print("Error Execution")
