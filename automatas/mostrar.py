def afd_mostrar(lexema):
    tabla_transicion={
        'A':{'m':'B'},
        'B':{'o':'C'},
        'C':{'s':'D'},
        'D':{'t':'E'},
        'E':{'r':'F'},
        'F':{'a':'G'},
        'G':{'r':'H'},
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

print(afd_mostrar(input()))