---
name: pcb-node-diagram
description: Genera un diagrama de conexiones (netlist) claro y a escala a partir de un esquemático o una placa. Los componentes se dibujan en su posición física real (como la vista de montaje del PCB), cada pata se marca como entrada/salida/alimentación con su número, y las pistas se rutean en ángulo recto agrupadas por nodo, con aislamiento interactivo por nodo y una tabla de nodos. Usar cuando el usuario pide "qué pata va con cuál", "diagrama de nodos", "mapa de conexiones", "cómo conectar/soldar", "trazar el cobre a mano", o entrega fotos de un esquemático/PCB y quiere entender o armar el circuito. Produce un artifact HTML autocontenido.
---

# Diagrama de conexiones por nodos (para armar / rutear a mano)

Produce un HTML autocontenido: los componentes en su **posición física real**, cada
pata marcada como **entrada (◂) / salida (▸) / alimentación (▪) / sin polaridad (●)**
con su número, pistas **ortogonales** agrupadas por nodo, **aislamiento interactivo**
(tocar un nodo apaga el resto y muestra su recorrido limpio) y una **tabla de nodos**
que es la referencia definitiva.

Todo el diagrama se genera a partir de **un solo objeto JSON** (`components` + `nets`).
El motor de render (`assets/diagram-template.html`) no se toca: solo se reemplaza ese JSON.

## Por qué así (lecciones aprendidas)

Un rat's-nest con curvas Bézier que conecta pares de patas se ve **caótico**. Lo que
lo hace legible:
1. **Posición real** de cada componente (igual que la vista de montaje del PCB), no un
   layout por flujo de señal.
2. **Marcadores de rol** siempre visibles (◂▸▪●) para que se distinga entrada de salida.
3. **Ruteo ortogonal** (solo ángulos rectos) con un tronco por nodo y bajadas — nunca
   curvas que conectan pares al azar.
4. **Aislar un nodo** como modo de lectura principal: todo tenue salvo el nodo elegido.
5. **Tabla de nodos** como respaldo textual: si una línea se pierde, la tabla manda.

## Flujo de trabajo

### 1. Conseguir el netlist
Si el usuario da un esquemático (foto), extraé el conexionado **zona por zona** con una
cuadrícula de coordenadas encima de la imagen (muy efectivo con JPEG borrosos):

- Renderizá recortes ampliados de la imagen con una grilla de coordenadas (px del
  original) superpuesta. Un `<img>` posicionado con `left/top` negativos y escalado, más
  divs de líneas magenta cada 20 px etiquetados con la coordenada real. Sacá screenshot
  con el Chromium headless preinstalado (`/opt/pw-browsers/chromium-1194/chrome-linux/chrome
  --headless --no-sandbox --screenshot`).
- Seguí cada cable por los **puntos de unión** (los "dots" rojos = nodos eléctricos).
  Dos cables que se cruzan **sin** dot NO están conectados.
- Anotá, por componente, a qué **nodo** va cada pata. Un nodo = un nombre corto (`+12`,
  `GND`, `DRAIN`, `GATE`…). Misma etiqueta en dos patas = van soldadas.

Si algo queda borroso/ambiguo, marcá esas uniones como "verificar en la placa con
multímetro (continuidad)" en las notas — no inventes con falsa seguridad.

### 2. Armar el modelo de datos
Editá el bloque `<script id="netdata" type="application/json">` del template.

```jsonc
{
 "view":{"w":912,"h":703,"railTop":16,"railBot":690},   // lienzo; rieles +12/GND
 "nets":{
   "+12":{"c":"#E4572E","d":"Alimentación +12 V","rail":"top"},   // rail:"top"|"bot" = bus en el borde
   "GND":{"c":"#5C7186","d":"Masa","rail":"bot"},
   "DRAIN":{"c":"#D64550","d":"Drenaje + bobina + diodos"}         // nodo normal (sin rail)
 },
 "components":[
   {"ref":"U1","sub":"NE555","cx":253,"cy":130,"w":66,"h":172,"kind":"ic",
    "pins":[
      {"n":"1","net":"GND","s":"L","at":0.12,"r":"pwr"},
      {"n":"3","net":"OUT5","s":"L","at":0.62,"r":"out"},
      {"n":"8","net":"+12","s":"R","at":0.12,"r":"pwr"}
    ]}
 ]
}
```

