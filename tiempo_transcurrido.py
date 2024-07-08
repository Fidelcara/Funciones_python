import time
def timer(tiempo_inicio):
    tiempo_transcurrido=time.time()-tiempo_inicio
    print(f"Han transcurrido {tiempo_transcurrido:.4f} segundos")