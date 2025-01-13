from os import listdir,path
from Language_processing import tokenización
from pickle import dump
from math import log

vocabulario = [] # Inicializa el vocabulario de palabras
matriz_tf = [] # Inicializa la matriz TF

nom_archivos = listdir ('./Db') # Lista de nombres de los archivos a procesar

for nom_archivo in nom_archivos: # Iterar por los archivos
    # Construir vectores TF para la matriz
    if vocabulario:
        matriz_tf.append ([0]*len(vocabulario))
    else:
        matriz_tf.append ([])
    ubicación = path.join ('./Db',nom_archivo)
    archivo = open (ubicación , 'r' , encoding='utf-8')
    contenido = archivo.read ()

    contenido_tok = tokenización (contenido)

    for palabra in contenido_tok:
        if palabra not in vocabulario:
            vocabulario.append (palabra)
            for fila in matriz_tf [:-1]:
                fila.append (0)
            matriz_tf [-1].append (1 + log(contenido_tok.count (palabra)))
        else:
            i = vocabulario.index(palabra)
            if not (matriz_tf [-1] [i]):
                matriz_tf [-1] [i] = (1 + log (contenido_tok.count(palabra)))
    
    db = open ('db.pickle','wb')  # Guardar progreso de procesamiento en caso de fallo futuro
    dump ([matriz_tf , vocabulario],db)

    print (f'{len (matriz_tf)} / {len(nom_archivos)}') # Imprimir progreso

total_doc = len (matriz_tf) # Cantidad total de documentos
idf_l = [] # Lista de Inverse Document Frequency por palabra

# Construir la lista de IDF por palabra
for columna in range (len (matriz_tf [0])):
    doc_frec = 0
    for fila in matriz_tf:
        if fila [columna]:
            doc_frec += 1
    idf = 1 + log (total_doc / doc_frec)
    idf_l.append (idf)

# Convertir la matriz TF en matriz TF-IDF
for columna in range (len (matriz_tf [0])):
    for fila in matriz_tf:
        fila [columna] *= idf_l [columna]

db = open ('db.pickle','wb')  # Guardar datos procesados
dump ([matriz_tf , vocabulario , nom_archivos], db)