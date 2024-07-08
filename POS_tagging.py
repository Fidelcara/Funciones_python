import re

# Basic lexicon with words and their corresponding POS tags
lexicon = {
    
    #numeros
    "uno":"NUM",
    "dos":"NUM",
    "tres":"NUM",
    "cuatro":"NUM",
    "cinco":"NUM",
    "seis":"NUM",
    "siete":"NUM",
    "ocho":"NUM",
    "nueve":"NUM",
    "diez":"NUM",
    "once":"NUM",
    "doce":"NUM",
    "trece":"NUM",
    "catorce":"NUM",
    "quince":"NUM",
    
    # Determiners
    "el": "DET",
    "la": "DET",
    "los": "DET",
    "las": "DET",
    "un": "DET",
    "una": "DET",
    "unos": "DET",
    "unas": "DET",
    "este": "DET",
    "esta": "DET",
    "estos": "DET",
    "estas": "DET",
    "ese": "DET",
    "esa": "DET",
    "esos": "DET",
    "esas": "DET",
    
    # Adjectives
    "bueno": "ADJ",
    "buena": "ADJ",
    "buenos": "ADJ",
    "buenas": "ADJ",
    "malo": "ADJ",
    "mala": "ADJ",
    "malos": "ADJ",
    "malas": "ADJ",
    "grande": "ADJ",
    "grandes": "ADJ",
    "pequeño": "ADJ",
    "pequeña": "ADJ",
    "pequeños": "ADJ",
    "pequeñas": "ADJ",
    "nuevo": "ADJ",
    "nueva": "ADJ",
    "nuevos": "ADJ",
    "nuevas": "ADJ",
    
    # Nouns
    "paciente": "NOUN",
    "fiebre": "NOUN",
    "tos": "NOUN",
    "dolor": "NOUN",
    "cabeza": "NOUN",
    "doctor": "NOUN",
    "doctora": "NOUN",
    "hospital": "NOUN",
    "enfermedad": "NOUN",
    "medicina": "NOUN",
    
    # Verbs
    "tener": "VERB",
    "tiene": "VERB",
    "tienen": "VERB",
    "tener": "VERB",
    "tomar": "VERB",
    "toma": "VERB",
    "tomar": "VERB",
    "tomaron": "VERB",
    "estar": "VERB",
    "está": "VERB",
    "están": "VERB",
    "ser": "VERB",
    "es": "VERB",
    "son": "VERB",
    "hacer": "VERB",
    "hace": "VERB",
    "hacen": "VERB",
    
    # Adverbs
    "no": "ADV",
    "sí": "ADV",
    "muy": "ADV",
    "bien": "ADV",
    "mal": "ADV",
    "ahora": "ADV",
    "siempre": "ADV",
    "nunca": "ADV",
    "aquí": "ADV",
    "allí": "ADV",
    "ayer": "ADV",
    "hoy": "ADV",
    
    # Prepositions
    "de": "PREP",
    "a": "PREP",
    "en": "PREP",
    "con": "PREP",
    "por": "PREP",
    "para": "PREP",
    "sin": "PREP",
    "sobre": "PREP",
    
    # Conjunctions
    "y": "CONJ",
    "o": "CONJ",
    "que": "CONJ",
    "pero": "CONJ",
    "porque": "CONJ",
    "aunque": "CONJ",
    
    # Pronouns
    "yo": "PRON",
    "tú": "PRON",
    "él": "PRON",
    "ella": "PRON",
    "nosotros": "PRON",
    "nosotras": "PRON",
    "vosotros": "PRON",
    "vosotras": "PRON",
    "ellos": "PRON",
    "ellas": "PRON",
    "me": "PRON",
    "te": "PRON",
    "se": "PRON",
    "nos": "PRON",
    "os": "PRON"
}
# Suffix rules for identifying POS tags
suffix_rules = {
    "ar": "VERB",
    "er": "VERB",
    "ir": "VERB",
    "ción": "NOUN",
    "sión": "NOUN",
    "dad": "NOUN",
    "tad": "NOUN",
    "mente": "ADV",
    "oso": "ADJ",
    "osa": "ADJ",
    "al": "ADJ",
    "able": "ADJ",
    "ible": "ADJ",
    "ado": "ADJ",
    "ada": "ADJ",
}

