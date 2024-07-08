pronombres=[
    'yo','tú','él','nosotros','vosotros','ellos','uestedes',
    'me','te','se','le'
]

preposiciones = [
    "a", "ante", "bajo", "cabe", "con", "contra",
    "de", "desde", "durante",
    "en", "entre",
    "hacia", "hasta",
    "mediante",
    "para", "por",
    "según", "sin", "so", "sobre",
    "tras",
    "versus", "vía"
]
determinantes=['el', 'la', 'los', 'las', 'un', 'una', 'unos', 'unas', 'este', 'esta', 'estos', 'estas', 'ese', 'esa', 'esos', 'esas', ' aquel', 'aquella', 'aquellos', 'aquellas', 
    'mi', 'tu', 'su', 'nuestro', 'vuestro', 'su', 'mis', 'tus', 'sus', 'nuestros', 'vuestros', 'sus', 
    'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve', 'diez', 'primero', 'segundo', 'tercero', 'cuarto', 'quinto', 
    'alguno', 'alguna', 'algunos', 'algunas', 'mucho', 'mucha', 'muchos', 'muchas', 'poco', 'poca', 'pocos', 'pocas', 'varios', 'varias', 'tanto', 'tanta', 'tantos', 'tantas', 
    'qué', 'cuál', 'cuánto', 'cuánta', 'cuántos', 'cuántas', 
    'todo', 'toda', 'todos', 'todas', 'cada'
]
articulos=['un', 'una', 'unos', 'unas', 'el', 'los', 'la', 'las', 'lo','al','del']
conjunciones=[
    # Conjunciones Coordinantes
    "y", "e",  # Copulativas
    "o", "u",  # Disyuntivas
    "pero", "mas", "sino",  # Adversativas
    "luego", "así que", "por tanto",  # Consecutivas
    "ni",  # Negativas
    
    # Conjunciones Subordinantes
    "que", 
    "como", 
    "si", 
    "aunque", 
    "cuando", 
    "porque", 
    "mientras", 
    "antes de que", 
    "después de que", 
    "en cuanto", 
    "tan pronto como", 
    "siempre que", 
    "a menos que", 
    "para que", 
    "a fin de que", 
    "supuesto que"
]
verbos={
    #ser
    "ser": ['sido','siendo',
    'soy', 'eres', 'es', 'somos', 'sois', 
    'son', 'era', 'eras', 'éramos', 'erais', 'eran', 
    'fui', 'fuiste', 'fue', 'fuimos', 'fuisteis', 'fueron', 
    'seré', 'serás', 'será', 'seremos', 'seréis', 'serán', 
    'sea', 'seas', 'sea', 'seamos', 'seáis', 'sean', 
    'fuera', 'fuese', 'fueras', 'fueses', 
    'fuera', 'fuese', 'fuéramos', 'fuésemos', 'fuerais', 'fueseis', 'fueran', 
    'fuesen', 'sé', 'sed'
    ],
    #haber
    "haber": ['habido', 'habiendo',
    'he', 'has', 'ha', 'hemos', 'habéis', 'han',
    'había', 'habías', 'había', 'habíamos', 'habíais', 'habían',
    'hube', 'hubiste', 'hubo', 'hubimos', 'hubisteis', 'hubieron',
    'habré', 'habrás', 'habrá', 'habremos', 'habréis', 'habrán',
    'haya', 'hayas', 'haya', 'hayamos', 'hayáis', 'hayan',
    'hubiera', 'hubiese', 'hubieras', 'hubieses', 'hubiera', 'hubiese', 'hubiéramos', 'hubiésemos', 'hubierais', 'hubieseis', 'hubieran', 'hubiesen',
    'habría', 'habrías', 'habría', 'habríamos', 'habríais', 'habrían'
    ],
    #estar
    "estar": ['estado', 'estando',
    'estoy', 'estás', 'está', 'estamos', 'estáis', 'están',
    'estaba', 'estabas', 'estaba', 'estábamos', 'estabais', 'estaban',
    'estuve', 'estuviste', 'estuvo', 'estuvimos', 'estuvisteis', 'estuvieron',
    'estaré', 'estarás', 'estará', 'estaremos', 'estaréis', 'estarán',
    'esté', 'estés', 'esté', 'estemos', 'estéis', 'estén',
    'estuviera', 'estuviese', 'estuvieras', 'estuvieses', 'estuviera', 'estuviese', 'estuviéramos', 'estuviésemos', 'estuvierais', 'estuvieseis', 'estuvieran', 'estuviesen',
    'estaría', 'estarías', 'estaría', 'estaríamos', 'estaríais', 'estarían'
    ],
    #tener
    "tener": ['tenido', 'teniendo',
    'tengo', 'tienes', 'tiene', 'tenemos', 'tenéis', 'tienen',
    'tenía', 'tenías', 'tenía', 'teníamos', 'teníais', 'tenían',
    'tuve', 'tuviste', 'tuvo', 'tuvimos', 'tuvisteis', 'tuvieron',
    'tendré', 'tendrás', 'tendrá', 'tendremos', 'tendréis', 'tendrán',
    'tenga', 'tengas', 'tenga', 'tengamos', 'tengáis', 'tengan',
    'tuviera', 'tuviese', 'tuvieras', 'tuvieses', 'tuviera', 'tuviese', 'tuviéramos', 'tuviésemos', 'tuvierais', 'tuvieseis', 'tuvieran', 'tuviesen',
    'tendría', 'tendrías', 'tendría', 'tendríamos', 'tendríais', 'tendrían'
    ],
    #hacer
    "hacer": ['hecho', 'haciendo',
    'hago', 'haces', 'hace', 'hacemos', 'hacéis', 'hacen',
    'hacía', 'hacías', 'hacía', 'hacíamos', 'hacíais', 'hacían',
    'hice', 'hiciste', 'hizo', 'hicimos', 'hicisteis', 'hicieron',
    'haré', 'harás', 'hará', 'haremos', 'haréis', 'harán',
    'haga', 'hagas', 'haga', 'hagamos', 'hagáis', 'hagan',
    'hiciera', 'hiciese', 'hicieras', 'hicieses', 'hiciera', 'hiciese', 'hiciéramos', 'hiciésemos', 'hicierais', 'hicieseis', 'hicieran', 'hiciesen',
    'haría', 'harías', 'haría', 'haríamos', 'haríais', 'harían'
    ],
    #poder
    "poder": ['podido', 'pudiendo',
    'puedo', 'puedes', 'puede', 'podemos', 'podéis', 'pueden',
    'podía', 'podías', 'podía', 'podíamos', 'podíais', 'podían',
    'pude', 'pudiste', 'pudo', 'pudimos', 'pudisteis', 'pudieron',
    'podré', 'podrás', 'podrá', 'podremos', 'podréis', 'podrán',
    'pueda', 'puedas', 'pueda', 'podamos', 'podáis', 'puedan',
    'pudiera', 'pudiese', 'pudieras', 'pudieses', 'pudiera', 'pudiese', 'pudiéramos', 'pudiésemos', 'pudierais', 'pudieseis', 'pudieran', 'pudiesen',
    'podría', 'podrías', 'podría', 'podríamos', 'podríais', 'podrían'
    ],
    #decir
    "decir": ['dicho','diciendo',
    'digo', 'dices', 'dice', 'decimos', 'decís', 'dicen',
    'decía', 'decías', 'decía', 'decíamos', 'decíais', 'decían',
    'dije', 'dijiste', 'dijo', 'dijimos', 'dijisteis', 'dijeron',
    'diré', 'dirás', 'dirá', 'diremos', 'diréis', 'dirán',
    'diga', 'digas', 'diga', 'digamos', 'digáis', 'digan',
    'dijera', 'dijese', 'dijeras', 'dijeses', 'dijera', 'dijese', 'dijéramos', 'dijésemos', 'dijerais', 'dijeseis', 'dijeran', 'dijesen',
    'diría', 'dirías', 'diría', 'diríamos', 'diríais', 'dirían'
    ],
    #ir
    "ir": ['ido', 'yendo',
    'voy', 'vas', 'va', 'vamos', 'vais', 'van',
    'iba', 'ibas', 'iba', 'íbamos', 'ibais', 'iban',
    'fui', 'fuiste', 'fue', 'fuimos', 'fuisteis', 'fueron',
    'iré', 'irás', 'irá', 'iremos', 'iréis', 'irán',
    'vaya', 'vayas', 'vaya', 'vayamos', 'vayáis', 'vayan',
    'fuera', 'fuese', 'fueras', 'fueses', 'fuera', 'fuese', 'fuéramos', 'fuésemos', 'fuerais', 'fueseis', 'fueran', 'fuesen',
    'iría', 'irías', 'iría', 'iríamos', 'iríais', 'irían'
    ],
    #ver
    "ver": ['visto', 'viendo',
    'veo', 'ves', 've', 'vemos', 'veis', 'ven', 
    'veía', 'veías', 'veía', 'veíamos', 'veíais', 'veían', 
    'vi', 'viste', 'vio', 'vimos', 'visteis', 'vieron', 
    'veré', 'verás', 'verá', 'veremos', 'veréis', 'verán', 
    'vea', 'veas', 'vea', 'veamos', 'veáis', 'vean', 
    'viera', 'viese', 'vieras', 'vieses', 'viera', 'viese', 'viéramos', 'viésemos', 'vierais', 'vieseis', 'vieran', 'viesen', 
    'vería', 'verías', 'vería', 'veríamos', 'veríais', 'verían'
    ],
    #dar
    "dar": ['dado', 'dando',
    'doy', 'das', 'da', 'damos', 'dais', 'dan', 
    'daba', 'dabas', 'daba', 'dábamos', 'dabais', 'daban', 
    'di', 'diste', 'dio', 'dimos', 'disteis', 'dieron', 
    'daré', 'darás', 'dará', 'daremos', 'daréis', 'darán', 
    'dé', 'des', 'dé', 'demos', 'deis', 'den', 
    'diera', 'diese', 'dieras', 'dieses', 'diera', 'diese', 'diéramos', 'diésemos', 'dierais', 'dieseis', 'dieran', 'diesen', 
    'daría', 'darías', 'daría', 'daríamos', 'daríais', 'darían'
    ],
    #saber
    "saber": [],
    #querer
    "querer": [],
    #llegar
    "llegar": ['llegado', 'llegando',
    'llego', 'llegas', 'llega', 'llegamos', 'llegáis', 'llegan',
    'llegaba', 'llegabas', 'llegaba', 'llegábamos', 'llegabais', 'llegaban',
    'llegué', 'llegaste', 'llegó', 'llegamos', 'llegasteis', 'llegaron',
    'llegaré', 'llegarás', 'llegará', 'llegaremos', 'llegaréis', 'llegarán',
    'llegue', 'llegues', 'llegue', 'lleguemos', 'lleguéis', 'lleguen',
    'llegara', 'llegase', 'llegaras', 'llegases', 'llegara', 'llegase', 'llegáramos', 'llegásemos', 'llegarais', 'llegaseis', 'llegaran', 'llegasen',
    'llegaría', 'llegarías', 'llegaría', 'llegaríamos', 'llegaríais', 'llegarían'
    ],
    #pasar
    "pasar": [],
    #deber
    "deber": [],
    #poner
    "poner": [],
    #parecer
    "parecer": [],
    #quedar
    "quedar": [],
    #creer
    "creer": [],
    #hablar
    "hablar": [],
    #llevar
    "llevar": [],
    #dejar
    "dejar": [],
    #seguir
    "seguir": [],
    #encontrar
    "encontrar": [],
    #llamar
    "llamar": ['llamado', 'llamando',
    'llamo', 'llamas', 'llama', 'llamamos', 'llamáis', 'llaman',
    'llamaba', 'llamabas', 'llamaba', 'llamábamos', 'llamabais', 'llamaban',
    'llamé', 'llamaste', 'llamó', 'llamamos', 'llamasteis', 'llamaron',
    'llamaré', 'llamarás', 'llamará', 'llamaremos', 'llamaréis', 'llamarán',
    'llame', 'llames', 'llame', 'llamemos', 'llaméis', 'llamen',
    'llamara', 'llamase', 'llamaras', 'llamases', 'llamara', 'llamase', 'llamáramos', 'llamásemos', 'llamarais', 'llamaseis', 'llamaran', 'llamasen',
    'llamaría', 'llamarías', 'llamaría', 'llamaríamos', 'llamaríais', 'llamarían'
    ],
    #venir
    "venir": [],
    #pensar
    "pensar": [],
    #salir
    "salir": [],
    #volver
    "volver": [],
    #tomar
    "tomar": ['tomado', 'tomando'
    'tomo', 'tomas', 'toma', 'tomamos', 'tomáis', 'toman',
    'tomaba', 'tomabas', 'tomaba', 'tomábamos', 'tomabais', 'tomaban',
    'tomé', 'tomaste', 'tomó', 'tomamos', 'tomasteis', 'tomaron',
    'tomaré', 'tomarás', 'tomará', 'tomaremos', 'tomaréis', 'tomarán',
    'tome', 'tomes', 'tome', 'tomemos', 'toméis', 'tomen',
    'tomara', 'tomase', 'tomaras', 'tomases', 'tomara', 'tomase', 'tomáramos', 'tomásemos', 'tomarais', 'tomaseis', 'tomaran', 'tomasen',
    'tomaría', 'tomarías', 'tomaría', 'tomaríamos', 'tomaríais', 'tomarían'
    ],
    #conocer
    "conocer": [],
    #vivir
    "vivir": [],
    #sentir
    "sentir": ['sentido', 'sintiendo',
    'siento', 'sientes', 'siente', 'sentimos', 'sentís', 'sienten',
    'sentía', 'sentías', 'sentía', 'sentíamos', 'sentíais', 'sentían',
    'sentí', 'sentiste', 'sintió', 'sentimos', 'sentisteis', 'sintieron',
    'sentiré', 'sentirás', 'sentirá', 'sentiremos', 'sentiréis', 'sentirán',
    'sienta', 'sientas', 'sienta', 'sintamos', 'sintáis', 'sientan',
    'sintiera', 'sintiese', 'sintieras', 'sintieses', 'sintiera', 'sintiese', 'sintiéramos', 'sintiésemos', 'sintierais', 'sintieseis', 'sintieran', 'sintiesen',
    'sentiría', 'sentirías', 'sentiría', 'sentiríamos', 'sentiríais', 'sentirían'],
    #trabajar
    "trabajar": ['trabajado', 'trabajando',
    'trabajo', 'trabajas', 'trabaja', 'trabajamos', 'trabajáis', 'trabajan',
    'trabajaba', 'trabajabas', 'trabajaba', 'trabajábamos', 'trabajabais', 'trabajaban',
    'trabajé', 'trabajaste', 'trabajó', 'trabajamos', 'trabajasteis', 'trabajaron',
    'trabajaré', 'trabajarás', 'trabajará', 'trabajaremos', 'trabajaréis', 'trabajarán',
    'trabaje', 'trabajes', 'trabaje', 'trabajemos', 'trabajéis', 'trabajen',
    'trabajara', 'trabajase', 'trabajaras', 'trabajases', 'trabajara', 'trabajase', 'trabajáramos', 'trabajásemos', 'trabajarais', 'trabajaseis', 'trabajaran', 'trabajasen',
    'trabajaría', 'trabajarías', 'trabajaría', 'trabajaríamos', 'trabajaríais', 'trabajarían'
    ],
    #escribir
    "escribir": [],
    #perder
    "perder": ['perdido', 'perdiendo',
    'pierdo', 'pierdes', 'pierde', 'perdemos', 'perdéis', 'pierden',
    'perdía', 'perdías', 'perdía', 'perdíamos', 'perdíais', 'perdían',
    'perdí', 'perdiste', 'perdió', 'perdimos', 'perdisteis', 'perdieron',
    'perderé', 'perderás', 'perderá', 'perderemos', 'perderéis', 'perderán',
    'pierda', 'pierdas', 'pierda', 'perdamos', 'perdáis', 'pierdan',
    'perdiera', 'perdiese', 'perdieras', 'perdieses', 'perdiera', 'perdiese', 'perdiéramos', 'perdiésemos', 'perdierais', 'perdieseis', 'perdieran', 'perdiesen',
    'perdería', 'perderías', 'perdería', 'perderíamos', 'perderíais', 'perderían'
    ],
    #pedir
    "pedir": [],
    #recibir
    "recibir": ['recibido', 'recibiendo',
    'recibo', 'recibes', 'recibe', 'recibimos', 'recibís', 'reciben',
    'recibía', 'recibías', 'recibía', 'recibíamos', 'recibíais', 'recibían',
    'recibí', 'recibiste', 'recibió', 'recibimos', 'recibisteis', 'recibieron',
    'recibiré', 'recibirás', 'recibirá', 'recibiremos', 'recibiréis', 'recibirán',
    'reciba', 'recibas', 'reciba', 'recibamos', 'recibáis', 'reciban',
    'recibiera', 'recibiese', 'recibieras', 'recibieses', 'recibiera', 'recibiese', 'recibiéramos', 'recibiésemos', 'recibierais', 'recibieseis', 'recibieran', 'recibiesen',
    'recibiría', 'recibirías', 'recibiría', 'recibiríamos', 'recibiríais', 'recibirían'
    ],
    #decidir
    "decidir": [],
    #entrar
    "entrar": [],
    #presentar
    "presentar": ['presentado', 'presentando', 
    'presento', 'presentas', 'presenta', 'presentamos', 'presentáis', 'presentan',
    'presentaba', 'presentabas', 'presentaba', 'presentábamos', 'presentabais', 'presentaban',
    'presenté', 'presentaste', 'presentó', 'presentamos', 'presentasteis', 'presentaron',
    'presentaré', 'presentarás', 'presentará', 'presentaremos', 'presentaréis', 'presentarán',
    'presente', 'presentes', 'presente', 'presentemos', 'presentéis', 'presenten',
    'presentara', 'presentase', 'presentaras', 'presentases', 'presentara', 'presentase', 'presentáramos', 'presentásemos', 'presentarais', 'presentaseis', 'presentaran', 'presentasen',
    'presentaría', 'presentarías', 'presentaría', 'presentaríamos', 'presentaríais', 'presentarían'
    ],
    #referir
    'referir':['referido', 'refiriendo', 'refiero', 'refieres', 'refiere', 'referimos', 'referís', 'refieren',
    'refería', 'referías', 'refería', 'referíamos', 'referíais', 'referían',
    'referí', 'referiste', 'refirió', 'referimos', 'referisteis', 'refirieron',
    'referiré', 'referirás', 'referirá', 'referiremos', 'referiréis', 'referirán',
    'refiera', 'refieras', 'refiera', 'refiramos', 'refiráis', 'refieran',
    'refiriera', 'refiriese', 'refirieras', 'refirieses', 'refiriera', 'refiriese', 'refiriéramos', 'refiriésemos', 'refirierais', 'refirieseis', 'refirieran', 'refiriesen',
    'referiría', 'referirías', 'referiría', 'referiríamos', 'referiríais', 'referirían'
    ]
}
adverbios=[
    # Adverbios de Lugar
    "aquí", "allí", "arriba", "abajo", "cerca", "lejos", "adelante", "atrás", "dentro", "fuera",
    
    # Adverbios de Tiempo
    "ahora", "antes", "después", "luego", "pronto", "tarde", "temprano", "ayer", "hoy", "mañana",
    
    # Adverbios de Modo
    "bien", "mal", "así", "rápido", "despacio", "fácilmente", "dificilmente", "apenas", "justo", "claramente",
    
    # Adverbios de Cantidad
    "mucho", "poco", "bastante", "más", "menos", "casi", "solo", "tan", "tanto", "todo",
    
    # Adverbios de Afirmación
    "sí", "también", "ciertamente", "efectivamente", "claro",
    
    # Adverbios de Negación
    "no", "nunca", "jamás", "tampoco",
    
    # Adverbios de Duda
    "quizás", "acaso", "probablemente", "posiblemente", "tal vez",
]


def palabras_vacias(grupos_deseados=None):
    elementos = {
        "pronombres": pronombres,
        "preposiciones": preposiciones,
        "determinantes": determinantes,
        "articulos": articulos,
        "conjunciones": conjunciones,
        "verbos": verbos,
        "adverbios": adverbios
    }
    lista_resultante=[]
    if grupos_deseados is None:
        # Si no se especifican grupos, devolver todos los elementos
        for clave, valor in elementos.items():
            if isinstance(valor,dict):
                for infinitivo,conjugaciones in valor.items():
                    
                    lista_resultante=lista_resultante+conjugaciones
            else:
                lista_resultante=lista_resultante+valor
        return lista_resultante
    else:
        # Devolver solo los grupos específicos solicitados
        for clave, valor in elementos.items():
            if clave in grupos_deseados:
                if isinstance(valor,dict):
                    for infinitivo,conjugaciones in valor.items():
                        
                        lista_resultante=lista_resultante+conjugaciones+infinitivo
                else:
                    lista_resultante=lista_resultante+valor
            else:
                pass
        return lista_resultante