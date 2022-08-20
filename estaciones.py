mes = input ("Digita el mes: ")

if(mes == "enero" or mes == "febrero" or mes == "marzo"):
    print(f'estas en {mes} es invierno')
elif(mes == "abril" or mes == "mayo" or mes == "junio"):
    print(f'estas en {mes}  es primavera')
elif(mes == "julio" or mes == "agosto" or mes == "septiembre"):
    print(f'estas en {mes} es verano')
elif(mes == "octubre" or mes == "noviembre" or mes == "diciembre"):
    print(f'estas en {mes} es otoño')
else:
    print("no se reconocio el mes")