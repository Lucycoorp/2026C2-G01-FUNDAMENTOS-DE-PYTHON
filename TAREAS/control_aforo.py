
CAPACIDAD_MAXIMA = 700

ocupacion_actual = 0
grupos_aceptados = []
grupos_rechazados = []

entrada = ""

while entrada != "fin":
    entrada = input("Ingrese el tamaño del grupo (o 'fin' para terminar): ").strip().lower()

    if entrada == "fin":
        break

    try:
        grupo = int(entrada)
    except ValueError:
        print("Entrada inválida. Ingrese un número entero mayor que cero o 'fin'.")
        continue

    if grupo <= 0:
        print("Entrada inválida. El tamaño del grupo debe ser mayor que cero.")
        continue

    if ocupacion_actual + grupo <= CAPACIDAD_MAXIMA:
        ocupacion_actual += grupo
        grupos_aceptados.append(grupo)
        espacios_disponibles = CAPACIDAD_MAXIMA - ocupacion_actual
        print(f"Grupo ACEPTADO.")
        print(f"  Ocupación actual: {ocupacion_actual} personas | Espacios disponibles: {espacios_disponibles}")
    else:
        grupos_rechazados.append(grupo)
        espacios_disponibles = CAPACIDAD_MAXIMA - ocupacion_actual
        print(f"Grupo RECHAZADO. No hay espacio suficiente.")
        print(f"  Ocupación actual: {ocupacion_actual} personas | Espacios disponibles: {espacios_disponibles}")

# Reporte final
print("\n" + "=" * 50)
print("REPORTE FINAL")
print("=" * 50)
print(f"Grupos aceptados:   {len(grupos_aceptados)}")
print(f"Grupos rechazados:  {len(grupos_rechazados)}")
print(f"Personas admitidas: {ocupacion_actual}")
print(f"Capacidad máxima:   {CAPACIDAD_MAXIMA}")
print(f"Espacios libres:    {CAPACIDAD_MAXIMA - ocupacion_actual}")

if CAPACIDAD_MAXIMA > 0:
    porcentaje = (ocupacion_actual / CAPACIDAD_MAXIMA) * 100
    print(f"Porcentaje de ocupación: {porcentaje:.1f}%")

if len(grupos_aceptados) > 0:
    print(f"Grupo aceptado más pequeño: {min(grupos_aceptados)}")
    print(f"Grupo aceptado más grande:  {max(grupos_aceptados)}")
else:
    print("No se aceptó ningún grupo.")

if ocupacion_actual < 560:
    estado = "disponibilidad normal"
elif ocupacion_actual <= 699:
    estado = "ocupación preventiva"
else:
    estado = "capacidad completa"

print(f"Estado final: {estado.upper()}")
print("=" * 50)
