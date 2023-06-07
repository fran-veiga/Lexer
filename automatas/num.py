def afd_num(lexema):
    if lexema.isnumeric():
        return "FINAL"
    else: 
        return "TRAMPA"
    
print(afd_num(input()))

