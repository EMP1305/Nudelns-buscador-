def producto_escalar (v1:list,v2:list) -> int|None:
    '''
    Función que retorna el producto escalar entre dos vectores

    Entrada:
    v1 -> vector 1
    v2 -> vector 2

    Salida:
    int -> producto escalar
    None -> producto no válido
    '''

    if len (v1) != len (v2) or not (v1) or not (v2): # Si los vectores no tienen la misma cantidad de componentes o un vector no tiene componentes
        return None

    producto = 0
    for i in range (len(v1)): # Itera en los componentes de uno de los vectores
        producto += v1 [i] * v2 [i]
    
    return producto

def mod_vector (v:list) -> int:
    '''
    Función que devuelve el módulo de un vector dado

    Entrada:
    v -> vector

    Salida:
    int -> módulo del vector
    ''' 

    temp = 0 # Variable que albergará la suma de los cuadrados de los componentes del vector
    for componente in v:
        temp += componente**2
    
    return temp**(1/2)

def similitud_cos (v1: list , v2: list) -> int:
    '''
    Función que calcula la similitud de coseno entre dos vectores

    Entrada:
    v1 -> vector
    v2 -> vector

    Salida:
    int -> similitud de coseno calculada en porciento
    '''

    # Módulo de los vectores
    mod_v1 = mod_vector (v1)
    mod_v2 = mod_vector (v2)

    # Si ningún vector es el vector nulo, opera usando el producto punto (escalar)
    if mod_v1 and mod_v2:
        return producto_escalar (v1,v2) / (mod_v1*mod_v2) * 100
    else: # Si al menos uno es nulo, el producto escalar es 0
        return 0