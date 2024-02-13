Persona = {
    "Nombre":"Jennifer Lorena",
    "Apellido":"Guerrrero Perdomo",
    "Estatura":1.54,
    "Edad":20,
    "Emai":"Jenifer20lorena@gmail.com",
    "CiudadNac":"Bogotá",
    "Genero":["Femenino","Masculino","Otro"]
}

print(Persona)
print(f"El nombre de la persona es:",{Persona["Nombre"]})

Persona["Telefono"]=3057405847
print(Persona)

Persona["Celular"]=Persona.pop("Telefono")
print(Persona)

del Persona["Celular"]
print(Persona)

for clave,valor in Persona.items():
    print(clave,  ":",  valor)
