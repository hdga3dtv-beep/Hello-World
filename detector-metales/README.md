# Detector de metales PI — proyecto de diagramas para armado

Detector de metales **por inducción de pulsos** (tipo "Pirat"): `NE555` genera
pulsos → `IRF840` conmuta la bobina → `TL072` amplifica/compara el eco → `BC547`
hace sonar el parlante. Estos archivos ayudan a **armar la placa** a quien no sabe
leer el esquemático oficial.

> **Rama de trabajo:** `claude/diagrama-u2-c5-c7-componentes-9ywhjx`
> Todo está commiteado y pusheado a GitHub (`hdga3dtv-beep/Hello-World`).
> Para seguir en otro chat: abrir el repo, esa rama, y esta carpeta.

## Archivos de esta carpeta

| Archivo | Qué es |
|---|---|
| `conexiones.html` | **Principal.** Mapa de conexiones por nodos: componentes en su posición real dibujados como lo que son, patas marcadas entrada/salida/alimentación, ruteo ortogonal tipo "peine", panel emergente por componente, aislamiento por nodo y tabla de nodos. Es un artifact autocontenido. |
| `mapa-placa.html` | Primera versión: mapa de la placa que identifica cada designador de la serigrafía (R1…R18, C1…C8, U1/U2, Q1…Q3, D2/D3, P1…P3) con su componente, valor y código de colores. |
| `LISTA-COMPONENTES.md` | La lista de componentes en tabla + orden de soldadura + qué hace cada bloque. |

### Artifacts publicados (claude.ai)
- Mapa de conexiones: https://claude.ai/code/artifact/cec2557c-d5b3-4d40-8c56-679ef58a4cdc
- Mapa de la placa: https://claude.ai/code/artifact/30a73ef3-18ea-4eb0-9dbd-ddf0684ec6ee

## Cómo se genera el diagrama de conexiones

`conexiones.html` se arma con la skill **`pcb-node-diagram`** (en
`.claude/skills/pcb-node-diagram/`). Todo el diagrama sale de **un solo objeto
JSON** embebido en `<script id="netdata">` (componentes + nodos + info). El mismo
netlist está en `.claude/skills/pcb-node-diagram/references/example-detector.json`.
Para editar: cambiar ese JSON y republicar el artifact (misma ruta = misma URL).

### Netlist (resumen de nodos)
`+12`, `GND`, `TIM`(555 2/6), `DISCH`(555 7), `RT`(R2/R18), `CONT`(555 5),
`OUT5`(555 3), `QB`/`QC`(Q3), `GATE`/`DRAIN`(Q2), `CLAMP`(D2/D3), `SAMP`(R4/C3),
`VREF`(R5/R6), `AIN`/`AOUT`(U2 1ª etapa), `POT`, `BINp`/`BINn`/`BOUT`(U2 2ª etapa),
`QBAS`/`QCOL`(Q1), `SPK`. Detalle pata por pata: tabla de nodos en `conexiones.html`.

## Estado y avisos importantes (leer antes de seguir)
- **Comparador sin confirmar:** la zona R9, R10, R11, R13 (pot) y patas 5/6 del
  TL072 salía **borrosa** en la foto del esquemático. Se dibujó lo más probable —
  **verificar esas uniones con multímetro (continuidad)** contra el cobre real.
- **Errata Q1:** en el video, el BC547 (Q1) está montado **girado** respecto a la
  serigrafía. Revisar antes de soldar.
- **C4 no se monta:** el esquema la lista (10µF) pero la placa no tiene lugar; va en
  paralelo con la alimentación como C6/C7. No aparece en el diagrama.
- **Resistencias:** las bandas de color del diagrama se calculan del valor a 4 bandas;
  las reales de las fotos eran de 5 bandas/azules → para el valor exacto, medir.

## Ideas para seguir mejorando (próximo chat)
- Confirmar y corregir el bloque del comparador con multímetro.
- Modo "ver nodos de a uno" (botón siguiente/anterior) además del aislar por clic.
- Ajustar radio de curva / grosor de pista al aislar (quedó pendiente de gusto).
- Opción para exportar/imprimir la tabla de nodos o el diagrama a 1:1.
- Revisar solapes de tronco puntuales (el ruteo peine es simple, no evita todos los
  cruces entre nodos distintos).

## Historial de decisiones de diseño (por si ayuda)
1. Se leyó el esquemático **zona por zona** con una cuadrícula de coordenadas sobre
   la imagen (método documentado en `SKILL.md`).
2. El rat's-nest con curvas era caótico → se pasó a posición real + marcadores de
   rol + ruteo ortogonal + aislamiento por nodo + tabla.
3. Se agregó panel emergente por componente (identidad) y se quitaron las etiquetas
   bajo cada dibujo.
4. Cada componente se dibuja como lo que es (bandas, banda de diodo, disco, etc.).
5. Ruteo "peine": cada pata baja **derecho** a un tronco común, para que la pista no
   parezca cruzarse sobre sí misma.
