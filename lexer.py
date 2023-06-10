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
    programa = programa.strip()
    tokens_out = []
    tokens_posibles = [t for t in tokens]
    tokens_posibles_1mas = tokens_posibles.copy()
    lexema = ""
    lexema1mas = ""
    for i in range(len(programa)):
        tokens_final = []

        # lexema += programa[i]
        lexema = lexema1mas
        lexema1mas = lexema1mas + programa[i]
        tokens_posibles = tokens_posibles_1mas.copy()

        if lexema == " " or lexema == "\n":
            # print("salteado espacio\n")
            lexema1mas = programa[i]
            continue

        for token in tokens_posibles:
            estado_1mas = tokens[token](lexema1mas)
            if estado_1mas == "TRAMPA":
                tokens_posibles_1mas.remove(token)
            estado_actual = tokens[token](lexema)
            if estado_actual == "FINAL":
                tokens_final.append(token)

        # print(f"lexema: \"{lexema}\"")
        # print(f"lexema 1 mas: lexema: \"{lexema1mas}\"")
        # print("Tokens posibles: ", tokens_posibles)
        # print("Tokens 1 mas   : ", str(tokens_posibles_1mas))
        # print("Tokens finales : ", str(tokens_final) + "\n")

        if tokens_posibles_1mas == []:
            if tokens_final != []:
                tokens_out.append(tokens_final[0])
                tokens_posibles = [t for t in tokens]
                tokens_posibles_1mas = tokens_posibles.copy()
                lexema1mas = programa[i]
            else:
                raise ValueError()

    error = True
    for token in tokens_posibles_1mas:
        estado_actual = tokens[token](lexema1mas)
        # print(lexema1mas)
        # print(estado_actual)
        if estado_actual == "FINAL":
            tokens_out.append(token)
            error = False
            break
        else:
            continue
    if error:
        raise ValueError()

    return tokens_out


programa = '''
x=98234;


si 6 < 7 entonces
    x = x / 4;
sino
    x = x / 3;
finsi
    

'''

print(f"input: {programa}")
print(lexer(programa))