**Reglas del modelo:**
- **Posición (`cx,cy`)**: colocá cada componente donde va físicamente en la placa real.
  Copiá las posiciones de la foto de montaje / serigrafía. No reordenar por señal.
- **`kind`** (define forma y estilo): `ic` (DIP, con muesca), `mos` (TO-220), `tr`
  (transistor, círculo), `elec` (electrolítico, círculo con +), `cap` (cerámico,
  rectángulo), `res` (resistencia), `dio` (diodo), `pot` (potenciómetro/preset, azul),
  `conn` (conector/terminal, amarillo).
- **`w,h`**: tamaño en px del lienzo. Resistencia horizontal ~66×24; vertical ~24×66.
  Elegí orientación acorde a cómo caen las patas en la placa.
- **Patas (`pins`)**: cada una lleva
  - `n`: número/nombre visible (`"3"`, `"G"`, `"+"`, `"k"`; `""` si no aplica).
  - `net`: nombre del nodo (debe existir en `nets`).
  - `s`: lado del cuerpo donde sale — `"L"`,`"R"`,`"T"`,`"B"`. Ubicalo del lado real.
  - `at`: posición fraccional a lo largo de ese lado (0..1).
  - `r`: **rol** → `"in"` (◂), `"out"` (▸), `"pwr"` (▪ para +12/GND), `"pas"` (● pasivo
    sin polaridad, para R y C). Marcá in/out en chips y transistores según la función.
- **Colores de nodo (`c`)**: fijá `+12` rojo-naranja y `GND` azul-gris. Para el resto
  usá tonos distintos y saturados; evitá que dos nodos vecinos compartan color.
- **Nodos de 1 sola pata**: no existen; cada nodo debe tener ≥2 patas. Si te queda uno,
  te falta una conexión.

### 3. Generar el HTML
- Copiá `assets/diagram-template.html` al destino (p. ej. `<proyecto>/conexiones.html`).
- Reemplazá el bloque `netdata` con tu JSON.
- Ajustá `<title>`, el encabezado y las notas ("Antes de empezar") al circuito concreto.
- No modifiques el `<script>` del motor salvo que agregues un `kind` nuevo.

### 4. Verificar (obligatorio antes de entregar)
Con el Chromium headless, envolvé el archivo en un HTML completo y sacá screenshots:
- **Vista default** (todos los nodos): debe verse como la placa real, ortogonal, sin
  desborde horizontal. Comprobá que no haya scroll lateral del body.
- **Vista aislada**: disparar el click de un `.chip` en `load` (p. ej. `DRAIN`) y
  confirmar que el recorrido se ve limpio y el resto tenue.
- **Tabla**: que cada nodo liste las patas correctas.
Iterá hasta que las tres se vean bien. Revisá también modo claro y oscuro.

### 5. Publicar
Cargá la skill `artifact-design` (calibra el diseño), luego publicá con la herramienta
`Artifact`. Favicon sugerido: 🔌. Commit + push si el usuario trabaja en un repo.

## Checklist de calidad
- [ ] Componentes en posición física real (coincide con la foto de montaje).
- [ ] Cada pata con marcador de rol correcto (◂▸▪●) y su número.
- [ ] Cantidad de patas correcta por componente (8 en DIP, 3 en transistor/pot, etc.).
- [ ] Todos los nodos con ≥2 patas; nombres consistentes.
- [ ] Ruteo ortogonal; rieles +12/GND en los bordes.
- [ ] Aislar un nodo muestra un recorrido claro.
- [ ] Tabla de nodos completa y correcta.
- [ ] Sin desborde horizontal; claro y oscuro OK.
- [ ] Zonas dudosas del esquemático marcadas como "verificar con multímetro".

## Archivos
- `assets/diagram-template.html` — motor de render + datos de ejemplo (reemplazables).
- `references/example-detector.json` — netlist completo de ejemplo (detector de metales
  NE555 + TL072) que muestra todos los `kind` y roles.
