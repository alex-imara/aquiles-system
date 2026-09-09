#!/usr/bin/env python3
"""Traduce las zonas de un export de Boleto Movil a las zonas de Fernando.

Se detiene si una zona no esta en el catalogo, y se detiene si los totales
no cuadran antes y despues del mapeo. Nunca ajusta un numero por su cuenta.

    python3 scripts/mapea_zonas.py [config.json]

Requiere openpyxl solo si el export viene en .xlsx.
"""

import csv
import json
import re
import sys
from collections import defaultdict
from decimal import Decimal, InvalidOperation
from pathlib import Path


class Alto(Exception):
    """Algo no cuadra y no se sigue."""


def normaliza(texto):
    """Zona comparable: sin acentos de espacio, sin mayusculas, sin dobles espacios."""
    return re.sub(r"\s+", " ", str(texto or "").strip()).upper()


def a_numero(valor, campo, renglon):
    if valor is None or str(valor).strip() == "":
        return Decimal(0)
    limpio = re.sub(r"[^\d.\-]", "", str(valor))
    try:
        return Decimal(limpio or "0")
    except InvalidOperation:
        raise Alto(f"Renglon {renglon}: '{valor}' no es un numero en la columna {campo}.")


def lee_tabla(ruta, hoja, fila_encabezado):
    """Regresa (encabezados, renglones) de un .csv o .xlsx."""
    ruta = Path(ruta)
    if not ruta.exists():
        raise Alto(f"No existe el archivo {ruta}.")

    if ruta.suffix.lower() in {".csv", ".txt"}:
        with ruta.open(newline="", encoding="utf-8-sig") as f:
            filas = list(csv.reader(f))
    elif ruta.suffix.lower() in {".xlsx", ".xlsm"}:
        try:
            import openpyxl
        except ImportError:
            raise Alto("El export es .xlsx y falta openpyxl. Instalalo con: pip install openpyxl")
        libro = openpyxl.load_workbook(ruta, data_only=True, read_only=True)
        pagina = libro[hoja] if hoja else libro[libro.sheetnames[0]]
        filas = [list(r) for r in pagina.iter_rows(values_only=True)]
    else:
        raise Alto(f"No se que hacer con un archivo {ruta.suffix}.")

    if len(filas) < fila_encabezado:
        raise Alto(f"{ruta} tiene menos renglones que la fila de encabezado indicada.")

    encabezados = [str(c).strip() if c is not None else "" for c in filas[fila_encabezado - 1]]
    cuerpo = [f for f in filas[fila_encabezado:] if any(c not in (None, "") for c in f)]
    return encabezados, cuerpo


def lee_catalogo(cfg):
    ruta = Path(cfg["archivo"])
    if not ruta.exists():
        raise Alto(f"No existe el catalogo de zonas en {ruta}.")

    mapa, repetidas = {}, []
    with ruta.open(newline="", encoding="utf-8-sig") as f:
        for fila in csv.DictReader(f):
            origen = normaliza(fila.get(cfg["columna_origen"]))
            destino = str(fila.get(cfg["columna_destino"]) or "").strip()
            if not origen or not destino:
                continue
            if origen in mapa and mapa[origen] != destino:
                repetidas.append(origen)
            mapa[origen] = destino

    if repetidas:
        raise Alto(
            "El catalogo tiene la misma zona de Boleto Movil apuntando a dos zonas "
            "distintas de Fernando: " + ", ".join(sorted(set(repetidas)))
        )
    if not mapa:
        raise Alto(f"El catalogo {ruta} esta vacio.")
    return mapa


