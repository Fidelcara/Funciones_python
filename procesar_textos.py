from collections import defaultdict
from funciones.funciones_texto import limpiar_texto, separar_frases,levenshtein_distance
from unidecode import unidecode
from typing import Union, List, Set

def merge_dicts(dicts):
    result = defaultdict(int)
    for d in dicts:
        for k, v in d.items():
            result[k] += v
    return dict(result)



# Función para crear el diccionario de sinónimos
def crear_diccionario_sinonimos(antecedentes):
    diccionario = {}
    for clave, sinonimos in antecedentes.items():
        diccionario[unidecode(clave.lower())]= clave
        for sinonimo in sinonimos:
            diccionario[unidecode(sinonimo.lower())] = clave
    return diccionario

# Función para extraer n-gramas de una frase
def obtener_ngramas(palabras, n):
    return [' '.join(palabras[i:i+n]) for i in range(len(palabras)-n+1)]

def gestion_mods(secuencia:str, mods) -> bool:
    if mods==None:
        return False
    return any(f" {mod} " in secuencia or secuencia.startswith(f"{mod} ") or secuencia.endswith(f" {mod}") for mod in mods)

def extraer_palabras_clave(
    texto: str, 
    diccionario_sinonimos: dict , 
    mod_negativos: List[str] = None, 
    longitud_cadena: float = 5, 
    step: int = 10
    ) -> Set[str]:
    # if isinstance(texto,list):
    #     texto = [limpiar_texto(frase) for frase in texto]
    # elif isinstance(texto,list):
    texto = limpiar_texto(texto)
    
    palabras_clave_encontradas = set()
    
    frases=separar_frases(texto)
    
    for frase in frases:
        palabras = frase.split()
        for n in range(1, 4):
            ngramas = obtener_ngramas(palabras, n)
            
            for i, ngrama in enumerate(ngramas):
                
                if not ngrama:
                    continue
                
                ngrama_lower = ngrama.lower()
                
                #!gestiona la presencia de mods negativos
                if (i > 0 and palabras[i-1].lower() in mod_negativos) or (i > 1 and palabras[i-2].lower() in mod_negativos):
                    continue
                
                if gestion_mods(ngrama_lower,mod_negativos):
                    continue
                    
                if ngrama_lower in diccionario_sinonimos:
                    palabra_clave = diccionario_sinonimos[ngrama_lower]
                    palabras_clave_encontradas.add(palabra_clave)
                    continue
                
                if len(ngrama_lower)>=longitud_cadena:
                    palabra=""
                    ganador=10 #?vale cualquier valor alto
                    #! calcula el número de fallos permitidos 
                    #! en función del step que establezcamos
                    #! por cada 10 letras +1 fallo
                    threshold=len(ngrama_lower)//step+1
                    
                    for key, value in diccionario_sinonimos.items():
                        puntuacion=levenshtein_distance(ngrama_lower,key,cost_substitution=1)
                        # print('puntuación: ',puntuacion, ' longitud palabra: ' ,len(ngrama_lower))
                        score=puntuacion
                        
                        #! incluimos ganador por si hubiera más de una coincidencia coger la de mayor score
                        if score <= threshold and score<ganador:
                            # print(f'threshold, score, ganador: {threshold} {score} {ganador} \r\n ngrama, objetivo: {ngrama_lower} -> {value} \r\n')
                            ganador=score
                            palabra=value #palabra clave que más se parece
                            
                    if palabra:
                        palabras_clave_encontradas.add(palabra)
                        
    return palabras_clave_encontradas


def preprocess_modificadores(modificadores):
    mod_set = set()
    for mod in modificadores:
        mod_split = mod.split()
        if len(mod_split) > 1:
            mod_set.add('_'.join(mod_split))
        else:
            mod_set.add(mod)
    return mod_set

