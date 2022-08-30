import sys
import csv

argumentos = sys.argv[1:]
nombre_del_archivo = argumentos[0]
dni_a_filtrar = argumentos[1]
salida = argumentos[2]
tipo_de_cheque = argumentos[3]

res = []

with open(nombre_del_archivo, "r") as archivo_csv:
    csv_reader = csv.reader(archivo_csv, delimiter=",")
    for fila in csv_reader:
        dni = fila[8]
        tipo = fila[9]

        if dni != dni_a_filtrar or tipo != tipo_de_cheque:
            continue
        res.append(fila)

vistos = set()
for fila in res:
    numero_cheque = fila[0]
    numero_cuenta = fila[3]
    dni = fila[8]
    if (numero_cheque, numero_cuenta, dni) in vistos:
        res.append("Los datos estan repetidos")
    else:
        vistos.add((numero_cheque, numero_cuenta, dni))

if salida == "PANTALLA":
    for fila in res:
        print(fila)
elif salida == "CSV":
    datosFiltrados = [[fila[3],fila[5],fila[6],fila[7]] for fila in res]
    with open("salida.csv") as archivo_salida:
        writer = csv.writer(archivo_salida)
        writer.writerows(datosFiltrados)
