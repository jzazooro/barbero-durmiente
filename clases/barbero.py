import threading
import time

class Barbero:
    def __init__(self, nombre, barberia):
        self.nombre=nombre
        self.barberia=barberia

    def trabajar(self):
        while True:
            if self.barberia.sillas.empty():
                print(self.nombre, " se duerme")
            
            else:
                cliente=self.barberia.sillas.get()
                print(self.nombre, " empieza a cortar el pelo a ", cliente)
                time.sleep(5)