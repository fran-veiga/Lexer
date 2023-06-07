def afd_hasta(lexema):
    tabla_transicion={
        'A':{'h':'B'},
        'B':{'a':'C'},
        'C':{'s':'D'},
        'D':{'t':'E'},
        'E':{'a':'F'},
        'F':{},
        'T':{}
        }
    
    estado_actual = "A"
    estados_finales = ["F"]

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