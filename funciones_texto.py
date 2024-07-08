import re
from unidecode import unidecode
import numpy
from collections import defaultdict
# import multiprocessing as mp

def cargar_archivo(path_archivo:str, tipo_archivo:str):
    if tipo_archivo not in ['txt', 'csv', 'xlsx']:
        raise ValueError("Tipo de archivo no soportado. Use 'txt', 'csv' o 'xlsx'.")
    if tipo_archivo=='txt':
        with open(f'{path_archivo}', 'r', encoding='ISO-8859-1') as file:
            # Lee el contenido del archivo
            texto = file.read()
        return texto
    
    elif tipo_archivo=='xlsx' or tipo_archivo=='csv':
        import pandas as pd
        if tipo_archivo=='xlsx':
            df = pd.read_excel(f'{path_archivo}')
        elif tipo_archivo=='csv':
            df = pd.read_csv(f'{path_archivo}')
        return df    
    else:
        return print(f'{Exception}')

def limpiar_texto(texto: str, espacios_blanco: bool = True):
    # """
    # Convierte el texto a minúsculas, elimina acentos, tokeniza,
    # y elimina palabras no alfabéticas y stopwords.
    # """
    texto = unidecode(texto)
    texto=texto.lower()
    texto=re.sub(r'[\r\n]+', '.', texto) #Quita tanto \r, \n, \r\n por un punto
    texto=re.sub(r'[\/\.\-]+', '.', texto)
    if espacios_blanco==True:
        patron = r"[\{\}\(\)\¿\?\¡\!\|\[\]\*\-\+\¡\!\,\\/\{\}\"\'_:;]+"
        texto = re.sub(patron, " ", texto).strip()
    
    #! separar puntos de palabra siguiente
    texto=re.sub(r'(\.)([a-zA-Z0-9-])', r'\1 \2', texto)
    #! separar palabras de números posteriores que pueda no haber espacio
    texto=re.sub(r'([a-zA-Z])([0-9])', r'\1 \2', texto)
    #! separar palabras de números anteriores que pueda no haber espacio
    texto=re.sub(r'([0-9])([a-zA-Z])', r'\1 \2', texto)

    return texto

def separar_y_eliminar_texto(texto):
    # Define el patrón de separación para incluir dígitos
    # Además de los caracteres de separación, incluye dígitos (\d+) en el patrón
    patron = r"[\,\/\(\)\[\];:\\\|\-_]"
    
    texto_sin_puntuacion = re.sub(patron, " ", texto)
    
    # Usa re.split() para dividir el texto basado en el patrón
    palabras = re.split(r"\s+", texto_sin_puntuacion.strip())
    
    return palabras

def separar_frases(texto:str):
    """
    Sirve tanto para separar frases en un texto completo 
    como para separar frases dentro de una frase o línea larga
    """
    #split necesita strings, no listas
    frases = re.sub(r"(\w{2,}|\d)(\.)",r'\1 \2', texto).split(" .")
    frases=[frase.strip() for frase in frases if frase]
    
    return frases

def contar_frases(frases):
    
    lista_frases = {}
    for frase in frases:
        frase_filtro=frase.strip()
        if frase_filtro not in lista_frases:
            lista_frases[frase_filtro] = 1
        else:
            try:
                # Si la frase ya está en el diccionario, incrementa su frecuencia en 1
                lista_frases[frase_filtro] += 1
            except:
                pass

    lista_frases = sorted(lista_frases.items(), key=lambda item: item[1],reverse=True)
    return lista_frases

def contar_palabras(palabras, stop_words=[]):
    # """
    # Utiliza procesamiento paralelo para contar la frecuencia de sustantivos en los comentarios.
    # """
    lista_palabras = {}
    for palabra in palabras:
        
        if palabra not in lista_palabras and palabra not in stop_words:
            lista_palabras[palabra] = 1
        else:
            try:
                # Si la palabra ya está en el diccionario, incrementa su frecuencia en 1
                lista_palabras[palabra] += 1
            except:
                pass

    lista_palabras = sorted(lista_palabras.items(), key=lambda item: item[1],reverse=True)
    return lista_palabras

