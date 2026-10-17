from procesos import (
    cargar_expedientes,
    registrar_expediente,
    buscar_expediente,
    listar_expedientes,
    filtrar_por_area,
    ordenar_por_codigo,
    eliminar_expediente
)


cargar_expedientes()

while True:
    print("""
===== MESA DE PARTES - CENTRO MÉDICO =====

1. Registrar expediente
2. Buscar expediente por código
3. Listar expedientes
4. Filtrar por área destinataria
5. Ordenar por código
6. Eliminar expediente
7. Guardar expedientes
0. Salir
""")

    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        registrar_expediente()

    elif opcion == "2":
        buscar_expediente()

    elif opcion == "3":
        listar_expedientes()

    elif opcion == "4":
        filtrar_por_area()

    elif opcion == "5":
        ordenar_por_codigo()

    elif opcion == "6":
        eliminar_expediente()

    elif opcion == "7":
        from procesos import guardar_expedientes
        guardar_expedientes()
        print("Expedientes guardados.")

    elif opcion == "0":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida. Intente nuevamente.")
