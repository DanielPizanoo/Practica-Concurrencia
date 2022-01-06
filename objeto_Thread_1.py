import threading

def trabajador():
    """función del hilo"""
    print('Trabajador')

hilos = []
for i in range(5):
    h = threading.Thread(target=trabajador)
    hilos.append(h)
    h.start()