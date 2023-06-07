def afd_id(lexema):
    estados = ['A', 'B', 'T']
    estados_finales = ['B']
    estado_actual = 'A'
    for c in lexema:
        if estado_actual == 'A' and c.isalpha():
            estado_actual = 'B'
        elif estado_actual == 'B' and c.isalnum():
            estado_actual = 'B'
        else:
            estado_actual = 'T'
            break
    
    if estado_actual in estados_finales:
        return True
    else:
        return False


if afd_id(input()):
    print("exito")
else:
    print("no exito")