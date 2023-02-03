import threading
import time
import queue

import Logger as log
resultado = 0

def worker(q):
    global resultado
    tempo = 0
    log.warn("Inicio da Thread")
    while True:
        tempo += 1
        try:
            resultado = q.get(block=False)
            log.warn("Dado recebido")
        except queue.Empty:
            time.sleep(0.7)
            log.warn('------')
            continue
        if resultado is None:
            break
        # process the resultado
        # log.warn("Respondendo")
        log.debug(f"Worker received: {resultado} no tempo {tempo}")
        return f"Worker received: {resultado} no tempo {tempo}"

q = queue.Queue()
t = threading.Thread(target=worker, args=(q,))
t.start()

# Add items to the queue
for i in range(500):
    received = input("O que quer comunicar? ")
    log.warn("enviando")
    q.put(received)
    log.warn("aguardando")
    log.warn(resultado)
    # t.join()
    log.warn("Chegou")
    # data = q.get()
    print(resultado)

# Wait for the worker to finish processing
# q.put(None)
# t.join()