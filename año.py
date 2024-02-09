def es_bisiesto(año):
   
    if año % 400 == 0:
        return True
    elif año % 100 == 0:
        return False
    elif año % 4 == 0:
        return True
    else:
        return False
    
print("Ingrese el año:", es_bisiesto)