import json
import os
from datetime import datetime
from data_base import expedientes

CARPETA = os.path.dirname(os.path.abspath(__file__))
ARCHIVO = os.path.join(CARPETA, "expedientes.txt")


def guardar_expedientes():
    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(expedientes, archivo, ensure_ascii=False, indent=4)


def cargar_expedientes():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            try:
                datos = json.load(archivo)

                if isinstance(datos, list):
                    expedientes.clear()
                    expedientes.extend(datos)
                else:
                    print("El archivo no contiene datos válidos.")

            except json.JSONDecodeError:
                print("El archivo está vacío o contiene datos inválidos.")


def mostrar_expediente(expediente, contador=0):
    print(f"\n{contador}. Expediente encontrado:")
    print("{")

    print(f'    "codigo": "{expediente["codigo"]}",')
    print(f'    "fecha": "{expediente["fecha"]}",')
    print(f'    "remitente": "{expediente["remitente"]}",')
    print(f'    "tipo_documento": "{expediente["tipo_documento"]}",')
    print(f'    "asunto": "{expediente["asunto"]}",')
    print(f'    "area_destino": "{expediente["area_destino"]}",')
    print(f'    "estado": "{expediente["estado"]}",')
    print(f'    "dni": "{expediente["dni"]}"')

    print("}")


def registrar_expediente():
    codigo = input("Ingrese código del expediente: ").strip().upper()

    if codigo == "":
        print("El código no puede estar vacío.")
        return

    validar = False

    for expediente in expedientes:
        if codigo == expediente["codigo"].upper():
            validar = True
            break

    if validar:
        print(f"Ya existe un expediente con el código {codigo}.")
        return

    remitente = input("Ingrese nombre completo del remitente: ").strip()
    dni = input("Ingrese DNI del remitente: ").strip()
    tipo = input("Ingrese tipo de documento: ").strip().capitalize()
    asunto = input("Ingrese asunto: ").strip()
    fecha = input("Ingrese fecha (DD/MM/AAAA): ").strip()
    area = input("Ingrese área destinataria: ").strip().capitalize()

    if not all([remitente, dni, tipo, asunto, fecha, area]):
        print("Todos los campos son obligatorios.")
        return

    if not dni.isdigit() or len(dni) != 8:
        print("El DNI debe contener exactamente 8 dígitos.")
        return

    try:
        datetime.strptime(fecha, "%d/%m/%Y")
    except ValueError:
        print("La fecha debe ser válida y tener el formato DD/MM/AAAA.")
        return

    nuevo_expediente = {
        "codigo": codigo,
        "fecha": fecha,
        "remitente": remitente,
        "tipo_documento": tipo,
        "asunto": asunto,
        "area_destino": area,
        "estado": "Recibido",
        "dni": dni
    }

    expedientes.append(nuevo_expediente)
    guardar_expedientes()

    print(f"Se registró el expediente {codigo} correctamente.")


def buscar_expediente():
    buscar_codigo = input("Ingrese código del expediente: ").strip().upper()
    validar = False

    for expediente in expedientes:
        if buscar_codigo == expediente["codigo"].upper():
            mostrar_expediente(expediente, 1)
            validar = True
            break

    if validar == False:
        print(f"No se encontró el expediente con código {buscar_codigo}.")


def listar_expedientes():
    contador = 1

    if len(expedientes) != 0:
        for expediente in expedientes:
            mostrar_expediente(expediente, contador)
            contador += 1
    else:
        print("No hay expedientes registrados.")


def filtrar_por_area():
    buscar_area = input("Ingrese el área destinataria: ").strip()
    validar = False
    contador = 1

    for expediente in expedientes:
        if buscar_area.casefold() == expediente["area_destino"].casefold():
            mostrar_expediente(expediente, contador)
            contador += 1
            validar = True

    if validar == False:
        print(f"No se encontraron expedientes para el área {buscar_area}.")


def ordenar_por_codigo():
    if len(expedientes) != 0:
        expedientes.sort(key=lambda expediente: expediente["codigo"])
        guardar_expedientes()

        print("Expedientes ordenados por código:")
        listar_expedientes()
    else:
        print("No hay expedientes para ordenar.")


def eliminar_expediente():
    buscar_codigo = input(
        "Ingrese código del expediente a eliminar: "
    ).strip().upper()

    validar = False

    for expediente in expedientes:
        if buscar_codigo == expediente["codigo"].upper():
            mostrar_expediente(expediente, 1)
            validar = True
            break

    if validar:
        confirmacion = input(
            "¿Está seguro de eliminarlo? (s/n): "
        ).strip().lower()

        if confirmacion == "s":
            expedientes.remove(expediente)
            guardar_expedientes()
            print(f"El expediente {buscar_codigo} fue eliminado.")
        else:
            print("Eliminación cancelada.")
    else:
        print(f"No se encontró el expediente {buscar_codigo}.")

