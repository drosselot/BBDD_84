import csv

############
# Abre unidades y crea una lista de listas con la info
unidades = open('ParesV3/unidades.csv')
csv_unidades = csv.reader(unidades)

Unidades = []
x=0
for row in csv_unidades:
    if x != 0:
        Unidades.append(row)
    else:
        x += 1


# Abre direcciones y crea una lista de listas con la info
direcciones = open('direcciones.csv')
csv_direcciones = csv.reader(direcciones)

Direcciones = []
x=0
for row in csv_direcciones:
    if x != 0:
        Direcciones.append(row)
    else:
        x += 1

# Abre vehiculos y crea uan lista de listas con la info
vehiculos = open('ParesV3/vehiculos.csv')
csv_vehiculos = csv.reader(vehiculos)

Vehiculos = []
x=0
for row in csv_vehiculos:
    if x!=0:
        Vehiculos.append(row)
    else:
        x+=1

# Abre personal y crea uan lista de listas con la info
personal = open('ParesV3/personalV2.csv')
csv_personal = csv.reader(personal)

Personal = []
x=0
for row in personal:
    if x!=0:
        Personal.append(row.rstrip('\n').split(","))
    else:
        x+=1

# Abre despachos y crea una lista de listas con la info
despachos = open('ParesV3/despachosV2.csv')
csv_despachos = csv.reader(despachos)

Despachos = []
x=0
for row in despachos:
    if x!=0:
        Despachos.append(row.rstrip('\n').split(","))
    else:
        x+=1
##################

# Saca todas las comunas que existen en direcciones y unidades y crea un set, que luego convierte en lista con ids
Tabla_Comunas = set()

for row in Unidades:
    Tabla_Comunas.add(row[3])
for row in Direcciones:
    Tabla_Comunas.add(row[2])

Tabla_Comunas = list(Tabla_Comunas)
a = 0
for comuna in Tabla_Comunas:
    Tabla_Comunas[a] = [str(a+1), comuna]
    a += 1

# Tabla Personal, Administrativos y Licencias
Tabla_Personal = []
Tabla_Administrativos = []
Tabla_Licencias = set()
Tabla_RelacionVR = []

for persona in Personal:
    if persona[5]!='':
        Tabla_Personal.append([persona[0], persona[1], persona[2], persona[3], persona[4], 'administrativo'])
        Tabla_Administrativos.append([persona[0], persona[6], persona[5]])
    else:
        Tabla_Personal.append([persona[0], persona[1], persona[2], persona[3], persona[4], 'repartidor'])
        Tabla_Licencias.add((persona[0], persona[7]))
        Tabla_RelacionVR.append([persona[0], persona[8]])

# Tabla Unidades y Cobertura
Tabla_Unidades = set()
Tabla_Cobertura = []

x = 1
for unidad in Unidades:
    Tabla_Unidades.add((unidad[0], unidad[1], unidad[2]))
    Tabla_Cobertura.append([str(a), unidad[0], unidad[3]])
    x+=1

#Tabla Vehiculos, Frescos, Frios, Carga
Tabla_Vehiculos = []
Tabla_Frescos = []
Tabla_Frios = []
Tabla_Carga = []

for vehiculo in Vehiculos:
    if vehiculo[4]!='':
        Tabla_Vehiculos.append([vehiculo[0], vehiculo[1], vehiculo[9], vehiculo[2], vehiculo[3], 'carga'])
        Tabla_Carga.append([vehiculo[0], vehiculo[4], vehiculo[5]])
    elif vehiculo[6]!='':
        Tabla_Vehiculos.append([vehiculo[0], vehiculo[1], vehiculo[9], vehiculo[2], vehiculo[3], 'frescos'])
        Tabla_Frescos.append(vehiculo[6])
    else:
        Tabla_Vehiculos.append([vehiculo[0], vehiculo[1], vehiculo[9], vehiculo[2], vehiculo[3], 'cadena fria'])
        Tabla_Frescos.append([vehiculo[7], vehiculo[8]])



#########################
# Escribe lo que debería ir en la tabla Unidades
with open('Reales/Unidades.csv', mode='w', newline='') as documento:
    escritor = csv.writer(documento, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for fila in Tabla_Unidades:
        escritor.writerow(fila)

with open('Reales/Personal.csv', mode='w', newline='') as documento:
    escritor = csv.writer(documento, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for fila in Tabla_Personal:
        escritor.writerow(fila)

with open('Reales/Administrativos.csv', mode='w', newline='') as documento:
    escritor = csv.writer(documento, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for fila in Tabla_Administrativos:
        escritor.writerow(fila)

with open('Reales/Licencias.csv', mode='w', newline='') as documento:
    escritor = csv.writer(documento, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for fila in Tabla_Licencias:
        escritor.writerow(fila)

with open('Reales/Vehiculos.csv', mode='w', newline='') as documento:
    escritor = csv.writer(documento, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for fila in Tabla_Vehiculos:
        escritor.writerow(fila)

with open('Reales/Cobertura.csv', mode='w', newline='') as documento:
    escritor = csv.writer(documento, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for fila in Tabla_Cobertura:
        escritor.writerow(fila)

with open('Reales/Frescos.csv', mode='w', newline='') as documento:
    escritor = csv.writer(documento, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for fila in Tabla_Frescos:
        escritor.writerow(fila)

with open('Reales/Frios.csv', mode='w', newline='') as documento:
    escritor = csv.writer(documento, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for fila in Tabla_Frios:
        escritor.writerow(fila)

with open('Reales/Carga.csv', mode='w', newline='') as documento:
    escritor = csv.writer(documento, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for fila in Tabla_Carga:
        escritor.writerow(fila)

with open('Reales/RelacionVR.csv', mode='w', newline='') as documento:
    escritor = csv.writer(documento, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for fila in Tabla_RelacionVR:
        escritor.writerow(fila)

with open('Reales/Comunas.csv', mode='w', newline='') as documento:
    escritor = csv.writer(documento, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for fila in Tabla_Comunas:
        escritor.writerow(fila)