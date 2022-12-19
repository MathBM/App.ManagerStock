from random import randint
import time
import zmq

class LeitorCodigoBarras:
    def __init__(self, nome):
        self.nome = nome      
    def __str__(self):
        return f"{self.nome}" #f?
    def leCodigo(self):
        self.ultimaLeitura = randint(1000,9999)
    def conectar(self): #como server
        self.context = zmq.Context() #tipo o  tópico do MQTT
        self.socket = self.context.socket(zmq.REP) #modelo request/response
        self.socket.bind("tcp://*:5555") 
    def monitorarConexao(self):
        #  Wait for next request from client
        self.message = self.socket.recv()
        print(f"Received request: {self.message}")

        #  processando
        time.sleep(1) #espera ocupada, simula espera do click do leitor pelo usuário

        #  Send reply back to clients
        self.leCodigo()
        self.socket.send_string(f"{self.ultimaLeitura}")

leitor = LeitorCodigoBarras("leitor1")
leitor.conectar()

while True:
    leitor.monitorarConexao()
