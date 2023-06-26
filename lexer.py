from automatas import *

tokens = {
    "DerParen": afd_der_paren,
    "IzqParen": afd_izq_paren,
    "PuntoYComa": afd_puntoycoma,
    "Entonces": afd_entonces,
    "Equal": afd_equal,
    "FinFunc": afd_finfunc,
    "FinSi": afd_finsi,
    "Func": afd_func,
    "Hasta": afd_hasta,
    "Leer": afd_leer,
    "Mostrar": afd_mostrar,
    "Repetir": afd_repetir,
    "Si": afd_si,
    "Sino": afd_sino,
    "Oprel": afd_oprel,
    "Opmult": afd_opmult,
    "Opsuma": afd_opsuma,
    "Num": afd_num,
    "Id": afd_id,
}


def lexer(programa):
    # Eliminar espacio en blanco antes y despues del programa, y agregar un
    # espacio al final para poder agregar el ultimo token.
    programa = programa.strip()
    programa += " "

    tokens_out = []  # La salida del programa
    tokens_posibles = [t for t in tokens]  # los tokens posibles para el lexema
    # tokens posibles para un caracter mas
    tokens_posibles_1mas = tokens_posibles.copy()
    lexema = ""
    lexema1mas = ""
    for i in range(len(programa)):

        # Se incrementan el lexema y el lexema1mas en un caracter
        lexema = lexema1mas
        lexema1mas = lexema1mas + programa[i]

        # Si tokens_posibles es vacío esto es porque se acaba de agregar un
        # lexema a la salida, entonces hay que agregar los tokens posibles con
        # para el unico caracter que contiene el lexema
        if tokens_posibles == []:
            for token in tokens:
                if tokens[token](lexema) != "TRAMPA":
                    tokens_posibles.append(token)
            tokens_posibles_1mas = tokens_posibles.copy()
        else:
            # Si tokens_posibles no esta vacio, solo se copian los tokens
            # posibles con un caracter mas del ciclo anterior
            tokens_posibles = tokens_posibles_1mas.copy()

        # si el lexema es solo un espacio en blanco o un salto de linea, saltear
        # un caracter y no hacer nada.
        if lexema == " " or lexema == "\n" or lexema == "\t":
            lexema1mas = programa[i]
            continue

        # contiene los tokens en estado final con el lexema (se llena en el ciclo)
        tokens_final = []
        for token in tokens_posibles:
            # si el afd para un token con el lexema1mas cae en estado trampa,
            # eliminar ese token de los tokens_posibles_1mas
            estado_1mas = tokens[token](lexema1mas)
            if estado_1mas == "TRAMPA":
                tokens_posibles_1mas.remove(token)
            # si el afd para un token con el lexema cae en un estado final,
            # agregarlo a los tokens_finales
            estado_actual = tokens[token](lexema)
            if estado_actual == "FINAL":
                tokens_final.append(token)

        # SACAR COMENTARIO PARA VER EL ESTADO DEL PROGRAMA PASO A PASO
        # print(f"lexema: \"{lexema}\"")
        # print(f"lexema 1 mas: lexema: \"{lexema1mas}\"")
        # print("Tokens posibles: ", tokens_posibles)
        # print("Tokens 1 mas   : ", str(tokens_posibles_1mas))
        # print("Tokens finales : ", str(tokens_final) + "\n")

        # si no hay ningun token posible con un caracter mas, y hay al menos un
        # token en estado final, agregar ese token a la salida del lexer.
        if tokens_posibles_1mas == []:
            if tokens_final != []:
                tokens_out.append({tokens_final[0]: lexema})
                lexema1mas = programa[i]
                tokens_posibles = []
            else:
                # En caso de que no haya ningun token posible con un caracter
                # mas pero tampoco haya ninguno en estado final, terminar el
                # lexer con un error de token invalido.
                raise ValueError("Token invalido")

    return tokens_out


tests = [
    # test 1
    '''
x equal 98234;


si 6 < 7 entonces
    x equal x / 4;
sino
    x equal x / 3;
finsi
''',

    # test 2
    '''
func mult(n1; n2)
    x equal n1 * n2;
    mostrar x;
finfunc
''',

    # test 3
    '''
leer x;

i equal 0
repetir
    mostrar i;
    i equal i + 1
hasta i = x
''',

    # test 4
    '''
23hola+-sifinsi
''',

    # test 5
    ''' 
repetir
    iequali+1;
    leerx;
    x=x*x
    mostrarx;
hasta i=33
''',

    # test 6
    ''' 
vmax=0;
leer y;
si y>vmax entonces
    vmax equal y;
sino
    e equal e+1;
finsi
mostrar vmax;
mostrar e;
''',

    # test 7
    '''
repetir
    i equal i+1;
    leer nombre;
    leer edad;
    si edad>=18 entonces 
        mostrar nombre;
    sino
        vdif equal 18-edad;
        mostrar vdif;
    finsi
hasta i=20
''',

    # test 8
    '''
leer x;
leer y;
si x>y entonces 
    x equal x+y;
sino
    y equal x+y;
finsi
''',

    # test 9
    '''
func rest(n1; n2)
    x equal n1 - n2;
    mostrar x;
finfunc
''',

    # test 10
    '''
vmax equal 0;
repetir
    i equal i+1;
    leer socio;
    leer dni;
    leer edad;
    si edad>vmax entonces 
        msocio equal socio;
        mdni equal dni;
        medad equal edad;
    finsi
hasta i=50
mostrar msocio;
mostrar mdni;
mostrar medad;
''',
]


for i in range(len(tests)):
    print(f'=========TEST N°{i+1}=========')
    print(tests[i])
    print(f'---- OUTPUT \n{lexer(tests[i])}')
    print("")
    print("")
