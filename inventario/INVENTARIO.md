# Inventario de componentes electrónicos

Catálogo generado por `build.py` a partir de `datos/`. No editar a mano.

**Total: 503 componentes** en 11 categorías.

| Categoría | Elementos |
|---|---:|
| [Resistores, potenciómetros y afines](#resistores) | 43 |
| [Capacitores](#capacitores) | 21 |
| [Inductores, transformadores y cristales](#inductivos_y_frecuencia) | 23 |
| [Protección (fusibles, varistores, TVS)](#proteccion) | 19 |
| [Semiconductores discretos (diodos, transistores, tiristores)](#semiconductores_discretos) | 86 |
| [Optoelectrónica (LEDs, optoacopladores, displays de LED)](#optoelectronica) | 30 |
| [Sensores](#sensores) | 112 |
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

<a id="semiconductores_discretos"></a>
## Semiconductores discretos (diodos, transistores, tiristores)

| Componente | Montaje | Encapsulado / huella | Valores o variantes comunes | Popularidad |
|---|---|---|---|---|
| **Diodo de recuperación rápida 1 A (FR107 / UF4007 / HER108)**<br><sub>`dio-rapido-fr107-uf4007`</sub> | THT | DO-41 (DO-204AL) plástico (2p, 10.16 mm) | FR101–FR107 (50–1000 V, trr 150–500 ns), UF4001–UF4007 (50–1000 V, trr 50–75 ns), HER101–HER108 (50–1000 V, trr 50–75 ns) | alta |
| **Diodo rápido 2–3 A (FR207 / FR307 / HER308 / UF5408)**<br><sub>`dio-rapido-fr207-fr307-uf5408`</sub> | THT | DO-15 (DO-204AC) (2p, 12.7 mm); DO-201AD (DO-27) (2p, 15.24 mm) | FR207 (2 A 1000 V, DO-15), HER208 (2 A 1000 V, DO-15), FR307 (3 A 1000 V, DO-201AD), HER308 (3 A 1000 V), UF5408 (3 A 1000 V, trr 75 ns) | media |
| **Diodo rectificador 1N4001–1N4007 (1 A)**<br><sub>`dio-1n4001-1n4007`</sub> | THT | DO-41 (DO-204AL) plástico (2p, 10.16 mm) | 1N4001 (50 V), 1N4002 (100 V), 1N4003 (200 V), 1N4004 (400 V), 1N4005 (600 V), 1N4006 (800 V), 1N4007 (1000 V) | muy alta |
| **Diodo rectificador 1N5400–1N5408 (3 A)**<br><sub>`dio-1n5400-1n5408`</sub> | THT | DO-201AD (DO-27) (2p, 15.24 mm) | 1N5400 (50 V), 1N5401 (100 V), 1N5402 (200 V), 1N5404 (400 V), 1N5406 (600 V), 1N5407 (800 V), 1N5408 (1000 V) | alta |
| **Diodo rectificador 6A05–6A10 (6 A) / 10A10**<br><sub>`dio-6a10-r6`</sub> | THT | R-6 (P600) (2p, 20.32 mm) | 6A05 (50 V), 6A1 (100 V), 6A2 (200 V), 6A4 (400 V), 6A6 (600 V), 6A8 (800 V), 6A10 (1000 V), 10A10 (10 A, 1000 V) | media |
| **Diodo Schottky 1N5817 / 1N5818 / 1N5819 (1 A)**<br><sub>`dio-schottky-1n5817-1n5819`</sub> | THT | DO-41 (DO-204AL) plástico (2p, 10.16 mm) | 1N5817 (20 V), 1N5818 (30 V), 1N5819 (40 V), SR160/SB160 (60 V), SR1100 (100 V) | muy alta |
| **Diodo Schottky 3–5 A (1N5820–1N5822, SR540/SR560, SB560)**<br><sub>`dio-schottky-1n5822-sr560`</sub> | THT | DO-201AD (DO-27) (2p, 15.24 mm) | 1N5820 (3 A 20 V), 1N5821 (3 A 30 V), 1N5822 (3 A 40 V), SR540/SB540 (5 A 40 V), SR560/SB560 (5 A 60 V), SR5100 (5 A 100 V) | alta |
| **Diodo de señal/conmutación 1N4148 / 1N914**<br><sub>`dio-1n4148-1n914`</sub> | THT | DO-35 (DO-204AH) vidrio (2p, 7.62 mm) | 1N4148, 1N914, 1N4448 | muy alta |
| **Diodo de germanio 1N34A / 1N60**<br><sub>`dio-germanio-1n34a-1n60`</sub> | THT | DO-7 / DO-35 vidrio (axial) (2p, 7.62 mm) | 1N34A, 1N60, OA90 (ocasional) | media |
| **Diodo rectificador SMD M1–M7 / S1M (SMA)**<br><sub>`dio-smd-m7-s1m`</sub> | SMD | SMA (DO-214AC) (2p) | M1 (50 V), M4 (400 V), M7 (1000 V), S1M (1000 V), S2M (2 A, SMB) | alta |
| **Diodo Schottky SMD SS14 / SS34 / SS36 / SS54**<br><sub>`dio-smd-schottky-ss14-ss34`</sub> | SMD | SMA (DO-214AC) (2p); SMB (DO-214AA) (2p); SMC (DO-214AB) (2p) | SS14 (1 A 40 V, SMA), SS16 (1 A 60 V), SS34 (3 A 40 V, SMA/SMB), SS36 (3 A 60 V), SS54 (5 A 40 V, SMC) | alta |
| **Diodo de señal SMD LL4148 / 1N4148W / 1N4148WS**<br><sub>`dio-smd-ll4148-1n4148w`</sub> | SMD | MiniMELF (SOD-80 / LL-34) (2p); SOD-123 (2p); SOD-323 (2p) | LL4148 (MiniMELF), 1N4148W (SOD-123), 1N4148WS (SOD-323), BAV99 (doble, SOT-23) | media |
| **Diodo Zener SMD (ZMM / MMSZ52xx / BZT52)**<br><sub>`dio-zener-smd`</sub> | SMD | MiniMELF (SOD-80 / LL-34) (2p); SOD-123 (2p) | 3.3 V, 5.1 V, 6.2 V, 9.1 V, 12 V, 15 V, 24 V | media |
| **Diodo Zener 0.5 W (BZX55C / 1N52xxB / BZX79)**<br><sub>`dio-zener-05w`</sub> | THT | DO-35 (DO-204AH) vidrio (2p, 7.62 mm) | 2.7 V, 3.0 V, 3.3 V, 3.6 V, 3.9 V, 4.3 V, 4.7 V, 5.1 V, … (+36) | muy alta |
| **Diodo Zener 1 W (1N4728A–1N4753A / BZX85C)**<br><sub>`dio-zener-1w`</sub> | THT | DO-41 (DO-204AL) plástico (2p, 10.16 mm) | 1N4728A=3.3 V, 1N4729A=3.6 V, 1N4730A=3.9 V, 1N4731A=4.3 V, 1N4732A=4.7 V, 1N4733A=5.1 V, 1N4734A=5.6 V, 1N4735A=6.2 V, … (+17) | alta |
| **DIAC DB3 / DB4**<br><sub>`tir-diac-db3`</sub> | THT | DO-35 (DO-204AH) vidrio (2p, 7.62 mm) | DB3 (VBO 28–36 V), DB4 (≈35–45 V) | alta |
| **Transistor uniunión (UJT) 2N2646 / 2N2647**<br><sub>`tir-ujt-2n2646`</sub> | THT | TO-18 (TO-206AA) metálico (3p) | 2N2646, 2N2647 | media |
| **Transistor uniunión programable (PUT) 2N6027 / 2N6028**<br><sub>`tir-put-2n6027`</sub> | THT | TO-92 (TO-226AA) (3p, 1.27 mm) | 2N6027, 2N6028 (más sensible) | media |
| **Puente rectificador cuadrado 10–50 A (KBPC1010 / KBPC2510 / KBPC3510)**<br><sub>`dio-puente-kbpc`</sub> | panel | KBPC (cuadrado, terminales faston 6.3 mm) (4p); KBPC-W (cuadrado, terminales de alambre) (4p); BR-10x (cuadrado pequeño) (4p) | KBPC1010 (10 A 1000 V), KBPC2510 (25 A 1000 V), KBPC3510 (35 A 1000 V), KBPC5010 (50 A), KBPC3510W (alambre), BR104 (10 A 400 V) | alta |
| **Puente rectificador DIP-4 1 A (DB101–DB107)**<br><sub>`dio-puente-db107`</sub> | THT | DB-1 (DIP-4) (4p, 5.08 mm, filas 7.62 mm); DB-S / DBS (SMD, DB107S) (4p) | DB101 (50 V), DB102 (100 V), DB104 (400 V), DB106 (600 V), DB107 (1000 V), DB107S (SMD), DF10M (1 A 1000 V, DIP-4 pequeño) | alta |
| **Puente rectificador en línea 2–4 A (KBP206/KBP307 / KBL04–KBL410)**<br><sub>`dio-puente-linea-kbp-kbl`</sub> | THT | KBP (en línea, 4 pines) (4p, 3.8 mm); KBL (en línea, 4 pines) (4p, 5.08 mm) | KBP206 (2 A 600 V), KBP210 (2 A 1000 V), KBP307 (3 A 1000 V), KBL04 (4 A 400 V), KBL406 (4 A 600 V), KBL410 (4 A 1000 V), KBL-4/200 (Steren, 4 A 200 V) | alta |
| **Puente rectificador redondo 1.5–2 A (W10M / 2W10 / WB152)**<br><sub>`dio-puente-redondo-w10m-2w10`</sub> | THT | WOB / WOM redondo (4p) | W005M (50 V), W02M (200 V), W04M (400 V), W08M (800 V), W10M (1000 V), 2W10 (2 A 1000 V), WB152 (Steren, 200 V 2 A), WB154 (Steren, 400 V 1.5 A) | alta |
| **Puente rectificador en línea 4–25 A (GBU / KBU / GBJ)**<br><sub>`dio-puente-linea-gbu-kbu-gbj`</sub> | THT | GBU (en línea) (4p); KBU (en línea) (4p); GBJ (en línea) (4p) | GBU4M (4 A 1000 V), GBU6M (6 A), GBU8M (8 A), GBU806/GBU810, KBU8M (8 A), KBU810, GBJ1510 (15 A), GBJ2510 (25 A), … (+1) | media |
| **Puente rectificador SMD MB6S / MB10S**<br><sub>`dio-puente-smd-mb10s`</sub> | SMD | MBS (TO-269AA, SOIC-4) (4p, 2.54 mm) | MB6S (0.5 A 600 V), MB10S (0.5 A 1000 V), MB10F (cuerpo plano), ABS10 (1 A) | media |
| **SCR BT151-500R / -650R / -800R (12 A, TO-220)**<br><sub>`tir-scr-bt151`</sub> | THT | TO-220 (TO-220AB) (3p, 2.54 mm) | BT151-500R, BT151-650R, BT151-800R | alta |
| **SCR C106D / C106M (4 A, TO-126)**<br><sub>`tir-scr-c106`</sub> | THT | TO-126 (SOT-32 / TO-225AA) (3p, 2.29 mm) | C106B (200 V), C106D (400 V), C106M (600 V) | alta |
| **SCR pequeño 2N5060 / MCR100-6 / MCR100-8 (0.8 A, TO-92)**<br><sub>`tir-scr-2n5060-mcr100`</sub> | THT | TO-92 (TO-226AA) (3p, 1.27 mm) | 2N5060 (30 V), 2N5061 (60 V), 2N5062 (100 V), 2N5064 (200 V), MCR100-6 (400 V), MCR100-8 (600 V) | media |
| **SCR TIC106 / TIC126 (5 A / 12 A, TO-220)**<br><sub>`tir-scr-tic106-tic126`</sub> | THT | TO-220 (TO-220AB) (3p, 2.54 mm) | TIC106D (5 A 400 V), TIC106M (5 A 600 V), TIC116D (8 A), TIC126D (12 A 400 V), TIC126M (12 A 600 V) | media |
| **TRIAC aislado BTA08 / BTA12 / BTA16 / BTA24-600B (TO-220AB)**<br><sub>`tir-triac-bta08-bta12-bta16`</sub> | THT | TO-220AB aislado (BTA) / TO-220AB (BTB) (3p, 2.54 mm) | BTA08-600B (8 A), BTA12-600B (12 A), BTA16-600B (16 A), BTA16-800B (16 A 800 V), BTA24-600B (25 A), sufijo BW/CW = snubberless | muy alta |
| **TRIAC BT136 / BT137 / BT138 (4–12 A, TO-220)**<br><sub>`tir-triac-bt136-bt137-bt138`</sub> | THT | TO-220 (TO-220AB) (3p, 2.54 mm) | BT136-600E (4 A), BT137-600E (8 A), BT138-600E (12 A), BT139-600E (16 A), sufijo E = compuerta sensible (≤10 mA) | muy alta |
| **TRIAC BTA41-600B / BTA40 (40 A, TOP3)**<br><sub>`tir-triac-bta41`</sub> | THT | TOP3 aislado (TOP3I) (3p, 5.45 mm) | BTA41-600B, BTA41-800B, BTA40-600B (RD91) | media |
| **TRIAC pequeño MAC97A6 / MAC97A8 (0.8 A, TO-92)**<br><sub>`tir-triac-mac97a`</sub> | THT | TO-92 (TO-226AA) (3p, 1.27 mm) | MAC97A6 (400 V), MAC97A8 (600 V), Z0607 (ST, pinout distinto: verificar) | media |
| **TRIAC TIC226D / TIC226M (8 A, TO-220)**<br><sub>`tir-triac-tic226`</sub> | THT | TO-220 (TO-220AB) (3p, 2.54 mm) | TIC206D (4 A), TIC226D (8 A 400 V), TIC226M (8 A 600 V), TIC246 (16 A) | media |
| **Transistor NPN 2N2222A / PN2222A / MPS2222A (TO-92)**<br><sub>`trn-2n2222a-to92`</sub> | THT | TO-92 (TO-226AA) (3p, 1.27 mm) | 2N2222A (TO-92), PN2222A (Fairchild/onsemi), MPS2222A (Steren), P2N2222A (onsemi, ¡C-B-E!) | muy alta |
| **Transistor NPN 2N3904**<br><sub>`trn-2n3904`</sub> | THT | TO-92 (TO-226AA) (3p, 1.27 mm) | 2N3904, MMBT3904 (SMD SOT-23) | muy alta |
| **Transistor NPN BC546 / BC547 / BC548 / BC549**<br><sub>`trn-bc547-bc548-bc549`</sub> | THT | TO-92 (TO-226AA) (3p, 1.27 mm) | BC546 (65 V), BC547 (45 V), BC548 (30 V), BC549 (30 V, bajo ruido), BC550 (45 V, bajo ruido), sufijo A (hFE 110–220), sufijo B (200–450), sufijo C (420–800) | muy alta |
| **Transistor NPN de potencia TIP31C (3 A)**<br><sub>`trn-tip31c`</sub> | THT | TO-220 (TO-220AB) (3p, 2.54 mm) | TIP31 (40 V), TIP31A (60 V), TIP31B (80 V), TIP31C (100 V) | muy alta |
| **Transistor NPN de potencia TIP41C (6 A)**<br><sub>`trn-tip41c`</sub> | THT | TO-220 (TO-220AB) (3p, 2.54 mm) | TIP41 (40 V), TIP41A (60 V), TIP41B (80 V), TIP41C (100 V) | muy alta |
| **Transistor PNP 2N3906**<br><sub>`trn-2n3906`</sub> | THT | TO-92 (TO-226AA) (3p, 1.27 mm) | 2N3906, MMBT3906 (SOT-23) | muy alta |
| **Transistor PNP BC556 / BC557 / BC558 / BC559**<br><sub>`trn-bc557-bc558`</sub> | THT | TO-92 (TO-226AA) (3p, 1.27 mm) | BC556 (−65 V), BC557 (−45 V), BC558 (−30 V), BC559/BC560 (bajo ruido), sufijos A/B/C | muy alta |
| **Transistor NPN 2N2222A metálico (TO-18)**<br><sub>`trn-2n2222a-to18`</sub> | THT | TO-18 (TO-206AA) metálico (3p) | 2N2222A (TO-18), 2N2219A (TO-39, mayor potencia) | alta |
| **Transistor NPN alto voltaje 2N5551 / 2N5550**<br><sub>`trn-2n5551`</sub> | THT | TO-92 (TO-226AA) (3p, 1.27 mm) | 2N5551 (160 V), 2N5550 (140 V) | alta |
| **Transistor NPN BC337 / BC338 (800 mA)**<br><sub>`trn-bc337`</sub> | THT | TO-92 (TO-226AA) (3p, 1.27 mm) | BC337-16 (hFE 100–250), BC337-25 (160–400), BC337-40 (250–630), BC338 (25 V) | alta |
| **Transistor NPN BD135 / BD137 / BD139 (1.5 A, TO-126)**<br><sub>`trn-bd135-bd137-bd139`</sub> | THT | TO-126 (SOT-32 / TO-225AA) (3p, 2.29 mm) | BD135 (45 V), BD137 (60 V), BD139 (80 V), sufijos -10/-16 (grupo hFE) | alta |
| **Transistor NPN de audio 2SC5200 (C5200)**<br><sub>`trn-2sc5200`</sub> | THT | TO-3PL / TO-264 (Toshiba 2-21F1A) (3p, 5.45 mm) | 2SC5200 (Toshiba/ISC) | alta |
| **Transistor NPN de potencia 2N3055 (TO-3)**<br><sub>`trn-2n3055`</sub> | panel | TO-3 (TO-204AA) metálico (2p, 10.92 mm) | 2N3055, MJE3055T (versión TO-220, pinout B-C-E) | alta |
| **Transistor NPN japonés 2SC945 / 2SC1815 (C945, C1815)**<br><sub>`trn-2sc945-2sc1815`</sub> | THT | TO-92 (TO-226AA) (3p, 1.27 mm) | C945 (2SC945), C1815 (2SC1815, grupos O/Y/GR/BL) | alta |
| **Transistor NPN S8050 / SS8050**<br><sub>`trn-s8050`</sub> | THT | TO-92 (TO-226AA) (3p, 1.27 mm); SOT-23 (TO-236AB) (3p, 0.95 mm) | S8050 (0.5 A), SS8050 (1.5 A), S8050 SMD SOT-23 (marcado J3Y), grados de hFE B/C/D | alta |
| **Transistor NPN S9013 / S9014 / S9018**<br><sub>`trn-s9013-s9014`</sub> | THT | TO-92 (TO-226AA) (3p, 1.27 mm) | S9013 (500 mA), S9014 (100 mA bajo ruido), S9018 (RF, fT ≈700 MHz) | alta |
| **Transistor PNP 2N2907A / PN2907A**<br><sub>`trn-2n2907a`</sub> | THT | TO-92 (TO-226AA) (3p, 1.27 mm); TO-18 (TO-206AA) metálico (3p) | PN2907A (TO-92), 2N2907A (TO-18 metálico), MMBT2907A (SOT-23) | alta |
| **Transistor PNP alto voltaje 2N5401 / 2N5400**<br><sub>`trn-2n5401`</sub> | THT | TO-92 (TO-226AA) (3p, 1.27 mm) | 2N5401 (−150 V), 2N5400 (−120 V) | alta |
| **Transistor PNP BD136 / BD138 / BD140 (1.5 A, TO-126)**<br><sub>`trn-bd136-bd138-bd140`</sub> | THT | TO-126 (SOT-32 / TO-225AA) (3p, 2.29 mm) | BD136 (−45 V), BD138 (−60 V), BD140 (−80 V) | alta |
| **Transistor PNP de audio 2SA1943 (A1943)**<br><sub>`trn-2sa1943`</sub> | THT | TO-3PL / TO-264 (Toshiba 2-21F1A) (3p, 5.45 mm) | 2SA1943 | alta |
| **Transistor PNP de potencia TIP32C (3 A)**<br><sub>`trn-tip32c`</sub> | THT | TO-220 (TO-220AB) (3p, 2.54 mm) | TIP32 (−40 V), TIP32A, TIP32B, TIP32C (−100 V) | alta |
| **Transistor PNP de potencia TIP42C (6 A)**<br><sub>`trn-tip42c`</sub> | THT | TO-220 (TO-220AB) (3p, 2.54 mm) | TIP42 (−40 V), TIP42A, TIP42B, TIP42C (−100 V) | alta |
| **Transistor PNP japonés 2SA733 / 2SA1015 (A733, A1015)**<br><sub>`trn-2sa733-2sa1015`</sub> | THT | TO-92 (TO-226AA) (3p, 1.27 mm) | A733 (2SA733), A1015 (2SA1015) | alta |
| **Transistor PNP S8550 / SS8550**<br><sub>`trn-s8550`</sub> | THT | TO-92 (TO-226AA) (3p, 1.27 mm); SOT-23 (TO-236AB) (3p, 0.95 mm) | S8550 (0.5 A), SS8550 (1.5 A), SMD SOT-23 (marcado 2TY) | alta |
| **Transistor PNP S9012 / S9015**<br><sub>`trn-s9012-s9015`</sub> | THT | TO-92 (TO-226AA) (3p, 1.27 mm) | S9012 (−500 mA), S9015 (−100 mA, bajo ruido) | alta |
| **Transistor NPN 2N4401**<br><sub>`trn-2n4401`</sub> | THT | TO-92 (TO-226AA) (3p, 1.27 mm) | 2N4401, MMBT4401 (SOT-23) | media |
| **Transistor NPN 2SD882 (D882, 3 A)**<br><sub>`trn-d882`</sub> | THT | TO-126 (SOT-32 / TO-225AA) (3p, 2.29 mm); TO-92L / TO-92NL (3p, 1.27 mm) | D882 (TO-126), 2SD882 en SOT-89/TO-252 (pinout distinto) | media |
| **Transistor NPN alta ganancia 2N5088 / 2N5089**<br><sub>`trn-2n5088-2n5089`</sub> | THT | TO-92 (TO-226AA) (3p, 1.27 mm) | 2N5088 (hFE 300–900), 2N5089 (hFE 400–1200) | media |
| **Transistor NPN alto voltaje MJE13005 / MJE13007 (TO-220)**<br><sub>`trn-mje13005-mje13007`</sub> | THT | TO-220 (TO-220AB) (3p, 2.54 mm); TO-220F / ITO-220 (plástico aislado) (3p, 2.54 mm) | MJE13005 (4 A), MJE13007 (8 A), MJE13009 (12 A) | media |
| **Transistor NPN alto voltaje MPSA42 / MPSA43**<br><sub>`trn-mpsa42`</sub> | THT | TO-92 (TO-226AA) (3p, 1.27 mm) | MPSA42 (300 V), MPSA43 (200 V), KSP42 | media |
| **Transistor NPN de potencia TIP3055 (15 A)**<br><sub>`trn-tip3055`</sub> | THT | TO-247 (TO-247AC) (3p, 5.45 mm) | TIP3055 | media |
| **Transistor PNP 2N4403**<br><sub>`trn-2n4403`</sub> | THT | TO-92 (TO-226AA) (3p, 1.27 mm) | 2N4403 | media |
| **Transistor PNP 2SB772 (B772, 3 A)**<br><sub>`trn-b772`</sub> | THT | TO-126 (SOT-32 / TO-225AA) (3p, 2.29 mm) | B772 (TO-126) | media |
| **Transistor PNP alto voltaje MPSA92 / MPSA93**<br><sub>`trn-mpsa92`</sub> | THT | TO-92 (TO-226AA) (3p, 1.27 mm) | MPSA92 (−300 V), MPSA93 (−200 V) | media |
| **Transistor PNP BC327 / BC328 (800 mA)**<br><sub>`trn-bc327`</sub> | THT | TO-92 (TO-226AA) (3p, 1.27 mm) | BC327-16, BC327-25, BC327-40, BC328 (−25 V) | media |
| **Transistor PNP de potencia MJ2955 (TO-3)**<br><sub>`trn-mj2955`</sub> | panel | TO-3 (TO-204AA) metálico (2p, 10.92 mm) | MJ2955, MJE2955T (TO-220) | media |
| **Transistor PNP de potencia TIP2955 (15 A)**<br><sub>`trn-tip2955`</sub> | THT | TO-247 (TO-247AC) (3p, 5.45 mm) | TIP2955 | media |
| **Transistor Darlington NPN TIP120 / TIP121 / TIP122 (5 A)**<br><sub>`trn-tip120-tip122`</sub> | THT | TO-220 (TO-220AB) (3p, 2.54 mm) | TIP120 (60 V), TIP121 (80 V), TIP122 (100 V) | muy alta |
| **Transistor Darlington PNP TIP125 / TIP126 / TIP127 (5 A)**<br><sub>`trn-tip125-tip127`</sub> | THT | TO-220 (TO-220AB) (3p, 2.54 mm) | TIP125 (−60 V), TIP126 (−80 V), TIP127 (−100 V) | alta |
| **JFET canal N 2N3819 (TO-92)**<br><sub>`trn-jfet-2n3819`</sub> | THT | TO-92 (TO-226AA) (3p, 1.27 mm) | 2N3819 | media |
| **JFET canal N 2N5457 / MPF102 / J201 (TO-92)**<br><sub>`trn-jfet-2n5457-mpf102-j201`</sub> | THT | TO-92 (TO-226AA) (3p, 1.27 mm) | 2N5457 (IDSS 1–5 mA), 2N5458 (2–9 mA), 2N5459 (4–16 mA), MPF102 (2–20 mA), J201 (0.2–1 mA), J113, J310 (RF) | media |
| **JFET canal N BF245A / BF245B / BF245C**<br><sub>`trn-jfet-bf245`</sub> | THT | TO-92 (TO-226AA) (3p, 1.27 mm) | BF245A (IDSS 2–6.5 mA), BF245B (6–15 mA), BF245C (12–25 mA) | media |
| **MOSFET canal N IRF520 / IRF530 / IRF540N (100 V, TO-220)**<br><sub>`trn-irf520-irf530-irf540`</sub> | THT | TO-220 (TO-220AB) (3p, 2.54 mm) | IRF520N (9.7 A, 0.20 Ω), IRF530N (17 A, 0.09 Ω), IRF530 (14 A, 0.16 Ω), IRF540N (33 A, 0.044 Ω), IRF540 (28 A, 0.077 Ω) | muy alta |
| **MOSFET canal N IRFZ44N (55 V, 49 A)**<br><sub>`trn-irfz44n`</sub> | THT | TO-220 (TO-220AB) (3p, 2.54 mm) | IRFZ44N, IRFZ48N (64 A), IRFZ46N (53 A) | muy alta |
| **MOSFET canal N 2N7000 (TO-92)**<br><sub>`trn-2n7000`</sub> | THT | TO-92 (TO-226AA) (3p, 1.27 mm) | 2N7000, 2N7002 (versión SOT-23) | alta |
| **MOSFET canal N IRF3205 (55 V, 110 A)**<br><sub>`trn-irf3205`</sub> | THT | TO-220 (TO-220AB) (3p, 2.54 mm) | IRF3205 | alta |
| **MOSFET canal N nivel lógico IRLZ44N / IRLZ34N / IRL540N**<br><sub>`trn-irlz44n-irlz34n`</sub> | THT | TO-220 (TO-220AB) (3p, 2.54 mm) | IRLZ44N (55 V 47 A, ≈22–25 mΩ), IRLZ34N (55 V 30 A, ≈35–46 mΩ), IRL540N (100 V, ≈36 A) | alta |
| **MOSFET canal N SMD AO3400 / 2N7002 (SOT-23)**<br><sub>`trn-ao3400-2n7002`</sub> | SMD | SOT-23 (TO-236AB) (3p, 0.95 mm) | AO3400A (30 V 5.7 A, marcado A09T), SI2302 (20 V 2.6 A), 2N7002 (60 V 115 mA), 2N7002K (300 mA) | alta |
| **MOSFET canal P IRF9540N / IRF9530N / IRF4905**<br><sub>`trn-irf9540n-irf9530n`</sub> | THT | TO-220 (TO-220AB) (3p, 2.54 mm) | IRF9530N (−100 V −14 A, 0.20 Ω), IRF9540N (−100 V −23 A, 0.117 Ω), IRF4905 (−55 V −74 A, 0.02 Ω) | alta |
| **MOSFET canal N alto voltaje IRF840 / IRF740 / IRF830**<br><sub>`trn-irf840-irf740`</sub> | THT | TO-220 (TO-220AB) (3p, 2.54 mm); TO-220F / ITO-220 (plástico aislado) (3p, 2.54 mm) | IRF840 (500 V 8 A, 0.85 Ω), IRF830 (500 V 4.5 A, 1.5 Ω), IRF740 (400 V 10 A, 0.55 Ω) | media |
| **MOSFET canal N BS170 (TO-92)**<br><sub>`trn-bs170`</sub> | THT | TO-92 (TO-226AA) (3p, 1.27 mm) | BS170 | media |
| **MOSFET canal N TO-247 IRFP250N / IRFP260N / IRFP460**<br><sub>`trn-irfp250-irfp260`</sub> | THT | TO-247 (TO-247AC) (3p, 5.45 mm) | IRFP250N (200 V 30 A, 0.075 Ω), IRFP260N (200 V 50 A, 0.04 Ω), IRFP460 (500 V 20 A, 0.27 Ω) | media |
| **MOSFET canal P SMD AO3401 (SOT-23)**<br><sub>`trn-ao3401`</sub> | SMD | SOT-23 (TO-236AB) (3p, 0.95 mm) | AO3401A (−30 V −4 A, marcado A19T), SI2301 (−20 V) | media |

<a id="optoelectronica"></a>
## Optoelectrónica (LEDs, optoacopladores, displays de LED)

| Componente | Montaje | Encapsulado / huella | Valores o variantes comunes | Popularidad |
|---|---|---|---|---|
| **Display de 7 segmentos de 1 dígito 0.36" / 0.56" / 0.8" / 1"**<br><sub>`opt-display-7seg-1-digito`</sub> | THT | 0.56" 1 dígito (DIP-10) (10p, 2.54 mm, filas 15.24 mm); 0.36" 1 dígito (10 pines) (10p, 2.54 mm); 0.8" y 1" 1 dígito (10 pines) (10p, 2.54 mm) | 0.56" cátodo común rojo (5161AS), 0.56" ánodo común rojo (5161BS), verde, azul, amarillo, blanco, 0.36", 0.8", … (+3) | muy alta |
| **Display de 7 segmentos de 4 dígitos 0.36" / 0.56" (12 pines, multiplexado)**<br><sub>`opt-display-7seg-4-digitos`</sub> | THT | 0.56" 4 dígitos (12 pines) (12p, 2.54 mm, filas 15.24 mm); 0.36" 4 dígitos (12 pines) (12p, 2.54 mm) | 0.56" cátodo común (5461AS), 0.56" ánodo común (5461BS), 0.36" CC (3461AS), 0.36" CA (3461BS), rojo, verde, azul, con dos puntos de reloj (14–16 pines, pinout distinto) | alta |
| **Matriz LED 8x8 (1088AS / 1088BS / 788BS / 1588BS)**<br><sub>`opt-matriz-led-8x8`</sub> | THT | 1088AS/BS 32 x 32 mm, punto de 3 mm (16 pines) (16p, 2.54 mm); 788BS 20 x 20 mm, punto de 1.9 mm (16 pines) (16p, 2.54 mm); 1588BS ≈38 x 38 mm (16 pines) (16p, 2.54 mm) | 1088AS (rojo 3 mm), 1088BS (polaridad invertida), 788BS (20 mm), 1588BS (38 mm), rojo, verde, bicolor (24 pines) | alta |
| **Barra de LED de 10 segmentos (bargraph DIP-20)**<br><sub>`opt-barra-led-10-segmentos`</sub> | THT | DIP-20 (bargraph) (20p, 2.54 mm, filas 7.62 mm) | rojo, verde, amarillo, azul, multicolor (verde/amarillo/rojo) | media |
| **Fototransistor (PT333-3C / 3DU5C / L14G1)**<br><sub>`opt-fototransistor`</sub> | THT | LED 5 mm (T-1¾) radial (2p, 2.54 mm); LED 3 mm (T-1) radial (2p, 2.54 mm); TO-18 con lente (L14G1/L14G2), 3 patas (3p) | 5 mm transparente (luz visible/IR), 5 mm negro (solo IR), 3 mm, L14G1 (TO-18) | alta |
| **Fotodiodo (BPW34 / 5 mm IR negro / PD333)**<br><sub>`opt-fotodiodo`</sub> | THT | LED 5 mm (T-1¾) radial (2p, 2.54 mm); BPW34 (plano, 2 patas) (2p, 5.08 mm) | BPW34, 5 mm negro 940 nm, 5 mm transparente, PD333-3C | media |
| **LED infrarrojo emisor 940 nm / 850 nm (3 y 5 mm)**<br><sub>`opt-led-ir-940nm`</sub> | THT | LED 5 mm (T-1¾) radial (2p, 2.54 mm); LED 3 mm (T-1) radial (2p, 2.54 mm) | 940 nm transparente, 940 nm azulado, 850 nm, 5 mm, 3 mm | muy alta |
| **Receptor infrarrojo 38 kHz VS1838B / HS0038 / TL1838**<br><sub>`opt-receptor-ir-vs1838b`</sub> | THT | Receptor IR 3 pines con domo (3p, 2.54 mm) | VS1838B, HS0038B, TL1838, 38 kHz | muy alta |
| **Receptor infrarrojo Vishay TSOP4838 / TSOP1738**<br><sub>`opt-receptor-ir-tsop4838`</sub> | THT | Receptor IR Vishay 3 pines (3p, 2.54 mm) | TSOP4838 (OUT-GND-VS), TSOP38238 (OUT-GND-VS), TSOP1738 (GND-VS-OUT, obsoleto) | media |
| **Diodo láser rojo 650 nm 5 mW (cabezal Ø6 mm / módulo KY-008)**<br><sub>`opt-laser-650nm-ky008`</sub> | modulo | Cabezal láser Ø6 mm con cables (2p); Módulo KY-008 (header 3 pines) (3p, 2.54 mm) | 650 nm 5 mW punto, 650 nm línea, 650 nm cruz, 3 V y 5 V | media |
| **LED 3 mm (colores estándar y alta luminosidad)**<br><sub>`opt-led-3mm`</sub> | THT | LED 3 mm (T-1) radial (2p, 2.54 mm) | rojo, verde, amarillo, naranja, azul, blanco, difuso, transparente (alto brillo), … (+1) | muy alta |
| **LED 5 mm (difuso, transparente y ultrabrillante)**<br><sub>`opt-led-5mm`</sub> | THT | LED 5 mm (T-1¾) radial (2p, 2.54 mm); LED 5 mm 'sombrero de paja' (straw hat) (2p, 2.54 mm) | rojo, verde, amarillo, naranja, azul, blanco, blanco cálido, violeta/UV 395 nm, … (+3) | muy alta |
| **LED RGB 5 mm de 4 patas, ánodo común**<br><sub>`opt-led-rgb-anodo-comun`</sub> | THT | LED 5 mm RGB 4 patas (4p, 1.27 mm) | difuso, transparente, 3 mm (menos común), 8 mm (menos común) | muy alta |
| **LED 8 mm y 10 mm (jumbo)**<br><sub>`opt-led-8mm-10mm`</sub> | THT | LED 8 mm radial (2p, 2.54 mm); LED 10 mm radial (2p, 2.54 mm) | rojo, verde, amarillo, azul, blanco, RGB lento (2 patas), difuso, transparente | alta |
| **LED auto-intermitente y multicolor automático (arcoíris) 3/5 mm**<br><sub>`opt-led-intermitente-multicolor`</sub> | THT | LED 3 mm (T-1) radial (2p, 2.54 mm); LED 5 mm (T-1¾) radial (2p, 2.54 mm) | intermitente rojo, intermitente verde/amarillo/azul, RGB lento (slow), RGB rápido (fast), 3 mm y 5 mm | alta |
| **LED bicolor 5 mm (2 y 3 patas)**<br><sub>`opt-led-bicolor`</sub> | THT | LED 5 mm bicolor 2 patas (2p, 2.54 mm); LED 5 mm bicolor 3 patas (3p, 2.54 mm) | rojo/verde 2 patas, rojo/verde 3 patas cátodo común, rojo/verde 3 patas ánodo común, 3 mm | alta |
| **LED RGB 5 mm de 4 patas, cátodo común**<br><sub>`opt-led-rgb-catodo-comun`</sub> | THT | LED 5 mm RGB 4 patas (4p, 1.27 mm) | difuso, transparente | alta |
| **LED rectangular, cuadrado y triangular (2x5x7, 3x4)**<br><sub>`opt-led-formas`</sub> | THT | LED rectangular 2x5x7 mm (2p, 2.54 mm) | rojo, verde, amarillo, azul, blanco, bicolor | media |
| **LED de potencia 1 W / 3 W (con estrella de aluminio)**<br><sub>`opt-led-potencia-1w-3w`</sub> | THT/SMD | Emisor de potencia (tipo Lumileds/Bridgelux genérico) (2p); Estrella de aluminio (MCPCB) 20 mm (2p) | 1 W blanco frío/cálido, 3 W blanco, rojo, verde, azul, UV 395 nm, RGB 3 W (6 pads) | alta |
| **LED SMD 0603 / 0805 / 1206**<br><sub>`opt-led-smd-0805-1206`</sub> | SMD | 0603 (1608 métrico) (2p); 0805 (2012 métrico) (2p); 1206 (3216 métrico) (2p) | rojo, verde, amarillo, azul, blanco, naranja | alta |
| **LED SMD PLCC 3528 / 2835 / 5050**<br><sub>`opt-led-smd-plcc-3528-2835-5050`</sub> | SMD | 3528 (PLCC-2) (2p); 2835 (2p); 5050 (PLCC-6) (6p) | 3528 blanco/colores (≈20 mA), 2835 blanco 0.2–0.5 W, 5050 blanco (≈60 mA, 3 chips), 5050 RGB | alta |
| **Optoacoplador con salida TRIAC MOC3010/3011/3020/3021/3023 (fase aleatoria)**<br><sub>`opt-moc3021-moc3011`</sub> | THT | DIP-6 (6p, 2.54 mm, filas 7.62 mm) | MOC3010 (250 V, IFT 15 mA), MOC3011 (250 V, 10 mA), MOC3012 (5 mA), MOC3020 (400 V, 30 mA), MOC3021 (400 V, 15 mA), MOC3022 (10 mA), MOC3023 (5 mA) | muy alta |
| **Optoacoplador PC817 / EL817 / LTV-817 / TLP521-1 (DIP-4)**<br><sub>`opt-pc817`</sub> | THT | DIP-4 (4p, 2.54 mm, filas 7.62 mm); SOP-4 / SMD-4 (PC817 SMD) (4p, 2.54 mm) | PC817 (rangos A, B, C, D de CTR), EL817, LTV-817, TLP521-1, PC817 SMD | muy alta |
| **Optoacoplador 4N25 / 4N26 / 4N35 / 4N33 (DIP-6)**<br><sub>`opt-4n25-4n35`</sub> | THT | DIP-6 (6p, 2.54 mm, filas 7.62 mm) | 4N25 (CTR ≥20 %), 4N26, 4N28, 4N35 (CTR ≥100 %), 4N37, 4N33 (Darlington, CTR ≥500 %) | alta |
| **Optoacoplador con TRIAC y cruce por cero MOC3041/3042/3043 y MOC3061/3062/3063**<br><sub>`opt-moc3041-moc3063`</sub> | THT | DIP-6 (6p, 2.54 mm, filas 7.62 mm) | MOC3041 (400 V, IFT 15 mA), MOC3042 (10 mA), MOC3043 (5 mA), MOC3061 (600 V, 15 mA), MOC3062 (10 mA), MOC3063 (600 V, 5 mA) | alta |
| **Optoacoplador digital rápido 6N137 (10 Mbit/s)**<br><sub>`opt-6n137`</sub> | THT | DIP-8 (8p, 2.54 mm, filas 7.62 mm) | 6N137, HCPL-2601, HCPL-2631 (doble) | media |
| **Optoacoplador multicanal TLP521-2 / TLP521-4 / PC827 / PC847**<br><sub>`opt-tlp521-multicanal`</sub> | THT | DIP-8 (8p, 2.54 mm, filas 7.62 mm); DIP-16 (16p, 2.54 mm, filas 7.62 mm) | TLP521-2 / PC827 (2 canales, DIP-8), TLP521-4 / PC847 (4 canales, DIP-16) | media |
| **Sensor óptico reflectivo TCRT5000 / TCRT5000L (suelto)**<br><sub>`opt-tcrt5000`</sub> | THT | TCRT5000 4 pines (4p) | TCRT5000, TCRT5000L (patas largas) | alta |
| **Interruptor óptico ranurado H21A1 / ITR9608 / TCST2103**<br><sub>`opt-interruptor-ranurado`</sub> | THT | Optointerruptor ranurado 4 pines (4p) | H21A1, ITR9608, TCST2103, MOC70T2 | media |
| **Sensor óptico reflectivo CNY70**<br><sub>`opt-cny70`</sub> | THT | CNY70 4 pines (4p) | CNY70 | media |

<a id="sensores"></a>
## Sensores

| Componente | Montaje | Encapsulado / huella | Valores o variantes comunes | Popularidad |
|---|---|---|---|---|
| **Higrómetro de suelo resistivo YL-69 / FC-28 (sonda + placa LM393)**<br><sub>`sen-humedad-suelo-resistivo`</sub> | modulo | Placa de control con header 1x4 (VCC, GND, DO, AO) + 2 pines hacia la sonda (4p, 2.54 mm); Sonda de horquilla con 2 pines (2p, 2.54 mm) | YL-69 + YL-38, FC-28 | muy alta |
| **Sensor capacitivo de humedad de suelo v1.2 / v2.0**<br><sub>`sen-humedad-suelo-capacitivo`</sub> | modulo | Sonda-placa con conector PH2.0 de 3 pines (paso 2.0 mm) + cable a Dupont 2.54 (3p, 2.0 mm) | v1.2, v2.0 | muy alta |
| **Interruptor de nivel tipo flotador (vertical, con reed switch)**<br><sub>`sen-flotador-nivel`</sub> | panel | Cuerpo de PP con rosca y 2 cables (2p) | vertical, horizontal, acero inoxidable | alta |
| **Sensor de flujo de agua YF-S201 (1/2")**<br><sub>`sen-flujo-yf-s201`</sub> | n/a | Cuerpo de plástico con roscas G1/2" y cable de 3 hilos (3p) | YF-S201 1/2", YF-S401 1/4", YF-B5 | alta |
| **Sensor de lluvia FC-37 / YL-83 (placa detectora + LM393)**<br><sub>`sen-lluvia-fc37`</sub> | modulo | Placa de control con header 1x4 (VCC, GND, DO, AO) + 2 pines a la placa detectora (4p, 2.54 mm); Placa detectora con 2 pines (2p, 2.54 mm) | FC-37, YL-83, con relevador (UNIT) | alta |
| **Sensor de nivel de agua tipo tira (Water Sensor)**<br><sub>`sen-nivel-agua-tira`</sub> | modulo | Módulo con header 1x3 a 2.54 mm (3p, 2.54 mm) | Water Sensor rojo | alta |
| **Módulo sensor de pH PH-4502C con electrodo BNC**<br><sub>`sen-ph-4502c`</sub> | modulo | Placa con header 1x6 a 2.54 mm + conector BNC (6p, 2.54 mm) | PH-4502C + E-201-C | media |
| **Sensor de turbidez del agua (sonda + placa adaptadora)**<br><sub>`sen-turbidez`</sub> | modulo | Placa adaptadora con header 1x3 a 2.54 mm + cable a la sonda (3p, 2.54 mm) | SEN0189 | media |
| **Sensor TDS de calidad de agua (sólidos disueltos totales)**<br><sub>`sen-tds`</sub> | modulo | Placa con header 1x3 (o conector PH2.0) + sonda con conector de 2 pines (3p, 2.54 mm) | TDS v1.0 | media |
| **Lector de huella dactilar óptico AS608 / R307 / FPM10A**<br><sub>`sen-huella-as608`</sub> | modulo | Módulo con conector de 6 pines de paso pequeño (≈1.0–1.25 mm) y cable (6p) | AS608, R307, FPM10A | alta |
| **Oxímetro y sensor de pulso MAX30102**<br><sub>`sen-max30102`</sub> | modulo | Módulo con header 1x7 a 2.54 mm (7p, 2.54 mm) | MAX30102 morado | alta |
| **Sensor de pulso cardiaco óptico (Pulse Sensor / XD-58C)**<br><sub>`sen-pulso-cardiaco`</sub> | modulo | Disco Ø16 mm con 3 cables o pines (3p, 2.54 mm) | XD-58C, XD-58D | alta |
| **Módulo de electrocardiograma (ECG) AD8232**<br><sub>`sen-ad8232`</sub> | modulo | Módulo con header 1x6 a 2.54 mm + jack 3.5 mm para electrodos (6p, 2.54 mm) | AD8232 + cable 3 electrodos | media |
| **Oxímetro y sensor de pulso MAX30100 (GY-MAX30100)**<br><sub>`sen-max30100`</sub> | modulo | Módulo con header 1x7 a 2.54 mm (7p, 2.54 mm) | GY-MAX30100 | media |
| **Sensor de corriente por efecto Hall ACS712 (5 A / 20 A / 30 A)**<br><sub>`sen-acs712`</sub> | modulo | Módulo con header 1x3 a 2.54 mm + bornera de tornillo de 2 posiciones (3p, 2.54 mm); IC SOIC-8 (SMD) (8p, 1.27 mm) | 5 A (185 mV/A), 20 A (100 mV/A), 30 A (66 mV/A) | muy alta |
| **Medidor de energía AC PZEM-004T v3.0 (UART/Modbus)**<br><sub>`sen-pzem-004t`</sub> | modulo | Placa con header TTL 1x4 + borneras de línea AC y transformador de corriente (4p, 2.54 mm) | 100 A con TC, 10 A con shunt interno | alta |
| **Módulo sensor de voltaje DC 0–25 V (divisor resistivo)**<br><sub>`sen-voltaje-0-25v`</sub> | modulo | Módulo con bornera de 2 posiciones (VCC, GND de entrada) + header 1x3 a 2.54 mm (3p, 2.54 mm) | 0–25 V | alta |
| **Sensor de corriente AC no invasivo SCT-013 (pinza)**<br><sub>`sen-sct-013`</sub> | n/a | Pinza de núcleo partido con cable ≈1 m y plug de 3.5 mm (2p) | SCT-013-000 (100 A : 50 mA), SCT-013-030 (30 A / 1 V), SCT-013-050 (50 A / 1 V) | alta |
| **Sensor de corriente, voltaje y potencia INA219 (I2C)**<br><sub>`sen-ina219`</sub> | modulo | Módulo con header 1x6 a 2.54 mm + bornera de 2 posiciones (VIN+, VIN−) (6p, 2.54 mm) | shunt 0.1 Ω (R100) | alta |
| **Módulo sensor de voltaje AC ZMPT101B**<br><sub>`sen-zmpt101b`</sub> | modulo | Módulo con header 1x4 a 2.54 mm + bornera de 2 posiciones para la línea AC (4p, 2.54 mm) | ZMPT101B | media |
| **Sensor de corriente y voltaje INA226 (I2C, 16 bits, hasta 36 V)**<br><sub>`sen-ina226`</sub> | modulo | Módulo con header de 2.54 mm (8p, 2.54 mm) | shunt R100 (0.1 Ω), shunt R010 (0.01 Ω) | media |
| **Sensor de movimiento PIR HC-SR501**<br><sub>`sen-pir-hc-sr501`</sub> | modulo | Módulo con header macho 1x3 a 2.54 mm (3p, 2.54 mm) | HC-SR501 | muy alta |
| **Sensor infrarrojo de obstáculos FC-51 (y KY-032)**<br><sub>`sen-ir-obstaculo-fc51`</sub> | modulo | Módulo FC-51 con header 1x3 a 2.54 mm (3p, 2.54 mm); Módulo KY-032 con header 1x4 (GND, +, OUT, EN) (4p, 2.54 mm) | FC-51, KY-032 | muy alta |
| **Sensor ultrasónico de distancia HC-SR04**<br><sub>`sen-hc-sr04`</sub> | modulo | Módulo con header macho 1x4 a 2.54 mm (centrado en el borde inferior) (4p, 2.54 mm) | HC-SR04 (5 V) | muy alta |
| **Sensor óptico reflectivo TCRT5000 (módulo y suelto)**<br><sub>`sen-tcrt5000`</sub> | modulo | Módulo LM393 con header 1x4 a 2.54 mm (4p, 2.54 mm); TCRT5000 suelto (THT 4 patas) (4p) | módulo 4 pines, TCRT5000 suelto | muy alta |
| **Módulo seguidor de línea de 3 y 5 canales (TCRT5000)**<br><sub>`sen-seguidor-linea-multicanal`</sub> | modulo | Módulo de 5 canales con header 1x7 a 2.54 mm (7p, 2.54 mm); Módulo de 3 canales con header 1x5 a 2.54 mm (5p, 2.54 mm) | 3 canales, 5 canales | alta |
| **Sensor de distancia láser ToF VL53L0X**<br><sub>`sen-vl53l0x`</sub> | modulo | Módulo con header 1x6 a 2.54 mm (6p, 2.54 mm) | GY-530, GY-VL53L0XV2 | alta |
| **Sensor de movimiento por microondas (radar Doppler) RCWL-0516**<br><sub>`sen-rcwl-0516`</sub> | modulo | Módulo con 5 pines a 2.54 mm (fila en un extremo) (5p, 2.54 mm) | RCWL-0516 | alta |
| **Sensor ultrasónico HC-SR04P (3.3–5 V)**<br><sub>`sen-hc-sr04p`</sub> | modulo | Módulo con header macho 1x4 a 2.54 mm (4p, 2.54 mm) | HC-SR04P | alta |
| **Sensor ultrasónico impermeable JSN-SR04T**<br><sub>`sen-jsn-sr04t`</sub> | modulo | Placa de control con header/bornera 1x4 a 2.54 mm + transductor con cable (4p, 2.54 mm) | v2.0, v3.0 | alta |
| **Mini sensor PIR AM312**<br><sub>`sen-am312`</sub> | modulo | Módulo con 3 pines a 2.54 mm (3p, 2.54 mm) | AM312 | media |
| **Sensor de distancia infrarrojo Sharp GP2Y0A21YK0F (10–80 cm)**<br><sub>`sen-sharp-gp2y0a21`</sub> | modulo | Cuerpo con conector JST PH de 3 pines (paso 2.0 mm) (3p, 2.0 mm) | GP2Y0A21YK0F (10–80 cm), GP2Y0A02YK0F (20–150 cm), GP2Y0A41SK0F (4–30 cm) | media |
| **Sensor de distancia láser ToF VL53L1X (hasta 4 m)**<br><sub>`sen-vl53l1x`</sub> | modulo | Módulo con header 1x6 a 2.54 mm (6p, 2.54 mm) | VL53L1X | media |
| **Módulo encoder rotativo KY-040**<br><sub>`sen-encoder-ky040`</sub> | modulo | Módulo con header 1x5 a 2.54 mm (a 90°) (5p, 2.54 mm) | KY-040 | muy alta |
| **Módulo joystick analógico KY-023**<br><sub>`sen-joystick-ky023`</sub> | modulo | Módulo con header 1x5 a 2.54 mm (a 90°) (5p, 2.54 mm) | KY-023 | muy alta |
| **Botón táctil capacitivo TTP223**<br><sub>`sen-touch-ttp223`</sub> | modulo | Módulo con header 1x3 a 2.54 mm (3p, 2.54 mm) | TTP223 rojo, TTP223 azul | alta |
| **Controlador táctil capacitivo de 12 canales MPR121**<br><sub>`sen-mpr121`</sub> | modulo | Módulo con header de 2.54 mm + 12 pads de electrodo (6p, 2.54 mm) | MPR121 | media |
| **Teclado capacitivo de 16 teclas TTP229**<br><sub>`sen-ttp229`</sub> | modulo | Placa con header de 2.54 mm (P1 de 4 pines + P2 de 8 salidas) (12p, 2.54 mm) | TTP229 16 teclas | media |
| **Amplificador/convertidor para celdas de carga HX711**<br><sub>`sen-hx711`</sub> | modulo | Módulo con header 1x4 (lado MCU) + 1x6 (lado celda) a 2.54 mm (10p, 2.54 mm) | HX711 verde, HX711 rojo | muy alta |
| **Celda de carga de barra (1, 5, 10, 20 kg)**<br><sub>`sen-celda-carga-barra`</sub> | n/a | Barra de aluminio con 4 cables (4p) | 1 kg, 5 kg, 10 kg, 20 kg | alta |
| **Galga de báscula 50 kg de medio puente (3 cables)**<br><sub>`sen-celda-carga-50kg`</sub> | n/a | Placa metálica con 3 cables (3p) | 50 kg c/u, kit de 4 + HX711 | alta |
| **Galga extensométrica BF350-3AA (350 Ω)**<br><sub>`sen-galga-bf350`</sub> | n/a | Galga adhesiva con 2 terminales de soldar (2p) | 350 Ω | media |
| **Sensor de flexión (flex sensor) 2.2" y 4.5"**<br><sub>`sen-flex`</sub> | THT | Tira con 2 terminales (2p, 2.54 mm) | 2.2 pulgadas, 4.5 pulgadas | media |
| **Sensor de fuerza resistivo FSR402 (y FSR400/FSR406)**<br><sub>`sen-fsr402`</sub> | THT | Película redonda con cola y 2 terminales (2p, 2.54 mm) | FSR400 (Ø5 mm), FSR402 (Ø12.7 mm), FSR406 (38 mm cuadrado) | media |
| **Sensor de gas MQ-135 (módulo)**<br><sub>`sen-mq-135`</sub> | modulo | Módulo MQ con header macho 1x4 a 2.54 mm (4p, 2.54 mm); Sensor MQ suelto de 6 patas (ver sen-mq-suelto) (6p) | MQ-135 módulo, MQ-135 suelto | muy alta |
| **Sensor de gas MQ-2 (módulo)**<br><sub>`sen-mq-2`</sub> | modulo | Módulo MQ con header macho 1x4 a 2.54 mm (4p, 2.54 mm); Sensor MQ suelto de 6 patas (ver sen-mq-suelto) (6p) | MQ-2 módulo, MQ-2 suelto | muy alta |
| **Sensor de gas MQ-3 (módulo)**<br><sub>`sen-mq-3`</sub> | modulo | Módulo MQ con header macho 1x4 a 2.54 mm (4p, 2.54 mm); Sensor MQ suelto de 6 patas (ver sen-mq-suelto) (6p) | MQ-3 módulo, MQ-3 suelto | alta |
| **Sensor de gas MQ-7 (módulo)**<br><sub>`sen-mq-7`</sub> | modulo | Módulo MQ con header macho 1x4 a 2.54 mm (4p, 2.54 mm); Sensor MQ suelto de 6 patas (ver sen-mq-suelto) (6p) | MQ-7 módulo, MQ-7 suelto | alta |
| **Sensor de gas serie MQ suelto (6 patas, para PCB)**<br><sub>`sen-mq-suelto`</sub> | THT | Base de baquelita con 6 patas en círculo y capuchón de malla metálica (6p) | MQ-2, MQ-3, MQ-4, MQ-5, MQ-6, MQ-7, MQ-8, MQ-9, … (+1) | alta |
| **Sensor ambiental BME680 (gas VOC, presión, temperatura y humedad)**<br><sub>`sen-bme680`</sub> | modulo | Módulo con header 1x6 (6p, 2.54 mm) | CJMCU-680 | media |
| **Sensor de calidad del aire CCS811 (eCO2 y TVOC, CJMCU-811)**<br><sub>`sen-ccs811`</sub> | modulo | Módulo CJMCU-811 con header 1x8 a 2.54 mm (8p, 2.54 mm) | CJMCU-811, CCS811 + HDC1080 | media |
| **Sensor de calidad del aire SGP30 (TVOC y eCO2, I2C)**<br><sub>`sen-sgp30`</sub> | modulo | Módulo con header 1x4 a 2.54 mm (4p, 2.54 mm) | SGP30 | media |
| **Sensor de CO2 infrarrojo NDIR MH-Z19B / MH-Z19C**<br><sub>`sen-mh-z19`</sub> | modulo | Módulo con pines a 2.54 mm en los extremos (o conector JST con cable) (7p, 2.54 mm) | MH-Z19B 0–5000 ppm, MH-Z19C, rango 0–2000/5000/10000 ppm | media |
| **Sensor de gas MQ-4 (módulo)**<br><sub>`sen-mq-4`</sub> | modulo | Módulo MQ con header macho 1x4 a 2.54 mm (4p, 2.54 mm); Sensor MQ suelto de 6 patas (ver sen-mq-suelto) (6p) | MQ-4 módulo, MQ-4 suelto | media |
| **Sensor de gas MQ-5 (módulo)**<br><sub>`sen-mq-5`</sub> | modulo | Módulo MQ con header macho 1x4 a 2.54 mm (4p, 2.54 mm); Sensor MQ suelto de 6 patas (ver sen-mq-suelto) (6p) | MQ-5 módulo, MQ-5 suelto | media |
| **Sensor de gas MQ-6 (módulo)**<br><sub>`sen-mq-6`</sub> | modulo | Módulo MQ con header macho 1x4 a 2.54 mm (4p, 2.54 mm); Sensor MQ suelto de 6 patas (ver sen-mq-suelto) (6p) | MQ-6 módulo, MQ-6 suelto | media |
| **Sensor de gas MQ-8 (módulo)**<br><sub>`sen-mq-8`</sub> | modulo | Módulo MQ con header macho 1x4 a 2.54 mm (4p, 2.54 mm); Sensor MQ suelto de 6 patas (ver sen-mq-suelto) (6p) | MQ-8 módulo, MQ-8 suelto | media |
| **Sensor de gas MQ-9 (módulo)**<br><sub>`sen-mq-9`</sub> | modulo | Módulo MQ con header macho 1x4 a 2.54 mm (4p, 2.54 mm); Sensor MQ suelto de 6 patas (ver sen-mq-suelto) (6p) | MQ-9 módulo, MQ-9 suelto | media |
| **Sensor óptico de polvo Sharp GP2Y1010AU0F**<br><sub>`sen-polvo-gp2y1010`</sub> | modulo | Cuerpo con conector de 6 hilos (paso pequeño ≈1.5 mm, verificar) (6p) | GP2Y1010AU0F | media |
| **Módulo sensor de luz con fotorresistencia LDR (KY-018 / LM393)**<br><sub>`sen-ldr-modulo`</sub> | modulo | Módulo serie KY-0xx, header macho 1x3 a 2.54 mm (3p, 2.54 mm); Módulo comparador LM393, header macho 1x4 a 2.54 mm (4p, 2.54 mm) | KY-018, módulo LM393 4 pines, módulo LM393 3 pines | muy alta |
| **Sensor de color TCS3200 / TCS230 (módulo GY-31)**<br><sub>`sen-tcs3200`</sub> | modulo | Módulo con 2 tiras de 4 pines a 2.54 mm (a los lados) (8p, 2.54 mm) | TCS3200, TCS230 | alta |
| **Sensor de intensidad luminosa BH1750 (GY-302)**<br><sub>`sen-bh1750`</sub> | modulo | Módulo GY-302 con header 1x5 a 2.54 mm (5p, 2.54 mm) | GY-302 | alta |
| **Sensor de color RGB TCS34725 (I2C)**<br><sub>`sen-tcs34725`</sub> | modulo | Módulo con header 1x7 a 2.54 mm (7p, 2.54 mm) | TCS34725 | media |
| **Sensor de gestos, proximidad y color APDS-9960**<br><sub>`sen-apds9960`</sub> | modulo | Módulo con header 1x6 a 2.54 mm (6p, 2.54 mm) | GY-9960-3.3 | media |
| **Sensor de luz ultravioleta GUVA-S12SD**<br><sub>`sen-uv-guva-s12sd`</sub> | modulo | Módulo con header 1x3 a 2.54 mm (3p, 2.54 mm) | GUVA-S12SD | media |
| **Sensor de luz ultravioleta ML8511 (GY-8511)**<br><sub>`sen-uv-ml8511`</sub> | modulo | Módulo con header 1x5 a 2.54 mm (5p, 2.54 mm) | GY-8511 | media |
| **Módulo reed switch KY-021 / KY-025**<br><sub>`sen-reed-modulo`</sub> | modulo | Módulo serie KY-0xx, header macho 1x3 a 2.54 mm (3p, 2.54 mm); Módulo KY-025 con header 1x4 (AO, G, +, DO) (4p, 2.54 mm); Reed switch suelto en ampolla de vidrio (THT axial, 2 terminales) (2p) | KY-021, KY-025, reed suelto | alta |
| **Sensor de efecto Hall A3144 (interruptor unipolar)**<br><sub>`sen-hall-a3144`</sub> | THT | UA / TO-92S plano (SIP-3) (3p, 1.27 mm) | A3144, OH3144E | alta |
| **Módulo sensor Hall digital KY-003 (A3144)**<br><sub>`sen-ky-003`</sub> | modulo | Módulo serie KY-0xx, header macho 1x3 a 2.54 mm (3p, 2.54 mm) | KY-003 | media |
| **Módulo sensor Hall lineal KY-024 (49E + LM393)**<br><sub>`sen-ky-024`</sub> | modulo | Módulo con header 1x4 a 2.54 mm (4p, 2.54 mm) | KY-024 | media |
| **Sensor de efecto Hall lineal SS49E**<br><sub>`sen-hall-ss49e`</sub> | THT | TO-92S plano (SIP-3) (3p, 1.27 mm) | SS49E | media |
| **Acelerómetro y giroscopio de 6 ejes MPU-6050 (GY-521)**<br><sub>`sen-mpu6050`</sub> | modulo | Módulo GY-521 con header 1x8 a 2.54 mm (8p, 2.54 mm) | GY-521 | muy alta |
| **Acelerómetro digital de 3 ejes ADXL345 (GY-291)**<br><sub>`sen-adxl345`</sub> | modulo | Módulo GY-291 con header 1x8 a 2.54 mm (8p, 2.54 mm) | GY-291 | alta |
| **Interruptor de inclinación de bola SW-520D (suelto)**<br><sub>`sen-inclinacion-sw520d`</sub> | THT | Cilindro metálico con 2 patas (2p) | SW-520D, SW-200D | alta |
| **Magnetómetro / brújula digital de 3 ejes HMC5883L / QMC5883L (GY-273)**<br><sub>`sen-hmc5883l-qmc5883l`</sub> | modulo | Módulo GY-273 con header 1x5 a 2.54 mm (5p, 2.54 mm) | HMC5883L (0x1E), QMC5883L (0x0D) | alta |
| **Módulo sensor de inclinación (KY-020 / LM393 con SW-520D)**<br><sub>`sen-inclinacion-modulo`</sub> | modulo | Módulo serie KY-0xx, header macho 1x3 a 2.54 mm (3p, 2.54 mm); Módulo comparador LM393, header macho 1x3 a 2.54 mm (3p, 2.54 mm) | KY-020, módulo LM393 3 pines | alta |
| **Módulo sensor de vibración SW-420**<br><sub>`sen-vibracion-sw420`</sub> | modulo | Módulo comparador LM393, header macho 1x3 a 2.54 mm (3p, 2.54 mm) | SW-420 | alta |
| **Acelerómetro analógico de 3 ejes ADXL335 (GY-61)**<br><sub>`sen-adxl335`</sub> | modulo | Módulo GY-61 con header 1x5 a 2.54 mm (5p, 2.54 mm) | GY-61 | media |
| **IMU de 9 ejes MPU-9250 (GY-9250)**<br><sub>`sen-mpu9250`</sub> | modulo | Módulo con header 1x10 a 2.54 mm (10p, 2.54 mm) | GY-9250, GY-6500 (sin magnetómetro) | media |
| **Interruptor de vibración de resorte SW-18010P (suelto)**<br><sub>`sen-vibracion-sw18010p`</sub> | THT | Cilindro con 2 patas (2p) | SW-18010P, SW-18015P, SW-18020P (distinta sensibilidad) | media |
| **Módulo sensor de golpe KY-031 (knock sensor)**<br><sub>`sen-golpe-ky031`</sub> | modulo | Módulo serie KY-0xx, header macho 1x3 a 2.54 mm (3p, 2.54 mm) | KY-031 | media |
| **Kit de 37 sensores (serie KY-0xx)**<br><sub>`sen-kit-37-sensores`</sub> | n/a | — | KY-001 DS18B20, KY-002 vibración, KY-003 Hall, KY-004 botón, KY-005 LED IR, KY-006 buzzer pasivo, KY-008 láser, KY-009 LED RGB SMD, … (+29) | alta |
| **Módulo sensor de llama infrarrojo (760–1100 nm)**<br><sub>`sen-flama`</sub> | modulo | Módulo comparador LM393, header macho 1x4 a 2.54 mm (4p, 2.54 mm); Módulo KY-026 con header 1x4 (AO, G, +, DO) (4p, 2.54 mm) | 4 pines, 3 pines, 5 canales, KY-026 | alta |
| **Kit de 45 sensores en 1**<br><sub>`sen-kit-45-sensores`</sub> | n/a | — | 45 módulos (variable) | media |
| **Micrófono electret (cápsula suelta de 2 pines)**<br><sub>`sen-microfono-electret`</sub> | THT | Cápsula Ø6 x 5 mm con 2 patas (2p); Cápsula Ø9.7 mm (alto 4.5–6.7 mm) con 2 patas o pads (2p) | Ø6 x 5 mm, Ø9.7 x 4.5 mm, Ø9.7 x 6.7 mm | muy alta |
| **Módulo sensor de sonido KY-038 (micrófono pequeño + LM393)**<br><sub>`sen-ky-038`</sub> | modulo | Módulo con header 1x4 a 2.54 mm (4p, 2.54 mm) | KY-038 | muy alta |
| **Módulo sensor de sonido KY-037 (micrófono grande, alta sensibilidad)**<br><sub>`sen-ky-037`</sub> | modulo | Módulo con header 1x4 a 2.54 mm (4p, 2.54 mm) | KY-037 | alta |
| **Módulo sensor de sonido LM393 de 3 pines (salida digital)**<br><sub>`sen-sonido-lm393`</sub> | modulo | Módulo comparador LM393, header macho 1x3 a 2.54 mm (3p, 2.54 mm) | FC-04 | alta |
| **Módulo amplificador de micrófono con AGC MAX9814**<br><sub>`sen-max9814`</sub> | modulo | Módulo con header 1x5 a 2.54 mm (5p, 2.54 mm) | MAX9814 | media |
| **Módulo amplificador de micrófono MAX4466 (ganancia ajustable)**<br><sub>`sen-max4466`</sub> | modulo | Módulo con header 1x3 a 2.54 mm (3p, 2.54 mm) | MAX4466 | media |
| **Módulo DHT11 de 3 pines (KY-015 y similares)**<br><sub>`sen-dht11-modulo`</sub> | modulo | Módulo con header macho 1x3 a 2.54 mm (3p, 2.54 mm) | KY-015, módulo azul 3 pines | muy alta |
| **Sensor de temperatura analógico LM35 (TO-92)**<br><sub>`sen-lm35`</sub> | THT | TO-92 (3p, 1.27 mm) | LM35DZ (0–100 °C), LM35CZ, LM35 TO-92 | muy alta |
| **Sensor de temperatura digital DS18B20 (TO-92)**<br><sub>`sen-ds18b20`</sub> | THT | TO-92 (3p, 1.27 mm); Módulo serie KY-0xx, header macho 1x3 a 2.54 mm (3p, 2.54 mm) | DS18B20 TO-92, módulo KY-001 | muy alta |
| **Sensor de temperatura y humedad DHT11 (suelto, 4 pines)**<br><sub>`sen-dht11`</sub> | THT | SIP-4 (cuerpo plástico azul con rejilla) (4p, 2.54 mm) | DHT11 azul | muy alta |
| **Sensor de temperatura y humedad DHT22 / AM2302 (suelto, 4 pines)**<br><sub>`sen-dht22`</sub> | THT | SIP-4 (cuerpo plástico blanco con rejilla) (4p, 2.54 mm) | DHT22, AM2302 | muy alta |
| **Sonda impermeable DS18B20 (acero inoxidable con cable)**<br><sub>`sen-ds18b20-sonda`</sub> | n/a | Sonda de acero inoxidable con cable de 3 hilos (3p) | 1 m, 2 m, 3 m | muy alta |
| **Módulo DHT22 / AM2302 con cables o placa de 3 pines**<br><sub>`sen-dht22-modulo`</sub> | modulo | Módulo con header macho 1x3 a 2.54 mm (3p, 2.54 mm); AM2302 en carcasa con 3 cables (rojo/amarillo/negro) (3p) | placa 3 pines, AM2302 con cables, AM2301A | alta |
| **Módulo MAX6675 con termopar tipo K**<br><sub>`sen-max6675-termopar`</sub> | modulo | Módulo con header 1x5 a 2.54 mm + bornera de 2 tornillos para el termopar (5p, 2.54 mm) | módulo solo, kit con termopar M6 (0–400 °C típ.) | alta |
| **Módulo sensor de temperatura con termistor NTC (KY-013 / LM393)**<br><sub>`sen-ntc-modulo`</sub> | modulo | Módulo serie KY-0xx, header macho 1x3 a 2.54 mm (3p, 2.54 mm); Módulo comparador LM393, header macho 1x4 a 2.54 mm (4p, 2.54 mm) | NTC 10 kΩ B≈3950, KY-013, módulo LM393 4 pines | alta |
| **Sensor ambiental BME280 (presión, temperatura y humedad)**<br><sub>`sen-bme280`</sub> | modulo | Módulo 3.3 V con header 1x6 (VCC, GND, SCL, SDA, CSB, SDO) (6p, 2.54 mm); Módulo 5 V con header 1x4 (VIN, GND, SCL, SDA) (4p, 2.54 mm); IC LGA-8 (SMD) (8p) | 3.3 V 6 pines, 5 V 4 pines | alta |
| **Sensor de presión y temperatura BMP280 (módulo GY-BMP280)**<br><sub>`sen-bmp280`</sub> | modulo | Módulo GY-BMP280-3.3 con header 1x6 (6p, 2.54 mm); IC LGA-8 (SMD, tapa metálica) (8p, 0.65 mm) | módulo 3.3 V 6 pines, módulo 5 V 4 pines, IC suelto | alta |
| **Sensor de temperatura analógico TMP36 (TO-92)**<br><sub>`sen-tmp36`</sub> | THT | TO-92 (3p, 1.27 mm) | TMP36GT9Z | alta |
| **Sonda termopar tipo K (rosca M6, bayoneta o gota)**<br><sub>`sen-termopar-k`</sub> | n/a | Sonda con 2 hilos o terminales de horquilla (2p) | M6 0–400 °C, gota de fibra de vidrio, −50 a 400 °C | alta |
| **Termómetro infrarrojo sin contacto MLX90614 (GY-906)**<br><sub>`sen-mlx90614`</sub> | modulo | Módulo GY-906 con header 1x4 (4p, 2.54 mm) | MLX90614ESF-BAA (3 V, 90°), MLX90614ESF-AAA (5 V), MLX90614ESF-DCC/DCI (campo estrecho) | alta |
| **Módulo AHT20 + BMP280 (humedad, temperatura y presión)**<br><sub>`sen-aht20-bmp280`</sub> | modulo | Módulo con header 1x4 (4p, 2.54 mm) | AHT20+BMP280 | media |
| **Módulo MAX31855 para termopar (K) — y el IC SO-8**<br><sub>`sen-max31855`</sub> | modulo | Módulo con header 1x5 o 1x6 a 2.54 mm + bornera para termopar (6p, 2.54 mm); IC SO-8 (SMD) (8p, 1.27 mm) | MAX31855K (tipo K), MAX31855 J/T | media |
| **Sensor de presión barométrica BMP180 (módulo GY-68)**<br><sub>`sen-bmp180`</sub> | modulo | Módulo GY-68 con header 1x4 (algunos 1x5 con salida 3.3 V) (4p, 2.54 mm) | GY-68 | media |
| **Sensor de temperatura LM335 (zener de temperatura, TO-92)**<br><sub>`sen-lm335`</sub> | THT | TO-92 (3p, 1.27 mm) | LM335Z, LM335AZ | media |
| **Sensor de temperatura y humedad AHT10 (módulo I2C)**<br><sub>`sen-aht10`</sub> | modulo | Módulo con header 1x4 (4p, 2.54 mm) | AHT10 | media |
| **Sensor de temperatura y humedad HTU21D (módulo GY-21)**<br><sub>`sen-htu21d`</sub> | modulo | Módulo con header 1x4 (4p, 2.54 mm) | HTU21D, Si7021, SHT21 | media |
| **Sensor de temperatura y humedad SHT31 (módulo GY-SHT31-D)**<br><sub>`sen-sht31`</sub> | modulo | Módulo con header 1x6 (6p, 2.54 mm) | SHT31, SHT30 | media |
| **Sensor de temperatura y humedad SHT40 (IC SMD DFN-4)**<br><sub>`sen-sht40`</sub> | SMD | DFN-4 (4p) | SHT40-AD1B (0x44) | media |

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
