import os
import csv
import random
clean="cls"
trabajadores=[["1.Juan Perez", "2.Maria Garcia", "3.Carlos Lopez", "4.Ana Martinez", "5.Pedro Rodriguez", "6.Laura Hernandez", "7.Miguel Sanchez", "8.Isabel Gomez", "9.Francisco Diaz", "10.Elena Fernandez"]]
sueldo1=random.randint(300000,2500000)
sueldo2=random.randint(300000,2500000)
sueldo3=random.randint(300000,2500000)
sueldo4=random.randint(300000,2500000)
sueldo5=random.randint(300000,2500000)
sueldo6=random.randint(300000,2500000)
sueldo7=random.randint(300000,2500000)
sueldo8=random.randint(300000,2500000)
sueldo9=random.randint(300000,2500000)
sueldo10=random.randint(300000,2500000)
juan=sueldo1
maria=sueldo2
carlos=sueldo3
ana=sueldo4
pedro=sueldo5
laura=sueldo6
miguel=sueldo7
isabel=sueldo8
francisco=sueldo9
elena=sueldo10

os.system(clean)

def calculo_de_sueldo(sueldo):
    desc_salud=round(sueldo*0.07)
    desc_afp=round(sueldo*0.12)
    liquido=round(sueldo-desc_afp-desc_salud)
    return print(f"Sueldo bruto: ${sueldo}\nDescuento salud: ${desc_salud}\nDescuento AFP: ${desc_afp}\nSueldo Liquido: ${liquido}") 

def estadistica():
    trabajador=[sueldo1,sueldo2,sueldo3,sueldo4,sueldo5,sueldo6,sueldo7,sueldo8,sueldo9,sueldo10]
    media_geometrica==media_geometrica(trabajador)
    print(media_geometrica)


def media_geometrica(data):
    producto=1
    for valor in data:
        producto*=valor
    return producto**(1/len(data))

def sueldo_trabajador():
    trabajador=[sueldo1,sueldo2,sueldo3,sueldo4,sueldo5,sueldo6,sueldo7,sueldo8,sueldo9,sueldo10]
    trabajadores.append([trabajador])
    print("Sueldo generados correctamente")
    for trabajador in trabajadores:
        print(trabajador)

def clasificar_sueldo():
    trabajadores=[["1.Juan Perez", "2.Maria Garcia", "3.Carlos Lopez", "4.Ana Martinez", "5.Pedro Rodriguez", "6.Laura Hernandez", "7.Miguel Sanchez", "8.Isabel Gomez", "9.Francisco Diaz", "10.Elena Fernandez"],
    [sueldo1,sueldo2,sueldo3,sueldo4,sueldo5,sueldo6,sueldo7,sueldo8,sueldo9,sueldo10]]

def guardar_archivo():
    with open("archivo.csv", mode="w", newline="") as archivo_csv:
        guardar=csv.writer(archivo_csv)
        guardar.writerow(trabajadores)
    print("Archivo guardado correctamente")
    
def cargar_archivo():
    try:
        with open("archivo.csv", mode="r") as archivo_csv:
            leer=csv.DictReader(archivo_csv)
            for fila in leer:
                trabajadores.append(fila)
            print("Archivo cargado correctamente")
    except FileNotFoundError:
        print("Archivo no encontrado")

def reporte_de_sueldo():
    for i in trabajadores:
        for fila in i:
            print(fila)
    res=input("Seleccione el trabajador para ver los detalles: ")
    if res=="1":
        print("Nombre del trabajador: Juan Perez")
        calculo_de_sueldo==calculo_de_sueldo(juan)
    elif res=="2":
        print("Nombre del trabajador: Maria Garia")
        calculo_de_sueldo==calculo_de_sueldo(maria)
    elif res=="3":
        print("Nombre del trabajador: Carlos Lopez")
        calculo_de_sueldo==calculo_de_sueldo(carlos)
    elif res=="4":
        print("Nombre del trabajador: Ana Martinez")
        calculo_de_sueldo==calculo_de_sueldo(ana)
    elif res=="5":
        print("Nombre del trabajador: Pedro Rodriguez")
        calculo_de_sueldo==calculo_de_sueldo(pedro)
    elif res=="6":
        print("Nombre del trabajador: Laura Hernandez")
        calculo_de_sueldo==calculo_de_sueldo(laura)
    elif res=="7":
        print("Nombre del trabajador: Miguel Sanchez")
        calculo_de_sueldo==calculo_de_sueldo(miguel)
    elif res=="8":
        print("Nombre del trabajador: Isabel Gomez")
        calculo_de_sueldo==calculo_de_sueldo(isabel)
    elif res=="9":
        print("Nombre del trabajador: Francisco Diaz")
        calculo_de_sueldo==calculo_de_sueldo(francisco)
    elif res=="10":
        print("Nombre del trabajador: Helena Fernandez")
        calculo_de_sueldo==calculo_de_sueldo(elena)
    else:
        print("Ingrese un numero valido")
        reporte_de_sueldo()

def menu():
    cargar_archivo()
    menu_principal=1
    while menu_principal==1:
        print("1. Asignar sueldos.\n2. Clasificar sueldos.\n3. Ver estadisticas.\n4. Reporte de sueldo.\n5. salir")
        opcion=input("Seleccione una opcion: ")
        if opcion=="1":
            os.system(clean)
            sueldo_trabajador()
        elif opcion=="2":
            os.system(clean)
            clasificar_sueldo()
        elif opcion=="3":
            os.system(clean)
            estadistica()
        elif opcion=="4":
            os.system(clean)
            reporte_de_sueldo()
        elif opcion=="5":
            os.system(clean)
            guardar_archivo()
            print("Finalizando programa...\nDesarrollado por Ruby Martinez\nRUT: 19.500.090-5")
            menu_principal=0

menu()

