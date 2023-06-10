from automatas import *

tokens = {
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


def lexer(programa):
    tokens_out = []
    tokens_posibles = [t for t in tokens]
    tokens_posibles_1mas = tokens_posibles.copy()
    lexema = ""
    lexema1mas = ""
    for i in range(len(programa) - 1):
        lexema += programa[i]
        lexema1mas = lexema + programa[i+1]
        tokens_posibles = tokens_posibles_1mas.copy()
        for token in tokens_posibles:
            estado_1mas = tokens[token](lexema1mas)
            if estado_1mas == "TRAMPA":
                tokens_posibles_1mas.remove(token)
        print("lexema: ", lexema)
        print("lexema 1 mas: ", lexema1mas)
        print("Tokens posibles: ", tokens_posibles)
        print("Tokens 1 mas   : ", str(tokens_posibles_1mas) + "\n")
        if tokens_posibles_1mas == []:
            tokens_out.append(tokens_posibles[0])
            tokens_posibles = [t for t in tokens]
            tokens_posibles_1mas = tokens_posibles.copy()
            lexema = ""

    return tokens_out


programa = "hola = 45"

print(lexer(programa))
