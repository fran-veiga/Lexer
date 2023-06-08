from automatas import *

tokens = [
    ("Id", afd_id),
    ("Coma", afd_coma),
    ("Entonces", afd_entonces),
    ("Equal", afd_equal),
    ("FinFunc", afd_finfunc),
    ("FinSi", afd_finsi),
    ("Func", afd_func),
    ("FinSi", afd_finsi),
    ("Hasta", afd_hasta),
    ("Leer", afd_leer),
    ("Mostrar", afd_mostrar),
    ("Num", afd_num),
    ("Num", afd_num),
    ("Num", afd_num),
    ("Num", afd_num),   # COMPLETAR
    ("Num", afd_num),
    ("Num", afd_num),
    ("Num", afd_num),

]


def lexer (programa):
    for i in range(len(programa) - 1):
