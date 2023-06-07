def afd_entonces (lexema):
    tabla_transicion={
            'A':{'e':'B'},
            'C':{'t':'D'},
            'D':{'o':'E'},
            'B':{'n':'C'},
            'E':{'n':'F'},
            'F':{'c':'G'},
            'G':{'e':'H'},
            'H':{'s':'I'},
            'I':{},
            'T':{}
            }

    estado_actual='A'
    estados_finales=['I']
    for caracter in lexema:
        if caracter not in tabla_transicion[estado_actual]:
            # return False
            estado_actual='T'
            break
        estado_actual=tabla_transicion[estado_actual][caracter]
    if estado_actual in estados_finales:
        return "FINAL"
    elif estado_actual == 'T':
        return "TRAMPA"
    else:
        return "NO FINAL"
afd_entonces(input())
