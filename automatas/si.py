def afd_si(lexema):
    tabla_transicion = {
        'A':{'s':'B'},
        'B':{'i':'C'},
        'C':{}
    }
    estados_finales = ['C']
    estado_actual = 'A'
    for c in lexema:
        if c in tabla_transicion[estado_actual]:
            estado_actual = tabla_transicion[estado_actual][c]
        else:
            estado_actual = 'T'
            break
    if estado_actual in estados_finales:
        return 'FINAL'
    elif estado_actual == 'T':
        return "TRAMPA"
    else:
        return "NO FINAL"

if afd_si(input()):
    print("existo")
else:
    print("no sebas no")