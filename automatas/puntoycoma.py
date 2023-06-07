def afd_puntoycoma(lexema):
    if lexema == ";":
        return "FINAL"
    else:
        return "TRAMPA"
    
if afd_puntoycoma(input()):
    print("vamos puntoynahuelll")
else:
    print("nooo donde te puntoysentaste")