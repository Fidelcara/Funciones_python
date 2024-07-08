import spacy
from spacy.matcher import Matcher

nlp = spacy.load("es_core_news_sm")
matcher = Matcher(nlp.vocab)

def get_reversed(token):
    return token.text[::-1]


def obtener_tipo_palabra(text,nlp=nlp):
    # Procesa el texto
    doc = nlp(text)

    for token in doc:
        # Obtén el texto del token, el part-of-speech tag y el dependency label
        token_text = token.text #palabra
        token_pos = token.pos_ #sintactico
        token_dep = token.dep_ #dependencia
        # Esto es solo por formato
        print(f"{token_text:<12}{token_pos:<10}{token_dep:<10}")
        
def encontrar_patrones(text,pattern,matcher=matcher,nombre=''):
    # pattern = [{"TEXT": "iOS"}, {"IS_DIGIT": True}]

    # Añade el patrón al matcher y usa el matcher sobre el documento
    matcher.add(f"{nombre}", [pattern])
    matches = matcher(doc)
    print("Total de resultados encontrados:", len(matches))

    # Itera sobre los resultados e imprime el texto del span
    for match_id, start, end in matcher(doc):
        print("Resultado encontrado:", doc.vocab.strings[match_id], doc[start:end].text)
    # [(doc.vocab.strings[match_id], doc[start:end].text) for match_id, start, end in matcher(doc)]

#Función de ejemplo
def longitud_doc(doc):
    
    doc_length = len(doc)
    print(f"Este documento tiene {doc_length} tokens.")
        # Devuelve el objeto doc
    return doc



# Crear una función para añadir el componente
def añadir_funciones_spacy(nombre_componente="longitud_doc", funcion=longitud_doc):
    @Language.component(nombre_componente)
    def componente(doc):
        return funcion(doc)
    return componente

# Procesa los textos e imprime los verbos en pantalla
# for doc in nlp.pipe(TEXTS):
#     print([token.text for token in doc if token.pos_ == "VERB"])

#Obtener una lista de palabras que concuerden con el matcher
# from spacy.lang.es import Spanish

# nlp = Spanish()

# people = ["David Bowie", "Angela Merkel", "Lady Gaga"]

# # Crea una lista de patrones para el PhraseMatcher
# patterns = list(nlp.pipe(people))


# def get_wikipedia_url(span):
#     # Obtén la URL de Wikipedia si el span tiene uno de los siguientes labels
#     if span.label_ in ("PER", "ORG", "LOC"):
#         entity_text = span.text.replace(" ", "_")
#         return "https://es.wikipedia.org/w/index.php?search=" + entity_text


# # Añade la extensión del Span, wikipedia_url, usando el getter get_wikipedia_url
# Span.set_extension("wikipedia_url", getter=get_wikipedia_url)

# doc = nlp(
#     "Antes de finalizar 1976, el interés de David Bowie en la "
#     "floreciente escena musical alemana, le llevó a mudarse a "
#     "Alemania para revitalizar su carrera."
# )
# for ent in doc.ents:
#     # Imprime en pantalla el texto y la URL de Wikipedia de la entidad
#     print(ent.text, ent._.wikipedia_url)
# OUTPUT
# David Bowie https://es.wikipedia.org/w/index.php?search=David_Bowie
# Alemania https://es.wikipedia.org/w/index.php?search=Alemania

    
"""
EJEMPLO
# import spacy
# from spacy.language import Language
# from spacy.matcher import PhraseMatcher
# from spacy.tokens import Span

# nlp = spacy.load("es_core_news_sm")
# animals = ["labrador dorado", "gato", "tortuga", "oso de anteojos"]
# animal_patterns = list(nlp.pipe(animals))
# print("patrones_de_animales:", animal_patterns)
# matcher = PhraseMatcher(nlp.vocab)
# matcher.add("ANIMAL", None, *animal_patterns)

# # Define el componente personalizado
# @Language.component("animal_component")
# def animal_component_function(doc):
#     # Aplica el matcher al doc
#     matches = matcher(doc)
#     # Crea un Span para cada resultado y asígnales el label "ANIMAL"
#     spans = [Span(doc, start, end, label="ANIMAL") for match_id, start, end in matches]
#     # Sobrescribe los doc.ents con los spans resultantes
#     doc.ents = spans
#     return doc


# # Añade el componente al pipeline después del componente "ner"
# nlp.add_pipe("animal_component", after="ner")
# print(nlp.pipe_names)

# # Procesa el texto e imprime en pantalla el texto y el label
# # de los doc.ents
# doc = nlp("Hoy vimos una tortuga y un oso de anteojos en nuestra caminata")
# print([(ent.text, ent.label_) for ent in doc.ents])

# nombre_componente = "mi_componente_personalizado"
# mi_componente = añadir_funciones_spacy(nombre_componente, mi_funcion_personalizada)
# nlp.add_pipe(nombre_componente, last=True)
"""
"""
Operadores spaCy
{"OP": "!"}	Negación: busca 0 veces
{"OP": "?"}	Opcional: busca 0 o 1 veces
{"OP": "+"}	Busca 1 o más veces
{"OP": "*"}	Busca 0 o más veces


pattern = [
    {"LEMMA": "comprar"},
    {"POS": "DET", "OP": "?"},  # opcional: encuentra 0 o 1 ocurrencias
    {"POS": "NOUN"}
]
doc = nlp("Me compré un smartphone. Ahora le estoy comprando aplicaciones.")
    
    OUTPUT:
    compré un smartphone
    comprando aplicaciones

"""
"""
GUÍA PATRONES
DET -> determinante
NOUN -> sustantivo
PROPN -> Nombre propio
LEMMA -> base de rupo de palabras, por ejemplo el verbo descargar(descargué, descargaste...)
IS_NUMBER: True or False -> si el elemento es número o no
ADJ -> Adjetivo
OP -> Opcional después (operadores spacy)
"""