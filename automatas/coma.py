def afd_coma(lexema):
    if lexema == ",":
        return "FINAL"
    else:
        return "TRAMPA"
    
if afd_coma(input()):
    print("vamos nahuelll")
else:
    print("nooo donde te sentaste")