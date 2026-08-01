# Detector de metales por pulsos (NE555 + TL072) — qué va en cada hueco

Guía de montaje: cada nombre de la serigrafía de la placa verde (`U2`, `C5`, `C7`,
`R17`, `R13`…) traducido al componente real que le corresponde.

Versión visual e interactiva de esta misma lista: **`mapa-placa.html`**.

---

## Resistencias fijas (1/4 W, sin polaridad)

| En la placa | Valor  | Colores (4 bandas)                | Para qué                          |
|-------------|--------|-----------------------------------|-----------------------------------|
| R1          | 47 k   | amarillo · violeta · naranja      | Temporización del NE555           |
| R3          | 220 Ω  | rojo · rojo · café                | Va a la bobina P1                 |
| R4          | 390 Ω  | naranja · blanco · café           | Entrada del amplificador          |
| R5          | 47 k   | amarillo · violeta · naranja      | Divisor de alimentación           |
| R6          | 62 k   | azul · rojo · naranja             | Referencia del TL072              |
| R7          | 1.2 M  | café · rojo · verde               | Realimentación, 1er operacional   |
| R8          | 10 Ω   | café · negro · negro              | En serie con el parlante          |
| R9          | 4.7 k  | amarillo · violeta · rojo         | Va al potenciómetro R13           |
| R10         | 62 k   | azul · rojo · naranja             | Realimentación, 2º operacional    |
| R11         | 120 k  | café · rojo · amarillo            | Divisor del comparador            |
| R12         | 470 k  | amarillo · violeta · amarillo     | Base de Q1                        |
| R14         | 10 k   | café · negro · naranja            | Base de Q3                        |
| R15         | 100 Ω  | café · negro · café               | Limitadora                        |
| R16         | 10 k   | café · negro · naranja            | Base de Q3                        |
| R17         | 150 Ω  | café · verde · café               | Limitadora de puerta              |
| R18         | 1 k    | café · negro · rojo               | Junto al preset R2                |

La cuarta banda (tolerancia) es dorada en todas.

## Ajustables

| En la placa | Valor | Qué es                                                        |
|-------------|-------|---------------------------------------------------------------|
| R2          | 10 k  | **Preset** — el cuadradito azul que se ajusta con destornillador. Ajusta el pulso. |
| R13         | 50 k  | **Potenciómetro de eje** — el mando de **sensibilidad**, va al panel. |

## Condensadores

| En la placa | Valor    | Tipo / marcado                          |
|-------------|----------|-----------------------------------------|
| C1          | 100 nF   | Cerámico, marcado `104`. Sin polaridad. |
| C2          | 100 nF   | Cerámico, marcado `104`. Sin polaridad. |
| C8          | 1 nF     | Cerámico, marcado `102`. Sin polaridad. |
| C3          | 1 µF     | Electrolítico — **respeta el +**        |
| C5          | 1 µF     | Electrolítico — **respeta el +**        |
| C6          | 10 µF    | Electrolítico — **respeta el +**        |
| C7          | 1000 µF  | Electrolítico, el más grande. Filtra los 12 V. |

En los electrolíticos la **pata larga es el +** y la raya del cuerpo marca el **−**.

## Semiconductores

| En la placa | Componente | Detalle                                                    |
|-------------|------------|------------------------------------------------------------|
| U1          | NE555P     | Temporizador, 8 patas. **Muesca hacia arriba.**             |
| U2          | TL072      | Doble amplificador operacional, 8 patas. **Muesca a la izquierda.** |
| Q1          | BC547      | Transistor NPN (TO-92). **Ver ERRATA abajo.**               |
| Q3          | BC557      | Transistor PNP (TO-92). ¡No confundir con el BC547!         |
| Q2          | IRF840     | MOSFET de potencia TO-220, con chapa metálica.              |
| D2          | 1N4148     | Diodo. La **banda** va del lado que marca la serigrafía.    |
| D3          | 1N4148     | Diodo. La **banda** va del lado que marca la serigrafía.    |

## Conectores (aquí van cables, no componentes)

| En la placa | Va conectado a                          |
|-------------|-----------------------------------------|
| P1          | La **bobina** de búsqueda (2 hilos)     |
| P2          | El **parlante** o audífono              |
| P3          | La **batería de 12 V** (rojo = +, negro = masa) |

---

## Tres avisos importantes

1. **ERRATA en Q1.** Una de las fotos del video marca con flecha roja el transistor
   Q1 (BC547): ahí está montado **girado** respecto al dibujo de la serigrafía, con
   las patas dobladas. Mira ese punto del video antes de soldarlo — la serigrafía de
   Q1 parece estar mal impresa.

2. **C4 no existe en la placa.** El esquema lista `C4 = 10 µF`, pero la placa **no
   tiene hueco para C4**. Va en paralelo con la alimentación, igual que C6 y C7, así
   que simplemente no la montes.

3. **Resistencias de 5 bandas.** En las fotos hay resistencias azules de 5 bandas
   (1 %). Los códigos de color de la tabla son de 4 bandas. Si las tuyas son azules,
   mídelas con el multímetro en vez de fiarte del color.

---

## Orden recomendado para soldar

1. Las **18 resistencias** primero: son las más planas y luego no estorban.
2. Los **diodos D2 y D3**, respetando la banda.
3. Los **zócalos de U1 y U2** si los tienes (muy recomendable), con la muesca alineada.
4. Los **cerámicos C1, C2 y C8**.
5. Los **transistores Q3 (BC557), Q1 (BC547)** y luego **Q2 (IRF840)**; la cara plana
   va donde el dibujo tiene el lado recto.
6. Los **electrolíticos C3, C5, C6 y C7**, respetando el **+**.
7. El **preset R2**, y por último los **conectores P1, P2, P3** y el **potenciómetro
   R13** de 50 k con eje.
8. Al final, **U1 (NE555)** y **U2 (TL072)** en sus zócalos, muesca con muesca.

## Qué hace cada bloque

- **U1 · NE555** — genera los pulsos que disparan la bobina; R1, R2, C1 y C2 fijan
  cada cuánto y cuánto duran.
- **Q2 · IRF840** — transistor de potencia: cada pulso lo abre y descarga corriente
  por la bobina. Es el que más calienta.
- **P1 · bobina** — al cortar el pulso genera un pico de tensión que cambia si hay
  metal cerca.
- **D2 · D3** — recortan ese pico para que la etapa de amplificación no se dañe.
- **U2 · TL072** — amplifica la señal débil de la bobina y la compara con un nivel
  de referencia.
- **R13 · 50 k** — mueve ese nivel de referencia: es el mando de **sensibilidad**.
- **Q1 · BC547** — excita el parlante de P2 para que suene el pitido.
- **C7 · 1000 µF** — filtra la alimentación de 12 V que entra por P3.
