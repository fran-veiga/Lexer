def afd_equal(lexema):
    if lexema == "=":
        return "FINAL"
    else: 
        return "TRAMPA"
    
print(afd_equal(input()))