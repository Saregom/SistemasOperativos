class FIFOQueue:
    def __init__(self):
        self.queue = []

    def add_process(self, process=None):
        if process is None:
            name = input("\nNombre del nuevo proceso: ")
            if not name:
                name = "Proceso sin nombre"
            while True:
                try:
                    priority = int(input("Prioridad del nuevo proceso: "))
                    process = {'name': name, 'priority': priority}
                    break
                except ValueError:
                    print("!!Error: La prioridad debe ser un numero entero\n")
        
        self.queue.append(process)
        print(f"Proceso agregado: {self.print_process(process)}")

    def show_current_process(self):
        print(f"\nProceso actual: ")
        if self.queue:
            print(f"1. {self.print_process(self.queue[0])}")
        else:
            print("No hay procesos en la cola")

    def remove_process(self):
        if self.queue:
            print(f"\nProceso eliminado: {self.print_process(self.queue.pop(0))}")
        else:
            print("\nNo hay procesos en la cola para eliminar")

    def show_state(self):
        print("\nEstado de la cola:")
        if not self.queue:
            print("La cola esta vacia")
            return
        else:
            for i, process in enumerate(self.queue):
                print(f"{i+1}. {self.print_process(process)}")

    def print_process(self, process):
        return f"{process['name']} - Prioridad: {process['priority']}"

if __name__ == "__main__":
    new_queue = FIFOQueue()

    processes = [
        {
            'name': 'Proceso A',
            'priority': 5
        },
        {
            'name': 'Proceso B',
            'priority': 1
        },
        {
            'name': 'Proceso C',
            'priority': 4
        },
        {
            'name': 'Proceso D',
            'priority': 2
        },
        {
            'name': 'Proceso E',
            'priority': 3
        }
    ]

    for process in processes:
        new_queue.add_process(process)

    new_queue.show_state()
    new_queue.show_current_process()

    # Simulacion 
    while True:
        print("\n-------- ¿Que deseas hacer? --------")
        print("- Agregar proceso (a)")
        print("- Mostrar proceso actual (p)")
        print("- Eliminar proceso actual (e)")
        print("- Mostrar estado de la cola (s)")
        print("- Salir (q)")
        option = input("Opcion: ")

        match option:
            case "a":
                new_queue.add_process()
            case "p":
                new_queue.show_current_process()
            case "e":
                new_queue.remove_process()
            case "s":
                new_queue.show_state()
            case "q":
                print("Saliendo...")
                break
            case _:
                print("\n!!Opcion no valida")

    print("\nSe han ejecutado todos los procesos")