def contar_grupo_de_palabras(frases: list, stopwords, num_palabras=2, orden=False):
    
    #Filtramos las frases con solo 1 palabra
    frases_filtradas= [frase for frase in frases if len(frase.split()) >=num_palabras]
    # Creamos un diccionario con valor por defecto 0 para contar los grupo de palabras
    grupo_de_palabras = defaultdict(int)
    

    for frase in frases_filtradas:
    # Dividimos la frase en palabras
        palabras = frase.split()
        if len(palabras) < num_palabras:
            continue
        else:
            palabras_filtradas = [palabra for palabra in palabras if palabra not in stopwords]
            
            if len(palabras_filtradas) < num_palabras:
                pass
            else:
                for i in range(len(palabras_filtradas) - (num_palabras-1)):
                    if orden == True:
                        palabras_ordenadas = sorted(palabras_filtradas[i:i+num_palabras])
                        grupo = " ".join(palabras_ordenadas)
                    else:
                        grupo = f"{palabras_filtradas[i:i+num_palabras]}"
                    grupo_de_palabras[grupo] += 1

    return dict(sorted(grupo_de_palabras.items(), key=lambda x: x[1], reverse=True))

def filtrar_texto(texto,stop_words=[],num_palabras=2, tipo_separacion='frases',orden=False, espacios_blanco=True):
    texto=limpiar_texto(texto, espacios_blanco)
    if tipo_separacion == 'palabras':
        palabras=separar_y_eliminar_texto(texto)
        lista=contar_palabras(palabras,stop_words)
    elif tipo_separacion == 'frases':
        frases=separar_frases(texto)
        lista=contar_frases(frases)
    elif tipo_separacion == 'grupos':
        frases=separar_frases(texto)
        lista=contar_grupo_de_palabras(frases,stop_words,num_palabras,orden)
    else:
        print('Opción de separación no válida. Las opciones disponibles son palabras, frases y grupos')
    try:
        return lista
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

#DISTANCIA DE LEVENSHTEIN OBTENIDO EN: https://blog.paperspace.com/implementing-levenshtein-distance-word-autocomplete-autocorrect/

def printDistances(distances, token1Length, token2Length):
    for t1 in range(token1Length + 1):
        for t2 in range(token2Length + 1):
            print(int(distances[t1][t2]), end=" ")
        print()

# def levenshteinDistanceDP(token1, token2):
#     distances = numpy.zeros((len(token1) + 1, len(token2) + 1))

#     for t1 in range(len(token1) + 1):
#         distances[t1][0] = t1

#     for t2 in range(len(token2) + 1):
#         distances[0][t2] = t2
        
#     printDistances(distances, len(token1), len(token2))
#     return 0


def levenshteinDistanceDP(token1, token2,pintar=False):
    distances = numpy.zeros((len(token1) + 1, len(token2) + 1))

    for t1 in range(len(token1) + 1):
        distances[t1][0] = t1

    for t2 in range(len(token2) + 1):
        distances[0][t2] = t2
        
    a = 0
    b = 0
    c = 0
    
    for t1 in range(1, len(token1) + 1):
        for t2 in range(1, len(token2) + 1):
            if (token1[t1-1] == token2[t2-1]):
                distances[t1][t2] = distances[t1 - 1][t2 - 1]
            else:
                a = distances[t1][t2 - 1]
                b = distances[t1 - 1][t2]
                c = distances[t1 - 1][t2 - 1]
                
                if (a <= b and a <= c):
                    distances[t1][t2] = a + 1
                elif (b <= a and b <= c):
                    distances[t1][t2] = b + 1
                else:
                    distances[t1][t2] = c + 1
    if pintar==True:
        printDistances(distances, len(token1), len(token2))
    return distances[len(token1)][len(token2)]



def calcDictDistance(word, numWords,pintar=False):
    from diccionario_stopwords import palabras_vacias
    lines=palabras_vacias()
    dictWordDist = []
    wordIdx = 0
    
    for line in lines: 
        wordDistance = levenshteinDistanceDP(word, line.strip())
        if wordDistance >= 10:
            wordDistance = 9
        dictWordDist.append(str(int(wordDistance)) + "-" + line.strip())
        wordIdx = wordIdx + 1

    closestWords = []
    wordDetails = []
    currWordDist = 0
    dictWordDist.sort()
    if pintar==True:
        print(dictWordDist)
    for i in range(numWords):
        currWordDist = dictWordDist[i]
        wordDetails = currWordDist.split("-")
        closestWords.append(wordDetails[1])
    return closestWords

def levenshtein_distance(s1:str, s2:str, cost_insertion=1, cost_deletion=1, cost_substitution=2) -> int:
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1, cost_insertion, cost_deletion, cost_substitution)

    # Initialize the matrix
    previous_row = range(len(s2) + 1)
    
    # Loop through each character in s1
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + cost_insertion  # insertion
            deletions = current_row[j] + cost_deletion        # deletion
            substitutions = previous_row[j] + (cost_substitution if c1 != c2 else 0)  # substitution
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]