import threading
import time
import random

AZUL = "\033[94m"
VERDE = "\033[92m"
ROJO = "\033[95m"
RESET = "\033[0m"

class Filosofo(threading.Thread):
    def __init__(self, nombre, tenedor_izq, tenedor_der, comidas_necesarias=3):
        super().__init__()
        self.nombre = nombre
        self.tenedor_izq = tenedor_izq
        self.tenedor_der = tenedor_der
        self.comidas_necesarias = comidas_necesarias # numero maximo de veces que el filosofo puede comer

    def run(self):
        for cantidad_comidas in range(self.comidas_necesarias):
            print(f"{self.nombre} está pensando...")
            time.sleep(random.uniform(1, 3))
            print(f"{self.nombre} intenta tomar tenedores")
            
            cambio = False
            # se evalua si el tenerdor derecho tiene un indice menor que el izquierdo
            if self.tenedor_der[0] < self.tenedor_izq[0]:
                # si es asi, se intercambian los tenedores para que el filosofo tome primero el derecho
                self.tenedor_izq, self.tenedor_der = self.tenedor_der, self.tenedor_izq
                cambio = True

            with self.tenedor_izq[1]:
                print(f"{self.nombre} tomó tenedor {'izquierdo' if not cambio else 'derecho'} (#{self.tenedor_izq[0]})")
                time.sleep(random.uniform(0.1, 0.5))
                with self.tenedor_der[1]:
                    print(f"{self.nombre} tomó tenedor {'derecho' if not cambio else 'izquierdo'} (#{self.tenedor_der[0]})")
                    print(f"{self.nombre} está comiendo...")
                    time.sleep(random.uniform(1, 2))
                    print(f"{self.nombre} terminó de comer")

                    cantidad_comidas += 1
                    
                    COLOR = AZUL if cantidad_comidas < 3 else VERDE
                    print(f"{COLOR}{self.nombre} ha comido {cantidad_comidas} {'vez' if cantidad_comidas==1 else 'veces'}\n{RESET}")

# ahora se crean los tenedores como tuplas para almacenar el indice de cada uno(índice, tenedor)
tenedores = [(index, threading.Lock()) for index in range(5)]
filosofos = []

for i in range(5):
    f = Filosofo(f"Filósofo {i+1}", tenedores[i], tenedores[(i+1) % 5], 3)
    filosofos.append(f)
    f.start()

# Esperamos a que todos los filosofos terminen de comer
for f in filosofos:
    f.join()

print(F"{ROJO}Todos los filósofos han terminado de comer.{RESET}")

