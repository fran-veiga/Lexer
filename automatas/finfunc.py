def afd_hasta(lexema):
    tabla_transicion={
        'A':{'f':'B'},
        'B':{'i':'C'},
        'C':{'n':'D'},
        'D':{'f':'E'},
        'E':{'u':'F'},
        'F':{'n':'G'},
        'G':{'c':'H'},
        'H':{},
        'T':{}
        }
    
    estado_actual = "A"
    estados_finales = ["H"]

    for c in lexema:
        if c in tabla_transicion[estado_actual]:
            estado_actual = tabla_transicion[estado_actual][c]
        else:
            estado_actual = 'T'
            break
    if estado_actual in estados_finales:
        return "FINAL"
    elif estado_actual == 'T':
        return "TRAMPA"
    else:
        return "NO FINAL"

print(afd_hasta(input()))