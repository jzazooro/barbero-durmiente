import threading
import time
from clases.barberia import Barberia
from clases.barbero import Barbero
from clases.cliente import Cliente

def main():
    barberia=Barberia(4)
    barbero=Barbero("Zazo", barberia)
    cliente1=Cliente("Ruben", barberia)
    cliente2=Cliente("Gonzalo", barberia)
    cliente3=Cliente("German", barberia)
    cliente4=Cliente("Moyis", barberia)
    cliente5=Cliente("Carlos", barberia)
    listaclientes=[cliente1, cliente2, cliente3, cliente4, cliente5]
    hilobarbero=threading.Thread(target=barbero.trabajar)
    hilobarbero.start()

    for cliente in listaclientes:
        cliente.visita()
        time.sleep(1)
    barberia.salir(barbero.nombre)