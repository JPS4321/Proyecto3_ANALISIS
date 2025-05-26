def imtf(config, secuencia):
    lista = config[:]
    costo_total = 0

    print("Configuración inicial:", lista)
    print("\nSolicitud | Costo | Lista después de IMTF")
    print("--------------------------------------------")

    for idx, solicitud in enumerate(secuencia):
        i = lista.index(solicitud)
        costo = i + 1
        costo_total += costo

        # Mirada hacia adelante
        lookahead = secuencia[idx + 1: idx + i]  # i - 1 elementos siguientes
        mover = solicitud in lookahead

        if mover:
            lista.remove(solicitud)
            lista.insert(0, solicitud)

        print(f"    {solicitud}     |   {costo}   | {lista}")

    print("\nCosto total de accesos:", costo_total)
    print("-" * 50)
    return costo_total


# Casos de prueba: mejor y peor caso de MTF
configuracion = [0, 1, 2, 3, 4]
mejor = [0] * 20          # Mismo elemento repetido 20 veces
peor  = [4, 3, 2, 1, 0] * 4  # Alternancia que genera máximo costo en MTF

print("🔹 Mejor caso de MTF usando IMTF")
costo_mejor = imtf(configuracion, mejor)

print("\n🔹 Peor caso de MTF usando IMTF")
costo_peor = imtf(configuracion, peor)
