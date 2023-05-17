import queue
import threading
import time

class Barberia:
    def __init__(self, numerosillas):
        self.numerosillas=numerosillas
        self.sillas=queue.Queue(numerosillas)
    
    def entrar(self, cliente):
        if self.sillas.full():
            print("No hay sillas disponibles")
        else:
            self.sillas.put(cliente)
            print("El cliente ", cliente, " se ha sentado")

    def salir(self, trabajador):
        print("el barbero ha terminado y se va")