def main(ruta_config="config.json"):
    cfg = json.loads(Path(ruta_config).read_text(encoding="utf-8"))
    exp = cfg["export"]
    cols = exp["columnas"]

    faltantes = [k for k, v in cols.items() if not v or v == "PENDIENTE"]
    if faltantes:
        raise Alto(
            "Faltan nombres de columna en config.json: " + ", ".join(faltantes) +
            ". Salen del primer export crudo de Boleto Movil."
        )

    encabezados, renglones = lee_tabla(exp["archivo"], exp.get("hoja"), exp.get("fila_encabezado", 1))
    indice = {h: i for i, h in enumerate(encabezados)}

    sin_columna = [v for v in cols.values() if v not in indice]
    if sin_columna:
        raise Alto(
            "El export no trae estas columnas: " + ", ".join(sin_columna) +
            ".\nLo que si trae: " + ", ".join(h for h in encabezados if h)
        )

    def campo(fila, nombre):
        i = indice[cols[nombre]]
        return fila[i] if i < len(fila) else None

    # Totales del archivo crudo. Contra estos se cuadra todo lo demas.
    boletos_antes = Decimal(0)
    importe_antes = Decimal(0)
    for n, fila in enumerate(renglones, start=exp.get("fila_encabezado", 1) + 1):
        boletos_antes += a_numero(campo(fila, "boletos"), cols["boletos"], n)
        importe_antes += a_numero(campo(fila, "importe"), cols["importe"], n)

    catalogo = lee_catalogo(cfg["catalogo"])

    huerfanas = defaultdict(lambda: [Decimal(0), Decimal(0)])
    corte = defaultdict(lambda: [Decimal(0), Decimal(0)])

    for n, fila in enumerate(renglones, start=exp.get("fila_encabezado", 1) + 1):
        zona_cruda = str(campo(fila, "zona") or "").strip()
        boletos = a_numero(campo(fila, "boletos"), cols["boletos"], n)
        importe = a_numero(campo(fila, "importe"), cols["importe"], n)
        destino = catalogo.get(normaliza(zona_cruda))

        if destino is None:
            huerfanas[zona_cruda or "(vacia)"][0] += boletos
            huerfanas[zona_cruda or "(vacia)"][1] += importe
            continue

        llave = (
            str(campo(fila, "partido") or "").strip(),
            str(campo(fila, "fecha") or "").strip(),
            destino,
        )
        corte[llave][0] += boletos
        corte[llave][1] += importe

    if huerfanas:
        detalle = "\n".join(
            f"  {z}  ->  {b} boletos, {i} de importe"
            for z, (b, i) in sorted(huerfanas.items())
        )
        raise Alto(
            "Estas zonas del reporte no estan en el catalogo:\n" + detalle +
            "\n\nAgregalas a catalogo-zonas.csv con la zona de Fernando que les toca "
            "y vuelve a correr. No se carga un corte incompleto."
        )

    boletos_despues = sum((v[0] for v in corte.values()), Decimal(0))
    importe_despues = sum((v[1] for v in corte.values()), Decimal(0))

    if boletos_despues != boletos_antes or importe_despues != importe_antes:
        raise Alto(
            "El corte no cuadra contra el archivo crudo.\n"
            f"  boletos: {boletos_antes} antes / {boletos_despues} despues\n"
            f"  importe: {importe_antes} antes / {importe_despues} despues\n"
            "Revisa si hay renglones duplicados en el export."
        )

    salida = Path(cfg["salidas"]["corte"])
    salida.parent.mkdir(parents=True, exist_ok=True)
    with salida.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["partido", "fecha", "zona_fernando", "boletos", "importe"])
        for (partido, fecha, zona), (b, i) in sorted(corte.items()):
            w.writerow([partido, fecha, zona, b, i])

    reporte = Path(cfg["salidas"]["reporte"])
    reporte.parent.mkdir(parents=True, exist_ok=True)
    lineas = [
        f"# Mapeo de zonas — {Path(exp['archivo']).name}",
        "",
        f"- Renglones leidos: {len(renglones)}",
        f"- Renglones del corte: {len(corte)}",
        f"- Boletos: {boletos_antes} (cuadra)",
        f"- Importe: {importe_antes} (cuadra)",
        "",
        "| Zona de Fernando | Boletos | Importe |",
        "|---|---:|---:|",
    ]
    por_zona = defaultdict(lambda: [Decimal(0), Decimal(0)])
    for (_, _, zona), (b, i) in corte.items():
        por_zona[zona][0] += b
        por_zona[zona][1] += i
    for zona, (b, i) in sorted(por_zona.items()):
        lineas.append(f"| {zona} | {b} | {i} |")
    reporte.write_text("\n".join(lineas) + "\n", encoding="utf-8")

    print(f"Listo. {len(corte)} renglones en {salida}")
    print(f"Boletos {boletos_antes}, importe {importe_antes}. Cuadra contra el crudo.")
    print(f"Resumen por zona en {reporte}")


if __name__ == "__main__":
    try:
        main(sys.argv[1] if len(sys.argv) > 1 else "config.json")
    except Alto as e:
        print(f"\nALTO: {e}\n", file=sys.stderr)
        sys.exit(1)
