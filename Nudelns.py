from Language_processing import tokenización
from pickle import load
from math import log
from cos_sim import similitud_cos

def imprime_resultados (resultados: list , nombres_archivos: list , lim_p_i = 0 , lim_p_s = 100 , inc_i = True , inc_s = True) -> None:
    '''
    Función que dado una lista de resultados porcentuales, un límite porcentual establecido y la inclusión del límite, devuelve los resultados deseados.

    Entrada:
    resultados -> lista de resultados porcentuales
    lim_p_i -> límite porcentual inferior establecido
    lim_p_s -> límite porcentual superior establecido
    nombres_archivos -> lista con los nombres de los archivos
    inc -> incluir el límite. Verdadero si se incluye

    Devuelve:
    * Imprime resultados deseados
    None -> La función solo imprime
    '''

    while (lim_p_i <= max (resultados) <= lim_p_s if inc_i and inc_s else
           lim_p_i < max (resultados) <= lim_p_s if not (inc_i) and inc_s else
           lim_p_i <= max (resultados) < lim_p_s if inc_i and not inc_s else
           lim_p_i < max (resultados) < lim_p_s):
        i = resultados.index (max (resultados))
        print (f'- {nombres_archivos [i]} -> {max (resultados)} %')
        resultados [i] = 0

entrada = input ('Ingrese la búsqueda: ')

continuar = True

while not entrada: # Si no se ingresa nada
    entrada = input ('Debe ingresar una búsqueda para continuar: ')

while continuar:

    #Procesar la entrada (tokenizar)
    consulta = tokenización (entrada)
    print (consulta)

    # Cargar datos de la base de datos
    file = open ('db.pickle','rb')
    data = load (file)
    matriz_tf_idf = data [0] # Importa la matriz tf_idf
    vocabulario = data [1] # Importa el vocabulario
    nom_archivos = data [2] # Importa el nombre de los archivos procesados

    vector_tf_idf_c = [] # Inicializar vector TF-IDF de la consulta
    doc_total = len (matriz_tf_idf)

    # Construcción del vector consulta
    for i in range (len(vocabulario)):
        palabra = vocabulario [i]
        if palabra in consulta:
            tf = 1 + log (consulta.count (palabra))
            doc_frec = 0
            
            for fila in matriz_tf_idf:
                if fila [i]:
                    doc_frec += 1
            if i == 3:
                print (doc_total/doc_frec)
            idf = 1 + log (doc_total / doc_frec)

            vector_tf_idf_c.append (tf*idf)
        else:
            vector_tf_idf_c.append (0)

    resultados = [] # Inicializar la lista de resultados para la posterior aplicación de similitud de cosenos
    for vector_tf_idf in matriz_tf_idf:
        resultados.append (similitud_cos (vector_tf_idf,vector_tf_idf_c))

    print ('\nEl porcentaje de relevancia indica la similitud entre la consulta y el documento referido: \n')

    if max (resultados): # Imprime los resultados en orden decreciente de relevancia, hasta que no haya más resultados relevantes
        if max (resultados) > 50:
            print ('Los resultados de alta relevancia son:')
            imprime_resultados (resultados,nom_archivos,50,inc_i=False)
        if 0 < max (resultados) <= 50:
            print ('Los resultados pocos relevantes son:')
            imprime_resultados (resultados,nom_archivos,lim_p_s=50,inc_i=False)
    else:
        print ('No hay resultados relevantes')

    elección = input ('\n¿Desea ingresar otra búsqueda? \n').lower()

    if elección not in ['sí','si','afirmativo','positivo','efectivamente','yes','indeed','obviously','obviamente']:
        continuar = False