# Función para extraer palabras clave con acompañantes
def extraer_palabras_clave_con_acompanantes(frase, diccionario_sinonimos, variantes, modificadores, incluir_negativos=True):
    
    frase = limpiar_texto(frase,espacios_blanco=True)
    print(f'frase: {frase}')
    
        # Join multi-word modifiers into single tokens
    for mod in modificadores:
        mod_split = mod.split()
        if len(mod_split) > 1:
            frase = frase.replace(mod, '_'.join(mod_split))
    
    palabras = frase.split()
    # palabras_clave_encontradas = set()
    resultado = set()
    modificador=''
    palabra_seguida=''
    # Procesar n-gramas de 1, 2 y 3 palabras
    for n in range(1, 4):
        ngramas = obtener_ngramas(palabras, n)
        # print(f'ngramas: {ngramas}')
        for i, ngrama in enumerate(ngramas):
            ngrama_lower = ngrama.lower().replace('_', ' ')
            # print(f'ngrama_lower: {ngrama_lower}')
            if ngrama_lower in diccionario_sinonimos:
                palabra_clave = diccionario_sinonimos[ngrama_lower]
                # print(f'palabra_clave: {palabra_clave}')

                # Verificar si hay un modificador en la palabra anterior
                if i > 0 and palabras[i-1].lower().replace('_', ' ') in modificadores:
                    if i == "presenta":
                        modificador = palabras[i-1].lower() + palabras[i].lower()
                        continue
                    modificador = palabras[i-1].lower()
                    # print(f'modificador: {modificador}')

                # Decide whether to include negative mentions
                if incluir_negativos or modificador == '':
                    
                    if palabras[i].lower() in diccionario_sinonimos:
                        
                        tipo = [unidecode(variantes.lower()) for variantes in variantes.get(palabra_clave, [])]
                        palabra_seguida=''
                        try:
                            
                            if i + 1 < len(palabras) and palabras[i+1].lower() in tipo:
                                palabra_seguida = palabras[i+1]
                            elif i + 2 < len(palabras) and palabras[i+2].lower() in tipo:
                                palabra_seguida = palabras[i+2]
                                
                        except IndexError:
                            pass
                        
                        patologia=f"{modificador} {palabra_clave} {palabra_seguida}".strip()

                        resultado.add(patologia)
                        # print(f'patologia: {patologia}')
                        # print(f'resultado: {resultado}')
                        #reseteo las palabras opcionales
                        modificador=''
                        palabra_seguida=''

    return ', '.join(set(resultado))

def extraer_palabras_clave_backup(texto: Union[str,list], diccionario_sinonimos: dict, modificadores: list, longitud_cadena: float = 5, threshold: int = 0.8)->set:
    
    texto = limpiar_texto(texto)
    palabras_clave_encontradas = set()
    
    frases=separar_frases(texto)
    
    for frase in frases:
        palabras = frase.split()
        for n in range(1, 4):
            ngramas = obtener_ngramas(palabras, n)
            for i, ngrama in enumerate(ngramas):
                
                if ngrama == '' or ngrama == None:
                    continue
                if i > 0 and palabras[i-1].lower() in modificadores:
                    continue
                else:
                    ngrama_lower = ngrama.lower()
                    
                    if ngrama_lower in diccionario_sinonimos:
                        palabra_clave = diccionario_sinonimos[ngrama_lower]
                        palabras_clave_encontradas.add(palabra_clave)
                        continue
                    if len(ngrama_lower)>longitud_cadena:
                        ganador=0
                        palabra=""
                        for key, value in diccionario_sinonimos.items():
                            puntuacion=levenshtein_distance(ngrama_lower,key,cost_substitution=1)
                            # print('puntuación: ',puntuacion, ' longitud palabra: ' ,len(ngrama_lower))
                            score=1-(puntuacion/len(ngrama_lower))
                            #! incluimos ganador por si hubiera más de una coincidencia coger la de mayor score
                            if score >= threshold and score>ganador:
                                # print(ngrama_lower,' -> ',value)
                                ganador=score
                                palabra=value #palabra clave que más se parece
                                
                        if ganador>0 and palabra:
                            palabras_clave_encontradas.add(palabra)
                            
    return palabras_clave_encontradas