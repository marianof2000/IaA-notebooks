#proyecto ahorcado
import getpass
ahorcado={
        "a" : '''
   ____
  |   
  |   
  |  
  |______  
        ''',
        "b": '''
   ____
  |   
  |   
  |  /                     
  |______               
         ''',
        "c" :'''
   ____
  |   
  |   
  |  / \                
  |______              
        ''',
        "d" : '''
   ____
  |   
  |   | 
  |  / \                  
  |______  ''',
        "e" : '''
   ____
  |   
  |  /| 
  |  / \                 
  |______  ''',
        "f" : '''
   ____
  |   
  |  /|\ 
  |  / \                                  
  |______ ''',
        "g": '''
   ____
  |   0
  |  /|\ 
  |  / \            
  |______
  ''',
        }

def errores(contador):
    '''muestra el dibujo a medida que erremos'''
    if contador > 0 and contador < 8:
        if contador== 1:
            return ahorcado["a"]
        elif contador== 2:
            return ahorcado["b"] 
        elif contador== 3:
            return ahorcado["c"]
        elif contador == 4:
            return ahorcado["d"]
        elif contador == 5:
            return ahorcado["e"]
        elif contador == 6:
            return ahorcado["f"]
        elif contador == 7:
            return ahorcado["g"]
        else:
            return "hola"

def lineas(secret):
    linea = '_ '
    largo = len(secret)
    vacio = []
    for x in range(largo):
        vacio.append(linea)
    return vacio

def compara(secret, grupo):
    ''' le pasamos la palabra secreta y la letra a comparar y luego nos retorna si fue acertada o erronea'''
    largo = len(secret)
    acertado = False
    # Creo que position no se usa
    position = []
    for x in range(largo):
        if secret[x] == grupo:
            acertado = True
            vacio[x]=grupo

    # Acá compara la palabra secreta con la letra? O sea un string de len>1 con un string de len=1?
    # No me queda claro, para que nunca entra en ese IF
    if secret == grupo:
        acertado = True
        for x in range (largo):
            vacio[x]=grupo[x]
        return f'Acertaron la palabra!!'

    if acertado:
        return f'Le acertaron'
    else:
        return 'No le acertaron!'

def adivina(secret, vacio):
    '''Recorremos la lista (vacio) y comparamos con la palabra secreta, si todas las letras en el mismo indice son iguales es que la palabra es correcta'''
    largo = len(secret)
    correcto = True
    for x in range(largo):
        if secret[x] != vacio[x]:
            correcto = False
    if correcto: 
        print('Adivinaron la palabra felicidadess!!')
        # Retorna solo si es correcto? Sino no retorna nada?
        return correcto
        
palabra = True
while True:
    #toma de datos de la palabra inicial 
    if palabra:
        # Si secret tiene espacios, la toma igual?
        secret = getpass.getpass("Ingrese la palabra que el equipo contrario debe adivinar: ")
        #convertimos en mayuscula para comparar
        secret = secret.upper()
        contadorerror = 0
        # Arma una lista con guiones bajos, uno por cada letra.
        vacio = lineas(secret)
        # Qué hace esto desde este lugar?
        correcto = False
        palabra = False

    #toma de datos x letras para adivinar la palabra incial 
    # Si grupo tiene más de una letra, funciona?
    grupo = input('Ingresen la letra que decidieron: ')

    #convertimos en mayuscula para comparar 
    grupo = grupo.upper()

    # En caso de acertar los felicita y plantea jugar otra vez
    if secret == grupo:
        print('Adivinaron la palabra felicidades!!')
        retorno = input('Desea volver a jugar? Ingrese si o no ')
        retorno = retorno.upper()
        if retorno == 'SI':
            palabra = True
        else:
            break
    
    # En respuesta queda un string
    respuesta= compara(secret, grupo)
    print(respuesta)

    if respuesta == "No le acertaron!":
        contadorerror += 1
        print(errores(contadorerror))
    print(vacio)
    print()

    # Qué retorna la función adivina? True y algo más?
    correcto = adivina(secret,vacio)

    if correcto == True :
        retorno = input('Desea volver a jugar? Ingrese si o no ')
        retorno = retorno.upper()
        if retorno == 'SI':
            palabra = True
        else:
            break

    if contadorerror == 7:
        print('Perdieron!!')
        retorno = input('Desea volver a jugar? Ingrese si o no ')
        retorno = retorno.upper()
        if retorno == 'SI':
            palabra = True
        else:
            break
