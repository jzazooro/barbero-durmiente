# barbero-durmiente

El enlace al repositorio de GitHub de este proyecto es el siguiente: [GitHub](https://github.com/jzazooro/barbero-durmiente.git)

He resuelto el ejercicio del barbero durmiente

### Main

```
from lanzador import main

if __name__ == '__main__':
    main()
```

### Lanzador

```
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
```

### Clases(barberia)

```
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
```

### Clases(barbero)

```
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
```

### Clases(cliente)

```
import threading
import time

class Cliente:
    def __init__(self, nombre, barberia):
        self.nombre=nombre
        self.barberia=barberia

    def visita(self):
        self.barberia.entrar(self.nombre)
```
