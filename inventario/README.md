# Inventario de componentes electrónicos

Inventario de los componentes, módulos, materiales y herramientas más comunes en
tiendas de electrónica de México y Latinoamérica (Steren, AG Electrónica, UNIT
Electronics, Geek Factory, 5Hertz, tiendas de la Rep. del Salvador en el Centro de
CDMX) para hacer pistas y tarjetas electrónicas caseras. Es la base de datos para una
aplicación de diseño de pistas (PCB).

El catálogo legible, con conteos por categoría, está en [INVENTARIO.md](INVENTARIO.md).

## Archivos

| Archivo | Para qué sirve |
|---|---|
| `componentes.json` | Todo el inventario en un solo archivo, listo para que la app lo cargue. |
| `componentes.csv` | Vista plana para abrir en una hoja de cálculo. |
| `INVENTARIO.md` | Catálogo por categoría (nombre, montaje, huella, valores comunes). |
| `datos/*.json` | Fuente editable, un archivo por familia de componentes. |
| `ESQUEMA.md` | Descripción de cada campo de un componente. |
| `build.py` | Valida `datos/` y regenera `componentes.json`, `componentes.csv` e `INVENTARIO.md`. |
| `aplicar_revision.py` | Aplica a `datos/` las correcciones, altas y duplicados de una verificación cruzada. |

Para regenerar después de editar `datos/`:

```sh
python3 inventario/build.py
```

## Qué trae cada componente

Además del nombre, alias, descripción, valores comunes, especificaciones, usos y
tiendas, cada componente incluye lo que la app de pistas necesita para dibujarlo:

- `mounting`: `THT`, `SMD`, `THT/SMD`, `modulo`, `panel` o `n/a`.
- `packages`: encapsulados o formatos físicos con número de pines, paso entre pines
  (`pitch_mm`), separación entre filas (`row_spacing_mm`, p. ej. DIP angosto 7.62 mm
  o ancho 15.24 mm), dimensiones del cuerpo y diámetro de terminal.
- `pinout`: lista de pines (número, nombre y función) para circuitos integrados,
  transistores, reguladores, módulos y placas; polaridad para componentes de dos
  terminales.
- `schematic_symbol`: identificador sugerido del símbolo esquemático.

El detalle de cada campo está en [ESQUEMA.md](ESQUEMA.md).

## Cómo se hizo

1. Diez agentes de investigación, uno por familia de componentes, consultaron
   catálogos de tiendas y hojas de datos y llenaron `datos/` con el mismo esquema.
2. Una verificación cruzada revisó cada lote: un revisor técnico buscó errores de
   pinout, huella y especificaciones, y un verificador escéptico intentó refutar cada
   corrección; solo se aplicaron las que el escéptico aceptó.
3. Críticos por dominio buscaron componentes comunes que faltaban y un último paso
   eliminó duplicados entre familias.

## Limitaciones

- **Medidas aproximadas.** El cupo de búsquedas web se agotó durante la investigación y
  los sitios de las tiendas no se pudieron abrir directamente, así que muchas medidas y
  pinouts salen del conocimiento de hojas de datos de los agentes. Lo no verificado
  está marcado como «aprox.» o «verificar» en `notes`, o en `null`. **Antes de fabricar
  una placa, confirma la huella con la hoja de datos del fabricante de la pieza que
  compraste**: el orden de pines de algunos transistores (p. ej. 2N2222 vs PN2222A vs
  P2N2222A) y de los módulos chinos cambia entre fabricantes.
- **Precios.** Casi todos están en `null`; los pocos que hay son aproximados y vienen
  de Steren o UNIT.
- **Tiendas.** La lista de `stores` indica dónde se encuentra típicamente cada pieza; no
  todas las tiendas se pudieron verificar en línea (AG Electrónica, Geek Factory y
  5Hertz quedaron con verificación parcial).
- **La tienda «Idea».** No se pudo identificar con certeza. Las candidatas más cercanas
  son IDEAR Electrónica (Tehuantepec 286, Col. Hipódromo, CDMX) e IDESA Electrónica
  (Cd. Juárez).
