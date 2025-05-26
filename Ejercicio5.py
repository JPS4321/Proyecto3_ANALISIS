def mtf(config, secuencia):
    lista = config[:]
    costo_total = 0

    print("Configuración inicial:", lista)
    print("\nSolicitud | Costo | Lista después de MTF")
    print("-------------------------------------------")

    for solicitud in secuencia:
        costo = lista.index(solicitud) + 1
        costo_total += costo
        lista.remove(solicitud)
        lista.insert(0, solicitud)
        print(f"    {solicitud}     |   {costo}   | {lista}")

    print("\nCosto total de accesos:", costo_total)
    print("-" * 50)
    return costo_total


# Parte A: Repetición del número 2
configuracion = [0, 1, 2, 3, 4]
secuencia_2 = [2] * 20
print("🔹 Accesos con 20 repeticiones del número 2")
costo_2 = mtf(configuracion, secuencia_2)

# Parte B: Repetición del número 3
print("\n🔹 Accesos con 20 repeticiones del número 3")
costo_3 = mtf(configuracion, [3] * 20)


