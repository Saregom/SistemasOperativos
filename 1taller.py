def sum_pares(numbers): 
    sum = 0 
    for i in numbers: 
        if i % 2 == 0: 
            sum += i 
    
    return sum

# ------------------
def count_proceso(file_name): 
    file = open(file_name) 
    count_proceso = 0 
    for i in file.readlines(): 
        if "proceso" in i: 
            count_proceso += 1 
    return count_proceso

# ------------------
import threading

def tarea():
    print("Hola")

# ------------------
if __name__ == "__main__":
    print(sum_pares([1, 2, 3, 4, 5, 6]))

    print(count_proceso("file.txt"))

    print("Inicio")
    t1 = threading.Thread(target=tarea)
    t1.start()
    print("Fin")