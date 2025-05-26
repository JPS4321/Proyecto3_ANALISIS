def mtf(config, secuencia):
    lista = config[:]
    costo_total = 0

    print("Configuración inicial:", lista)
    print("\nSolicitud | Costo | Lista después de MTF")
    print("-------------------------------------------")

    for solicitud in secuencia:
        costo = lista.index(solicitud) + 1
        costo_total += costo

        # Mover al frente
        lista.remove(solicitud)
        lista.insert(0, solicitud)

        print(f"    {solicitud}     |   {costo}   | {lista}")

    print("\nCosto total de accesos:", costo_total)


# Datos del ejercicio
configuracion = [0, 1, 2, 3, 4]
secuencia = [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4]

# Ejecutar
mtf(configuracion, secuencia)
