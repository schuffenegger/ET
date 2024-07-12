import csv
import random

trabajadores=["Juan Perez","Maria Garcia","Carlos Lopez","Ana Martinez","Pedro Rodriguez","Laura Hernandez","Miguel Sanchez","Isabel Gomez","Francisco Diaz","Elena Fernandez"]

def asignar_sueldos_aleatorios():
    sueldos = {}
    for trabajador in trabajadores:
        sueldo = random.randint(300000, 2500000)
        sueldos[trabajador] = sueldo
    return sueldos

def clasificar_sueldos(sueldos):
    sueldos_bajos = {}
    sueldos_medios = {}
    sueldos_altos = {}

    for trabajador, sueldo in sueldos.items():
        if sueldo < 800000:
            sueldos_bajos[trabajador] = sueldo
        elif sueldo < 2000000:
            sueldos_medios[trabajador] = sueldo
        elif sueldo > 2000000:
            sueldos_altos[trabajador] = sueldo
    return sueldos_bajos, sueldos_medios, sueldos_altos

def mostrar_estadisticas(sueldos):
    lista_sueldos = list(sueldos.values())

    sueldo_mas_alto = max(lista_sueldos)
    sueldo_mas_bajo = min(lista_sueldos)
    promedio_sueldos = sum(lista_sueldos) / len(lista_sueldos)

    producto = 1
    for sueldo in lista_sueldos:
        producto *= sueldo
        media_geometrica = producto ** (1 / len(lista_sueldos))
    print(f"Sueldo mas alto: ${sueldo_mas_alto}\n")
    print(f"Sueldo mas bajo: ${sueldo_mas_bajo}\n")
    print(f"Promedio de sueldos: ${promedio_sueldos}")
    print(f"Media Geometrica de sueldos: ${media_geometrica}")

def reporte_sueldos(sueldos):
    with open('reporte_sueldos.csv','w', newline = '') as file:
        file.write('| Trabajador | Sueldo Base | Descuento Salud | Descuento AFP | Sueldo Liquido |\n')
        for trabajador,sueldo in sueldos.items():
            descuento_salud = sueldo * 0.07
            descuento_afp = sueldo * 0.12
            sueldo_liquido = sueldo - descuento_salud - descuento_afp
            file.write(f'|{trabajador}|,|${sueldo}|,|${descuento_salud}|,|${descuento_afp}|,|${sueldo_liquido}|\n')
    print("\nSe ha generado el reporte de sueldos")
def main():
    sueldos = {}

    while True:
        print("\n         Menu\n1) Asignar Sueldos Aleatorios\n2) Clasificar Sueldos\n3) Mostrar Estadisticas\n4) Generar Reporte\n5) Salir\n")
        opc = input("Ingresa una opcion del menu:\n")
        while not opc.isnumeric():
            opc=input("Debes ingresar una opcion numerica:\n")
        if int(opc) == 1:
            sueldos = asignar_sueldos_aleatorios()
            print("Se han asignado")
        if int(opc) == 2:
            bajos, medios, altos = clasificar_sueldos(sueldos)
            print("\nSueldos mas bajos:\n")
            for trabajador, sueldo in bajos.items():
                print(f"{trabajador}: ${sueldo}")
            print("\nSueldos medios:\n")
            for trabajador, sueldo in medios.items():
                print(f"{trabajador}: ${sueldo}")
            print("\nSueldos mas altos:\n")
            for trabajador, sueldo in altos.items():
                print(f"{trabajador}: ${sueldo}")
        if int(opc) == 3:
            mostrar_estadisticas(sueldos)
        if int(opc) == 4:
            reporte_sueldos(sueldos)
        if int(opc) == 5:
            print("Hasta luego\n")
            break

if __name__ == "__main__":
    main()