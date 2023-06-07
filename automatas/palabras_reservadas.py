def automata_palabras_reservadas(lexema, tabla, estados_finales, estado_actual):
    for c in lexema:
        if c in tabla[estado_actual]:
            estado_actual = tabla[estado_actual][c]
        else:
            estado_actual = 'T'
            break
    if estado_actual in estados_finales:
        return "FINAL"
    elif estado_actual == 'T':
        return "TRAMPA"
    else:
        return "NO FINAL"
    

def afd_entonces(lexema):
    tabla = {
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
    return automata_palabras_reservadas(lexema, tabla, ["I"], "A")


def afd_finfunc(lexema):
    tabla = {
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
    return automata_palabras_reservadas(lexema, tabla, ["H"], "A")
    


def afd_finsi(lexema):
    tabla = {
        'A':{'f':'B'},
        'B':{'i':'C'},
        'C':{'n':'D'},
        'D':{'s':'E'},
        'E':{'i':'F'},
        'F':{},
        'T':{}
    }
    return automata_palabras_reservadas(lexema, tabla, ["F"], "A")



def afd_func(lexema):
    tabla = {
        'A':{'f':'B'},
        'B':{'u':'C'},
        'C':{'n':'D'},
        'D':{'c':'E'},
        'E':{},
        'T':{}
    }
    return automata_palabras_reservadas(lexema, tabla, ["E"], "A")



def afd_hasta(lexema):
    tabla = {
        'A':{'h':'B'},
        'B':{'a':'C'},
        'C':{'s':'D'},
        'D':{'t':'E'},
        'E':{'a':'F'},
        'F':{},
        'T':{}
    }
    return automata_palabras_reservadas(lexema, tabla, ["F"], "A")
    


def afd_leer(lexema):
    tabla = {
        'A':{'l':'B'},
        'B':{'e':'C'},
        'C':{'e':'D'},
        'D':{'r':'E'},
        'E':{},
        'T':{}
    }
    return automata_palabras_reservadas(lexema, tabla, ["E"], "A")


def afd_mostrar(lexema):
    tabla = {
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
    return automata_palabras_reservadas(lexema, tabla, ["H"], "A")



def afd_repetir(lexema):
    tabla = {
        'A':{'r':'B'},
        'B':{'e':'C'},
        'C':{'p':'D'},
        'D':{'e':'E'},
        'E':{'t':'F'},
        'F':{'i':'G'},
        'G':{'r':'H'},
        'H':{},
        'T':{}
    }
    return automata_palabras_reservadas(lexema, tabla, ["H"], "A")



def afd_si(lexema):
    tabla = {
        'A':{'s':'B'},
        'B':{'i':'C'},
        'C':{}
    }
    return automata_palabras_reservadas(lexema, tabla, ["C"], "A")



def afd_sino(lexema):
    tabla = {
        'A':{'s':'B'},
        'B':{'i':'C'},
        'C':{'n':'D'},
        'D':{'o':'E'},
        'E':{},
        'T':{}
    }
    return automata_palabras_reservadas(lexema, tabla, ["E"], "A")
