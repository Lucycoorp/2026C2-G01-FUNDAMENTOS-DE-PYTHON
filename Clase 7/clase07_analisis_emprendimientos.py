"""Practica Semana 07: analisis de emprendimientos costarricenses.

Complete los espacios marcados con TODO. El objetivo es generar un reporte por
sede usando listas, diccionarios, funciones, ciclos y condicionales.
"""

from sedes import sedes

print("Datos cargados:", len(sedes), "sedes")
print("Primera sede:", sedes[0])


def eliminar_sedes_duplicadas(sedes):
    """Retorna una lista de sedes sin nombres repetidos.

    Si dos sedes tienen el mismo nombre, conserva solo la primera aparicion
    e informa por consola cuales nombres estaban duplicados.
    """
    nombres_vistos = set()
    sedes_unicas = []
    nombres_duplicados = []

    for sede in sedes:
        nombre = sede["nombre"]
        if nombre not in nombres_vistos:
            nombres_vistos.add(nombre)
            sedes_unicas.append(sede)
        else:
            nombres_duplicados.append(nombre)

    if nombres_duplicados:
        print(f"Aviso: se encontraron sedes duplicadas y fueron omitidas: {nombres_duplicados}")

    return sedes_unicas


def calcular_total(ventas):
    """Retorna la suma de una lista de ventas."""
    return sum(ventas)


def calcular_promedio(ventas):
    """Retorna el promedio de una lista de ventas."""
    return sum(ventas) / len(ventas)


def calcular_porcentaje_cumplimiento(total, meta):
    """Retorna el porcentaje de cumplimiento respecto a la meta."""
    return total / meta * 100


def clasificar_sede(total, meta):
    """Clasifica una sede segun su total semanal y su meta."""
    if total >= meta:
        return "Meta alcanzada"
    if total >= meta * 0.8:
        return "Cerca de la meta"
    return "Requiere atencion"


def crear_reporte(sedes):
    """Construye los datos calculados para cada sede."""
    reporte = []

    for sede in sedes:
        total = calcular_total(sede["ventas"])
        promedio = calcular_promedio(sede["ventas"])
        porcentaje = calcular_porcentaje_cumplimiento(total, sede["meta"])
        estado = clasificar_sede(total, sede["meta"])

        reporte.append(
            {
                "nombre": sede["nombre"],
                "provincia": sede["provincia"],
                "tipo": sede["tipo"],
                "total": total,
                "promedio": promedio,
                "porcentaje": porcentaje,
                "estado": estado,
            }
        )

    return reporte


def mostrar_reporte(reporte):
    """Imprime el reporte de analisis."""
    print("REPORTE DE EMPRENDIMIENTOS CR")
    print("-" * 72)

    for fila in reporte:
        print(f"Sede: {fila['nombre']}")
        print(f"Provincia: {fila['provincia']}")
        print(f"Tipo: {fila['tipo']}")
        print(f"Total semanal: C{fila['total']:,.0f}")
        print(f"Promedio diario: C{fila['promedio']:,.0f}")
        print(f"Cumplimiento: {fila['porcentaje']:.1f}%")
        print(f"Estado: {fila['estado']}")
        print("-" * 72)


def mostrar_resumen(reporte):
    """Imprime resultados agregados usando set y tuplas."""
    provincias = set()
    sedes_atencion = []
    ranking = []

    for fila in reporte:
        provincias.add(fila["provincia"])
        ranking.append((fila["nombre"], fila["total"]))

        if fila["estado"] == "Requiere atencion":
            sedes_atencion.append(fila["nombre"])

    ranking_ordenado = sorted(ranking, key=lambda par: par[1], reverse=True)
    mejor_sede, mejor_total = ranking_ordenado[0]

    print("RESUMEN FINAL")
    print(f"Provincias presentes: {provincias}")
    print(f"Sedes que requieren atencion: {sedes_atencion}")
    print(f"Mejor sede: {mejor_sede} con C{mejor_total:,.0f}")
    print("Ranking:")

    for posicion, (nombre, total) in enumerate(ranking_ordenado, start=1):
        print(f"{posicion}. {nombre}: C{total:,.0f}")


def ejecutar_pruebas():
    """Validaciones minimas para la solucion docente."""
    assert calcular_total([100, 200, 300]) == 600
    assert calcular_promedio([100, 200, 300]) == 200
    assert calcular_porcentaje_cumplimiento(450000, 450000) == 100
    assert clasificar_sede(500000, 450000) == "Meta alcanzada"
    assert clasificar_sede(380000, 450000) == "Cerca de la meta"
    assert clasificar_sede(250000, 450000) == "Requiere atencion"

    sedes_prueba = [
        {"nombre": "Marisqueria Puntarenas", "provincia": "Puntarenas",
         "tipo": "Restaurante", "ventas": [1, 1, 1, 1, 1], "meta": 1},
        {"nombre": "Marisqueria Puntarenas", "provincia": "Puntarenas",
         "tipo": "Restaurante", "ventas": [1, 1, 1, 1, 1], "meta": 1},
        {"nombre": "Soda San Pedro", "provincia": "San Jose",
         "tipo": "Alimentacion", "ventas": [1, 1, 1, 1, 1], "meta": 1},
    ]
    sedes_unicas = eliminar_sedes_duplicadas(sedes_prueba)
    assert len(sedes_unicas) == 2
    assert sedes_unicas[0]["nombre"] == "Marisqueria Puntarenas"
    assert sedes_unicas[1]["nombre"] == "Soda San Pedro"


if __name__ == "__main__":
    ejecutar_pruebas()
    sedes_sin_duplicados = eliminar_sedes_duplicadas(sedes)
    reporte = crear_reporte(sedes_sin_duplicados)
    mostrar_reporte(reporte)
    mostrar_resumen(reporte)