# Prefix rules for identifying POS tags
prefix_rules = {
    "pre": "VERB",
    "re": "VERB",
    "des": "VERB",
    "in": "ADJ",
    "im": "ADJ",
    "dieci":"NUM",
    "veinti":"NUM",
    "treintai":"NUM",
    "cuarentai":"NUM",
    "cincuentai":"NUM",
    "sesentai":"NUM",
    "setentai":"NUM",
    "ochentai":"NUM",
    "noventai":"NUM",
}
# Contextual rules for identifying POS tags
contextual_rules = {
    "det": ["el", "la", "los", "las", "un", "una", "unos", "unas", "este", "esta", "estos", "estas", "ese", "esa", "esos", "esas","del","al"],
    "prep": ["de", "a", "en", "con", "por", "para", "sin", "sobre"],
    "conj": ["pero", "que" "porque", "aunque"], #"y", "o",
    "adv":['muy']
}

def pos_tag(word, prev_word=None):
    
    # Check the lexicon first
    if word in lexicon:
        return lexicon[word]
    
    if re.match(r"\d+",word):
        return "NUM"
    
        # Apply contextual rules
    if prev_word:
        if prev_word in contextual_rules.get("det", []):
            return "NOUN"
        if prev_word in contextual_rules.get("prep", []):
            return "NOUN"
        if prev_word in contextual_rules.get("conj", []):
            return "VERB"
    
    # Apply suffix rules
    for suffix, tag in suffix_rules.items():
        if word.endswith(suffix):
            return tag
    
    # Apply prefix rules
    for prefix, tag in prefix_rules.items():
        if word.startswith(prefix):
            return tag

    # Default to NOUN if no match found
    return "NOUN"

def pos_tag_text(text):
    # Clean and split the text into words
    words = text.lower().split()
    tagged_words = []
    prev_word = None
    
    for word in words:
        tag = pos_tag(word, prev_word)
        tagged_words.append((word, tag))
        prev_word = word
    
    return tagged_words

def refine_tags(tagged_words: tuple) -> tuple:
    refined_tags = []
    
    for i, (word, tag) in enumerate(tagged_words):
        # Apply additional rules to correct tags based on context
        if tag == "NOUN" and word in contextual_rules.get("det", []):
            if i + 1 < len(tagged_words) and tagged_words[i + 1][1] == "NOUN":
                refined_tags.append((word, "DET"))
            else:
                refined_tags.append((word, tag))
        elif tag == "NOUN" and word in contextual_rules.get("prep", []):
            if i + 1 < len(tagged_words) and tagged_words[i + 1][1] == "NOUN":
                refined_tags.append((word, "PREP"))
            else:
                refined_tags.append((word, tag))
        elif tag == "VERB" and word in contextual_rules.get("conj", []):
            if i + 1 < len(tagged_words) and tagged_words[i + 1][1] == "VERB":
                refined_tags.append((word, "CONJ"))
            else:
                refined_tags.append((word, tag))
        else:
            refined_tags.append((word, tag))

    # Specific refinements based on common patterns
    for i, (word, tag) in enumerate(refined_tags):
        if word.endswith("mente") and tag == "NOUN":
            refined_tags[i] = (word, "ADV")
        elif word.endswith("ción") and tag == "VERB":
            refined_tags[i] = (word, "NOUN")
        elif word.endswith("ado") or word.endswith("ada") and tag == "NOUN":
            refined_tags[i] = (word, "ADJ")
        elif word.endswith("oso") or word.endswith("osa") and tag == "NOUN":
            refined_tags[i] = (word, "ADJ")

    return refined_tags
