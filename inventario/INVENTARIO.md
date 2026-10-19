# Inventario de componentes electrónicos

Catálogo generado por `build.py` a partir de `datos/`. No editar a mano.

**Total: 275 componentes** en 8 categorías.

| Categoría | Elementos |
|---|---:|
| [Resistores, potenciómetros y afines](#resistores) | 43 |
| [Capacitores](#capacitores) | 21 |
| [Inductores, transformadores y cristales](#inductivos_y_frecuencia) | 23 |
| [Protección (fusibles, varistores, TVS)](#proteccion) | 19 |
| [Materiales para fabricar PCB](#materiales_pcb) | 37 |
| [Soldadura y consumibles](#soldadura_y_consumibles) | 29 |
| [Herramientas e instrumentos](#herramientas) | 70 |
| [Energía (pilas, baterías, fuentes)](#energia) | 33 |

<a id="resistores"></a>
## Resistores, potenciómetros y afines

| Componente | Montaje | Encapsulado / huella | Valores o variantes comunes | Popularidad |
|---|---|---|---|---|
| **Kit / surtido de resistencias THT**<br><sub>`res-kit-tht`</sub> | THT | — | 10 Ω, 22 Ω, 47 Ω, 100 Ω, 150 Ω, 200 Ω, 220 Ω, 270 Ω, … (+22) | alta |
| **Kit de trimpots / potenciómetros**<br><sub>`res-kit-potenciometros`</sub> | THT | — | 100 Ω, 200 Ω, 500 Ω, 1 kΩ, 2 kΩ, 5 kΩ, 10 kΩ, 20 kΩ, … (+5) | media |
| **Libro-kit de resistencias SMD (0603 / 0805 / 1206)**<br><sub>`res-kit-smd`</sub> | SMD | — | 0603 (≈170 valores), 0805 (≈170 valores), 1206 (≈170 valores) | media |
| **Potenciómetro rotatorio 16 mm para PCB (mono)**<br><sub>`res-pot-16mm-pcb`</sub> | THT | 16 mm, 3 pines PCB en línea (WH148 / RV16) (3p, 5.0 mm) | B1K, B2K, B5K, B10K, B20K, B50K, B100K, B250K, … (+7) | muy alta |
| **Potenciómetro con interruptor (switch)**<br><sub>`res-pot-con-interruptor`</sub> | THT | 16 mm con interruptor SPST (3 + 2 pines) (5p, 5.0 mm) | A10K, A50K, A100K, B10K, B50K, B100K, A500K, A1M | alta |
| **Potenciómetro doble (estéreo) 16 mm para PCB**<br><sub>`res-pot-16mm-doble`</sub> | THT | 16 mm doble, 6 pines (2 filas de 3) (6p, 5.0 mm) | A10K, A50K, A100K, B10K, B50K, B100K | alta |
| **Potenciómetro rotatorio 24 mm con terminales para cable**<br><sub>`res-pot-24mm`</sub> | panel | 24 mm, 3 terminales de oreja (solder lug) (3p) | B1K, B5K, B10K, B50K, B100K, A10K, A50K, A100K, … (+3) | alta |
| **Potenciómetro de alambre / reóstato de panel**<br><sub>`res-reostato-alambre`</sub> | panel | Panel con 3 terminales de soldar (3p) | 10 Ω, 50 Ω, 100 Ω, 500 Ω, 1 kΩ, 5 kΩ, 10 kΩ | media |
| **Potenciómetro deslizable (slide / fader)**<br><sub>`res-pot-deslizable`</sub> | THT | Deslizable mono (carrera 45 mm, cuerpo ≈60 mm) (3p); Deslizable carrera 60 mm (cuerpo ≈75–88 mm) (3p) | B10K, B20K, B50K, B100K, A10K, A50K | media |
| **Potenciómetro miniatura 9 mm para PCB**<br><sub>`res-pot-9mm`</sub> | THT | 9 mm vertical, 3 pines en línea + 2 patas de sujeción (3p, 2.5 mm) | B1K, B5K, B10K, B20K, B50K, B100K | media |
| **Potenciómetro multivuelta de precisión 3590S (10 vueltas)**<br><sub>`res-pot-multivuelta-3590s`</sub> | panel | Cilíndrico de panel con 3 terminales de soldar (3p) | 100 Ω, 500 Ω, 1 kΩ, 2 kΩ, 5 kΩ, 10 kΩ, 20 kΩ, 50 kΩ, … (+1) | media |
| **Red resistiva SIP (bus o aislada)**<br><sub>`res-red-sip`</sub> | THT | SIP-5 (5p, 2.54 mm); SIP-6 (6p, 2.54 mm); SIP-8 (8p, 2.54 mm); SIP-9 (el más común, p. ej. A103J) (9p, 2.54 mm); SIP-10 (10p, 2.54 mm) | A221J (220 Ω), A331J (330 Ω), A471J (470 Ω), A102J (1 kΩ), A222J (2.2 kΩ), A472J (4.7 kΩ), A103J (10 kΩ), A473J (47 kΩ), … (+1) | alta |
| **Red resistiva DIP-14/16**<br><sub>`res-red-dip`</sub> | THT | DIP-16 (16p, 2.54 mm, filas 7.62 mm); DIP-14 (14p, 2.54 mm, filas 7.62 mm) | 220 Ω, 330 Ω, 470 Ω, 1 kΩ, 4.7 kΩ, 10 kΩ | media |
| **Red resistiva SMD (array 4 x 0603 / 4 x 0402)**<br><sub>`res-red-smd`</sub> | SMD | 4 x 0603 (4D03, 1206 de 8 terminales) (8p, 0.8 mm); 4 x 0402 (4D02, 0804 de 8 terminales) (8p, 0.5 mm) | 22 Ω, 33 Ω, 1 kΩ, 4.7 kΩ, 10 kΩ | media |
| **Resistor de película de carbón 1/4 W**<br><sub>`res-carbon-1-4w`</sub> | THT | Axial horizontal (1/4 W) (2p, 10.16 mm); Axial vertical (de pie, 1/4 W) (2p, 2.54 mm) | 1 Ω, 1.2 Ω, 1.5 Ω, 1.8 Ω, 2.2 Ω, 2.7 Ω, 3.3 Ω, 3.9 Ω, … (+77) | muy alta |
| **Resistor de película de carbón 1/2 W**<br><sub>`res-carbon-1-2w`</sub> | THT | Axial horizontal (1/2 W) (2p, 12.7 mm); Axial vertical (de pie, 1/2 W) (2p, 5.08 mm) | 1 Ω, 2.2 Ω, 4.7 Ω, 10 Ω, 22 Ω, 33 Ω, 47 Ω, 68 Ω, … (+25) | alta |
| **Resistor de película metálica 1/4 W 1 %**<br><sub>`res-metal-1-4w-1pct`</sub> | THT | Axial horizontal (1/4 W película metálica) (2p, 10.16 mm) | 10 Ω, 22 Ω, 47 Ω, 100 Ω, 120 Ω, 150 Ω, 200 Ω, 220 Ω, … (+26) | alta |
| **Resistor 0 Ω (puente / jumper)**<br><sub>`res-puente-0-ohm`</sub> | THT/SMD | Axial tamaño 1/4 W (una banda negra) (2p, 10.16 mm); SMD 0805 / 1206 (marcado 0 o 000) (2p) | 0 Ω axial, 0 Ω 0603, 0 Ω 0805, 0 Ω 1206 | media |
| **Resistor cerámico (cemento) 10 W**<br><sub>`res-ceramica-10w`</sub> | THT | Cerámico horizontal 10 W (SQP, axial) (2p, 55.88 mm) | 0.1 Ω, 0.22 Ω, 0.47 Ω, 1 Ω, 2.2 Ω, 4.7 Ω, 5 Ω, 8.2 Ω, … (+7) | alta |
| **Resistor cerámico (cemento) 5 W**<br><sub>`res-ceramica-5w`</sub> | THT | Cerámico horizontal 5 W (SQP, axial) (2p, 27.94 mm); Cerámico vertical 5 W (SQM, terminales por la base) (2p) | 0.1 Ω, 0.22 Ω, 0.33 Ω, 0.47 Ω, 1 Ω, 2.2 Ω, 4.7 Ω, 5 Ω, … (+11) | alta |
| **Resistor de óxido metálico 1 W**<br><sub>`res-oxido-metalico-1w`</sub> | THT | Axial 1 W (tamaño normal) (2p, 15.24 mm) | 0.1 Ω, 0.22 Ω, 0.47 Ω, 1 Ω, 2.2 Ω, 4.7 Ω, 10 Ω, 22 Ω, … (+11) | alta |
| **Resistor de óxido metálico 2 W**<br><sub>`res-oxido-metalico-2w`</sub> | THT | Axial 2 W (tamaño normal) (2p, 20.32 mm) | 0.1 Ω, 0.22 Ω, 0.47 Ω, 1 Ω, 2.2 Ω, 4.7 Ω, 10 Ω, 22 Ω, … (+10) | alta |
| **Resistor cerámico (cemento) 20 W**<br><sub>`res-ceramica-20w`</sub> | THT | Cerámico horizontal 20 W (SQP, axial) (2p) | 0.1 Ω, 0.5 Ω, 1 Ω, 4.7 Ω, 10 Ω, 22 Ω, 47 Ω, 100 Ω | media |
| **Resistor cerámico no inductivo BPR56 5 W**<br><sub>`res-ceramica-bpr56-5w`</sub> | THT | BPR56 (plano, terminales radiales) (2p) | 0.01 Ω, 0.1 Ω, 1 Ω | media |
| **Resistor de alambre vitrificado tubular**<br><sub>`res-alambre-vitrificado`</sub> | panel | Tubular con terminales de ojillo (2p) | 1 Ω, 10 Ω, 50 Ω, 100 Ω, 1 kΩ | media |
| **Resistor de potencia con carcasa de aluminio (10–100 W)**<br><sub>`res-potencia-aluminio`</sub> | panel | Carcasa de aluminio con 2 terminales de soldar (2p) | 0.1 Ω, 1 Ω, 4 Ω, 8 Ω, 10 Ω, 100 Ω | media |
| **Resistor de óxido metálico 3 W**<br><sub>`res-oxido-metalico-3w`</sub> | THT | Axial 3 W (2p, 25.4 mm) | 0.1 Ω, 0.22 Ω, 0.47 Ω, 1 Ω, 2.2 Ω, 4.7 Ω, 10 Ω, 22 Ω, … (+8) | media |
| **Fotorresistencia LDR (GL5528 y serie GL55xx)**<br><sub>`res-ldr-fotorresistencia`</sub> | THT | LDR 5 mm (GL55xx) (2p, 3.4 mm); LDR 12 mm / 20 mm (GL12528, GL20528) (2p) | GL5506 (2–5 kΩ a 10 lux, 0.2 MΩ oscuridad), GL5516 (5–10 kΩ, 0.5 MΩ), GL5528 (10–20 kΩ, 1 MΩ), GL5537-1 (20–30 kΩ, 2 MΩ), GL5537-2 (30–50 kΩ, 3 MΩ), GL5539 (50–100 kΩ, 5 MΩ), GL5549 (100–200 kΩ, 10 MΩ) | muy alta |
| **Termistor NTC 10 kΩ tipo gota epóxica (MF52)**<br><sub>`res-ntc-10k-mf52`</sub> | THT | Gota epóxica radial (MF52) (2p, 2.54 mm) | 1 kΩ, 2 kΩ, 5 kΩ, 10 kΩ B3950, 10 kΩ B3435, 47 kΩ, 50 kΩ, 100 kΩ B3950 | alta |
| **Termistor NTC de disco para corriente de arranque (MF72, 5D-9, 10D-13...)**<br><sub>`res-ntc-inrush`</sub> | THT | Disco Ø5–9 mm (p. ej. 5D-9, 10D-9) (2p, 5.0 mm); Disco Ø11–15 mm (p. ej. 5D-11, 10D-13, 5D-15) (2p, 7.5 mm); Disco Ø20–25 mm (p. ej. 5D-20, 10D-20) (2p, 7.5 mm) | 5D-9, 10D-9, 5D-11, 8D-11, 10D-11, 5D-13, 10D-13, 3D-15, … (+3) | alta |
| **Sensores resistivos PTC de temperatura (PT100/PT1000, KTY81)**<br><sub>`res-ptc-rtd-sensado`</sub> | THT | Elemento RTD de película delgada (chip cerámico con 2 hilos) (2p); KTY81 (SOD-70, 2 terminales) (2p) | PT100, PT1000, KTY81-110 (1 kΩ a 25 °C), KTY81-210 (2 kΩ a 25 °C) | media |
| **Termistor NTC de vidrio axial (MF58, 100 kΩ 3950)**<br><sub>`res-ntc-vidrio`</sub> | THT | Axial de vidrio (tipo DO-35) (2p, 7.62 mm) | 10 kΩ B3950, 50 kΩ, 100 kΩ B3950 | media |
| **Resistor SMD 0603**<br><sub>`res-smd-0603`</sub> | SMD | 0603 (1608 métrico) (2p, 1.65 mm) | 0 Ω, 10 Ω, 22 Ω, 33 Ω, 47 Ω, 100 Ω, 220 Ω, 330 Ω, … (+10) | alta |
| **Resistor SMD 0805**<br><sub>`res-smd-0805`</sub> | SMD | 0805 (2012 métrico) (2p, 1.825 mm) | 0 Ω, 10 Ω, 22 Ω, 47 Ω, 100 Ω, 220 Ω, 330 Ω, 470 Ω, … (+10) | alta |
| **Resistor SMD 1206**<br><sub>`res-smd-1206`</sub> | SMD | 1206 (3216 métrico) (2p, 2.925 mm) | 0 Ω, 1 Ω, 10 Ω, 47 Ω, 100 Ω, 220 Ω, 330 Ω, 470 Ω, … (+7) | alta |
| **Resistencia shunt de alambre (manganina/constantán)**<br><sub>`res-shunt-alambre`</sub> | THT | Alambre en U, 2 terminales (2p) | 5 mΩ (R005), 10 mΩ (R010), 20 mΩ, 50 mΩ (R050) | media |
| **Resistor shunt SMD 2512 (miliohms)**<br><sub>`res-shunt-smd-2512`</sub> | SMD | 2512 (6332 métrico) (2p) | R005 (5 mΩ), R010 (10 mΩ), R020, R050 (50 mΩ), R100 (0.1 Ω), R200, R500 | media |
| **Shunt de panel para amperímetro (75 mV / 50 mV)**<br><sub>`res-shunt-panel-75mv`</sub> | panel | Bloque con 2 tornillos de potencia + 2 de sensado (4p) | 10 A / 75 mV, 20 A / 75 mV, 50 A / 75 mV, 100 A / 75 mV, 200 A / 75 mV | media |
| **Trimpot multivuelta 3296W (ajuste superior, pines en línea)**<br><sub>`res-trimpot-3296w`</sub> | THT | 3296W (vertical, pines en línea) (3p, 2.54 mm) | 101 (100 Ω), 201 (200 Ω), 501 (500 Ω), 102 (1 kΩ), 202 (2 kΩ), 502 (5 kΩ), 103 (10 kΩ), 203 (20 kΩ), … (+6) | muy alta |
| **Trimpot de carbón 6 mm (RM-065 / preset)**<br><sub>`res-trimpot-carbon-6mm`</sub> | THT | RM-065 (pines en triángulo) (3p, 2.5 mm, filas 2.5 mm) | 100 Ω, 200 Ω, 500 Ω, 1 kΩ, 2 kΩ, 5 kΩ, 10 kΩ, 20 kΩ, … (+5) | alta |
| **Trimpot de una vuelta 3362P**<br><sub>`res-trimpot-3362p`</sub> | THT | 3362P (vertical, pines en triángulo) (3p, 2.54 mm, filas 2.54 mm) | 101 (100 Ω), 501 (500 Ω), 102 (1 kΩ), 202 (2 kΩ), 502 (5 kΩ), 103 (10 kΩ), 203 (20 kΩ), 503 (50 kΩ), … (+3) | alta |
| **Trimpot multivuelta 3296Y / 3296P (pines escalonados)**<br><sub>`res-trimpot-3296y`</sub> | THT | 3296Y (vertical, pines escalonados) (3p, 2.54 mm, filas 2.54 mm); 3296P (lateral, pines escalonados) (3p, 2.54 mm, filas 2.54 mm); 3296X (lateral, pines en línea) (3p, 2.54 mm) | 102 (1 kΩ), 502 (5 kΩ), 103 (10 kΩ), 503 (50 kΩ), 104 (100 kΩ), 105 (1 MΩ) | alta |
| **Trimpot de carbón 10 mm (tipo Piher PT10)**<br><sub>`res-trimpot-carbon-10mm`</sub> | THT | PT10 horizontal (H) (3p, 5.0 mm, filas 5.0 mm); PT10 vertical (V) (3p) | 470 Ω, 1 kΩ, 2.2 kΩ, 4.7 kΩ, 10 kΩ, 22 kΩ, 47 kΩ, 100 kΩ, … (+3) | media |

<a id="capacitores"></a>
## Capacitores

| Componente | Montaje | Encapsulado / huella | Valores o variantes comunes | Popularidad |
|---|---|---|---|---|
| **Capacitor cerámico de disco (lenteja) 50 V**<br><sub>`cap-ceramico-disco`</sub> | THT | Disco radial paso 5.08 mm (2p, 5.08 mm); Disco radial paso 2.54 mm (2p, 2.54 mm) | 10 pF (100), 15 pF (150), 18 pF (180), 22 pF (220), 27 pF (270), 33 pF (330), 47 pF (470), 68 pF (680), … (+11) | muy alta |
| **Capacitor cerámico de disco de alto voltaje (1 kV–3 kV)**<br><sub>`cap-ceramico-disco-alto-voltaje`</sub> | THT | Disco radial HV paso 5.0/7.5 mm (2p, 7.5 mm) | 100 pF 1 kV (101), 470 pF 1 kV (471), 1 nF 1 kV (102), 2.2 nF 1 kV (222), 4.7 nF 1 kV (472), 10 nF 1 kV (103), 1 nF 2 kV, 4.7 nF 2 kV, … (+1) | alta |
| **Capacitor cerámico multicapa (MLCC) THT 'monolítico'**<br><sub>`cap-mlcc-tht`</sub> | THT | Radial MLCC paso 5.08 mm (2p, 5.08 mm); Radial MLCC paso 2.54 mm (2p, 2.54 mm) | 22 pF, 100 pF, 1 nF (102), 10 nF (103), 100 nF (104), 220 nF (224), 470 nF (474), 1 µF (105), … (+1) | alta |
| **Capacitor cerámico multicapa SMD (0402/0603/0805/1206/1210)**<br><sub>`cap-mlcc-smd`</sub> | SMD | 0402 (1005 métrico) (2p); 0603 (1608 métrico) (2p, 1.55 mm); 0805 (2012 métrico) (2p, 1.9 mm); 1206 (3216 métrico) (2p, 3.0 mm); 1210 (3225 métrico) (2p) | 10 pF, 22 pF, 100 pF, 1 nF, 10 nF, 100 nF, 1 µF, 4.7 µF, … (+2) | alta |
| **Capacitor cerámico de seguridad clase Y1/Y2**<br><sub>`cap-ceramico-seguridad-y`</sub> | THT | Disco radial Y paso 7.5 mm (2p, 7.5 mm) | 470 pF (471M), 1 nF (102M), 2.2 nF (222M), 4.7 nF (472M) | media |
| **Capacitor electrolítico de aluminio radial**<br><sub>`cap-electrolitico-radial`</sub> | THT | Radial Ø5 mm (2p, 2.0 mm); Radial Ø6.3 mm (2p, 2.5 mm); Radial Ø8 mm (2p, 3.5 mm); Radial Ø10 mm (2p, 5.0 mm); Radial Ø12.5 mm (se vende como 13 mm) (2p, 5.0 mm); Radial Ø16 mm (2p, 7.5 mm); Radial Ø18 mm (2p, 7.5 mm); Radial Ø22 mm o más (2p, 10.0 mm) | 0.1 µF, 0.22 µF, 0.47 µF, 1 µF, 2.2 µF, 3.3 µF, 4.7 µF, 10 µF, … (+14) | muy alta |
| **Capacitor electrolítico bipolar / no polarizado (NP/BP)**<br><sub>`cap-electrolitico-bipolar`</sub> | THT | Radial (mismas latas que el electrolítico) (2p, 5.0 mm); Axial (2p) | 1 µF, 2.2 µF, 3.3 µF, 4.7 µF, 6.8 µF, 10 µF, 22 µF, 47 µF, … (+1) | alta |
| **Capacitor electrolítico axial**<br><sub>`cap-electrolitico-axial`</sub> | THT | Axial (cilindro horizontal) (2p) | 1 µF 50 V, 10 µF 50 V, 47 µF, 100 µF, 470 µF, 1000 µF, 2200 µF | media |
| **Capacitor electrolítico de aluminio SMD (V-chip)**<br><sub>`cap-electrolitico-smd`</sub> | SMD | Ø4 x 5.4 mm (2p); Ø5 x 5.4 mm (2p); Ø6.3 x 5.4 / 7.7 mm (2p); Ø8 x 10.2 mm (2p); Ø10 x 10.2 mm (2p) | 1 µF 50–100 V, 4.7 µF, 10 µF 35 V, 22 µF, 47 µF, 100 µF 16 V, 220 µF 25/50 V, 470 µF 35 V | media |
| **Capacitor electrolítico snap-in (gran capacidad / alto voltaje)**<br><sub>`cap-electrolitico-snap-in`</sub> | THT | Snap-in 2 pines (2p, 10.0 mm); Snap-in 3/4 pines (con pines de anclaje) (4p, 10.0 mm) | 100 µF 400 V, 150 µF 400 V, 220 µF 400 V, 330 µF 400 V, 470 µF 200 V, 680 µF 200 V, 4700 µF 63 V, 10000 µF 50–63 V | media |
| **Capacitor de marcha/arranque para motor (CBB60/CBB61/CBB65/CD60)**<br><sub>`cap-motor-marcha-arranque`</sub> | panel | CBB61 (rectangular, 2 cables) (2p); CBB60 (cilíndrico, cables o terminales) (2p); CBB65 (lata de aluminio, dual C/HERM/FAN) (3p); CD60 (arranque, electrolítico AC) (2p) | 1.5 µF, 2 µF, 2.5 µF, 3 µF, 3.5 µF, 4 µF, 4.5 µF, 5 µF 450 VAC (CBB61), … (+3) | media |
| **Capacitor de poliéster / mylar (película tipo lenteja)**<br><sub>`cap-poliester-mylar`</sub> | THT | Radial paso 5.0 mm (P5) (2p, 5.0 mm); Radial paso 10 mm (2p, 10.0 mm); Radial paso 15 mm (P15) (2p, 15.0 mm) | 1 nF (102), 2.2 nF (222), 4.7 nF (472), 10 nF (103), 22 nF (223), 47 nF (473), 100 nF (104), 220 nF (224), … (+4) | muy alta |
| **Capacitor de polipropileno metalizado CBB21/CBB22/CBB81**<br><sub>`cap-polipropileno-cbb`</sub> | THT | Radial paso 10 mm (2p, 10.0 mm); Radial paso 15 mm (2p, 15.0 mm); Radial paso 22.5–27.5 mm (2p, 22.5 mm) | 1 nF 2 kV (CBB81), 4.7 nF 1.6–2 kV, 10 nF 630 V, 100 nF 400/630 V (104J), 220 nF 400 V, 470 nF 400 V, 1 µF 250/400 V, 2.2 µF 250 V | alta |
| **Capacitor de polipropileno X2 para línea (MKP X2)**<br><sub>`cap-polipropileno-x2`</sub> | THT | Caja paso 10 mm (2p, 10.0 mm); Caja paso 15 mm (2p, 15.0 mm); Caja paso 22.5 mm (2p, 22.5 mm) | 10 nF (103K), 22 nF, 47 nF (473K), 100 nF (104K), 220 nF (224K), 330 nF, 470 nF (474K), 680 nF, … (+3) | alta |
| **Capacitor de poliéster metalizado en caja (MKT/MKS)**<br><sub>`cap-poliester-caja-mkt`</sub> | THT | Caja paso 5.0 mm (2p, 5.0 mm); Caja paso 7.5 mm (2p, 7.5 mm); Caja paso 10 mm (2p, 10.0 mm); Caja paso 15 mm (2p, 15.0 mm); Caja paso 22.5 mm (2p, 22.5 mm); Caja paso 27.5 mm (2p, 27.5 mm) | 1 nF, 10 nF, 22 nF, 47 nF, 100 nF, 220 nF, 330 nF, 470 nF, … (+3) | alta |
| **Supercapacitor cilíndrico 2.7 V (1–500 F)**<br><sub>`cap-supercapacitor-cilindrico-2v7`</sub> | THT | Radial tipo electrolítico (2p, 5.0 mm); Snap-in / terminales de tornillo (≥ 300 F) (2p) | 1 F, 3.3 F, 10 F, 22 F, 50 F, 100 F, 500 F (2.7 V) | media |
| **Supercapacitor tipo moneda 5.5 V (0.1–1.5 F)**<br><sub>`cap-supercapacitor-moneda-5v5`</sub> | THT | Moneda horizontal (H) 2 pines (2p, 5.08 mm); Cilíndrico tipo lata 5.5 V (2p) | 0.1 F, 0.22 F, 0.47 F, 1 F, 1.5 F (5.5 V) | media |
| **Capacitor de tantalio SMD (casos A/B/C/D)**<br><sub>`cap-tantalio-smd`</sub> | SMD | Caso A (EIA 3216-18) (2p); Caso B (EIA 3528-21) (2p); Caso C (EIA 6032-28) (2p); Caso D (EIA 7343-31) (2p) | 1 µF 35 V, 4.7 µF 16 V, 10 µF 16 V, 22 µF 10–16 V, 47 µF 10 V, 100 µF 6.3–10 V | media |
| **Capacitor de tantalio tipo gota (THT)**<br><sub>`cap-tantalio-gota`</sub> | THT | Gota radial paso 2.54 mm (2p, 2.54 mm); Gota radial paso 5.08 mm (2p, 5.08 mm) | 0.1 µF 35 V, 0.47 µF, 1 µF 35 V, 2.2 µF, 4.7 µF 16–25 V, 10 µF 16–25 V, 22 µF 16 V, 47 µF 10 V, … (+1) | media |
| **Capacitor trimmer (ajustable cerámico o de película)**<br><sub>`cap-trimmer`</sub> | THT | Trimmer cerámico 5–6 mm (3p); Trimmer de película 7 mm (2p); Trimmer SMD 3–4 mm (2p) | 2–6 pF, 3–10 pF, 5–20 pF, 6–30 pF, 10–40 pF, 10–60 pF | media |
| **Capacitor variable de sintonía (polyvaricon / de aire)**<br><sub>`cap-variable-sintonia`</sub> | THT | Polyvaricon 2 secciones (AM) (3p); Polyvaricon 4 secciones AM/FM (tipo 223P) (7p); Variable de aire 1–2 secciones (3p) | 2 x ≈266 pF (AM), AM/FM 223P (≈140 + 60 pF AM y 2 x ≈20 pF FM), Aire ≈365 pF | media |

<a id="inductivos_y_frecuencia"></a>
## Inductores, transformadores y cristales

| Componente | Montaje | Encapsulado / huella | Valores o variantes comunes | Popularidad |
|---|---|---|---|---|
| **Cristal de cuarzo HC-49/S (HC-49/US, perfil bajo)**<br><sub>`xtal-hc49s`</sub> | THT | HC-49/S (2p, 4.88 mm) | 4 MHz, 8 MHz, 11.0592 MHz, 12 MHz, 16 MHz, 20 MHz, 24 MHz, 25 MHz | muy alta |
| **Cristal de cuarzo HC-49/U (alto)**<br><sub>`xtal-hc49u`</sub> | THT | HC-49/U (2p, 4.88 mm) | 3.579545 MHz, 4 MHz, 6 MHz, 8 MHz, 10 MHz, 11.0592 MHz, 12 MHz, 16 MHz, … (+2) | alta |
| **Cristal de reloj 32.768 kHz cilíndrico (2x6 / 3x8 mm)**<br><sub>`xtal-32768-cilindrico`</sub> | THT | Cilindro Ø2 x 6 mm (2p); Cilindro Ø3 x 8 mm (2p); SMD 8038 (≈8.0 x 3.8 mm) (2p) | 32.768 kHz CL 6 pF, 32.768 kHz CL 12.5 pF | alta |
| **Cristal de cuarzo SMD (HC-49/SMD, 5032, 3225)**<br><sub>`xtal-smd`</sub> | SMD | HC-49/SMD (2 pads) (2p); 5032 (2 pads) (2p); 3225 (4 pads) (4p) | 8 MHz, 12 MHz, 16 MHz, 25 MHz, 26 MHz, 40 MHz | media |
| **Oscilador de cristal en lata DIP-14 (completo) / DIP-8 (medio)**<br><sub>`xtal-oscilador-dip`</sub> | THT | DIP-14 completo (4 pines: 1, 7, 8, 14) (4p, 15.24 mm, filas 7.62 mm); DIP-8 medio (4 pines: 1, 4, 5, 8) (4p, 7.62 mm, filas 7.62 mm) | 1 MHz, 4 MHz, 8 MHz, 10 MHz, 12 MHz, 16 MHz, 20 MHz, 24 MHz, … (+6) | media |
| **Resonador cerámico (3 pines con capacitores integrados / 2 pines)**<br><sub>`xtal-resonador-ceramico`</sub> | THT | Resonador 3 pines (ZTT/CSTLS) (3p, 2.5 mm); Resonador 2 pines (ZTB 455 kHz) (2p) | 455 kHz (2 pines), 2 MHz, 4 MHz, 8 MHz, 12 MHz, 16 MHz, 20 MHz | media |
| **Núcleo de ferrita de broche para cable (clip-on)**<br><sub>`ind-nucleo-ferrita-cable`</sub> | n/a | — | Diámetro interior 3.5 mm, 5 mm, 7 mm, 9 mm, 13 mm | media |
| **Perla de ferrita SMD (chip bead 0603/0805/1206)**<br><sub>`ind-perla-ferrita-smd`</sub> | SMD | 0603 (1608) (2p); 0805 (2012) (2p); 1206 (3216) (2p) | 120 Ω @100 MHz, 220 Ω, 600 Ω, 1 kΩ @100 MHz | media |
| **Perla de ferrita THT (axial / de varios orificios)**<br><sub>`ind-perla-ferrita-tht`</sub> | THT | Perla axial con alambre (2p, 10.16 mm); Perla de 6 orificios (wideband choke) (2p); Perla suelta para ensartar en cable | ≈ 60–1000 Ω @ 100 MHz | media |
| **Inductor axial tipo resistencia (código de colores)**<br><sub>`ind-axial-codigo-colores`</sub> | THT | Axial 0307 (≈ tamaño de resistencia de 1/4 W) (2p, 10.16 mm); Axial 0410 (≈ tamaño de 1/2 W) (2p, 12.7 mm); Axial 0510 (2p, 15.24 mm) | 1 µH, 2.2 µH, 4.7 µH, 10 µH, 22 µH, 33 µH, 47 µH, 68 µH, … (+5) | alta |
| **Inductor radial tipo tambor (drum core)**<br><sub>`ind-radial-tambor`</sub> | THT | Radial 6x8 mm (2p, 2.5 mm); Radial 8x10 mm (2p, 5.0 mm); Radial 10x12 / 12x16 mm (2p, 5.0 mm) | 10 µH, 22 µH, 33 µH, 47 µH, 68 µH, 100 µH, 220 µH, 330 µH, … (+2) | alta |
| **Inductor SMD de potencia (CD54, NR, CDRH)**<br><sub>`ind-smd-potencia`</sub> | SMD | CD43 (sin blindaje) (2p); CD54 (sin blindaje) (2p); CD105 (sin blindaje) (2p); NR3015 / NR4018 / NR4020 (blindado) (2p); 0630 / 6028 (blindado moldeado) (2p); CDRH104R / 1260 (blindado grande) (2p) | 1 µH, 2.2 µH, 4.7 µH, 10 µH, 22 µH, 33 µH, 47 µH, 68 µH, … (+2) | alta |
| **Inductor toroidal bobinado (potencia)**<br><sub>`ind-toroide-bobinado`</sub> | THT | Toroide montaje vertical (2 terminales) (2p); Toroide montaje horizontal (acostado) (2p) | 22 µH, 33 µH, 47 µH, 56 µH, 100 µH, 220 µH, 330 µH, 470 µH (3 A) | alta |
| **Bobina de choque / filtro de modo común**<br><sub>`ind-choque-modo-comun`</sub> | THT | UU9.8 / UU10.5 vertical (4 pines) (4p); Toroidal de modo común (4 terminales) (4p); SMD de modo común (USB/datos) (4p) | 2 x 5 mH, 2 x 10 mH, 2 x 20 mH, 2 x 30 mH, UU9.8 10–30 mH 0.5–1 A | media |
| **Inductor chip SMD (0603/0805/1206) multicapa o de hilo**<br><sub>`ind-smd-chip`</sub> | SMD | 0603 (1608) (2p); 0805 (2012) (2p); 1206 (3216) (2p) | 1 nH–100 nH (RF), 1 µH, 2.2 µH, 4.7 µH, 10 µH | media |
| **Transformador de FI / bobina de RF ajustable (455 kHz, 10.7 MHz)**<br><sub>`ind-bobina-fi-rf`</sub> | THT | Lata 7 x 7 mm (5 pines + 2 de lata) (7p); Lata 10 x 10 mm (7p) | 455 kHz rojo (oscilador AM), 455 kHz amarillo (FI 1), 455 kHz blanco (FI 2), 455 kHz negro (FI 3/detector), 10.7 MHz (FM) | media |
| **Núcleo toroidal sin bobinar (polvo de hierro T / ferrita FT)**<br><sub>`ind-nucleo-toroidal`</sub> | THT | T37 (polvo de hierro) (2p); T50 (polvo de hierro) (2p); T68 (polvo de hierro) (2p); T80 / T106 / T130 / T200 (2p); FT37 / FT50 / FT82 / FT114 (ferrita) (2p) | T37-2, T50-2 (rojo), T50-6 (amarillo), T68-2, T68-6, T106-26 (amarillo/blanco), FT37-43, FT50-43, … (+2) | media |
| **Transformador de línea 127 VAC → 6/9/12/18/24 VAC (montaje a chasis)**<br><sub>`trf-linea-chasis`</sub> | panel | EI con soporte y orejas para tornillo, salida por cables (5p) | 6 VC/T 1 A, 9 VC/T, 12 V 500 mA, 12 VC/T 1 A, 12 VC/T 2 A, 12 VC/T 3 A, 18 VC/T 1 A, 24 VC/T 1 A, … (+1) | muy alta |
| **Transformador de audio (salida, driver, línea 600 Ω)**<br><sub>`trf-audio`</sub> | THT | Miniatura EI14/EI19 con pines para PCB (5p); Transformador de salida para bulbos (chasis) (5p) | Salida 1 kΩ CT : 8 Ω, Driver ≈ 2 kΩ : 2 x ≈1.5 kΩ (aprox.), Línea 600 : 600 Ω, Bulbos 5 kΩ : 8 Ω | media |
| **Transformador de ferrita para fuente conmutada (EE/EI) y carrete**<br><sub>`trf-ferrita-conmutada`</sub> | THT | EE16 / EE19 (carrete de 8–10 pines) (10p); EE25 / EI28 / EE33 (10p) | EE13, EE16, EE19, EE25, EI28, EE33 | media |
| **Transformador de pulsos / bobina de disparo (trigger)**<br><sub>`trf-pulsos-disparo`</sub> | THT | Bobina de disparo de xenón (3 terminales) (3p); Transformador de pulsos para compuerta (4–6 pines) (4p) | Disparo xenón 4 kV, Disparo xenón 6 kV, Pulsos 1:1, Pulsos 1:1:1 | media |
| **Transformador encapsulado para PCB (EI30/EI38/EI42)**<br><sub>`trf-linea-pcb-encapsulado`</sub> | THT | EI30 encapsulado (5p); EI38 / EI42 / EI48 encapsulado (6p) | 127/220 V → 6 V 1–3 VA, 9 V, 12 V, 2 x 9 V, 2 x 12 V, 2 x 15 V | media |
| **Transformador toroidal de potencia**<br><sub>`trf-toroidal-potencia`</sub> | panel | Toroidal con tornillo central y cables (5p) | 12-0-12 V, 18-0-18 V, 24-0-24 V, 30-0-30 V; 50–500 VA | media |

<a id="proteccion"></a>
## Protección (fusibles, varistores, TVS)

| Componente | Montaje | Encapsulado / huella | Valores o variantes comunes | Popularidad |
|---|---|---|---|---|
| **Fusible de vidrio 5 x 20 mm (rápido F / lento T)**<br><sub>`prot-fusible-vidrio-5x20`</sub> | THT/SMD | Cartucho 5 x 20 mm (para portafusible o clips) (2p); 5 x 20 con terminales axiales (pigtail) (2p) | 100 mA, 200 mA, 250 mA, 315 mA, 500 mA, 630 mA, 800 mA, 1 A, … (+12) | muy alta |
| **Fusible automotriz de navaja (ATO/ATC, mini, maxi)**<br><sub>`prot-fusible-automotriz-navaja`</sub> | panel | ATO/ATC estándar (2p); Mini (ATM/APM) (2p); Maxi (2p) | 2 A gris, 3 A violeta, 4 A rosa, 5 A café claro, 7.5 A café, 10 A rojo, 15 A azul, 20 A amarillo, … (+2) | alta |
| **Fusible cerámico 5 x 20 / 6 x 30 / 6 x 32 mm (alta capacidad de ruptura)**<br><sub>`prot-fusible-ceramico`</sub> | panel | Cerámico 5 x 20 mm (2p); Cerámico 6 x 30 / 6 x 32 mm (2p) | 200 mA (multímetro), 500 mA, 1 A, 2 A, 3.15 A, 5 A, 8 A, 10 A, … (+2) | alta |
| **Fusible de vidrio 6 x 30 mm (1/4 x 1-1/4 in, tipo AGC/3AG)**<br><sub>`prot-fusible-vidrio-6x30`</sub> | panel | Cartucho 6.35 x 31.75 mm (2p) | 250 mA, 500 mA, 1 A, 2 A, 3 A, 5 A, 7.5 A, 10 A, … (+4) | alta |
| **Fusible miniatura radial TR5 / fusible tipo resistencia (picofusible)**<br><sub>`prot-fusible-miniatura-radial`</sub> | THT | TR5 radial (2p, 5.08 mm); Axial tipo resistencia (2p, 10.16 mm) | 100 mA, 250 mA, 500 mA, 1 A, 1.6 A, 2 A, 3.15 A, 5 A | media |
| **Fusible SMD de chip (0603/1206/2410)**<br><sub>`prot-fusible-smd`</sub> | SMD | 0603 (1608) (2p); 1206 (3216) (2p); 2410 (6125) (2p) | 500 mA, 1 A, 2 A, 3 A, 5 A | media |
| **Fusible rearmable PTC radial (polyfuse / polyswitch)**<br><sub>`prot-ptc-radial`</sub> | THT | Disco radial paso 5.1 mm (2p, 5.1 mm); Disco radial paso 10.2 mm (2p, 10.2 mm) | Ihold 0.1 A, 0.2 A, 0.3 A, 0.5 A, 0.75 A, 0.9 A, 1.1 A, 1.35 A, … (+5) | alta |
| **Fusible rearmable PTC SMD (0603–2920)**<br><sub>`prot-ptc-smd`</sub> | SMD | 0603 / 0805 (2p); 1206 (3216) (2p); 1210 (3225) (2p); 1812 (4532) (2p); 2920 (7451) (2p) | 0.05 A, 0.1 A, 0.2 A, 0.5 A (USB), 0.75 A, 1.1 A, 1.5 A, 2 A, … (+1) | media |
| **Clips portafusible para PCB (5 x 20 mm)**<br><sub>`prot-portafusible-clips-pcb`</sub> | THT | Par de clips para 5 x 20 mm (4p); Par de clips para 6 x 30 mm (4p) | 5 x 20 mm, 6 x 30 mm | alta |
| **Portafusible de panel (5 x 20 y 6 x 30 mm)**<br><sub>`prot-portafusible-panel`</sub> | panel | Panel para 5 x 20 mm (2p); Panel para 6 x 30 mm (2p) | 5 x 20 mm 10 A 250 V, 6 x 30 mm 15 A 250 V | alta |
| **Portafusible en línea (para cable)**<br><sub>`prot-portafusible-en-linea`</sub> | n/a | — | Para 5 x 20 mm, Para 6 x 30 mm, Para navaja ATO/mini, Cable de 14–18 AWG | alta |
| **Portafusible para PCB con tapa (5 x 20 mm, tipo BLX-A)**<br><sub>`prot-portafusible-pcb-tapa`</sub> | THT | Base 5 x 20 con tapa, 2 pines (2p); Zócalo para TR5 (2p, 5.08 mm) | 5 x 20 mm 6.3–10 A 250 V, TR5 | media |
| **Termofusible (fusible térmico, thermal cutoff)**<br><sub>`prot-termofusible`</sub> | THT | Axial metálico (tipo SEFUSE SF) (2p); Rectangular de resina/cerámica (2p) | 72 °C, 77 °C, 85 °C, 95 °C, 102 °C, 115 °C, 121 °C, 130 °C, … (+10) | alta |
| **Protector térmico bimetálico rearmable (KSD301 / KSD9700)**<br><sub>`prot-termostato-bimetalico`</sub> | panel | KSD301 (disco con terminales Faston 6.3 mm) (2p); KSD9700 (miniatura, cables o patas) (2p) | 40 °C, 45 °C, 50 °C, 60 °C, 70 °C, 85 °C, 100 °C, 120 °C, … (+1) | media |
| **Varistor de óxido metálico (MOV) de disco**<br><sub>`prot-varistor-mov`</sub> | THT | 05D (Ø ≈ 5–7 mm) (2p, 5.0 mm); 07D (Ø ≈ 7–9.5 mm) (2p, 5.0 mm); 10D (Ø ≈ 10–14 mm) (2p, 7.5 mm); 14D (Ø ≈ 14–17.5 mm) (2p, 7.5 mm); 20D (Ø ≈ 20–24 mm) (2p, 10.0 mm) | 07D471K, 10D471K, 14D471K, 20D471K, 10D431K, 14D431K, 10D391K, 14D391K, … (+7) | alta |
| **Descargador de gas (GDT, tubo de descarga)**<br><sub>`prot-descargador-gas`</sub> | THT | GDT 2 electrodos con terminales radiales/axiales (2p); GDT 3 electrodos (3p) | 90 V, 150 V, 230 V, 350 V, 470 V, 600 V, 800 V (DC de cebado) | media |
| **Diodo TVS 1.5KE (1500 W, DO-201)**<br><sub>`prot-tvs-1-5ke`</sub> | THT | DO-201AD/AE axial (2p, 15.24 mm) | 1.5KE6.8A, 1.5KE12A, 1.5KE15A, 1.5KE18A, 1.5KE24A, 1.5KE33A, 1.5KE200A, 1.5KE400A, … (+1) | media |
| **Diodo TVS P6KE (600 W, DO-15)**<br><sub>`prot-tvs-p6ke`</sub> | THT | DO-15 axial (2p, 10.16 mm) | P6KE6.8A, P6KE10A, P6KE12A, P6KE15A, P6KE18A, P6KE24A, P6KE33A, P6KE36A, … (+3) | media |
| **Diodo TVS SMD SMAJ / SMBJ / SMCJ**<br><sub>`prot-tvs-smd`</sub> | SMD | SMA (DO-214AC) – SMAJ 400 W (2p); SMB (DO-214AA) – SMBJ 600 W (2p); SMC (DO-214AB) – SMCJ 1500 W (2p) | SMBJ5.0A, SMBJ12A, SMBJ15A, SMBJ24A, SMBJ33A, SMAJ5.0A, SMAJ12A, SMCJ24A, … (+1) | media |

<a id="materiales_pcb"></a>
## Materiales para fabricar PCB

| Componente | Montaje | Encapsulado / huella | Valores o variantes comunes | Popularidad |
|---|---|---|---|---|
| **Barniz / laca protectora para PCB (conformal coating)**<br><sub>`mat-barniz-protector-pcb`</sub> | n/a | — | aerosol 200–400 ml, frasco con brocha | media |
| **Estañado químico (estaño líquido / por inmersión)**<br><sub>`mat-estano-quimico`</sub> | n/a | — | polvo para preparar, solución lista | media |
| **Guantes de nitrilo y equipo de protección (lentes)**<br><sub>`mat-guantes-nitrilo`</sub> | n/a | — | caja 100 pzs talla CH/M/G | muy alta |
| **Recipiente / charola para ataque químico**<br><sub>`mat-charola-ataque`</sub> | n/a | — | charola de revelado fotográfico, tupper de plástico, refractario de vidrio | alta |
| **Carbonato de sodio (revelador de dry film)**<br><sub>`mat-revelador-carbonato-sodio`</sub> | n/a | — | 250 g, 500 g, 1 kg | media |
| **Hidróxido de sodio (sosa cáustica) para remover fotorresina**<br><sub>`mat-sosa-caustica-removedor`</sub> | n/a | — | escamas 500 g, 1 kg | media |
| **Máscara antisoldante curable con UV (solder mask)**<br><sub>`mat-mascara-antisoldante-uv`</sub> | n/a | — | verde 10 ml, colores surtidos | media |
| **Película fotosensible seca (dry film photoresist)**<br><sub>`mat-dry-film-fotosensible`</sub> | n/a | — | rollo 30 cm x 1 m, rollo 30 cm x 5 m, hojas A4 | media |
| **Fibra, lija fina y esponja abrasiva para limpiar cobre**<br><sub>`mat-fibra-lija-limpieza-cobre`</sub> | n/a | — | fibra verde, lija 600, lija 1000, lana de acero 0000 | muy alta |
| **Acetona / thinner para remover tóner**<br><sub>`mat-acetona-thinner`</sub> | n/a | — | acetona pura 250 ml–1 L, thinner estándar | alta |
| **Placa perforada fenólica con islas (perfboard)**<br><sub>`mat-placa-perforada-islas`</sub> | n/a | Rejilla 2.54 mm (2.54 mm) | 5 x 7 cm, 7 x 9 cm, 9 x 15 cm, 10 x 15 cm | muy alta |
| **Placa fenólica perforada Steren (150CC y 155)**<br><sub>`mat-placa-perforada-steren`</sub> | n/a | 150CC (2.54 mm); 155 (2.54 mm) | 150CC: 10.7 x 14 cm, 155: 4.5 x 4.5 cm | alta |
| **Placa perforada de fibra de vidrio doble cara (verde, agujeros metalizados)**<br><sub>`mat-placa-perforada-fr4-doble-verde`</sub> | n/a | Kit surtido (2.54 mm) | 2 x 8 cm, 3 x 7 cm, 4 x 6 cm, 5 x 7 cm, 6 x 8 cm, 7 x 9 cm, 8 x 12 cm, 9 x 15 cm | alta |
| **Placa de tiras (stripboard / veroboard)**<br><sub>`mat-stripboard`</sub> | n/a | Rejilla 2.54 mm (2.54 mm) | varios tamaños | media |
| **Placa soldable con patrón de protoboard**<br><sub>`mat-placa-tipo-protoboard-soldable`</sub> | n/a | Patrón protoboard (2.54 mm, filas 7.62 mm) | tamaño 400 puntos, tamaño 830 puntos | media |
| **Placa fenólica (FR-2) con cobre a una cara**<br><sub>`mat-placa-fenolica-1-cara`</sub> | n/a | Steren PC-5X5; Steren PC-5X10; Steren PC-10X10; Steren PC-10X15; Steren PC-30X30; UNIT 5x5 / 5x10 / 10x10 / 10x15 / 30x30 cm | 5 x 5 cm (PC-5X5), 5 x 10 cm (PC-5X10), 10 x 10 cm (PC-10X10), 10 x 15 cm (PC-10X15), 30 x 30 cm (PC-30X30) | muy alta |
| **Placa de fibra de vidrio (FR-4) con cobre a dos caras**<br><sub>`mat-placa-fr4-2-caras`</sub> | n/a | UNIT: de 5 x 7 cm hasta 20 x 30 cm | 5 x 7 cm, 10 x 10 cm, 10 x 15 cm, 15 x 20 cm, 20 x 30 cm | alta |
| **Placa de fibra de vidrio (FR-4) con cobre a una cara**<br><sub>`mat-placa-fr4-1-cara`</sub> | n/a | Varios tamaños UNIT | 5 x 7 cm, 10 x 10 cm, 10 x 15 cm, 15 x 20 cm, 20 x 30 cm | alta |
| **Placa fenólica (FR-2) con cobre a dos caras**<br><sub>`mat-placa-fenolica-2-caras`</sub> | n/a | Medidas típicas | 10 x 10 cm, 10 x 15 cm | media |
| **Placa fotosensible (presensibilizada) positiva**<br><sub>`mat-placa-presensibilizada`</sub> | n/a | — | 10 x 10 cm, 10 x 15 cm, una cara, doble cara | media |
| **Protoboard de 400 puntos (media)**<br><sub>`mat-protoboard-400`</sub> | n/a | 400 puntos (2.54 mm, filas 7.62 mm) | Steren 509-003, Steren 509-005 (400 puntos, 2 líneas terminales), genérica 400 | muy alta |
| **Protoboard de 830 puntos**<br><sub>`mat-protoboard-830`</sub> | n/a | 830 puntos (2.54 mm, filas 7.62 mm) | Steren 509-010, Steren 509-015 (deslizable), Steren a presión 1 bloque 2 tiras, MB-102 genérica | muy alta |
| **Mini protoboard de 170 puntos**<br><sub>`mat-protoboard-170`</sub> | n/a | 170 puntos (2.54 mm) | blanca, colores surtidos | alta |
| **Tablilla protoboard Steren 509-030 con 3 bornes (1,580 puntos)**<br><sub>`mat-protoboard-steren-509-030`</sub> | n/a | 509-030 (2.54 mm, filas 7.62 mm) | 509-030 | alta |
| **Protoboard múltiple con base de aluminio y bornes (1660/2420/3220 puntos)**<br><sub>`mat-protoboard-multiple-base-aluminio`</sub> | n/a | Base de aluminio (2.54 mm, filas 7.62 mm) | 1660 puntos, 2420 puntos, 3220 puntos | media |
| **Cloruro férrico líquido para grabado de PCB**<br><sub>`mat-cloruro-ferrico-liquido`</sub> | n/a | — | 220 ml (MC025), 250 ml, 500 ml, 930 ml (MC100), 1 L | muy alta |
| **Cloruro férrico en polvo/granulado**<br><sub>`mat-cloruro-ferrico-polvo`</sub> | n/a | — | 250 g, 500 g, 1 kg | media |
| **Método ácido muriático + agua oxigenada (informativo)**<br><sub>`mat-acido-muriatico-agua-oxigenada`</sub> | n/a | — | — | media |
| **Persulfato de amonio (grabador de PCB)**<br><sub>`mat-persulfato-amonio`</sub> | n/a | — | 250 g, 500 g, 1 kg | media |
| **Persulfato de sodio (grabador de PCB)**<br><sub>`mat-persulfato-sodio`</sub> | n/a | — | 250 g, 500 g, 1 kg | media |
| **Cinta de cobre adhesiva**<br><sub>`mat-cinta-cobre-adhesiva`</sub> | n/a | — | 5 mm, 10 mm, 25 mm, 50 mm | media |
| **Pluma de tinta conductiva de cobre Steren (CONDU-PEN)**<br><sub>`mat-pluma-tinta-conductiva`</sub> | n/a | — | CONDU-PEN 6 ml | media |
| **Papel para transferencia térmica de tóner (transfer, couché, glossy)**<br><sub>`mat-papel-transfer-pcb`</sub> | n/a | — | papel transfer amarillo A4, papel couché 130–150 g, papel fotográfico glossy | muy alta |
| **Plumón indeleble para circuito impreso**<br><sub>`mat-plumon-indeleble-pcb`</sub> | n/a | — | Sharpie fino negro, Sharpie ultra fino, Staedtler Lumocolor permanente S/F, Edding | muy alta |
| **Acetato / transparencia para fotolito**<br><sub>`mat-acetato-fotolito`</sub> | n/a | — | tamaño carta, tamaño A4 | alta |
| **Calcomanías y transferibles para PCB (donas, pistas, patrones DIP)**<br><sub>`mat-calcomanias-pcb`</sub> | n/a | — | — | media |
| **Película Press-n-Peel (PnP Blue)**<br><sub>`mat-press-n-peel`</sub> | n/a | — | paquete de 5, 10 o 20 hojas | media |

<a id="soldadura_y_consumibles"></a>
## Soldadura y consumibles

| Componente | Montaje | Encapsulado / huella | Valores o variantes comunes | Popularidad |
|---|---|---|---|---|
| **Pegamento de cianoacrilato (Kola Loca / Super Bonder)**<br><sub>`sol-cianoacrilato`</sub> | n/a | — | 2 g, 5 g, gel | muy alta |
| **Silicón en barra para pistola (hot melt)**<br><sub>`sol-silicon-barra`</sub> | n/a | — | 7 mm, 11 mm, transparente, colores | muy alta |
| **Adhesivo epóxico de 5 minutos**<br><sub>`sol-epoxico-5-min`</sub> | n/a | — | jeringa doble 14–25 ml, tubos | alta |
| **Cinta doble cara (espuma y delgada)**<br><sub>`sol-cinta-doble-cara`</sub> | n/a | — | 12 mm, 19 mm, 24 mm | alta |
| **Silicón RTV de curado neutro**<br><sub>`sol-silicon-rtv-neutro`</sub> | n/a | — | transparente, blanco, negro, alta temperatura (rojo) | alta |
| **Resina para encapsular (potting)**<br><sub>`sol-resina-encapsular`</sub> | n/a | — | kit resina + endurecedor | media |
| **Cinta de aislar (PVC)**<br><sub>`sol-cinta-aislar`</sub> | n/a | — | negra 19 mm, colores | muy alta |
| **Tubo termocontráctil (termofil)**<br><sub>`sol-tubo-termocontractil`</sub> | n/a | — | kit 127 pzs, kit 328 pzs, kit 530 pzs, rollo por metro, negro, colores | muy alta |
| **Cinta Kapton (poliimida) resistente al calor**<br><sub>`sol-cinta-kapton`</sub> | n/a | — | 10 mm, 20 mm, 50 mm | alta |
| **Malla desoldadora (trenza de cobre)**<br><sub>`sol-malla-desoldadora`</sub> | n/a | — | 1.5 mm, 2.0 mm, 2.5 mm, 3.0 mm | alta |
| **Flux en gel en jeringa (tipo RMA-223)**<br><sub>`sol-flux-gel-rma223`</sub> | n/a | — | 10 cc, RMA-223, NC-559 | alta |
| **Pasta para soldar (flux en pasta) en lata**<br><sub>`sol-pasta-para-soldar-lata`</sub> | n/a | — | Steren SOL-060 60 g, Mechanic 60 g, Mechanic 200 g, Mechanic 500 g | alta |
| **Flux líquido**<br><sub>`sol-flux-liquido`</sub> | n/a | — | frasco 30 ml, frasco con pincel | media |
| **Pluma de flux**<br><sub>`sol-pluma-flux`</sub> | n/a | — | 10 ml | media |
| **Alcohol isopropílico (IPA)**<br><sub>`sol-alcohol-isopropilico`</sub> | n/a | — | 250 ml, 500 ml, 1 L, aerosol | muy alta |
| **Limpiador de contactos en aerosol**<br><sub>`sol-limpiador-contactos-aerosol`</sub> | n/a | — | aerosol 150–400 ml | alta |
| **Removedor de flux en aerosol**<br><sub>`sol-removedor-flux`</sub> | n/a | — | aerosol 200–400 ml | media |
| **Esponja de celulosa para base de cautín**<br><sub>`sol-esponja-celulosa`</sub> | n/a | — | cuadrada, redonda | alta |
| **Lana de latón para limpiar punta de cautín**<br><sub>`sol-lana-laton`</sub> | n/a | — | con contenedor, repuesto | alta |
| **Limpiador y regenerador de puntas (tip tinner)**<br><sub>`sol-tip-tinner`</sub> | n/a | — | lata 10 g, lata 15 g | alta |
| **Soldadura de estaño-plomo 60/40 con núcleo de resina**<br><sub>`sol-soldadura-60-40`</sub> | n/a | — | 0.5 mm, 0.6 mm, 0.8 mm, 1.0 mm, 1.2 mm, 1.5 mm, carrete 100 g, carrete 250 g, … (+1) | muy alta |
| **Soldadura en tubo dispensador (pluma)**<br><sub>`sol-soldadura-tubo-dispensador`</sub> | n/a | — | Steren SOL60-020 (17 g), tubo 20 g 1 mm | alta |
| **Soldadura eutéctica 63/37 con núcleo de resina**<br><sub>`sol-soldadura-63-37`</sub> | n/a | — | 0.5 mm, 0.8 mm, 1.0 mm, carrete 100 g, carrete 450 g | alta |
| **Soldadura sin plomo estaño-cobre 99.3/0.7**<br><sub>`sol-soldadura-sin-plomo-sncu`</sub> | n/a | — | 0.8 mm, 1.0 mm, 100 g, 250 g | media |
| **Soldadura sin plomo SAC305**<br><sub>`sol-soldadura-sin-plomo-sac305`</sub> | n/a | — | 0.6 mm, 0.8 mm, 1.0 mm, 100 g | media |
| **Soldadura en barra (para crisol)**<br><sub>`sol-soldadura-barra`</sub> | n/a | — | 60/40, 63/37 | media |
| **Pasta de soldadura para SMD (solder paste)**<br><sub>`sol-pasta-soldadura-smd`</sub> | n/a | — | jeringa 10 cc, frasco 50 g, Sn63Pb37, SAC305 | media |
| **Pasta térmica (grasa disipadora)**<br><sub>`sol-pasta-termica`</sub> | n/a | — | jeringa blanca, jeringa gris, bote | alta |
| **Almohadilla térmica (thermal pad)**<br><sub>`sol-almohadilla-termica`</sub> | n/a | — | 0.5 mm, 1 mm, 2 mm | media |

<a id="herramientas"></a>
## Herramientas e instrumentos

| Componente | Montaje | Encapsulado / huella | Valores o variantes comunes | Popularidad |
|---|---|---|---|---|
| **Base / soporte para cautín**<br><sub>`her-base-cautin`</sub> | n/a | — | base con esponja, base con lana de latón | muy alta |
| **Puntas de repuesto para cautín (cónica, cincel, bisel)**<br><sub>`her-puntas-cautin`</sub> | n/a | — | 900M-T-B, 900M-T-I, 900M-T-K, 900M-T-2.4D, 900M-T-3C, kit 10 puntas | alta |
| **Cautín de temperatura ajustable 60 W (con perilla en el mango)**<br><sub>`her-cautin-ajustable-60w`</sub> | n/a | — | solo cautín, kit con puntas y accesorios | muy alta |
| **Cautín tipo lápiz sin control (25/30/40/60 W)**<br><sub>`her-cautin-lapiz-generico`</sub> | n/a | — | 25 W (CAU-145), 30 W (CAU-105), 35 W (CAU-115/115A), 40 W (CAU-130), 60 W | muy alta |
| **Cautín tipo lápiz Steren 30 W (CAU-105)**<br><sub>`her-cautin-steren-cau-105`</sub> | n/a | — | CAU-105 | muy alta |
| **Cautín tipo lápiz Steren 30 W con ajuste de potencia (CAU-140)**<br><sub>`her-cautin-steren-cau-140`</sub> | n/a | — | CAU-140, CAU-150 (descontinuado) | alta |
| **Cautín de gas butano**<br><sub>`her-cautin-gas-butano`</sub> | n/a | — | — | media |
| **Cautín portátil inteligente (TS100 / TS101 / Pinecil)**<br><sub>`her-cautin-usb-portatil`</sub> | n/a | — | TS100, TS101, Pinecil V2, cautín USB 5 V | media |
| **Cautín tipo pistola / instantáneo 100 W**<br><sub>`her-cautin-pistola-100w`</sub> | n/a | — | 100 W, 100/140 W | media |
| **Fresadora CNC 3018 (como herramienta para PCB)**<br><sub>`her-cnc-3018`</sub> | n/a | — | 3018, 3018 Pro, 3018 Pro Max | media |
| **Fresas V-bit y fresas de corte para CNC (grabado de PCB)**<br><sub>`her-fresas-vbit-cnc`</sub> | n/a | — | V 20° 0.1 mm, V 30° 0.2 mm, kit 10 pzs | media |
| **Cizalla, guillotina o cutter para cortar placa**<br><sub>`her-cortadora-placa`</sub> | n/a | — | — | alta |
| **Sierra de arco (segueta) y caladora**<br><sub>`her-sierra-arco-segueta`</sub> | n/a | — | arco + hoja 32 TPI, mini segueta | alta |
| **Juego de limas de aguja**<br><sub>`her-lima-aguja`</sub> | n/a | — | 6 pzs, 10 pzs | media |
| **Bomba desoldadora / extractor de soldadura**<br><sub>`her-bomba-desoldadora`</sub> | n/a | — | chica, grande de aluminio | muy alta |
| **Cautín desoldador con perilla integrada**<br><sub>`her-cautin-desoldador-perilla`</sub> | n/a | — | — | media |
| **Perilla de succión para desoldar (bulbo de goma)**<br><sub>`her-perilla-succion`</sub> | n/a | — | — | media |
| **Pulsera antiestática (ESD)**<br><sub>`her-pulsera-antiestatica`</sub> | n/a | — | con cable y caimán | alta |
| **Tapete de silicón resistente al calor / tapete ESD**<br><sub>`her-tapete-silicon-esd`</sub> | n/a | — | silicón, ESD con conexión a tierra | media |
| **Estaciones de soldadura Steren (CAU-190 45 W y CAU-245 60 W)**<br><sub>`her-estacion-soldadura-steren`</sub> | n/a | — | CAU-190, CAU-245 | alta |
| **Estación de aire caliente (858D / 8586 / Steren CAU-280)**<br><sub>`her-estacion-aire-caliente`</sub> | n/a | — | 858D, 8586, CAU-280 | alta |
| **Estación de soldadura de temperatura controlada tipo Hakko 936 (y clones)**<br><sub>`her-estacion-soldadura-936`</sub> | n/a | — | 936 analógica, 937D digital, FX-888D | alta |
| **Pistola de calor (heat gun)**<br><sub>`her-pistola-calor`</sub> | n/a | — | — | alta |
| **Estación de soldadura con cartucho T12**<br><sub>`her-estacion-t12`</sub> | n/a | — | kit con mango y fuente, cartuchos T12 | media |
| **Estación profesional para soldar Steren con lupa y lámpara**<br><sub>`her-estacion-soldadura-steren-lupa`</sub> | n/a | — | — | media |
| **Fuente de alimentación de laboratorio 0–30 V 0–5 A**<br><sub>`her-fuente-laboratorio-30v-5a`</sub> | n/a | — | 30 V 5 A, 30 V 3 A, 60 V 5 A | alta |
| **Fuente para protoboard MB102 (3.3 V / 5 V)**<br><sub>`her-fuente-protoboard-mb102`</sub> | modulo | Módulo para riel de protoboard (2.54 mm) | MB102 | alta |
| **Fuente de alimentación de laboratorio 0–30 V 0–10 A**<br><sub>`her-fuente-laboratorio-30v-10a`</sub> | n/a | — | 30 V 10 A | media |
| **Generador de funciones DDS FeelElec FY6900**<br><sub>`her-generador-fy6900`</sub> | n/a | — | FY6900-20M, FY6900-60M, FY6900-100M | media |
| **Generador de funciones en módulo/kit (XR2206, AD9833)**<br><sub>`her-generador-funciones-modulo`</sub> | modulo | — | kit XR2206, módulo AD9833 | media |
| **Cutter de precisión / navaja tipo bisturí**<br><sub>`her-cutter-precision`</sub> | n/a | — | tipo X-Acto #11, cutter 9 mm, cutter 18 mm | muy alta |
| **Juego de desarmadores de precisión**<br><sub>`her-desarmadores-precision`</sub> | n/a | — | 6 pzs, kit de puntas 24–60 pzs | muy alta |
| **Pinzas de corte diagonal y de corte al ras**<br><sub>`her-pinzas-corte-diagonal`</sub> | n/a | — | 4.5 in, 5 in, corte al ras tipo 170 | muy alta |
| **Pinzas de punta (punta larga)**<br><sub>`her-pinzas-punta`</sub> | n/a | — | 5 in, 6 in, punta curva | muy alta |
| **Pinzas pelacables manuales (con calibres)**<br><sub>`her-pinzas-pelacables-manuales`</sub> | n/a | — | 10–22 AWG, 20–30 AWG | muy alta |
| **Pistola de silicón caliente**<br><sub>`her-pistola-silicon`</sub> | n/a | — | chica 7 mm, grande 11 mm | muy alta |
| **Pinzas de crimpeo (ponchadora) RJ45 / RJ11**<br><sub>`her-crimpeadora-rj45`</sub> | n/a | — | RJ45, RJ45/RJ11 | alta |
| **Pinzas de crimpeo Dupont / JST (SN-28B)**<br><sub>`her-crimpeadora-dupont`</sub> | n/a | — | SN-28B, SN-01BM | alta |
| **Pinzas de precisión antiestáticas (tweezers ESD)**<br><sub>`her-pinzas-tweezers-esd`</sub> | n/a | — | recta, curva, kit 6 pzs | alta |
| **Pinzas pelacables automáticas**<br><sub>`her-pinzas-pelacables-automaticas`</sub> | n/a | — | — | alta |
| **Extractor e insertor de circuitos integrados**<br><sub>`her-extractor-insertor-ci`</sub> | n/a | — | — | media |
| **Lupa con luz (de escritorio, de mano o de diadema)**<br><sub>`her-lupa-con-luz`</sub> | n/a | — | de escritorio, de mano, de diadema | alta |
| **Microscopio digital USB**<br><sub>`her-microscopio-usb`</sub> | n/a | — | USB, con pantalla LCD | media |
| **Kit de herramientas Steren para electrónica**<br><sub>`her-kit-herramientas-steren`</sub> | n/a | — | — | media |
| **Multímetro digital económico DT830B**<br><sub>`her-multimetro-dt830b`</sub> | n/a | — | DT830B, DT830D, DT832 | muy alta |
| **Analizador lógico USB de 8 canales (24 MHz)**<br><sub>`her-analizador-logico-24mhz`</sub> | n/a | — | 24 MHz 8 canales | alta |
| **Multímetro autorrango con capacitancia, frecuencia y temperatura**<br><sub>`her-multimetro-autorrango`</sub> | n/a | — | UNI-T UT33C+, UNI-T UT61E+, ANENG AN8008 | alta |
| **Multímetro digital DT9205A**<br><sub>`her-multimetro-dt9205a`</sub> | n/a | — | DT9205A | alta |
| **Multímetros digitales Steren (línea MUL)**<br><sub>`her-multimetro-steren`</sub> | n/a | — | MUL-010, MUL-265, MUL-270, MUL-281, MUL-105 (analógico) | alta |
| **Probador de componentes LCR-T4 / TC1**<br><sub>`her-probador-componentes-lcr-t4`</sub> | n/a | — | LCR-T4, TC1, T7 | alta |
| **Pinza amperimétrica**<br><sub>`her-pinza-amperimetrica`</sub> | n/a | — | AC 400–600 A, AC/DC | media |
| **Probador de continuidad**<br><sub>`her-probador-continuidad`</sub> | n/a | — | — | media |
| **Punta lógica**<br><sub>`her-punta-logica`</sub> | n/a | — | — | media |
| **Calibrador vernier digital 150 mm**<br><sub>`her-vernier-calibrador`</sub> | n/a | — | digital 150 mm, analógico | muy alta |
| **Regla y escuadra metálica**<br><sub>`her-regla-escuadra-metalica`</sub> | n/a | — | 15 cm, 30 cm, escuadra | muy alta |
| **Osciloscopio en kit DSO138**<br><sub>`her-osciloscopio-dso138`</sub> | n/a | — | kit THT, armado | alta |
| **Osciloscopio de banco básico (Rigol DS1054Z, Owon, Hantek, Siglent)**<br><sub>`her-osciloscopio-banco`</sub> | n/a | — | DS1054Z, SDS1102, DSO5102P, SDS1202X-E | media |
| **Osciloscopio de bolsillo / portátil**<br><sub>`her-osciloscopio-bolsillo`</sub> | n/a | — | DSO150, FNIRSI DSO-TC3, Hantek 2D72 | media |
| **Tercera mano con lupa**<br><sub>`her-tercera-mano-lupa`</sub> | n/a | — | con lupa, con lupa y LED | muy alta |
| **Tercera mano con brazos flexibles**<br><sub>`her-tercera-mano-brazos-flexibles`</sub> | n/a | — | 4 brazos, 6 brazos | alta |
| **Soporte / prensa para PCB**<br><sub>`her-soporte-placa-pcb`</sub> | n/a | — | — | media |
| **Brocas de carburo de tungsteno para PCB (zanco 3.175 mm)**<br><sub>`her-brocas-carburo-pcb`</sub> | n/a | — | 0.6 mm, 0.8 mm, 0.9 mm, 1.0 mm, 1.2 mm, 1.5 mm, kit 10 pzs 0.3–1.2 mm | alta |
| **Brocas HSS pequeñas (milimétricas y fraccionales)**<br><sub>`her-brocas-hss-pequenas`</sub> | n/a | — | 0.8 mm, 1.0 mm, 1/32 in, 3/64 in, 1/16 in | alta |
| **Mototool / herramienta rotativa (Dremel)**<br><sub>`her-mototool-dremel`</sub> | n/a | — | Dremel 3000, Dremel 4000, Truper mototool | alta |
| **Minitaladro para PCB de 12 V con portabrocas**<br><sub>`her-minitaladro-pcb-12v`</sub> | n/a | — | motor 385, motor 775, kit con brocas | media |
| **Portabrocas manual (pin vise)**<br><sub>`her-portabrocas-manual`</sub> | n/a | — | — | media |
| **Soporte de columna para minitaladro / Dremel**<br><sub>`her-soporte-columna-taladro`</sub> | n/a | — | Dremel 220, mini drill press 12 V | media |
| **Impresora láser (información para método de planchado)**<br><sub>`her-impresora-laser`</sub> | n/a | — | — | alta |
| **Plancha o laminadora para transferencia térmica**<br><sub>`her-plancha-laminadora`</sub> | n/a | — | plancha doméstica, laminadora A4 | alta |
| **Lámpara UV para insolado (exposición)**<br><sub>`her-lampara-uv-insolado`</sub> | n/a | — | LED 395 nm, LED 405 nm, lámpara de uñas 36–48 W | media |

<a id="energia"></a>
## Energía (pilas, baterías, fuentes)

| Componente | Montaje | Encapsulado / huella | Valores o variantes comunes | Popularidad |
|---|---|---|---|---|
| **Power bank (como fuente para proyectos)**<br><sub>`ene-power-bank`</sub> | n/a | — | 5000 mAh, 10000 mAh, 20000 mAh | alta |
| **Cargador de pilas NiMH AA/AAA**<br><sub>`ene-cargador-pilas-nimh`</sub> | n/a | — | 2 ranuras, 4 ranuras, USB | alta |
| **Cargador balanceador para LiPo (tipo iMAX B6)**<br><sub>`ene-cargador-balanceador-lipo`</sub> | n/a | — | iMAX B6, B6AC | media |
| **Cargador externo para baterías 18650 / Li-ion**<br><sub>`ene-cargador-18650`</sub> | n/a | — | 1 ranura USB, 2 ranuras, 4 ranuras | media |
| **Cargador USB de 5 V (cubo de pared)**<br><sub>`ene-cargador-usb-5v`</sub> | n/a | — | 5 V 1 A, 5 V 2 A, 5 V 2.4 A, USB-C 20 W | muy alta |
| **Eliminador de voltaje fijo 5/9/12 V con plug 5.5 x 2.1 mm**<br><sub>`ene-eliminador-fijo-plug-2-1`</sub> | n/a | Plug 5.5 x 2.1 mm | 5 V 1 A, 5 V 2 A, 9 V 1 A, 12 V 1 A, 12 V 2 A, 12 V 5 A | muy alta |
| **Eliminador de voltaje seleccionable (3–12 V) con puntas intercambiables**<br><sub>`ene-eliminador-voltaje-seleccionable`</sub> | n/a | Plug coaxial intercambiable | 500 mA, 1 A, 2 A | muy alta |
| **Fuente conmutada tipo caja metálica (S-60-12, S-120-12, etc.)**<br><sub>`ene-fuente-conmutada-caja-metalica`</sub> | panel | Bornera de tornillos | 5 V 5 A, 5 V 10 A, 12 V 5 A, 12 V 10 A, 12 V 30 A, 24 V 5 A, 24 V 15 A | alta |
| **Fuente de PC ATX (como recurso de alimentación)**<br><sub>`ene-fuente-atx`</sub> | n/a | — | 300 W, 500 W | media |
| **Batería Li-ion 18650 3.7 V**<br><sub>`ene-bateria-18650`</sub> | n/a | 18650 sin protección (2p); 18650 con protección (2p) | 2000 mAh, 2600 mAh, 3000 mAh, 3400 mAh, con protección, sin protección | muy alta |
| **Batería 18650 con lengüetas de níquel para soldar**<br><sub>`ene-bateria-18650-lengueta`</sub> | n/a | 18650 + lengüetas (2p) | con lengüetas planas, con lengüetas tipo pin | alta |
| **Batería 16340 (Li-ion 3.7 V) / CR123A (litio 3 V)**<br><sub>`ene-bateria-16340-cr123a`</sub> | n/a | 16340 / CR123A (2p) | CR123A, 16340 | media |
| **Batería Li-ion 14500 3.7 V (tamaño AA)**<br><sub>`ene-bateria-14500`</sub> | n/a | 14500 (2p) | 800 mAh, con protección | media |
| **Batería Li-ion 21700 3.7 V**<br><sub>`ene-bateria-21700`</sub> | n/a | 21700 (2p) | 4000 mAh, 5000 mAh | media |
| **Batería LiPo 3.7 V 1S con conector JST-PH**<br><sub>`ene-bateria-lipo-1s`</sub> | n/a | JST-PH 2.0 mm (2p, 2.0 mm) | 150 mAh, 500 mAh, 1000 mAh, 2000 mAh, 3000 mAh | alta |
| **Batería LiPo 2S (7.4 V) / 3S (11.1 V) para RC**<br><sub>`ene-bateria-lipo-2s-3s`</sub> | n/a | Balanceo JST-XH (2.54 mm) | 2S 1000–2200 mAh, 3S 1300–5000 mAh, 20C–50C | media |
| **Pila de 9 V alcalina (cuadrada)**<br><sub>`ene-pila-9v-alcalina`</sub> | n/a | PP3 / 6LR61 (2p) | alcalina 6LR61, zinc-carbón 6F22 | muy alta |
| **Pila de 9 V recargable (NiMH o Li-ion)**<br><sub>`ene-pila-9v-recargable`</sub> | n/a | PP3 (2p) | NiMH 8.4 V, Li-ion USB | media |
| **Pila de botón de litio CR2032 (3 V)**<br><sub>`ene-pila-boton-cr2032`</sub> | n/a | CR2032 (2p) | CR2032 | muy alta |
| **Pila de botón alcalina LR44 / AG13 (1.5 V)**<br><sub>`ene-pila-boton-lr44`</sub> | n/a | LR44 (2p) | LR44, SR44, AG13 | alta |
| **Pila de botón de litio CR1220 (3 V)**<br><sub>`ene-pila-boton-cr1220`</sub> | n/a | CR1220 (2p) | CR1220 | alta |
| **Pila de botón de litio CR2016 (3 V)**<br><sub>`ene-pila-boton-cr2016`</sub> | n/a | CR2016 (2p) | CR2016 | alta |
| **Pila de botón de litio CR2025 (3 V)**<br><sub>`ene-pila-boton-cr2025`</sub> | n/a | CR2025 (2p) | CR2025 | alta |
| **Otras pilas de botón (LR41/AG3, CR2450, CR1632, AG1–AG12)**<br><sub>`ene-pila-boton-otras`</sub> | n/a | LR41 (2p); CR2450 (2p); CR1632 (2p) | LR41/AG3, AG10/LR1130, CR2450, CR1632 | media |
| **Pila AA alcalina 1.5 V**<br><sub>`ene-pila-aa-alcalina`</sub> | n/a | AA (R6/LR6) (2p) | alcalina, zinc-carbón, blíster 2/4/8 pzs | muy alta |
| **Pila AAA alcalina 1.5 V**<br><sub>`ene-pila-aaa-alcalina`</sub> | n/a | AAA (R03/LR03) (2p) | alcalina, zinc-carbón | muy alta |
| **Pilas recargables NiMH AA y AAA 1.2 V**<br><sub>`ene-pila-aa-aaa-nimh`</sub> | n/a | AA (2p); AAA (2p) | AA 2000 mAh, AA 2500 mAh, AAA 800 mAh, AAA 1000 mAh | alta |
| **Pila AA de litio recargable 1.5 V con USB**<br><sub>`ene-pila-aa-litio-usb`</sub> | n/a | AA (2p) | AA, AAA | media |
| **Pilas C y D alcalinas 1.5 V**<br><sub>`ene-pila-c-d`</sub> | n/a | C (LR14) (2p); D (LR20) (2p) | C (LR14), D (LR20) | media |
| **Batería de plomo-ácido sellada 12 V 7 Ah**<br><sub>`ene-bateria-plomo-12v-7ah`</sub> | n/a | 12 V 7 Ah (2p) | 12 V 7 Ah, 12 V 9 Ah | alta |
| **Batería de plomo-ácido sellada 12 V 1.2 Ah**<br><sub>`ene-bateria-plomo-12v-1-2ah`</sub> | n/a | 12 V 1.2 Ah (2p) | 12 V 1.2 Ah, 12 V 1.3 Ah | media |
| **Batería de plomo-ácido sellada 6 V 4.5 Ah**<br><sub>`ene-bateria-plomo-6v-4-5ah`</sub> | n/a | 6 V 4.5 Ah (2p) | 6 V 4.5 Ah, 6 V 4 Ah | media |
| **Panel solar pequeño 5 V / 6 V / 12 V (0.5–10 W)**<br><sub>`ene-panel-solar-pequeno`</sub> | n/a | Panel (2p) | 5 V 1 W, 6 V 2 W, 6 V 3.5 W, 12 V 5 W, 12 V 10 W | media |
