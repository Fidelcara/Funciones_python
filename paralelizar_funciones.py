from multiprocessing import Pool
import ipyparallel as ipp
from typing import Callable, List, Any, Dict, Union

def paralelizar_multprocessing(func: Callable[..., Any], datos: List[Any], num_procesos: int = None, **kwargs) -> List[Any]:
    """
    Paraleliza la ejecución de una función dada en una lista de datos.

    :param func: La función a paralelizar.
    :param datos: Una lista de datos sobre los que aplicar la función.
    :param num_procesos: El número de procesos a usar. Si es None, se usará el número de CPUs disponibles.
    :param kwargs: Argumentos adicionales que se pasarán a la función.
    :return: Una lista de resultados de aplicar la función a los datos.
    """
    # Función contenedora para permitir el uso de argumentos adicionales
    def wrapper(item):
        return func(item, **kwargs)

    with Pool(processes=num_procesos) as pool:
        resultados = pool.map(wrapper, datos)
    
    # Paralelizar la función ejemplo_funcion
    # resultados = paralelizar(ejemplo_funcion, datos, diccionario_sinonimos=diccionario_sinonimos, modificadores=modificadores)
    
    return resultados

def paralelizar_ipyparallel(func: Callable[..., Any], datos: List[Any], num_procesos: int = None, **kwargs) -> List[Any]:
    """
    Paraleliza la ejecución de una función dada en una lista de datos utilizando ipyparallel.

    :param func: La función a paralelizar.
    :param datos: Una lista de datos sobre los que aplicar la función.
    :param num_procesos: El número de procesos a usar. Si es None, se usará el número de CPUs disponibles.
    :param kwargs: Argumentos adicionales que se pasarán a la función.
    :return: Una lista de resultados de aplicar la función a los datos.
    """
    # Inicializa el clúster
    cluster = ipp.Cluster(n=num_procesos)  # Si num_procesos es None, se usará el valor por defecto de ipyparallel
    cluster.start_and_connect_sync()
    
    # Crea un cliente
    rc = cluster.connect_client_sync()
    dview = rc[:]
    dview.block = True

    # Enviar la función y los argumentos adicionales a los motores
    dview.push({'func': func, 'kwargs': kwargs})

    # Función contenedora para permitir el uso de argumentos adicionales
    def wrapper(item):
        return func(item, **kwargs)

    # Ejecuta la función en paralelo
    resultados = dview.map_sync(wrapper, datos)
    
    # Cierra el clúster
    cluster.stop_cluster_sync()

    return resultados