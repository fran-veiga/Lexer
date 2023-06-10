from automatas import *
# def afd_coma(lexema):
#     if lexema == ",":
#         return "FINAL"
#     else:
#         return "TRAMPA"
#
#
# def afd_equal(lexema):
#     if lexema == "=":
#         return "FINAL"
#     else:
#         return "TRAMPA"
#
#
# def afd_id(lexema):
#     estados = ['A', 'B', 'T']
#     estados_finales = ['B']
#     estado_actual = 'A'
#     for c in lexema:
#         if estado_actual == 'A' and c.isalpha():
#             estado_actual = 'B'
#         elif estado_actual == 'B' and c.isalnum():
#             estado_actual = 'B'
#         else:
#             estado_actual = 'T'
#             break
#
#     if estado_actual in estados_finales:
#         return "FINAL"
#     else:
#         return "TRAMPA"
#
#
# def afd_num(lexema):
#     if lexema.isnumeric():
#         return "FINAL"
#     else:
#         return "TRAMPA"
#
#
# def afd_puntoycoma(lexema):
#     if lexema == ";":
#         return "FINAL"
#     else:
#         return "TRAMPA"
#
#
# def afd_finfunc(lexema):
#     tabla = {
#         'A': {'f': 'B'},
#         'B': {'i': 'C'},
#         'C': {'n': 'D'},
#         'D': {'f': 'E'},
#         'E': {'u': 'F'},
#         'F': {'n': 'G'},
#         'G': {'c': 'H'},
#         'H': {},
#         'T': {}
#     }
#     estado_actual='A'
#     estados_finales=['H']
#     for c in lexema:
#         if c in tabla[estado_actual]:
#           estado_actual = tabla[estado_actual][c]
#         else:
#           estado_actual = 'T'
#           break
#     if estado_actual in estados_finales:
#         return "FINAL"
#     elif estado_actual == 'T':
#         return "TRAMPA"
#     else:
#         return "NO FINAL"
#
#
# def afd_finsi(lexema):
#     tabla = {
#         'A': {'f': 'B'},
#         'B': {'i': 'C'},
#         'C': {'n': 'D'},
#         'D': {'s': 'E'},
#         'E': {'i': 'F'},
#         'F': {},
#         'T': {}
#     }
#     estado_actual='A'
#     estados_finales=['F']
#     for c in lexema:
#         if c in tabla[estado_actual]:
#             estado_actual = tabla[estado_actual][c]
#         else:
#             estado_actual = 'T'
#             break
#     if estado_actual in estados_finales:
#         return "FINAL"
#     elif estado_actual == 'T':
#         return "TRAMPA"
#     else:
#         return "NO FINAL"
#
#
# def afd_func(lexema):
#     tabla = {
#         'A': {'f': 'B'},
#         'B': {'u': 'C'},
#         'C': {'n': 'D'},
#         'D': {'c': 'E'},
#         'E': {},
#         'T': {}
#     }
#   estado_actual='A'
#   estados_finales=['E']
#   for c in lexema:
#     if c in tabla[estado_actual]:
#       estado_actual = tabla[estado_actual][c]
#     else:
#       estado_actual = 'T'
#       break
#   if estado_actual in estados_finales:
#       return "FINAL"
#   elif estado_actual == 'T':
#       return "TRAMPA"
#   else:
#       return "NO FINAL"
#
#
# def afd_hasta(lexema):
#     tabla = {
#         'A': {'h': 'B'},
#         'B': {'a': 'C'},
#         'C': {'s': 'D'},
#         'D': {'t': 'E'},
#         'E': {'a': 'F'},
#         'F': {},
#         'T': {}
#     }
#   estado_actual='A'
#   estados_finales=['F']
#   for c in lexema:
#     if c in tabla[estado_actual]:
#       estado_actual = tabla[estado_actual][c]
#     else:
#       estado_actual = 'T'
#       break
#   if estado_actual in estados_finales:
#       return "FINAL"
#   elif estado_actual == 'T':
#       return "TRAMPA"
#   else:
#       return "NO FINAL"
#
#
# def afd_leer(lexema):
#     tabla = {
#         'A': {'l': 'B'},
#         'B': {'e': 'C'},
#         'C': {'e': 'D'},
#         'D': {'r': 'E'},
#         'E': {},
#         'T': {}
#     }
#   estado_actual='A'
#   estados_finales=['E']
#   for c in lexema:
#     if c in tabla[estado_actual]:
#       estado_actual = tabla[estado_actual][c]
#     else:
#       estado_actual = 'T'
#       break
#   if estado_actual in estados_finales:
#       return "FINAL"
#   elif estado_actual == 'T':
#       return "TRAMPA"
#   else:
#       return "NO FINAL"
#
#
#
# def afd_mostrar(lexema):
#     tabla = {
#         'A': {'m': 'B'},
#         'B': {'o': 'C'},
#         'C': {'s': 'D'},
#         'D': {'t': 'E'},
#         'E': {'r': 'F'},
#         'F': {'a': 'G'},
#         'G': {'r': 'H'},
#         'H': {},
#         'T': {}
#     }
#   estado_actual='A'
#   estados_finales=['H']
#   for c in lexema:
#     if c in tabla[estado_actual]:
#       estado_actual = tabla[estado_actual][c]
#     else:
#       estado_actual = 'T'
#       break
#   if estado_actual in estados_finales:
#       return "FINAL"
#   elif estado_actual == 'T':
#       return "TRAMPA"
#   else:
#       return "NO FINAL"
#
#
#
# def afd_repetir(lexema):
#     tabla = {
#         'A': {'r': 'B'},
#         'B': {'e': 'C'},
#         'C': {'p': 'D'},
#         'D': {'e': 'E'},
#         'E': {'t': 'F'},
#         'F': {'i': 'G'},
#         'G': {'r': 'H'},
#         'H': {},
#         'T': {}
#     }
#   estado_actual='A'
#   estados_finales=['H']
#   for c in lexema:
#     if c in tabla[estado_actual]:
#       estado_actual = tabla[estado_actual][c]
#     else:
#       estado_actual = 'T'
#       break
#   if estado_actual in estados_finales:
#       return "FINAL"
#   elif estado_actual == 'T':
#       return "TRAMPA"
#   else:
#       return "NO FINAL"
#
#
# def afd_opmult(lexema):
#     tabla = {
#         'A': {"*": "B", "/": "B"},
#         'B': {},
#         'T': {},
#     }
#   estado_actual='A'
#   estados_finales=['B']
#   for c in lexema:
#     if c in tabla[estado_actual]:
#       estado_actual = tabla[estado_actual][c]
#     else:
#       estado_actual = 'T'
#       break
#   if estado_actual in estados_finales:
#       return "FINAL"
#   elif estado_actual == 'T':
#       return "TRAMPA"
#   else:
#       return "NO FINAL"
#
#
# def afd_oprel(lexema):
#     tabla = {
#         'A': {">": "B", "<": "B", "=": "C"},
#         'B': {"=": "D"},
#         'C': {"=": "D"},
#         'D': {},
#         'T': {}
#     }
#   estado_actual='A'
#   estados_finales=['D']
#   for c in lexema:
#     if c in tabla[estado_actual]:
#       estado_actual = tabla[estado_actual][c]
#     else:
#       estado_actual = 'T'
#       break
#   if estado_actual in estados_finales:
#       return "FINAL"
#   elif estado_actual == 'T':
#       return "TRAMPA"
#   else:
#       return "NO FINAL"
#
#
#
# def afd_opsuma(lexema):
#     tabla = {
#         'A': {"+": "B", "-": "B"},
#         'B': {},
#         'T': {},
#     }
#   estado_actual='A'
#   estados_finales=['B']
#   for c in lexema:
#     if c in tabla[estado_actual]:
#       estado_actual = tabla[estado_actual][c]
#     else:
#       estado_actual = 'T'
#       break
#   if estado_actual in estados_finales:
#       return "FINAL"
#   elif estado_actual == 'T':
#       return "TRAMPA"
#   else:
#       return "NO FINAL"
#
#
# def afd_si(lexema):
#     tabla = {
#         'A': {'s': 'B'},
#         'B': {'i': 'C'},
#         'C': {},
#         'T': {}
#     }
#   estado_actual='A'
#   estados_finales=['C']
#   for c in lexema:
#     if c in tabla[estado_actual]:
#       estado_actual = tabla[estado_actual][c]
#     else:
#       estado_actual = 'T'
#       break
#   if estado_actual in estados_finales:
#       return "FINAL"
#   elif estado_actual == 'T':
#       return "TRAMPA"
#   else:
#       return "NO FINAL"
#
#
# def afd_sino(lexema):
#     tabla = {
#         'A': {'s': 'B'},
#         'B': {'i': 'C'},
#         'C': {'n': 'D'},
#         'D': {'o': 'E'},
#         'E': {},
#         'T': {}
#     }
#   estado_actual='A'
#   estados_finales=['E']
#   for c in lexema:
#     if c in tabla[estado_actual]:
#       estado_actual = tabla[estado_actual][c]
#     else:
#       estado_actual = 'T'
#       break
#   if estado_actual in estados_finales:
#       return "FINAL"
#   elif estado_actual == 'T':
#       return "TRAMPA"
#   else:
#       return "NO FINAL"
#
#
# def afd_entonces(lexema):
#   tabla = {
#         'A': {'e': 'B'},
#         'C': {'t': 'D'},
#         'D': {'o': 'E'},
#         'B': {'n': 'C'},
#         'E': {'n': 'F'},
#         'F': {'c': 'G'},
#         'G': {'e': 'H'},
#         'H': {'s': 'I'},
#         'I': {},
#         'T': {}
#     }
#   estado_actual='A'
#   estados_finales=['I']
#   for c in lexema:
#     if c in tabla[estado_actual]:
#       estado_actual = tabla[estado_actual][c]
#     else:
#       estado_actual = 'T'
#       break
#   if estado_actual in estados_finales:
#       return "FINAL"
#   elif estado_actual == 'T':
#       return "TRAMPA"
#   else:
#       return "NO FINAL"


tokens_todos = {
    "Coma": afd_coma,
    "PuntoYComa": afd_puntoycoma,
    "Entonces": afd_entonces,
    "Equal": afd_equal,
    "FinFunc": afd_finfunc,
    "FinSi": afd_finsi,
    "Func": afd_func,
    "FinSi": afd_finsi,
    "Hasta": afd_hasta,
    "Leer": afd_leer,
    "Mostrar": afd_mostrar,
    "Si": afd_si,
    "Sino": afd_sino,
    "Oprel": afd_oprel,
    "Opmult": afd_opmult,
    "Opsuma": afd_opsuma,
    "Id": afd_id,
    "Num": afd_num,
}


def lexer(codigo_fuente):
    lexemas = codigo_fuente.split()
    tokens = []

    for lexema in lexemas:
        for tipo, afd in tokens_todos.items():
            resultado = afd(lexema)
            if resultado == "FINAL":
                tokens.append({"lexema": lexema, "tipo": tipo})
                break
            elif resultado == "TRAMPA":
                print("Error: Token no reconocido:", lexema)
                break

    return tokens
