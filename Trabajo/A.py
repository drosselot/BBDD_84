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

print(Tabla_Comunas)
Tabla_Comunas = list(Tabla_Comunas)
print(Tabla_Comunas)
a = 0
for comuna in Tabla_Comunas:
    Tabla_Comunas[a] = [str(a+1), comuna]
    a += 1
print(Tabla_Comunas)

# Tabla Personal, Administrativos y Licencias
Tabla_Personal = []
Tabla_Administrativos = []
Tabla_Licencias = set()
Tabla_RelacionVR = []
z = 1
v = 1

for persona in Personal:
    if persona[5]!='':
        Tabla_Personal.append([persona[0], persona[1], persona[2], persona[3], persona[4], 'administrativo'])
        Tabla_Administrativos.append([persona[0], persona[6], persona[5]])
    else:
        a = 0
        for repartidor in Tabla_Personal:
            if repartidor[0] == persona[0]:
                a = 1

        if a == 0:
            Tabla_Personal.append([persona[0], persona[1], persona[2], persona[3], persona[4], 'repartidor'])
        
        b = 0
        for licencia in Tabla_Licencias:
            if licencia[1] == persona[7]:
                b = 1
        
        if b == 0:
            Tabla_Licencias.add((str(z), persona[0], persona[7]))
            z+=1

        Tabla_RelacionVR.append([str(v), persona[8], persona[0]])
        v+=1

# Tabla Unidades y Cobertura
Tabla_Unidades = set()
Tabla_Cobertura = []

print(Tabla_Comunas)
x = 1
for unidad in Unidades:
    Tabla_Unidades.add((unidad[0], unidad[1], unidad[2]))
    for comuna in Tabla_Comunas:
        if comuna[1] == unidad[3]:
            Tabla_Cobertura.append([str(x), unidad[0], comuna[0]])
    x+=1
print(Tabla_Comunas)

#Tabla Vehiculos, Frescos, Frios, Carga
Tabla_Vehiculos = []
Tabla_Frescos = []
Tabla_Frios = []
Tabla_Carga = []
Tabla_Vehiculos_Ninguno = []

for vehiculo in Vehiculos:
    if vehiculo[4]!='':
        Tabla_Vehiculos.append([vehiculo[0], vehiculo[1], vehiculo[9], vehiculo[2], vehiculo[3], 'carga'])
        Tabla_Carga.append([vehiculo[0], vehiculo[4], vehiculo[5]])
    elif vehiculo[6]!='':
        Tabla_Vehiculos.append([vehiculo[0], vehiculo[1], vehiculo[9], vehiculo[2], vehiculo[3], 'frescos'])
        Tabla_Frescos.append([vehiculo[0], vehiculo[6]])
    elif vehiculo[7]!='':
        Tabla_Vehiculos.append([vehiculo[0], vehiculo[1], vehiculo[9], vehiculo[2], vehiculo[3], 'cadena fria'])
        Tabla_Frios.append([vehiculo[0], vehiculo[7], vehiculo[8]])
    else:
        Tabla_Vehiculos.append([vehiculo[0], vehiculo[1], vehiculo[9], vehiculo[2], vehiculo[3], 'ninguno'])

#Tabla Direcciones
Tabla_Direcciones = []

for direccion in Direcciones:
    a = 0
    for comuna in Tabla_Comunas:
        if direccion[2] == comuna[1]:
            Tabla_Direcciones.append([direccion[0], direccion[1], comuna[0]])
            a = 1
    if a == 0:
        print('error')

print(Tabla_Comunas)
# Tabla Despachos
Tabla_Despachos = []

for despacho in Despachos:
    Tabla_Despachos.append(despacho)


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
        print(fila)

print(Tabla_Comunas)
        
with open('Reales/Direcciones.csv', mode='w', newline='') as documento:
    escritor = csv.writer(documento, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for fila in Tabla_Direcciones:
        escritor.writerow(fila)
        
with open('Reales/Despachos.csv', mode='w', newline='') as documento:
    escritor = csv.writer(documento, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for fila in Tabla_Despachos:
        escritor.writerow(fila)
        
with open('Reales/Vehiculos_Ninguno.csv', mode='w', newline='') as documento:
    escritor = csv.writer(documento, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for fila in Tabla_Vehiculos_Ninguno:
        escritor.writerow(fila)
        
