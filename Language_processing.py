def tokenización (s: str) -> list:
    '''
    Función que separa un string en tokens (palabras o caracteres que no delimitan la cadena)

    Entrada:
    s -> cadena de caracteres a tokenizar

    Retorna:
    list -> lista de tokens extraídos de la cadena
    '''

    delimitadores = [
    ',',        # Coma
    ';',        # Punto y coma
    "'",        # Comillas simples
    '"',        # Comillas dobles
    '{', '}',   # Llaves
    '[', ']',   # Corchetes
    '(', ')',   # Paréntesis
    '|',        # Barra vertical
    '/',        # Barra oblicua
    '!',        # Signo de exclamación
    '?',        # Signo de interrogación
    '$',        # Signo de dólar
    '&',        # Ampersand
    '*',        # Asterisco
    '-',        # Guión
    '_',        # Guión bajo
    ':',        # Dos puntos
    '.',        # Punto
    '~',        # Tilde
    '%',        # Signo de porcentaje
    '\\',       # Barra inversa
    '<', '>',   # Paréntesis angulares
    ' ',        # espacio vacío
    '\n',       # salto de línea
    ]

    lista = []
    token = ""
    
    for i in range (len (s)):
        if s [i] in delimitadores:
            if token:
                lista.append (token.lower())
                token = ''
        else:
            token += s [i]
            if i == len (s) - 1:
                lista.append (token.lower())

    return lista
def stoppers_del (t:list) -> list: # Función opcional en caso de querer usar únicamente el TF-IDF
    '''
    Función q elimina los stoppers para priorizar palabras relevantes; bakup si solo se buscan stoppers

    Recibe:
    t -> lista de tokens

    Retorna:
    list -> lista de tokens con relevancia en la consulta
    '''

    stopwords = [
    # Idioma Español
    
    # Preposiciones  
    'a',
    'ante',
    'bajo',
    'cabe',
    'con',
    'contra',
    'de',
    'desde',
    'durante',
    'en',
    'entre',
    'hacia',
    'hasta',
    'mediante',
    'para',
    'por',
    'según',
    'sin',
    'so',
    'sobre',
    'tras',
    'versus',
    'vía',

    # Conjunciones simples
    'y',
    'e',
    'ni',
    'o',
    'u',
    'pero',
    'mas',
    'sino',
    'aunque',
    'porque',
    'pues',
    'como',
    'si',
    'cuando',
    'donde',
    'mientras',
    'aunque',

    # Pronombres
    'yo',
    'tú',
    'él',
    'ella',
    'usted',
    'nosotros',
    'nosotras',
    'vosotros',
    'vosotras',
    'ellos',
    'ellas',
    'ustedes',
    'mío',
    'tuyo',
    'suyo',
    'nuestro',
    'vuestro',
    'este',
    'esta',
    'estos',
    'estas',
    'ese',
    'esa',
    'esos',
    'esas',
    'aquel',
    'aquella',
    'aquellos',
    'aquellas',
    'alguien',
    'nadie',
    'alguno',
    'ninguno',
    'todo',
    'mucho',
    'poco',
    'quién',
    'qué',
    'cuál',
    'que',
    'quien',
    'cuyo',
    'lo',
    'la',
    'los',
    'las',
    'me',
    'te',
    'le',
    'nos',
    'os',
    'se',

    # Idioma inglés

    # Conjunciones
    'and',
    'but',
    'or',
    'nor',
    'for',
    'so',
    'yet',
    'if',
    'because',
    'although',
    'unless',
    'while',
    'when',
    'where',
    'as',
    'since',

    # Preposiciones
    'about',
    'above',
    'across',
    'after',
    'against',
    'along',
    'among',
    'around',
    'at',
    'before',
    'behind',
    'below',
    'beneath',
    'beside',
    'between',
    'beyond',
    'by',
    'during',
    'except',
    'for',
    'from',
    'in',
    'inside',
    'into',
    'near',
    'of',
    'off',
    'on',
    'onto',
    'opposite',
    'out',
    'outside',
    'over',
    'past',
    'since',
    'through',
    'throughout',
    'till',
    'to',
    'toward/towards',
    'under',
    'underneath',
    'until',
    'up',
    'upon',
    'with',
    'within',
    'without',

    # Pronombres
    'I',
    'you',
    'he',
    'she',
    'it',
    'we',
    'they',
    'me',
    'him',
    'her',
    'us',
    'them',
    'mine',
    'yours',
    'his',
    'hers',
    'its',
    'ours',
    'theirs',
    'this',
    'that',
    'these',
    'those',
    'anyone',
    'someone',
    'everyone',
    'anything',
    'something',
    'everything',
    'nothing',
    'who',
    'what',
    'which',
    'whom',
    'whose',
    'myself',
    'yourself',
    'himself',
    'herself',
    'itself',
    'ourselves',
    'yourselves',
    'themselves'
    ]

    backup_t = t.copy()
    i = 0
    while i < len (backup_t):
        word = backup_t [i].lower()

        if word in stopwords:
            del backup_t [i]
        else:
            i+=1
    
    return backup_t if len (backup_t) > 0 else t
