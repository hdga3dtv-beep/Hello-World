# Registro de la verificación cruzada

- `correcciones/<lote>.json`: correcciones propuestas por el revisor técnico de cada lote
  (`id`, `field`, `new_value`, `problem`, `evidence`, `confidence`).
  Los archivos `11-complementos-*.json` son la revisión de los componentes agregados por
  los críticos de completitud.
- `veredictos.json`: decisión del verificador escéptico sobre cada corrección de los lotes
  originales (`aceptada` y `razon`).

Ya se aplicaron a `../datos/` las correcciones aceptadas por el escéptico, más las
correcciones de los componentes nuevos. Las rechazadas quedan aquí solo como registro.
- `duplicados.json`: grupos de elementos repetidos entre familias que confirmó el verificador
  escéptico. Se quitó el sobrante y sus nombres, alias y tiendas pasaron al que se quedó.
