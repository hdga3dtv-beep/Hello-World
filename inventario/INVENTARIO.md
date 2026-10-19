# Inventario de componentes electrónicos

Catálogo generado por `build.py` a partir de `datos/`. No editar a mano.

**Total: 1176 componentes** en 22 categorías.

| Categoría | Elementos |
|---|---:|
| [Resistores, potenciómetros y afines](#resistores) | 43 |
| [Capacitores](#capacitores) | 21 |
| [Inductores, transformadores y cristales](#inductivos_y_frecuencia) | 23 |
| [Protección (fusibles, varistores, TVS)](#proteccion) | 19 |
| [Semiconductores discretos (diodos, transistores, tiristores)](#semiconductores_discretos) | 86 |
| [Optoelectrónica (LEDs, optoacopladores, displays de LED)](#optoelectronica) | 30 |
| [Circuitos integrados](#circuitos_integrados) | 264 |
| [Placas de desarrollo (Arduino, ESP, Raspberry Pi) y programadores](#placas_desarrollo) | 70 |
| [Módulos de comunicación](#modulos_comunicacion) | 36 |
| [Sensores](#sensores) | 112 |
| [Displays y pantallas](#displays) | 37 |
| [Actuadores y audio (motores, servos, buzzers, bocinas)](#actuadores_y_audio) | 37 |
| [Módulos de potencia y control](#modulos_potencia) | 42 |
| [Módulos varios (RTC, SD, audio, ADC...)](#modulos_varios) | 25 |
| [Electromecánicos (botones, interruptores, relevadores)](#electromecanicos) | 41 |
| [Conectores, bases y portapilas](#conectores) | 75 |
| [Cables y alambres](#cables) | 23 |
| [Mecánicos (disipadores, separadores, gabinetes)](#mecanicos) | 23 |
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

<a id="circuitos_integrados"></a>
## Circuitos integrados

| Componente | Montaje | Encapsulado / huella | Valores o variantes comunes | Popularidad |
|---|---|---|---|---|
| **Amplificador operacional cuádruple LM324**<br><sub>`ic-lm324`</sub> | THT/SMD | DIP-14 (14p, 2.54 mm, filas 7.62 mm); SOIC-14 (14p, 1.27 mm, filas 5.4 mm) | LM324N, LM2902N | muy alta |
| **Amplificador operacional doble LM358**<br><sub>`ic-lm358`</sub> | THT/SMD | DIP-8 (8p, 2.54 mm, filas 7.62 mm); SOIC-8 (8p, 1.27 mm, filas 5.4 mm) | LM358N, LM358P, LM2904 (automotriz) | muy alta |
| **Amplificador operacional LM741**<br><sub>`ic-lm741`</sub> | THT/SMD | DIP-8 (8p, 2.54 mm, filas 7.62 mm); SOIC-8 (8p, 1.27 mm, filas 5.4 mm) | LM741CN, UA741CP, MC1741CP1 (Steren) | muy alta |
| **Amplificador operacional doble de bajo ruido NE5532**<br><sub>`ic-ne5532`</sub> | THT/SMD | DIP-8 (8p, 2.54 mm, filas 7.62 mm); SOIC-8 (8p, 1.27 mm, filas 5.4 mm) | NE5532P, NE5532AP, LM833N (equivalente de pinout) | alta |
| **Amplificador operacional doble JFET TL072 / TL082**<br><sub>`ic-tl072`</sub> | THT/SMD | DIP-8 (8p, 2.54 mm, filas 7.62 mm); SOIC-8 (8p, 1.27 mm, filas 5.4 mm) | TL072CP, TL082CP, LF353N, TL062CP (bajo consumo) | alta |
| **Amplificador operacional doble JRC4558**<br><sub>`ic-jrc4558`</sub> | THT/SMD | DIP-8 (8p, 2.54 mm, filas 7.62 mm); SOIC-8 (8p, 1.27 mm, filas 5.4 mm) | JRC4558D, NJM4558D, RC4558P | alta |
| **Amplificador de instrumentación AD620**<br><sub>`ic-ad620`</sub> | THT/SMD | DIP-8 (8p, 2.54 mm, filas 7.62 mm); SOIC-8 (8p, 1.27 mm, filas 5.4 mm) | AD620AN (DIP-8), AD620ARZ (SOIC-8) | media |
| **Amplificador operacional BiMOS CA3140**<br><sub>`ic-ca3140`</sub> | THT | DIP-8 (8p, 2.54 mm, filas 7.62 mm) | CA3140EZ, CA3140E | media |
| **Amplificador operacional cuádruple JFET TL074 / TL084**<br><sub>`ic-tl074`</sub> | THT/SMD | DIP-14 (14p, 2.54 mm, filas 7.62 mm); SOIC-14 (14p, 1.27 mm, filas 5.4 mm) | TL074CN, TL084CN | media |
| **Amplificador operacional de precisión OP07**<br><sub>`ic-op07`</sub> | THT/SMD | DIP-8 (8p, 2.54 mm, filas 7.62 mm); SOIC-8 (8p, 1.27 mm, filas 5.4 mm) | OP07CP, OP07DP | media |
| **Amplificador operacional doble rail-to-rail MCP6002**<br><sub>`ic-mcp6002`</sub> | THT/SMD | DIP-8 (8p, 2.54 mm, filas 7.62 mm); SOIC-8 (8p, 1.27 mm, filas 5.4 mm); SOT-23-5 (MCP6001, sencillo) (5p, 0.95 mm) | MCP6002-I/P (DIP-8), MCP6002-I/SN (SOIC-8), MCP6004 (cuádruple DIP-14, pinout tipo LM324) | media |
| **Amplificador operacional sencillo JFET TL071 / TL081**<br><sub>`ic-tl071`</sub> | THT/SMD | DIP-8 (8p, 2.54 mm, filas 7.62 mm); SOIC-8 (8p, 1.27 mm, filas 5.4 mm) | TL071CP, TL081CP | media |
| **Amplificador de audio de baja potencia LM386**<br><sub>`ic-lm386`</sub> | THT/SMD | DIP-8 (8p, 2.54 mm, filas 7.62 mm); SOIC-8 (8p, 1.27 mm, filas 5.4 mm) | LM386N-1 (4–12 V), LM386N-3 (4–12 V, más potencia), LM386N-4 (5–18 V, ≈1 W) | muy alta |
| **Amplificador clase D estéreo 3 W PAM8403 (chip)**<br><sub>`ic-pam8403`</sub> | SMD | SOP-16 (150 mil) (16p, 1.27 mm, filas 5.4 mm) | PAM8403DR-H (chip SOP-16), Módulo PAM8403 con potenciómetro | alta |
| **Amplificador de audio 10 W TDA2003**<br><sub>`ic-tda2003`</sub> | THT | Pentawatt V (TO-220-5 vertical) (5p, 1.7 mm) | TDA2003V (vertical), TDA2003H (horizontal), TDA2003A | alta |
| **Amplificador de audio 100 W TDA7294 / TDA7296**<br><sub>`ic-tda7294`</sub> | THT | Multiwatt-15 V (15p, 1.27 mm) | TDA7294V, TDA7296 (60 W, mismo pinout), TDA7293V (pinout parecido, ver notas) | alta |
| **Amplificador de audio 18 W TDA2030A**<br><sub>`ic-tda2030a`</sub> | THT | Pentawatt V (TO-220-5 vertical) (5p, 1.7 mm) | TDA2030AV, TDA2030AH | alta |
| **Amplificador de audio 32 W TDA2050**<br><sub>`ic-tda2050`</sub> | THT | Pentawatt V (TO-220-5 vertical) (5p, 1.7 mm) | TDA2050V | alta |
| **Amplificador clase D 2x50 W TPA3116D2 (chip)**<br><sub>`ic-tpa3116d2`</sub> | SMD | HTSSOP-32 (DAD, PowerPAD arriba) (32p, 0.65 mm) | TPA3116D2DAD, Módulos 2×50 W, 100 W mono, 2.1 | media |
| **Amplificador cuádruple para auto TDA7388**<br><sub>`ic-tda7388`</sub> | THT | Flexiwatt-25 (25p, 1.0 mm) | TDA7388, TDA7386 / TDA7384 (familia, pinout similar) | media |
| **Amplificador de audio 20 W LM1875**<br><sub>`ic-lm1875`</sub> | THT | TO-220-5 (5p, 1.7 mm) | LM1875T | media |
| **Amplificador de audio 68 W LM3886**<br><sub>`ic-lm3886`</sub> | THT | TO-220-11 (TF aislado / T no aislado) (11p, 1.7 mm) | LM3886TF, LM3886T | media |
| **Amplificador de audio estéreo 2x15 W TDA7297**<br><sub>`ic-tda7297`</sub> | THT | Multiwatt-15 V (15p, 1.27 mm) | TDA7297 | media |
| **Amplificador de audio estéreo de bajo voltaje TDA2822**<br><sub>`ic-tda2822`</sub> | THT/SMD | DIP-8 (8p, 2.54 mm, filas 7.62 mm); SOIC-8 (8p, 1.27 mm, filas 5.4 mm) | TDA2822M | media |
| **Amplificador de audio estéreo LA4440**<br><sub>`ic-la4440`</sub> | THT | SIP-14H (con aleta) (14p) | LA4440 | media |
| **Amplificador de audio para auto TDA7377**<br><sub>`ic-tda7377`</sub> | THT | Multiwatt-15 V (15p, 1.27 mm) | TDA7377 | media |
| **Comparador doble LM393**<br><sub>`ic-lm393`</sub> | THT/SMD | DIP-8 (8p, 2.54 mm, filas 7.62 mm); SOIC-8 (8p, 1.27 mm, filas 5.4 mm) | LM393P, LM393N, LM2903 | muy alta |
| **Comparador cuádruple LM339**<br><sub>`ic-lm339`</sub> | THT/SMD | DIP-14 (14p, 2.54 mm, filas 7.62 mm); SOIC-14 (14p, 1.27 mm, filas 5.4 mm) | LM339N, LM2901N | alta |
| **Comparador rápido LM311**<br><sub>`ic-lm311`</sub> | THT/SMD | DIP-8 (8p, 2.54 mm, filas 7.62 mm); SOIC-8 (8p, 1.27 mm, filas 5.4 mm) | LM311P, LM311N | media |
| **Arreglo de 7 transistores Darlington ULN2003A**<br><sub>`ic-uln2003a`</sub> | THT/SMD | DIP-16 (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (16p, 1.27 mm, filas 5.4 mm) | ULN2003AN (DIP-16), ULN2003 SOP-16, ULN2004A (entradas 6–15 V CMOS) | muy alta |
| **Doble puente H L293D**<br><sub>`ic-l293d`</sub> | THT | DIP-16 (16p, 2.54 mm, filas 7.62 mm) | L293D (con diodos), L293/L293B (1 A, sin diodos internos), SN754410 (1 A, mismo pinout) | muy alta |
| **Arreglo de 8 transistores Darlington ULN2803A**<br><sub>`ic-uln2803a`</sub> | THT/SMD | DIP-18 (18p, 2.54 mm, filas 7.62 mm); SOIC-18 ancho (300 mil) (18p, 1.27 mm, filas 9.4 mm) | ULN2803APG (DIP-18), ULN2803 SOIC-18 | alta |
| **Controlador de displays/matriz de LEDs MAX7219**<br><sub>`ic-max7219`</sub> | THT/SMD | DIP-24 angosto (300 mil) (24p, 2.54 mm, filas 7.62 mm); SOIC-24 ancho (300 mil) (24p, 1.27 mm, filas 9.4 mm) | MAX7219CNG (DIP-24), MAX7219CWG (SOIC-24) | alta |
| **Doble puente H de 2 A L298N**<br><sub>`ic-l298n`</sub> | THT | Multiwatt-15 V (15p, 1.27 mm) | L298N (Multiwatt-15 V), L298HN (horizontal) | alta |
| **Driver de medio puente alto/bajo IR2110**<br><sub>`ic-ir2110`</sub> | THT/SMD | DIP-14 (14p, 2.54 mm, filas 7.62 mm); SOIC-16 ancho (300 mil) (16p, 1.27 mm, filas 9.4 mm) | IR2110PBF (500 V), IR2113PBF (600 V, mismo pinout) | alta |
| **Drivers de motor a pasos A4988 / DRV8825**<br><sub>`ic-a4988-drv8825`</sub> | SMD | Módulo StepStick/Pololu (2 filas x 8 pines) (16p, 2.54 mm, filas 12.7 mm); QFN-28 5x5 mm (chip A4988 ET) (28p, 0.5 mm); HTSSOP-28 PowerPAD (chip DRV8825 PWP) (28p, 0.65 mm) | Módulo A4988 (8–35 V, 1/16 paso), Módulo DRV8825 (8.2–45 V, 1/32 paso) | alta |
| **Doble puente H MOSFET TB6612FNG (chip)**<br><sub>`ic-tb6612fng`</sub> | SMD | SSOP-24 (24p, 0.65 mm) | TB6612FNG (chip SSOP-24), Módulo TB6612FNG | media |
| **Driver alto/bajo independiente IR2101**<br><sub>`ic-ir2101`</sub> | THT/SMD | DIP-8 (8p, 2.54 mm, filas 7.62 mm); SOIC-8 (8p, 1.27 mm, filas 5.4 mm) | IR2101PBF | media |
| **Driver autooscilante de medio puente IR2153**<br><sub>`ic-ir2153`</sub> | THT/SMD | DIP-8 (8p, 2.54 mm, filas 7.62 mm); SOIC-8 (8p, 1.27 mm, filas 5.4 mm) | IR2153PBF, IR2153D (con diodo bootstrap interno) | media |
| **Driver de medio puente con tiempo muerto IR2104**<br><sub>`ic-ir2104`</sub> | THT/SMD | DIP-8 (8p, 2.54 mm, filas 7.62 mm); SOIC-8 (8p, 1.27 mm, filas 5.4 mm) | IR2104PBF, IR2104SPBF | media |
| **Driver de MOSFET 6 A TC4420 / TC4429**<br><sub>`ic-tc4420`</sub> | THT/SMD | DIP-8 (8p, 2.54 mm, filas 7.62 mm); SOIC-8 (8p, 1.27 mm, filas 5.4 mm) | TC4420CPA (no inversor), TC4429CPA (inversor) | media |
| **Driver doble de MOSFET 1.5 A TC4426 / TC4427 / TC4428**<br><sub>`ic-tc4427`</sub> | THT/SMD | DIP-8 (8p, 2.54 mm, filas 7.62 mm); SOIC-8 (8p, 1.27 mm, filas 5.4 mm) | TC4426 (inversor), TC4427 (no inversor), TC4428 (mixto) | media |
| **Registro de desplazamiento de potencia TPIC6B595**<br><sub>`ic-tpic6b595`</sub> | THT/SMD | DIP-20 (20p, 2.54 mm, filas 7.62 mm); SOIC-20 ancho (300 mil) (20p, 1.27 mm, filas 9.4 mm) | TPIC6B595N (DIP-20), TPIC6B595DW (SOIC-20) | media |
| **Controladores de barra de LEDs LM3914 / LM3915 / LM3916**<br><sub>`ic-lm3914`</sub> | THT | DIP-18 (18p, 2.54 mm, filas 7.62 mm) | LM3914N-1 (lineal), LM3915N (logarítmico), LM3916 (VU) | alta |
| **Convertidor A/D de 3½ dígitos ICL7107 / ICL7106**<br><sub>`ic-icl7107`</sub> | THT | DIP-40 ancho (600 mil) (40p, 2.54 mm, filas 15.24 mm) | ICL7107CPL (LED), ICL7106CPL (LCD), TC7107 / TC7106 | alta |
| **Convertidor A/D de 8 bits ADC0804**<br><sub>`ic-adc0804`</sub> | THT | DIP-20 (20p, 2.54 mm, filas 7.62 mm) | ADC0804LCN | alta |
| **Amplificador de transconductancia doble LM13700**<br><sub>`ic-lm13700`</sub> | THT/SMD | DIP-16 (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (16p, 1.27 mm, filas 5.4 mm) | LM13700N, NJM13700D | media |
| **Codificador remoto HT12E**<br><sub>`ic-ht12e`</sub> | THT/SMD | DIP-18 (18p, 2.54 mm, filas 7.62 mm); SOP-20 (300 mil) (20p, 1.27 mm, filas 9.4 mm) | HT12E (DIP-18) | media |
| **Codificador remoto PT2262**<br><sub>`ic-pt2262`</sub> | THT/SMD | DIP-18 (18p, 2.54 mm, filas 7.62 mm) | PT2262 (DIP-18) | media |
| **Convertidor A/D de 8 bits y 8 canales ADC0808 / ADC0809**<br><sub>`ic-adc0808`</sub> | THT | DIP-28 ancho (600 mil) (28p, 2.54 mm, filas 15.24 mm) | ADC0808CCN, ADC0809CCN | media |
| **Convertidor A/D SPI de 10 bits y 8 canales MCP3008**<br><sub>`ic-mcp3008`</sub> | THT/SMD | DIP-16 (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (16p, 1.27 mm, filas 5.4 mm) | MCP3008-I/P (DIP-16), MCP3208 (12 bits, mismo pinout) | media |
| **Convertidor D/A de 8 bits DAC0808**<br><sub>`ic-dac0808`</sub> | THT | DIP-16 (16p, 2.54 mm, filas 7.62 mm) | DAC0808LCN, MC1408P8 | media |
| **Convertidor voltaje-frecuencia LM331**<br><sub>`ic-lm331`</sub> | THT/SMD | DIP-8 (8p, 2.54 mm, filas 7.62 mm); SOIC-8 (8p, 1.27 mm, filas 5.4 mm) | LM331N, LM331AN | media |
| **Decodificador de tonos LM567 / NE567**<br><sub>`ic-lm567`</sub> | THT/SMD | DIP-8 (8p, 2.54 mm, filas 7.62 mm); SOIC-8 (8p, 1.27 mm, filas 5.4 mm) | LM567CN, NE567N | media |
| **Decodificador remoto HT12D**<br><sub>`ic-ht12d`</sub> | THT/SMD | DIP-18 (18p, 2.54 mm, filas 7.62 mm) | HT12D (DIP-18) | media |
| **Decodificador remoto PT2272**<br><sub>`ic-pt2272`</sub> | THT/SMD | DIP-18 (18p, 2.54 mm, filas 7.62 mm) | PT2272-M4 (momentáneo, 4 datos), PT2272-L4 (retención, 4 datos), PT2272-T4 (biestable) | media |
| **Generador de funciones ICL8038**<br><sub>`ic-icl8038`</sub> | THT | DIP-14 (14p, 2.54 mm, filas 7.62 mm) | ICL8038CCPD, 8038C (Steren) | media |
| **Generador de funciones XR2206**<br><sub>`ic-xr2206`</sub> | THT | DIP-16 (16p, 2.54 mm, filas 7.62 mm) | XR2206CP | media |
| **Grabador/reproductor de voz ISD1820**<br><sub>`ic-isd1820`</sub> | modulo | Módulo ISD1820 (chip COB en placa) (2.54 mm) | Módulo ISD1820 con micrófono y bocina | media |
| **Cargador lineal de baterías Li-ion TP4056 (chip)**<br><sub>`ic-tp4056`</sub> | SMD | ESOP-8 / SOP-8 con pad térmico (8p, 1.27 mm, filas 5.4 mm) | TP4056 (chip ESOP-8), Módulo TP4056 con protección DW01A + FS8205A | alta |
| **Protector de batería Li-ion DW01A**<br><sub>`ic-dw01a`</sub> | SMD | SOT-23-6 (6p, 0.95 mm) | DW01A (SOT-23-6) | media |
| **Convertidor de niveles RS-232 MAX232 / MAX3232**<br><sub>`ic-max232`</sub> | THT/SMD | DIP-16 (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (16p, 1.27 mm, filas 5.4 mm) | MAX232 (5 V, capacitores 1 µF), MAX232A (0.1 µF), MAX3232 (3–5.5 V, 0.1 µF) | alta |
| **Convertidor USB a serie CH340G**<br><sub>`ic-ch340g`</sub> | SMD | SOIC-16 (16p, 1.27 mm, filas 5.4 mm) | CH340G (cristal externo), CH340C (sin cristal) | alta |
| **Convertidor USB a UART FT232RL**<br><sub>`ic-ft232rl`</sub> | SMD | SSOP-28 (28p, 0.65 mm) | FT232RL (SSOP-28), Módulos FTDI USB-TTL | alta |
| **Expansor de E/S I2C de 8 bits PCF8574**<br><sub>`ic-pcf8574`</sub> | THT/SMD | DIP-16 (16p, 2.54 mm, filas 7.62 mm); SOIC-16 ancho (300 mil) (16p, 1.27 mm, filas 9.4 mm) | PCF8574P (DIP-16), PCF8574T (SO-16), PCF8574A (direcciones 0x38–0x3F) | alta |
| **Transceptor RS-485 MAX485**<br><sub>`ic-max485`</sub> | THT/SMD | DIP-8 (8p, 2.54 mm, filas 7.62 mm); SOIC-8 (8p, 1.27 mm, filas 5.4 mm) | MAX485CPA (DIP-8), MAX485ESA (SOIC-8), MAX3485 (3.3 V), SN75176 (mismo pinout) | alta |
| **Controlador CAN con interfaz SPI MCP2515**<br><sub>`ic-mcp2515`</sub> | THT/SMD | DIP-18 (18p, 2.54 mm, filas 7.62 mm); SOIC-18 ancho (300 mil) (18p, 1.27 mm, filas 9.4 mm) | MCP2515-I/P (DIP-18), MCP2515-I/SO (SOIC-18) | media |
| **Controlador Ethernet SPI ENC28J60**<br><sub>`ic-enc28j60`</sub> | THT/SMD | DIP-28 angosto (300 mil) (28p, 2.54 mm, filas 7.62 mm); SOIC-28 ancho (300 mil) (28p, 1.27 mm, filas 9.4 mm) | ENC28J60-I/SP (DIP-28), Módulo ENC28J60 con RJ45 (HR911105A) | media |
| **Convertidor USB a UART CP2102**<br><sub>`ic-cp2102`</sub> | SMD | QFN-28 5x5 mm (28p, 0.5 mm) | CP2102 (QFN-28), CP2102N (QFN-24/28, pinout distinto) | media |
| **Expansor de E/S I2C de 16 bits MCP23017**<br><sub>`ic-mcp23017`</sub> | THT/SMD | DIP-28 angosto (300 mil) (28p, 2.54 mm, filas 7.62 mm); SOIC-28 ancho (300 mil) (28p, 1.27 mm, filas 9.4 mm) | MCP23017-E/SP (DIP-28), MCP23S17 (SPI) | media |
| **Transceptor CAN TJA1050 / MCP2551**<br><sub>`ic-tja1050`</sub> | THT/SMD | SOIC-8 (8p, 1.27 mm, filas 5.4 mm); DIP-8 (8p, 2.54 mm, filas 7.62 mm) | TJA1050T (SO-8), MCP2551-I/P (DIP-8) | media |
| **Contador de décadas Johnson con 10 salidas decodificadas CD4017**<br><sub>`ic-cd4017`</sub> | THT/SMD | DIP-16 (PDIP, 300 mil) (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (150 mil) (16p, 1.27 mm) | CD4017BE (DIP, TI), HEF4017BP (DIP, NXP/Nexperia), MC14017B (onsemi), CD4017BM (SOIC), 74HC4017 (2–6 V, mismo pinout) | muy alta |
| **Cuádruple compuerta AND de 2 entradas CD4081**<br><sub>`ic-cd4081`</sub> | THT/SMD | DIP-14 (PDIP, 300 mil) (14p, 2.54 mm, filas 7.62 mm); SOIC-14 (150 mil) (14p, 1.27 mm) | CD4081BE (DIP, TI), HEF4081BP (DIP, NXP/Nexperia), MC14081B (onsemi), CD4081BM (SOIC) | muy alta |
| **Cuádruple compuerta NAND de 2 entradas CD4011**<br><sub>`ic-cd4011`</sub> | THT/SMD | DIP-14 (PDIP, 300 mil) (14p, 2.54 mm, filas 7.62 mm); SOIC-14 (150 mil) (14p, 1.27 mm) | CD4011BE (DIP, TI), HEF4011BP (DIP, NXP/Nexperia), MC14011B (onsemi), CD4011BM (SOIC) | muy alta |
| **Cuádruple compuerta NAND Schmitt trigger de 2 entradas CD4093**<br><sub>`ic-cd4093`</sub> | THT/SMD | DIP-14 (PDIP, 300 mil) (14p, 2.54 mm, filas 7.62 mm); SOIC-14 (150 mil) (14p, 1.27 mm) | CD4093BE (DIP, TI), HEF4093BP (DIP, NXP/Nexperia), MC14093B (onsemi), CD4093BM (SOIC) | muy alta |
| **Cuádruple compuerta NOR de 2 entradas CD4001**<br><sub>`ic-cd4001`</sub> | THT/SMD | DIP-14 (PDIP, 300 mil) (14p, 2.54 mm, filas 7.62 mm); SOIC-14 (150 mil) (14p, 1.27 mm) | CD4001BE (DIP, TI), HEF4001BP (DIP, NXP/Nexperia), MC14001B (onsemi), CD4001BM (SOIC) | muy alta |
| **Decodificador/latch/driver BCD a 7 segmentos CD4511**<br><sub>`ic-cd4511`</sub> | THT/SMD | DIP-16 (PDIP, 300 mil) (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (150 mil) (16p, 1.27 mm) | CD4511BE (DIP, TI), HEF4511BP (DIP, NXP/Nexperia), MC14511B (onsemi), CD4511BM (SOIC), 74HC4511 (2–6 V, ≈10 mA por segmento) | muy alta |
| **Doble flip-flop tipo D con set y reset CD4013**<br><sub>`ic-cd4013`</sub> | THT/SMD | DIP-14 (PDIP, 300 mil) (14p, 2.54 mm, filas 7.62 mm); SOIC-14 (150 mil) (14p, 1.27 mm) | CD4013BE (DIP, TI), HEF4013BP (DIP, NXP/Nexperia), MC14013B (onsemi), CD4013BM (SOIC) | muy alta |
| **Séxtuple inversor CMOS CD4069**<br><sub>`ic-cd4069`</sub> | THT/SMD | DIP-14 (PDIP, 300 mil) (14p, 2.54 mm, filas 7.62 mm); SOIC-14 (150 mil) (14p, 1.27 mm) | CD4069BE (DIP, TI), HEF4069BP (DIP, NXP/Nexperia), MC14069B (onsemi), CD4069BM (SOIC), CD4069UBE (sin buffer, versión común) | muy alta |
| **Contador binario de 14 etapas con oscilador CD4060**<br><sub>`ic-cd4060`</sub> | THT/SMD | DIP-16 (PDIP, 300 mil) (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (150 mil) (16p, 1.27 mm) | CD4060BE (DIP, TI), HEF4060BP (DIP, NXP/Nexperia), MC14060B (onsemi), CD4060BM (SOIC), 74HC4060 | alta |
| **Contador binario de rizo de 12 etapas CD4040**<br><sub>`ic-cd4040`</sub> | THT/SMD | DIP-16 (PDIP, 300 mil) (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (150 mil) (16p, 1.27 mm) | CD4040BE (DIP, TI), HEF4040BP (DIP, NXP/Nexperia), MC14040B (onsemi), CD4040BM (SOIC), 74HC4040 | alta |
| **Contador de décadas con decodificador a 7 segmentos CD4026**<br><sub>`ic-cd4026`</sub> | THT/SMD | DIP-16 (PDIP, 300 mil) (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (150 mil) (16p, 1.27 mm) | CD4026BE (DIP, TI), HEF4026BP (DIP, NXP/Nexperia), MC14026B (onsemi), CD4026BM (SOIC) | alta |
| **Cuádruple compuerta OR de 2 entradas CD4071**<br><sub>`ic-cd4071`</sub> | THT/SMD | DIP-14 (PDIP, 300 mil) (14p, 2.54 mm, filas 7.62 mm); SOIC-14 (150 mil) (14p, 1.27 mm) | CD4071BE (DIP, TI), HEF4071BP (DIP, NXP/Nexperia), MC14071B (onsemi), CD4071BM (SOIC) | alta |
| **Cuádruple compuerta XOR de 2 entradas CD4070**<br><sub>`ic-cd4070`</sub> | THT/SMD | DIP-14 (PDIP, 300 mil) (14p, 2.54 mm, filas 7.62 mm); SOIC-14 (150 mil) (14p, 1.27 mm) | CD4070BE (DIP, TI), HEF4070BP (DIP, NXP/Nexperia), MC14070B (onsemi), CD4070BM (SOIC) | alta |
| **Cuádruple interruptor bilateral analógico CD4066**<br><sub>`ic-cd4066`</sub> | THT/SMD | DIP-14 (PDIP, 300 mil) (14p, 2.54 mm, filas 7.62 mm); SOIC-14 (150 mil) (14p, 1.27 mm) | CD4066BE (DIP, TI), HEF4066BP (DIP, NXP/Nexperia), MC14066B (onsemi), CD4066BM (SOIC), 74HC4066 (mismo pinout), CD4016BE | alta |
| **Doble contador BCD síncrono ascendente CD4518**<br><sub>`ic-cd4518`</sub> | THT/SMD | DIP-16 (PDIP, 300 mil) (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (150 mil) (16p, 1.27 mm) | CD4518BE (DIP, TI), HEF4518BP (DIP, NXP/Nexperia), MC14518B (onsemi), CD4518BM (SOIC), 74HC4518 | alta |
| **Doble flip-flop JK con set y reset CD4027**<br><sub>`ic-cd4027`</sub> | THT/SMD | DIP-16 (PDIP, 300 mil) (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (150 mil) (16p, 1.27 mm) | CD4027BE (DIP, TI), HEF4027BP (DIP, NXP/Nexperia), MC14027B (onsemi), CD4027BM (SOIC) | alta |
| **Multiplexor/demultiplexor analógico de 16 canales CD4067 / 74HC4067**<br><sub>`ic-cd4067`</sub> | THT/SMD | DIP-24 (PDIP, 600 mil) (24p, 2.54 mm, filas 15.24 mm); SOIC-24 ancho (300 mil) (24p, 1.27 mm) | CD4067BE, 74HC4067 (mismo pinout), CD74HC4067M (SOIC-24) | alta |
| **Multiplexor/demultiplexor analógico de 8 canales CD4051 / 74HC4051**<br><sub>`ic-cd4051`</sub> | THT/SMD | DIP-16 (PDIP, 300 mil) (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (150 mil) (16p, 1.27 mm) | CD4051BE (DIP, TI), HEF4051BP (DIP, NXP/Nexperia), MC14051B (onsemi), CD4051BM (SOIC), 74HC4051 (mismo pinout, 2–6 V), 74HCT4051 | alta |
| **Multiplexor/demultiplexor analógico doble de 4 canales CD4052 / 74HC4052**<br><sub>`ic-cd4052`</sub> | THT/SMD | DIP-16 (PDIP, 300 mil) (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (150 mil) (16p, 1.27 mm) | CD4052BE (DIP, TI), HEF4052BP (DIP, NXP/Nexperia), MC14052B (onsemi), CD4052BM (SOIC), 74HC4052 | alta |
| **Multivibrador astable/monoestable de bajo consumo CD4047**<br><sub>`ic-cd4047`</sub> | THT/SMD | DIP-14 (PDIP, 300 mil) (14p, 2.54 mm, filas 7.62 mm); SOIC-14 (150 mil) (14p, 1.27 mm) | CD4047BE (DIP, TI), HEF4047BP (DIP, NXP/Nexperia), MC14047B (onsemi), CD4047BM (SOIC) | alta |
| **Séxtuple buffer no inversor CMOS (convertidor de nivel) CD4050**<br><sub>`ic-cd4050`</sub> | THT/SMD | DIP-16 (PDIP, 300 mil) (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (150 mil) (16p, 1.27 mm) | CD4050BE (DIP, TI), HEF4050BP (DIP, NXP/Nexperia), MC14050B (onsemi), CD4050BM (SOIC) | alta |
| **Séxtuple inversor buffer CMOS (convertidor de nivel) CD4049**<br><sub>`ic-cd4049`</sub> | THT/SMD | DIP-16 (PDIP, 300 mil) (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (150 mil) (16p, 1.27 mm) | CD4049BE (DIP, TI), HEF4049BP (DIP, NXP/Nexperia), MC14049B (onsemi), CD4049BM (SOIC), CD4049UBE (sin buffer) | alta |
| **Séxtuple inversor Schmitt trigger CMOS CD40106**<br><sub>`ic-cd40106`</sub> | THT/SMD | DIP-14 (PDIP, 300 mil) (14p, 2.54 mm, filas 7.62 mm); SOIC-14 (150 mil) (14p, 1.27 mm) | CD40106BE, HEF40106BP, MC14106B, CD4584BE (equivalente) | alta |
| **Triple conmutador analógico de 2 canales CD4053 / 74HC4053**<br><sub>`ic-cd4053`</sub> | THT/SMD | DIP-16 (PDIP, 300 mil) (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (150 mil) (16p, 1.27 mm) | CD4053BE (DIP, TI), HEF4053BP (DIP, NXP/Nexperia), MC14053B (onsemi), CD4053BM (SOIC), 74HC4053 | alta |
| **Compuerta NAND/AND de 8 entradas CD4068**<br><sub>`ic-cd4068`</sub> | THT/SMD | DIP-14 (PDIP, 300 mil) (14p, 2.54 mm, filas 7.62 mm); SOIC-14 (150 mil) (14p, 1.27 mm) | CD4068BE (DIP, TI), HEF4068BP (DIP, NXP/Nexperia), MC14068B (onsemi), CD4068BM (SOIC) | media |
| **Contador ascendente/descendente BCD con preset CD4510**<br><sub>`ic-cd4510`</sub> | THT/SMD | DIP-16 (PDIP, 300 mil) (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (150 mil) (16p, 1.27 mm) | CD4510BE (DIP, TI), HEF4510BP (DIP, NXP/Nexperia), MC14510B (onsemi), CD4510BM (SOIC) | media |
| **Contador ascendente/descendente binario con preset CD4516**<br><sub>`ic-cd4516`</sub> | THT/SMD | DIP-16 (PDIP, 300 mil) (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (150 mil) (16p, 1.27 mm) | CD4516BE (DIP, TI), HEF4516BP (DIP, NXP/Nexperia), MC14516B (onsemi), CD4516BM (SOIC) | media |
| **Contador ascendente/descendente binario o BCD con preset CD4029**<br><sub>`ic-cd4029`</sub> | THT/SMD | DIP-16 (PDIP, 300 mil) (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (150 mil) (16p, 1.27 mm) | CD4029BE (DIP, TI), HEF4029BP (DIP, NXP/Nexperia), MC14029B (onsemi), CD4029BM (SOIC) | media |
| **Contador BCD de 3 dígitos multiplexado CD4553**<br><sub>`ic-cd4553`</sub> | THT/SMD | DIP-16 (PDIP, 300 mil) (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (150 mil) (16p, 1.27 mm) | CD4553BE (DIP, TI), HEF4553BP (DIP, NXP/Nexperia), MC14553B (onsemi), CD4553BM (SOIC) | media |
| **Contador binario de rizo de 14 etapas CD4020**<br><sub>`ic-cd4020`</sub> | THT/SMD | DIP-16 (PDIP, 300 mil) (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (150 mil) (16p, 1.27 mm) | CD4020BE (DIP, TI), HEF4020BP (DIP, NXP/Nexperia), MC14020B (onsemi), CD4020BM (SOIC), 74HC4020 | media |
| **Contador binario de rizo de 7 etapas CD4024**<br><sub>`ic-cd4024`</sub> | THT/SMD | DIP-14 (PDIP, 300 mil) (14p, 2.54 mm, filas 7.62 mm); SOIC-14 (150 mil) (14p, 1.27 mm) | CD4024BE (DIP, TI), HEF4024BP (DIP, NXP/Nexperia), MC14024B (onsemi), CD4024BM (SOIC) | media |
| **Contador de décadas con decodificador a 7 segmentos y supresión de ceros CD4033**<br><sub>`ic-cd4033`</sub> | THT/SMD | DIP-16 (PDIP, 300 mil) (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (150 mil) (16p, 1.27 mm) | CD4033BE (DIP, TI), HEF4033BP (DIP, NXP/Nexperia), MC14033B (onsemi), CD4033BM (SOIC) | media |
| **Contador octal Johnson con 8 salidas decodificadas CD4022**<br><sub>`ic-cd4022`</sub> | THT/SMD | DIP-16 (PDIP, 300 mil) (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (150 mil) (16p, 1.27 mm) | CD4022BE (DIP, TI), HEF4022BP (DIP, NXP/Nexperia), MC14022B (onsemi), CD4022BM (SOIC) | media |
| **Cuádruple compuerta XNOR de 2 entradas CD4077**<br><sub>`ic-cd4077`</sub> | THT/SMD | DIP-14 (PDIP, 300 mil) (14p, 2.54 mm, filas 7.62 mm); SOIC-14 (150 mil) (14p, 1.27 mm) | CD4077BE (DIP, TI), HEF4077BP (DIP, NXP/Nexperia), MC14077B (onsemi), CD4077BM (SOIC) | media |
| **Cuádruple compuerta XOR de 2 entradas CD4030**<br><sub>`ic-cd4030`</sub> | THT/SMD | DIP-14 (PDIP, 300 mil) (14p, 2.54 mm, filas 7.62 mm); SOIC-14 (150 mil) (14p, 1.27 mm) | CD4030BE (DIP, TI), HEF4030BP (DIP, NXP/Nexperia), MC14030B (onsemi), CD4030BM (SOIC) | media |
| **Cuádruple latch R-S con NAND y salidas de 3 estados CD4044**<br><sub>`ic-cd4044`</sub> | THT/SMD | DIP-16 (PDIP, 300 mil) (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (150 mil) (16p, 1.27 mm) | CD4044BE (DIP, TI), HEF4044BP (DIP, NXP/Nexperia), MC14044B (onsemi), CD4044BM (SOIC) | media |
| **Cuádruple latch R-S con NOR y salidas de 3 estados CD4043**<br><sub>`ic-cd4043`</sub> | THT/SMD | DIP-16 (PDIP, 300 mil) (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (150 mil) (16p, 1.27 mm) | CD4043BE (DIP, TI), HEF4043BP (DIP, NXP/Nexperia), MC14043B (onsemi), CD4043BM (SOIC) | media |
| **Decodificador BCD a decimal (1 de 10) CD4028**<br><sub>`ic-cd4028`</sub> | THT/SMD | DIP-16 (PDIP, 300 mil) (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (150 mil) (16p, 1.27 mm) | CD4028BE (DIP, TI), HEF4028BP (DIP, NXP/Nexperia), MC14028B (onsemi), CD4028BM (SOIC) | media |
| **Decodificador/demultiplexor 4 a 16 con latch (salidas en alto) CD4514**<br><sub>`ic-cd4514`</sub> | THT/SMD | DIP-24 (PDIP, 600 mil) (24p, 2.54 mm, filas 15.24 mm); SOIC-24 ancho (300 mil) (24p, 1.27 mm) | CD4514BE (DIP, TI), HEF4514BP (DIP, NXP/Nexperia), MC14514B (onsemi), CD4514BM (SOIC), CD4515 (salidas activas en bajo, mismo pinout) | media |
| **Decodificador/latch/driver BCD a 7 segmentos para LCD CD4543**<br><sub>`ic-cd4543`</sub> | THT/SMD | DIP-16 (PDIP, 300 mil) (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (150 mil) (16p, 1.27 mm) | CD4543BE (DIP, TI), HEF4543BP (DIP, NXP/Nexperia), MC14543B (onsemi), CD4543BM (SOIC) | media |
| **Doble compuerta NAND de 4 entradas CD4012**<br><sub>`ic-cd4012`</sub> | THT/SMD | DIP-14 (PDIP, 300 mil) (14p, 2.54 mm, filas 7.62 mm); SOIC-14 (150 mil) (14p, 1.27 mm) | CD4012BE (DIP, TI), HEF4012BP (DIP, NXP/Nexperia), MC14012B (onsemi), CD4012BM (SOIC) | media |
| **Doble compuerta OR de 4 entradas CD4072**<br><sub>`ic-cd4072`</sub> | THT/SMD | DIP-14 (PDIP, 300 mil) (14p, 2.54 mm, filas 7.62 mm); SOIC-14 (150 mil) (14p, 1.27 mm) | CD4072BE (DIP, TI), HEF4072BP (DIP, NXP/Nexperia), MC14072B (onsemi), CD4072BM (SOIC) | media |
| **Doble contador binario síncrono ascendente de 4 bits CD4520**<br><sub>`ic-cd4520`</sub> | THT/SMD | DIP-16 (PDIP, 300 mil) (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (150 mil) (16p, 1.27 mm) | CD4520BE (DIP, TI), HEF4520BP (DIP, NXP/Nexperia), MC14520B (onsemi), CD4520BM (SOIC), 74HC4520 | media |
| **Doble multivibrador monoestable CD4098**<br><sub>`ic-cd4098`</sub> | THT/SMD | DIP-16 (PDIP, 300 mil) (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (150 mil) (16p, 1.27 mm) | CD4098BE (DIP, TI), HEF4098BP (DIP, NXP/Nexperia), MC14098B (onsemi), CD4098BM (SOIC) | media |
| **Doble multivibrador monoestable de precisión CD4538**<br><sub>`ic-cd4538`</sub> | THT/SMD | DIP-16 (PDIP, 300 mil) (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (150 mil) (16p, 1.27 mm) | CD4538BE (DIP, TI), HEF4538BP (DIP, NXP/Nexperia), MC14538B (onsemi), CD4538BM (SOIC), 74HC4538 | media |
| **Lazo de seguimiento de fase (PLL) con VCO CD4046**<br><sub>`ic-cd4046`</sub> | THT/SMD | DIP-16 (PDIP, 300 mil) (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (150 mil) (16p, 1.27 mm) | CD4046BE (DIP, TI), HEF4046BP (DIP, NXP/Nexperia), MC14046B (onsemi), CD4046BM (SOIC), 74HC4046 (pin 15 = PC3 OUT, sin zener) | media |
| **Registro de desplazamiento de 8 bits con latch y 3 estados CD4094**<br><sub>`ic-cd4094`</sub> | THT/SMD | DIP-16 (PDIP, 300 mil) (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (150 mil) (16p, 1.27 mm) | CD4094BE (DIP, TI), HEF4094BP (DIP, NXP/Nexperia), MC14094B (onsemi), CD4094BM (SOIC), 74HC4094 | media |
| **Registro de desplazamiento de 8 etapas entrada paralelo/serie CD4021**<br><sub>`ic-cd4021`</sub> | THT/SMD | DIP-16 (PDIP, 300 mil) (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (150 mil) (16p, 1.27 mm) | CD4021BE (DIP, TI), HEF4021BP (DIP, NXP/Nexperia), MC14021B (onsemi), CD4021BM (SOIC) | media |
| **Sumador completo de 4 bits CMOS CD4008**<br><sub>`ic-cd4008`</sub> | THT/SMD | DIP-16 (PDIP, 300 mil) (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (150 mil) (16p, 1.27 mm) | CD4008BE (DIP, TI), HEF4008BP (DIP, NXP/Nexperia), MC14008B (onsemi), CD4008BM (SOIC) | media |
| **Temporizador programable con oscilador CD4541**<br><sub>`ic-cd4541`</sub> | THT/SMD | DIP-14 (PDIP, 300 mil) (14p, 2.54 mm, filas 7.62 mm); SOIC-14 (150 mil) (14p, 1.27 mm) | CD4541BE (DIP, TI), HEF4541BP (DIP, NXP/Nexperia), MC14541B (onsemi), CD4541BM (SOIC) | media |
| **Triple compuerta AND de 3 entradas CD4073**<br><sub>`ic-cd4073`</sub> | THT/SMD | DIP-14 (PDIP, 300 mil) (14p, 2.54 mm, filas 7.62 mm); SOIC-14 (150 mil) (14p, 1.27 mm) | CD4073BE (DIP, TI), HEF4073BP (DIP, NXP/Nexperia), MC14073B (onsemi), CD4073BM (SOIC) | media |
| **Triple compuerta NAND de 3 entradas CD4023**<br><sub>`ic-cd4023`</sub> | THT/SMD | DIP-14 (PDIP, 300 mil) (14p, 2.54 mm, filas 7.62 mm); SOIC-14 (150 mil) (14p, 1.27 mm) | CD4023BE (DIP, TI), HEF4023BP (DIP, NXP/Nexperia), MC14023B (onsemi), CD4023BM (SOIC) | media |
| **Triple compuerta NOR de 3 entradas CD4025**<br><sub>`ic-cd4025`</sub> | THT/SMD | DIP-14 (PDIP, 300 mil) (14p, 2.54 mm, filas 7.62 mm); SOIC-14 (150 mil) (14p, 1.27 mm) | CD4025BE (DIP, TI), HEF4025BP (DIP, NXP/Nexperia), MC14025B (onsemi), CD4025BM (SOIC) | media |
| **Triple compuerta OR de 3 entradas CD4075**<br><sub>`ic-cd4075`</sub> | THT/SMD | DIP-14 (PDIP, 300 mil) (14p, 2.54 mm, filas 7.62 mm); SOIC-14 (150 mil) (14p, 1.27 mm) | CD4075BE (DIP, TI), HEF4075BP (DIP, NXP/Nexperia), MC14075B (onsemi), CD4075BM (SOIC) | media |
| **Contador de décadas asíncrono (÷2 y ÷5) 7490**<br><sub>`ic-74xx90`</sub> | THT/SMD | DIP-14 (PDIP, 300 mil) (14p, 2.54 mm, filas 7.62 mm); SOIC-14 (150 mil) (14p, 1.27 mm) | 74LS90, SN74LS90N, 74HC390 (alternativa CMOS doble) | muy alta |
| **Cuádruple compuerta AND de 2 entradas 7408**<br><sub>`ic-74xx08`</sub> | THT/SMD | DIP-14 (PDIP, 300 mil) (14p, 2.54 mm, filas 7.62 mm); SOIC-14 (150 mil) (14p, 1.27 mm) | 74LS08, 74HC08, 74HCT08, SN74LS08N (DIP), SN74HC08N (DIP), 74HC08D (SOIC) | muy alta |
| **Cuádruple compuerta NAND de 2 entradas 7400**<br><sub>`ic-74xx00`</sub> | THT/SMD | DIP-14 (PDIP, 300 mil) (14p, 2.54 mm, filas 7.62 mm); SOIC-14 (150 mil) (14p, 1.27 mm) | 74LS00, 74HC00, 74HCT00, SN74LS00N (DIP), SN74HC00N (DIP), 74HC00D (SOIC) | muy alta |
| **Cuádruple compuerta NOR de 2 entradas 7402**<br><sub>`ic-74xx02`</sub> | THT/SMD | DIP-14 (PDIP, 300 mil) (14p, 2.54 mm, filas 7.62 mm); SOIC-14 (150 mil) (14p, 1.27 mm) | 74LS02, 74HC02, 74HCT02, SN74LS02N (DIP), SN74HC02N (DIP), 74HC02D (SOIC) | muy alta |
| **Cuádruple compuerta OR de 2 entradas 7432**<br><sub>`ic-74xx32`</sub> | THT/SMD | DIP-14 (PDIP, 300 mil) (14p, 2.54 mm, filas 7.62 mm); SOIC-14 (150 mil) (14p, 1.27 mm) | 74LS32, 74HC32, 74HCT32, SN74LS32N (DIP), SN74HC32N (DIP), 74HC32D (SOIC) | muy alta |
| **Cuádruple compuerta XOR (OR exclusiva) de 2 entradas 7486**<br><sub>`ic-74xx86`</sub> | THT/SMD | DIP-14 (PDIP, 300 mil) (14p, 2.54 mm, filas 7.62 mm); SOIC-14 (150 mil) (14p, 1.27 mm) | 74LS86, 74HC86, 74HCT86, SN74LS86N (DIP), SN74HC86N (DIP), 74HC86D (SOIC) | muy alta |
| **Decodificador BCD a 7 segmentos (cátodo común) 7448**<br><sub>`ic-74xx48`</sub> | THT/SMD | DIP-16 (PDIP, 300 mil) (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (150 mil) (16p, 1.27 mm) | 74LS48, SN74LS48N | muy alta |
| **Decodificador/driver BCD a 7 segmentos (ánodo común) 7447**<br><sub>`ic-74xx47`</sub> | THT/SMD | DIP-16 (PDIP, 300 mil) (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (150 mil) (16p, 1.27 mm) | 74LS47 (el más común), SN7447AN (TTL estándar, salida 30 V) | muy alta |
| **Doble flip-flop D con preset y clear 7474**<br><sub>`ic-74xx74`</sub> | THT/SMD | DIP-14 (PDIP, 300 mil) (14p, 2.54 mm, filas 7.62 mm); SOIC-14 (150 mil) (14p, 1.27 mm) | 74LS74, 74HC74, 74HCT74, SN74LS74N (DIP), SN74HC74N (DIP), 74HC74D (SOIC) | muy alta |
| **Registro de desplazamiento de 8 bits con latch de salida 74HC595**<br><sub>`ic-74xx595`</sub> | THT/SMD | DIP-16 (PDIP, 300 mil) (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (150 mil) (16p, 1.27 mm); TSSOP-16 (16p, 0.65 mm) | 74HC595N (DIP-16), 74HC595D (SOIC-16), 74HCT595, TPIC6B595 (versión de potencia, otro encapsulado/pinout) | muy alta |
| **Séxtuple inversor (compuerta NOT) 7404**<br><sub>`ic-74xx04`</sub> | THT/SMD | DIP-14 (PDIP, 300 mil) (14p, 2.54 mm, filas 7.62 mm); SOIC-14 (150 mil) (14p, 1.27 mm) | 74LS04, 74HC04, 74HCT04, SN74LS04N (DIP), SN74HC04N (DIP), 74HC04D (SOIC), 74HCU04 (sin buffer, para osciladores) | muy alta |
| **Séxtuple inversor Schmitt trigger 7414 / 74HC14**<br><sub>`ic-74xx14`</sub> | THT/SMD | DIP-14 (PDIP, 300 mil) (14p, 2.54 mm, filas 7.62 mm); SOIC-14 (150 mil) (14p, 1.27 mm) | 74LS14, 74HC14, 74HCT14, SN74LS14N (DIP), SN74HC14N (DIP), 74HC14D (SOIC) | muy alta |
| **Buffer/driver octal no inversor de 3 estados 74244**<br><sub>`ic-74xx244`</sub> | THT/SMD | DIP-20 (PDIP, 300 mil) (20p, 2.54 mm, filas 7.62 mm); SOIC-20 ancho (300 mil) (20p, 1.27 mm) | 74LS244, 74HC244, 74HCT244, SN74LS244N (DIP), SN74HC244N (DIP), 74HC244D (SOIC) | alta |
| **Comparador de magnitud de 4 bits 7485**<br><sub>`ic-74xx85`</sub> | THT/SMD | DIP-16 (PDIP, 300 mil) (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (150 mil) (16p, 1.27 mm) | 74LS85, 74HC85, SN74LS85N (DIP), SN74HC85N (DIP), 74HC85D (SOIC) | alta |
| **Contador binario de 4 bits asíncrono (÷2 y ÷8) 7493**<br><sub>`ic-74xx93`</sub> | THT/SMD | DIP-14 (PDIP, 300 mil) (14p, 2.54 mm, filas 7.62 mm); SOIC-14 (150 mil) (14p, 1.27 mm) | 74LS93, 74HC393 (alternativa CMOS doble) | alta |
| **Contador binario síncrono de 4 bits con carga (clear asíncrono) 74161**<br><sub>`ic-74xx161`</sub> | THT/SMD | DIP-16 (PDIP, 300 mil) (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (150 mil) (16p, 1.27 mm) | 74LS161, 74HC161, 74HCT161, SN74LS161N (DIP), SN74HC161N (DIP), 74HC161D (SOIC) | alta |
| **Contador síncrono ascendente/descendente BCD con dos relojes 74192**<br><sub>`ic-74xx192`</sub> | THT/SMD | DIP-16 (PDIP, 300 mil) (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (150 mil) (16p, 1.27 mm) | 74LS192, 74HC192, SN74LS192N (DIP), SN74HC192N (DIP), 74HC192D (SOIC) | alta |
| **Contador síncrono ascendente/descendente binario de 4 bits con dos relojes 74193**<br><sub>`ic-74xx193`</sub> | THT/SMD | DIP-16 (PDIP, 300 mil) (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (150 mil) (16p, 1.27 mm) | 74LS193, 74HC193, SN74LS193N (DIP), SN74HC193N (DIP), 74HC193D (SOIC) | alta |
| **Cuádruple buffer de 3 estados (habilitación en bajo) 74125**<br><sub>`ic-74xx125`</sub> | THT/SMD | DIP-14 (PDIP, 300 mil) (14p, 2.54 mm, filas 7.62 mm); SOIC-14 (150 mil) (14p, 1.27 mm) | 74LS125, 74HC125, 74HCT125, SN74LS125N (DIP), SN74HC125N (DIP), 74HC125D (SOIC) | alta |
| **Cuádruple compuerta NAND Schmitt trigger de 2 entradas 74132**<br><sub>`ic-74xx132`</sub> | THT/SMD | DIP-14 (PDIP, 300 mil) (14p, 2.54 mm, filas 7.62 mm); SOIC-14 (150 mil) (14p, 1.27 mm) | 74LS132, 74HC132, SN74LS132N (DIP), SN74HC132N (DIP), 74HC132D (SOIC) | alta |
| **Cuádruple multiplexor digital de 2 a 1 74157**<br><sub>`ic-74xx157`</sub> | THT/SMD | DIP-16 (PDIP, 300 mil) (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (150 mil) (16p, 1.27 mm) | 74LS157, 74HC157, 74HCT157, SN74LS157N (DIP), SN74HC157N (DIP), 74HC157D (SOIC) | alta |
| **Decodificador/demultiplexor 3 a 8 líneas 74138**<br><sub>`ic-74xx138`</sub> | THT/SMD | DIP-16 (PDIP, 300 mil) (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (150 mil) (16p, 1.27 mm) | 74LS138, 74HC138, 74HCT138, SN74LS138N (DIP), SN74HC138N (DIP), 74HC138D (SOIC) | alta |
| **Doble compuerta NAND de 4 entradas 7420**<br><sub>`ic-74xx20`</sub> | THT/SMD | DIP-14 (PDIP, 300 mil) (14p, 2.54 mm, filas 7.62 mm); SOIC-14 (150 mil) (14p, 1.27 mm) | 74LS20, 74HC20, SN74LS20N (DIP), SN74HC20N (DIP), 74HC20D (SOIC) | alta |
| **Doble decodificador 2 a 4 líneas 74139**<br><sub>`ic-74xx139`</sub> | THT/SMD | DIP-16 (PDIP, 300 mil) (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (150 mil) (16p, 1.27 mm) | 74LS139, 74HC139, SN74LS139N (DIP), SN74HC139N (DIP), 74HC139D (SOIC) | alta |
| **Doble flip-flop JK con borrado 7473**<br><sub>`ic-74xx73`</sub> | THT/SMD | DIP-14 (PDIP, 300 mil) (14p, 2.54 mm, filas 7.62 mm); SOIC-14 (150 mil) (14p, 1.27 mm) | 74LS73, SN74LS73AN, 74HC73 | alta |
| **Doble flip-flop JK con preset y clear (flanco de bajada) 74112**<br><sub>`ic-74xx112`</sub> | THT/SMD | DIP-16 (PDIP, 300 mil) (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (150 mil) (16p, 1.27 mm) | 74LS112, 74HC112, SN74LS112N (DIP), SN74HC112N (DIP), 74HC112D (SOIC) | alta |
| **Doble flip-flop JK con preset y clear 7476**<br><sub>`ic-74xx76`</sub> | THT/SMD | DIP-16 (PDIP, 300 mil) (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (150 mil) (16p, 1.27 mm) | 74LS76, SN74LS76AN | alta |
| **Doble multivibrador monoestable redisparable 74123**<br><sub>`ic-74xx123`</sub> | THT/SMD | DIP-16 (PDIP, 300 mil) (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (150 mil) (16p, 1.27 mm) | 74LS123, 74HC123, SN74LS123N (DIP), SN74HC123N (DIP), 74HC123D (SOIC) | alta |
| **Latch octal transparente tipo D de 3 estados (pinout de flujo) 74573**<br><sub>`ic-74xx573`</sub> | THT/SMD | DIP-20 (PDIP, 300 mil) (20p, 2.54 mm, filas 7.62 mm); SOIC-20 ancho (300 mil) (20p, 1.27 mm) | 74LS573, 74HC573, 74HCT573, SN74LS573N (DIP), SN74HC573N (DIP), 74HC573D (SOIC) | alta |
| **Latch octal transparente tipo D de 3 estados 74373**<br><sub>`ic-74xx373`</sub> | THT/SMD | DIP-20 (PDIP, 300 mil) (20p, 2.54 mm, filas 7.62 mm); SOIC-20 ancho (300 mil) (20p, 1.27 mm) | 74LS373, 74HC373, 74HCT373, SN74LS373N (DIP), SN74HC373N (DIP), 74HC373D (SOIC) | alta |
| **Multiplexor digital de 8 a 1 74151**<br><sub>`ic-74xx151`</sub> | THT/SMD | DIP-16 (PDIP, 300 mil) (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (150 mil) (16p, 1.27 mm) | 74LS151, 74HC151, SN74LS151N (DIP), SN74HC151N (DIP), 74HC151D (SOIC) | alta |
| **Registro de desplazamiento de 8 bits entrada paralelo / salida serie 74165**<br><sub>`ic-74xx165`</sub> | THT/SMD | DIP-16 (PDIP, 300 mil) (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (150 mil) (16p, 1.27 mm) | 74LS165, 74HC165, SN74LS165N (DIP), SN74HC165N (DIP), 74HC165D (SOIC) | alta |
| **Registro de desplazamiento de 8 bits entrada serie / salida paralelo 74164**<br><sub>`ic-74xx164`</sub> | THT/SMD | DIP-14 (PDIP, 300 mil) (14p, 2.54 mm, filas 7.62 mm); SOIC-14 (150 mil) (14p, 1.27 mm) | 74LS164, 74HC164, SN74LS164N (DIP), SN74HC164N (DIP), 74HC164D (SOIC) | alta |
| **Sumador binario completo de 4 bits con acarreo rápido 74283**<br><sub>`ic-74xx283`</sub> | THT/SMD | DIP-16 (PDIP, 300 mil) (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (150 mil) (16p, 1.27 mm) | 74LS283, 74HC283, SN74LS283N (DIP), SN74HC283N (DIP), 74HC283D (SOIC) | alta |
| **Séxtuple buffer de colector abierto alto voltaje 7407**<br><sub>`ic-74xx07`</sub> | THT/SMD | DIP-14 (PDIP, 300 mil) (14p, 2.54 mm, filas 7.62 mm); SOIC-14 (150 mil) (14p, 1.27 mm) | SN7407N, 74LS07, DM7407N | alta |
| **Séxtuple inversor de colector abierto alto voltaje 7406**<br><sub>`ic-74xx06`</sub> | THT/SMD | DIP-14 (PDIP, 300 mil) (14p, 2.54 mm, filas 7.62 mm); SOIC-14 (150 mil) (14p, 1.27 mm) | SN7406N (TTL estándar), 74LS06, DM7406N | alta |
| **Transceptor octal bidireccional de 3 estados 74245**<br><sub>`ic-74xx245`</sub> | THT/SMD | DIP-20 (PDIP, 300 mil) (20p, 2.54 mm, filas 7.62 mm); SOIC-20 ancho (300 mil) (20p, 1.27 mm) | 74LS245, 74HC245, 74HCT245, SN74LS245N (DIP), SN74HC245N (DIP), 74HC245D (SOIC) | alta |
| **Triple compuerta AND de 3 entradas 7411**<br><sub>`ic-74xx11`</sub> | THT/SMD | DIP-14 (PDIP, 300 mil) (14p, 2.54 mm, filas 7.62 mm); SOIC-14 (150 mil) (14p, 1.27 mm) | 74LS11, 74HC11, SN74LS11N (DIP), SN74HC11N (DIP), 74HC11D (SOIC) | alta |
| **Triple compuerta NAND de 3 entradas 7410**<br><sub>`ic-74xx10`</sub> | THT/SMD | DIP-14 (PDIP, 300 mil) (14p, 2.54 mm, filas 7.62 mm); SOIC-14 (150 mil) (14p, 1.27 mm) | 74LS10, 74HC10, SN74LS10N (DIP), SN74HC10N (DIP), 74HC10D (SOIC) | alta |
| **Buffer/driver octal inversor de 3 estados 74240**<br><sub>`ic-74xx240`</sub> | THT/SMD | DIP-20 (PDIP, 300 mil) (20p, 2.54 mm, filas 7.62 mm); SOIC-20 ancho (300 mil) (20p, 1.27 mm) | 74LS240, 74HC240, 74HCT240, SN74LS240N (DIP), SN74HC240N (DIP), 74HC240D (SOIC) | media |
| **Codificador de prioridad 10 a 4 líneas (decimal a BCD) 74147**<br><sub>`ic-74xx147`</sub> | THT/SMD | DIP-16 (PDIP, 300 mil) (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (150 mil) (16p, 1.27 mm) | 74LS147, 74HC147, SN74LS147N (DIP), SN74HC147N (DIP), 74HC147D (SOIC) | media |
| **Codificador de prioridad 8 a 3 líneas 74148**<br><sub>`ic-74xx148`</sub> | THT/SMD | DIP-16 (PDIP, 300 mil) (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (150 mil) (16p, 1.27 mm) | 74LS148, 74HC148, SN74LS148N (DIP), SN74HC148N (DIP), 74HC148D (SOIC) | media |
| **Compuerta NAND de 8 entradas 7430**<br><sub>`ic-74xx30`</sub> | THT/SMD | DIP-14 (PDIP, 300 mil) (14p, 2.54 mm, filas 7.62 mm); SOIC-14 (150 mil) (14p, 1.27 mm) | 74LS30, 74HC30, SN74LS30N (DIP), SN74HC30N (DIP), 74HC30D (SOIC) | media |
| **Contador binario síncrono de 4 bits con carga (clear síncrono) 74163**<br><sub>`ic-74xx163`</sub> | THT/SMD | DIP-16 (PDIP, 300 mil) (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (150 mil) (16p, 1.27 mm) | 74LS163, 74HC163, SN74LS163N (DIP), SN74HC163N (DIP), 74HC163D (SOIC) | media |
| **Contador divisor entre 12 (÷2 y ÷6) 7492**<br><sub>`ic-74xx92`</sub> | THT/SMD | DIP-14 (PDIP, 300 mil) (14p, 2.54 mm, filas 7.62 mm); SOIC-14 (150 mil) (14p, 1.27 mm) | 74LS92 | media |
| **Contador síncrono ascendente/descendente BCD (década) 74190**<br><sub>`ic-74xx190`</sub> | THT/SMD | DIP-16 (PDIP, 300 mil) (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (150 mil) (16p, 1.27 mm) | 74LS190, 74HC190, SN74LS190N (DIP), SN74HC190N (DIP), 74HC190D (SOIC) | media |
| **Contador síncrono ascendente/descendente binario de 4 bits 74191**<br><sub>`ic-74xx191`</sub> | THT/SMD | DIP-16 (PDIP, 300 mil) (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (150 mil) (16p, 1.27 mm) | 74LS191, 74HC191, SN74LS191N (DIP), SN74HC191N (DIP), 74HC191D (SOIC) | media |
| **Cuádruple buffer de 3 estados (habilitación en alto) 74126**<br><sub>`ic-74xx126`</sub> | THT/SMD | DIP-14 (PDIP, 300 mil) (14p, 2.54 mm, filas 7.62 mm); SOIC-14 (150 mil) (14p, 1.27 mm) | 74LS126, 74HC126, SN74LS126N (DIP), SN74HC126N (DIP), 74HC126D (SOIC) | media |
| **Cuádruple compuerta XNOR de 2 entradas 74266 / 74HC7266**<br><sub>`ic-74xx266`</sub> | THT/SMD | DIP-14 (PDIP, 300 mil) (14p, 2.54 mm, filas 7.62 mm); SOIC-14 (150 mil) (14p, 1.27 mm) | 74LS266 (colector abierto), 74HC7266 (totem-pole), CD4077 (equivalente CMOS 4000) | media |
| **Cuádruple flip-flop D con clear (salidas Q y /Q) 74175**<br><sub>`ic-74xx175`</sub> | THT/SMD | DIP-16 (PDIP, 300 mil) (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (150 mil) (16p, 1.27 mm) | 74LS175, 74HC175, SN74LS175N (DIP), SN74HC175N (DIP), 74HC175D (SOIC) | media |
| **Cuádruple latch biestable tipo D 7475**<br><sub>`ic-74xx75`</sub> | THT/SMD | DIP-16 (PDIP, 300 mil) (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (150 mil) (16p, 1.27 mm) | 74LS75, SN74LS75N, 74HC75 | media |
| **Decodificador BCD a decimal (1 de 10) 7442**<br><sub>`ic-74xx42`</sub> | THT/SMD | DIP-16 (PDIP, 300 mil) (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (150 mil) (16p, 1.27 mm) | 74LS42, 74HC42, SN74LS42N (DIP), SN74HC42N (DIP), 74HC42D (SOIC) | media |
| **Decodificador/demultiplexor 4 a 16 líneas 74154**<br><sub>`ic-74xx154`</sub> | THT/SMD | DIP-24 (PDIP, 600 mil) (24p, 2.54 mm, filas 15.24 mm); SOIC-24 ancho (300 mil) (24p, 1.27 mm) | 74LS154, 74HC154, SN74LS154N (DIP), SN74HC154N (DIP), 74HC154D (SOIC) | media |
| **Doble compuerta AND de 4 entradas 7421**<br><sub>`ic-74xx21`</sub> | THT/SMD | DIP-14 (PDIP, 300 mil) (14p, 2.54 mm, filas 7.62 mm); SOIC-14 (150 mil) (14p, 1.27 mm) | 74LS21, 74HC21, SN74LS21N (DIP), SN74HC21N (DIP), 74HC21D (SOIC) | media |
| **Doble contador binario de 4 bits asíncrono 74393**<br><sub>`ic-74xx393`</sub> | THT/SMD | DIP-14 (PDIP, 300 mil) (14p, 2.54 mm, filas 7.62 mm); SOIC-14 (150 mil) (14p, 1.27 mm) | 74LS393, 74HC393, SN74LS393N (DIP), SN74HC393N (DIP), 74HC393D (SOIC) | media |
| **Doble contador de décadas asíncrono 74390**<br><sub>`ic-74xx390`</sub> | THT/SMD | DIP-16 (PDIP, 300 mil) (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (150 mil) (16p, 1.27 mm) | 74LS390, 74HC390, SN74LS390N (DIP), SN74HC390N (DIP), 74HC390D (SOIC) | media |
| **Doble flip-flop JK con clear 74107**<br><sub>`ic-74xx107`</sub> | THT/SMD | DIP-14 (PDIP, 300 mil) (14p, 2.54 mm, filas 7.62 mm); SOIC-14 (150 mil) (14p, 1.27 mm) | 74LS107, 74HC107 | media |
| **Doble multiplexor digital de 4 a 1 74153**<br><sub>`ic-74xx153`</sub> | THT/SMD | DIP-16 (PDIP, 300 mil) (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (150 mil) (16p, 1.27 mm) | 74LS153, 74HC153, SN74LS153N (DIP), SN74HC153N (DIP), 74HC153D (SOIC) | media |
| **Flip-flop D octal con clear 74273**<br><sub>`ic-74xx273`</sub> | THT/SMD | DIP-20 (PDIP, 300 mil) (20p, 2.54 mm, filas 7.62 mm); SOIC-20 ancho (300 mil) (20p, 1.27 mm) | 74LS273, 74HC273, SN74LS273N (DIP), SN74HC273N (DIP), 74HC273D (SOIC) | media |
| **Flip-flop D octal de 3 estados (pinout de flujo) 74574**<br><sub>`ic-74xx574`</sub> | THT/SMD | DIP-20 (PDIP, 300 mil) (20p, 2.54 mm, filas 7.62 mm); SOIC-20 ancho (300 mil) (20p, 1.27 mm) | 74LS574, 74HC574, 74HCT574, SN74LS574N (DIP), SN74HC574N (DIP), 74HC574D (SOIC) | media |
| **Flip-flop D octal de 3 estados 74374**<br><sub>`ic-74xx374`</sub> | THT/SMD | DIP-20 (PDIP, 300 mil) (20p, 2.54 mm, filas 7.62 mm); SOIC-20 ancho (300 mil) (20p, 1.27 mm) | 74LS374, 74HC374, 74HCT374, SN74LS374N (DIP), SN74HC374N (DIP), 74HC374D (SOIC) | media |
| **Multivibrador monoestable 74121**<br><sub>`ic-74xx121`</sub> | THT/SMD | DIP-14 (PDIP, 300 mil) (14p, 2.54 mm, filas 7.62 mm); SOIC-14 (150 mil) (14p, 1.27 mm) | SN74121N (TTL estándar), 74LS121 (raro) | media |
| **Registro D de 4 bits con salidas de 3 estados 74173**<br><sub>`ic-74xx173`</sub> | THT/SMD | DIP-16 (PDIP, 300 mil) (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (150 mil) (16p, 1.27 mm) | 74LS173, 74HC173, SN74LS173N (DIP), SN74HC173N (DIP), 74HC173D (SOIC) | media |
| **Registro de desplazamiento de 8 bits PISO síncrono con clear 74166**<br><sub>`ic-74xx166`</sub> | THT/SMD | DIP-16 (PDIP, 300 mil) (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (150 mil) (16p, 1.27 mm) | 74LS166, 74HC166, SN74LS166N (DIP), SN74HC166N (DIP), 74HC166D (SOIC) | media |
| **Registro de desplazamiento universal bidireccional de 4 bits 74194**<br><sub>`ic-74xx194`</sub> | THT/SMD | DIP-16 (PDIP, 300 mil) (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (150 mil) (16p, 1.27 mm) | 74LS194, 74HC194, SN74LS194N (DIP), SN74HC194N (DIP), 74HC194D (SOIC) | media |
| **Sumador binario completo de 4 bits 7483**<br><sub>`ic-74xx83`</sub> | THT/SMD | DIP-16 (PDIP, 300 mil) (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (150 mil) (16p, 1.27 mm) | 74LS83A | media |
| **Séxtuple flip-flop D con clear 74174**<br><sub>`ic-74xx174`</sub> | THT/SMD | DIP-16 (PDIP, 300 mil) (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (150 mil) (16p, 1.27 mm) | 74LS174, 74HC174, SN74LS174N (DIP), SN74HC174N (DIP), 74HC174D (SOIC) | media |
| **Triple compuerta NOR de 3 entradas 7427**<br><sub>`ic-74xx27`</sub> | THT/SMD | DIP-14 (PDIP, 300 mil) (14p, 2.54 mm, filas 7.62 mm); SOIC-14 (150 mil) (14p, 1.27 mm) | 74LS27, 74HC27, SN74LS27N (DIP), SN74HC27N (DIP), 74HC27D (SOIC) | media |
| **Unidad aritmético-lógica (ALU) de 4 bits 74181**<br><sub>`ic-74xx181`</sub> | THT/SMD | DIP-24 (PDIP, 600 mil) (24p, 2.54 mm, filas 15.24 mm) | 74LS181 | media |
| **Memorias EEPROM I2C 24Cxx / 24LCxxx**<br><sub>`ic-24cxx`</sub> | THT/SMD | DIP-8 (8p, 2.54 mm, filas 7.62 mm); SOIC-8 (8p, 1.27 mm, filas 5.4 mm) | 24C02 (256 B), 24C04, 24C08, 24C16 (2 KB), 24C32 (4 KB), 24C64, 24LC256 (32 KB), 24LC512 (64 KB) | alta |
| **EEPROM paralela AT28C256 (32K x 8)**<br><sub>`ic-at28c256`</sub> | THT | DIP-28 ancho (600 mil) (28p, 2.54 mm, filas 15.24 mm) | AT28C256 (32 KB), AT28C64 (8 KB) | media |
| **EPROM borrable por UV 27C256**<br><sub>`ic-27c256`</sub> | THT | DIP-28 ancho (600 mil) (28p, 2.54 mm, filas 15.24 mm) | 27C256 (32 KB), 27C512 (64 KB: pin 1 = A15, pin 22 = /OE/VPP), 27C64 (8 KB) | media |
| **Memoria EEPROM Microwire 93C46**<br><sub>`ic-93c46`</sub> | THT/SMD | DIP-8 (8p, 2.54 mm, filas 7.62 mm); SOIC-8 (8p, 1.27 mm, filas 5.4 mm) | 93C46 (1 Kbit), 93C56 (2 Kbit), 93C66 (4 Kbit), 93C86 (16 Kbit) | media |
| **Memoria flash SPI W25Qxx / EEPROM SPI 25LCxxx**<br><sub>`ic-w25q32`</sub> | THT/SMD | SOIC-8 (150 mil, sufijo SN) (8p, 1.27 mm, filas 5.4 mm); SOIC-8 ancho (208 mil, sufijo SS) (8p, 1.27 mm); DIP-8 (8p, 2.54 mm, filas 7.62 mm) | W25Q16 (2 MB), W25Q32 (4 MB), W25Q64 (8 MB), W25Q128 (16 MB), 25LC256 (EEPROM 32 KB) | media |
| **Microcontrolador AVR ATmega328P-PU (28 pines, el del Arduino UNO)**<br><sub>`ic-atmega328p`</sub> | THT/SMD | DIP-28 (PDIP, 300 mil) (28p, 2.54 mm, filas 7.62 mm); TQFP-32 (32p, 0.8 mm); QFN/MLF-32 (32p, 0.5 mm) | ATmega328P-PU (DIP-28) sin bootloader, ATmega328P-PU con bootloader Arduino precargado, ATmega328P-AU (TQFP-32), ATmega168A/88PA (pin-compatibles, menos memoria) | muy alta |
| **Microcontrolador AVR ATtiny85-20PU (8 pines)**<br><sub>`ic-attiny85`</sub> | THT/SMD | DIP-8 (PDIP, 300 mil) (8p, 2.54 mm, filas 7.62 mm); SOIC-8 ancho (208 mil, -SU) (8p, 1.27 mm); QFN/MLF-20 (20p, 0.5 mm) | ATtiny85-20PU (DIP-8), ATtiny85-20SU (SOIC-8 ancho), ATtiny85V-10PU | muy alta |
| **Microcontrolador AVR ATmega32A-PU (40 pines)**<br><sub>`ic-atmega32a`</sub> | THT/SMD | DIP-40 (PDIP, 600 mil) (40p, 2.54 mm, filas 15.24 mm); TQFP-44 (44p, 0.8 mm); QFN/MLF-44 (44p, 0.5 mm) | ATmega32A-PU (DIP-40) | alta |
| **Microcontrolador AVR ATmega8A-PU (28 pines)**<br><sub>`ic-atmega8a`</sub> | THT/SMD | DIP-28 (PDIP, 300 mil) (28p, 2.54 mm, filas 7.62 mm); TQFP-32 (32p, 0.8 mm) | ATmega8A-PU (DIP-28), ATmega8-16PU | alta |
| **Microcontrolador AVR ATtiny13A-PU (8 pines)**<br><sub>`ic-attiny13a`</sub> | THT/SMD | DIP-8 (PDIP, 300 mil) (8p, 2.54 mm, filas 7.62 mm); SOIC-8 (150 mil) (8p, 1.27 mm) | ATtiny13A-PU (DIP-8), ATtiny13A-SSU (SOIC-8 150 mil) | alta |
| **Microcontrolador AVR ATmega16A-PU (40 pines)**<br><sub>`ic-atmega16a`</sub> | THT/SMD | DIP-40 (PDIP, 600 mil) (40p, 2.54 mm, filas 15.24 mm); TQFP-44 (44p, 0.8 mm); QFN/MLF-44 (44p, 0.5 mm) | ATmega16A-PU (DIP-40) | media |
| **Microcontrolador AVR ATmega2560 (TQFP-100, el del Arduino Mega) — solo referencia**<br><sub>`ic-atmega2560`</sub> | SMD | TQFP-100 (100p, 0.5 mm) | ATmega2560-16AU, ATmega1280-16AU (128 KB, mismo pinout) | media |
| **Microcontrolador AVR ATtiny2313A-PU (20 pines)**<br><sub>`ic-attiny2313`</sub> | THT/SMD | DIP-20 (PDIP, 300 mil) (20p, 2.54 mm, filas 7.62 mm); SOIC-20 ancho (300 mil) (20p, 1.27 mm) | ATtiny2313A-PU (DIP-20), ATtiny4313 (4 KB) | media |
| **Microcontrolador AVR ATtiny44A-PU (14 pines)**<br><sub>`ic-attiny44`</sub> | THT/SMD | DIP-14 (PDIP, 300 mil) (14p, 2.54 mm, filas 7.62 mm); SOIC-14 (150 mil) (14p, 1.27 mm) | ATtiny44A-PU (DIP-14), ATtiny24A (2 KB) | media |
| **Microcontrolador AVR ATtiny45-20PU (8 pines)**<br><sub>`ic-attiny45`</sub> | THT/SMD | DIP-8 (PDIP, 300 mil) (8p, 2.54 mm, filas 7.62 mm); SOIC-8 ancho (208 mil, -SU) (8p, 1.27 mm); QFN/MLF-20 (20p, 0.5 mm) | ATtiny45-20PU (DIP-8), ATtiny25-20PU (2 KB) | media |
| **Microcontrolador AVR ATtiny84A-PU (14 pines)**<br><sub>`ic-attiny84`</sub> | THT/SMD | DIP-14 (PDIP, 300 mil) (14p, 2.54 mm, filas 7.62 mm); SOIC-14 (150 mil) (14p, 1.27 mm) | ATtiny84A-PU (DIP-14) | media |
| **Microcontrolador 8051 AT89S52 (40 pines)**<br><sub>`ic-at89s52`</sub> | THT/SMD | DIP-40 (PDIP, 600 mil) (40p, 2.54 mm, filas 15.24 mm); PLCC-44 (44p, 1.27 mm); TQFP-44 (44p, 0.8 mm) | AT89S52-24PU (DIP-40), STC89C52RC (clon chino pin-compatible, se programa por UART), AT89C52 (obsoleto) | alta |
| **Microcontrolador 8051 AT89C2051 (20 pines)**<br><sub>`ic-at89c2051`</sub> | THT/SMD | DIP-20 (PDIP, 300 mil) (20p, 2.54 mm, filas 7.62 mm); SOIC-20 ancho (300 mil) (20p, 1.27 mm) | AT89C2051-24PU (DIP-20), AT89C4051 (4 KB) | media |
| **Microcontrolador 8051 AT89C51 / AT89S51 (40 pines)**<br><sub>`ic-at89c51`</sub> | THT/SMD | DIP-40 (PDIP, 600 mil) (40p, 2.54 mm, filas 15.24 mm); PLCC-44 (44p, 1.27 mm); TQFP-44 (44p, 0.8 mm) | AT89S51-24PU (reemplazo actual), AT89C51-24PC/PI (existencias viejas) | media |
| **Microcontrolador ARM Cortex-M3 STM32F103C8T6 (LQFP-48) — referencia**<br><sub>`ic-stm32f103c8t6`</sub> | SMD | LQFP-48 (48p, 0.5 mm) | STM32F103C8T6 (64 KB declarados), STM32F103CBT6 (128 KB), Clones CKS32/CS32/APM32/GD32F103C8T6 | media |
| **Microcontrolador RISC-V CH32V003 (WCH) — referencia**<br><sub>`ic-ch32v003`</sub> | SMD | TSSOP-20 (20p, 0.65 mm); SOP-8 (8p, 1.27 mm); SOP-16 (16p, 1.27 mm); QFN-20 (20p, 0.4 mm) | CH32V003F4P6 (TSSOP-20, el más común), CH32V003J4M6 (SOP-8) | media |
| **Microcontrolador RP2040 (Raspberry Pi, QFN-56) — referencia**<br><sub>`ic-rp2040`</sub> | SMD | QFN-56 (56p, 0.4 mm) | RP2040 (chip suelto, raro en México), RP2350A/B (sucesor, QFN-60/80) | media |
| **Microcontrolador PIC16F628A (18 pines)**<br><sub>`ic-pic16f628a`</sub> | THT/SMD | DIP-18 (PDIP, 300 mil) (18p, 2.54 mm, filas 7.62 mm); SOIC-18 ancho (300 mil) (18p, 1.27 mm) | PIC16F628A-I/P (DIP-18), PIC16F627A (1K palabras), PIC16F628A-I/SO (SOIC-18) | muy alta |
| **Microcontrolador PIC16F877A (40 pines)**<br><sub>`ic-pic16f877a`</sub> | THT/SMD | DIP-40 (PDIP, 600 mil) (40p, 2.54 mm, filas 15.24 mm); TQFP-44 (44p, 0.8 mm); PLCC-44 / QFN-44 (44p) | PIC16F877A-I/P (DIP-40), PIC16F877A-I/PT (TQFP-44), PIC16F874A (4K palabras) | muy alta |
| **Microcontrolador PIC18F4550 (40 pines, USB)**<br><sub>`ic-pic18f4550`</sub> | THT/SMD | DIP-40 (PDIP, 600 mil) (40p, 2.54 mm, filas 15.24 mm); TQFP-44 (44p, 0.8 mm); PLCC-44 / QFN-44 (44p) | PIC18F4550-I/P (DIP-40), PIC18F4455 (24 KB), PIC18F45K50 (sucesor) | muy alta |
| **Microcontrolador PIC12F675 (8 pines, con ADC)**<br><sub>`ic-pic12f675`</sub> | THT/SMD | DIP-8 (PDIP, 300 mil) (8p, 2.54 mm, filas 7.62 mm); SOIC-8 (150 mil) (8p, 1.27 mm) | PIC12F675-I/P (DIP-8), PIC12F675-I/SN (SOIC-8) | alta |
| **Microcontrolador PIC16F84A (18 pines, clásico)**<br><sub>`ic-pic16f84a`</sub> | THT/SMD | DIP-18 (PDIP, 300 mil) (18p, 2.54 mm, filas 7.62 mm); SOIC-18 ancho (300 mil) (18p, 1.27 mm) | PIC16F84A-04/P (4 MHz), PIC16F84A-20/P (20 MHz), PIC16F84A-20I/SO (SOIC-18) | alta |
| **Microcontrolador PIC16F876A (28 pines)**<br><sub>`ic-pic16f876a`</sub> | THT/SMD | DIP-28 (PDIP, 300 mil) (28p, 2.54 mm, filas 7.62 mm); SOIC-28 ancho (300 mil) (28p, 1.27 mm) | PIC16F876A-I/SP (DIP-28 angosto) | alta |
| **Microcontrolador PIC16F88 (18 pines, ADC, I2C/SPI, UART)**<br><sub>`ic-pic16f88`</sub> | THT/SMD | DIP-18 (PDIP, 300 mil) (18p, 2.54 mm, filas 7.62 mm); SOIC-18 ancho (300 mil) (18p, 1.27 mm) | PIC16F88-I/P (DIP-18), PIC16F87 | alta |
| **Microcontrolador PIC16F887 (40 pines, oscilador interno)**<br><sub>`ic-pic16f887`</sub> | THT/SMD | DIP-40 (PDIP, 600 mil) (40p, 2.54 mm, filas 15.24 mm); TQFP-44 (44p, 0.8 mm); PLCC-44 / QFN-44 (44p) | PIC16F887-I/P (DIP-40), PIC16F884 (4K palabras) | alta |
| **Microcontrolador PIC18F2550 (28 pines, USB)**<br><sub>`ic-pic18f2550`</sub> | THT/SMD | DIP-28 (PDIP, 300 mil) (28p, 2.54 mm, filas 7.62 mm); SOIC-28 ancho (300 mil) (28p, 1.27 mm) | PIC18F2550-I/SP (DIP-28 angosto), PIC18F2455 | alta |
| **Microcontrolador PIC12F629 (8 pines, sin ADC)**<br><sub>`ic-pic12f629`</sub> | THT/SMD | DIP-8 (PDIP, 300 mil) (8p, 2.54 mm, filas 7.62 mm); SOIC-8 (150 mil) (8p, 1.27 mm) | PIC12F629-I/P (DIP-8), PIC12F629-I/SN (SOIC-8) | media |
| **Microcontrolador PIC12F683 (8 pines, ADC y PWM)**<br><sub>`ic-pic12f683`</sub> | THT/SMD | DIP-8 (PDIP, 300 mil) (8p, 2.54 mm, filas 7.62 mm); SOIC-8 (150 mil) (8p, 1.27 mm) | PIC12F683-I/P (DIP-8) | media |
| **Microcontrolador PIC16F648A (18 pines, más memoria)**<br><sub>`ic-pic16f648a`</sub> | THT/SMD | DIP-18 (PDIP, 300 mil) (18p, 2.54 mm, filas 7.62 mm); SOIC-18 ancho (300 mil) (18p, 1.27 mm) | PIC16F648A-I/P (DIP-18) | media |
| **Microcontrolador PIC16F676 (14 pines, ADC de 8 canales)**<br><sub>`ic-pic16f676`</sub> | THT/SMD | DIP-14 (PDIP, 300 mil) (14p, 2.54 mm, filas 7.62 mm); SOIC-14 (150 mil) (14p, 1.27 mm) | PIC16F676-I/P (DIP-14) | media |
| **Microcontrolador PIC16F690 (20 pines)**<br><sub>`ic-pic16f690`</sub> | THT/SMD | DIP-20 (PDIP, 300 mil) (20p, 2.54 mm, filas 7.62 mm); SOIC-20 ancho (300 mil) (20p, 1.27 mm) | PIC16F690-I/P (DIP-20) | media |
| **Microcontrolador PIC16F873A (28 pines)**<br><sub>`ic-pic16f873a`</sub> | THT/SMD | DIP-28 (PDIP, 300 mil) (28p, 2.54 mm, filas 7.62 mm); SOIC-28 ancho (300 mil) (28p, 1.27 mm) | PIC16F873A-I/SP (DIP-28 angosto) | media |
| **Microcontrolador PIC18F4520 / PIC18F452 (40 pines)**<br><sub>`ic-pic18f4520`</sub> | THT/SMD | DIP-40 (PDIP, 600 mil) (40p, 2.54 mm, filas 15.24 mm); TQFP-44 (44p, 0.8 mm); PLCC-44 / QFN-44 (44p) | PIC18F4520-I/P (DIP-40), PIC18F452-I/P (obsoleto, aún en tiendas) | media |
| **Referencia de voltaje ajustable TL431**<br><sub>`ic-tl431`</sub> | THT/SMD | TO-92 (3p, 1.27 mm); SOT-23-3 (3p, 0.95 mm) | TL431A (TO-92), TL431 SOT-23 | alta |
| **Referencia de micropotencia LM385 (1.2 V / 2.5 V)**<br><sub>`ic-lm385`</sub> | THT/SMD | TO-92 (3p, 1.27 mm); SOIC-8 (8p, 1.27 mm, filas 5.4 mm) | LM385Z-1.2, LM385Z-2.5 | media |
| **Referencia de voltaje LM336 (2.5 V / 5 V)**<br><sub>`ic-lm336`</sub> | THT | TO-92 (3p, 1.27 mm) | LM336Z-2.5, LM336Z-5.0 | media |
| **Controlador PWM en modo corriente UC3842 / UC3843 / UC3845**<br><sub>`ic-uc3842`</sub> | THT/SMD | DIP-8 (8p, 2.54 mm, filas 7.62 mm); SOIC-8 (8p, 1.27 mm, filas 5.4 mm) | UC3842 (UVLO 16/10 V, 100 %), UC3843 (UVLO 8.4/7.6 V, 100 %), UC3844 (16/10 V, 50 %), UC3845 (8.4/7.6 V, 50 %) | alta |
| **Controlador PWM TL494**<br><sub>`ic-tl494`</sub> | THT/SMD | DIP-16 (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (16p, 1.27 mm, filas 5.4 mm) | TL494CN, KA7500B (equivalente) | alta |
| **Convertidor DC-DC MC34063 (buck/boost/inversor)**<br><sub>`ic-mc34063`</sub> | THT/SMD | DIP-8 (8p, 2.54 mm, filas 7.62 mm); SOIC-8 (8p, 1.27 mm, filas 5.4 mm) | MC34063AP (DIP-8), MC34063A SOP-8 | alta |
| **Regulador conmutado reductor LM2596 (3 A)**<br><sub>`ic-lm2596`</sub> | THT/SMD | TO-220-5 (5p, 1.7 mm); TO-263-5 (D2PAK-5) (5p, 1.7 mm) | LM2596T-ADJ (TO-220-5), LM2596S-ADJ, LM2596S-5.0, LM2596S-3.3, LM2596S-12 | alta |
| **Controlador PWM SG3525**<br><sub>`ic-sg3525`</sub> | THT/SMD | DIP-16 (16p, 2.54 mm, filas 7.62 mm); SOIC-16 (16p, 1.27 mm, filas 5.4 mm) | SG3525AN | media |
| **Convertidor elevador MT3608 (chip SOT-23-6)**<br><sub>`ic-mt3608`</sub> | SMD | SOT-23-6 (6p, 0.95 mm) | MT3608 (marcado B628) | media |
| **Convertidor elevador XL6009 (chip TO-263-5)**<br><sub>`ic-xl6009`</sub> | SMD | TO-263-5 (D2PAK-5) (5p, 1.7 mm) | XL6009E1 | media |
| **Convertidor reductor 5 A XL4015 (chip TO-263-5)**<br><sub>`ic-xl4015`</sub> | SMD | TO-263-5 (D2PAK-5) (5p, 1.7 mm) | XL4015E1 | media |
| **Inversor de voltaje por bomba de carga ICL7660**<br><sub>`ic-icl7660`</sub> | THT/SMD | DIP-8 (8p, 2.54 mm, filas 7.62 mm); SOIC-8 (8p, 1.27 mm, filas 5.4 mm) | ICL7660 (1.5–10 V), ICL7660S (hasta 12 V), MAX1044 | media |
| **Reguladores conmutados reductores LM2576 (3 A) / LM2575 (1 A)**<br><sub>`ic-lm2576-lm2575`</sub> | THT/SMD | TO-220-5 (5p, 1.7 mm); TO-263-5 (D2PAK-5) (5p, 1.7 mm) | LM2575-5.0 / -ADJ (1 A), LM2576-5.0 / -12 / -ADJ (3 A), LM2576HV (hasta 60 V) | media |
| **Regulador ajustable positivo LM317 (TO-220)**<br><sub>`ic-lm317t`</sub> | THT/SMD | TO-220-3 (3p, 2.54 mm); SOT-223 (4p, 2.3 mm, filas 6.3 mm) | LM317T (TO-220, 1.5 A), LM317 en SOT-223 / D2PAK | muy alta |
| **Regulador LDO AMS1117 / LM1117 / LD1117 (3.3 V, 5 V, ADJ)**<br><sub>`ic-ams1117`</sub> | THT/SMD | SOT-223 (4p, 2.3 mm, filas 6.3 mm); TO-252 (DPAK) (3p, 2.28 mm); TO-220-3 (3p, 2.54 mm) | AMS1117-3.3, AMS1117-5.0, AMS1117-ADJ, LM1117-3.3, LD1117V33 (TO-220), LD1117AS33 (SOT-223) | muy alta |
| **Reguladores positivos fijos 78xx (TO-220)**<br><sub>`ic-lm78xx`</sub> | THT/SMD | TO-220-3 (3p, 2.54 mm); TO-252 (DPAK) (3p, 2.28 mm) | 7805 (5 V), 7806 (6 V), 7808 (8 V), 7809 (9 V), 7812 (12 V), 7815 (15 V), 7824 (24 V) | muy alta |
| **Regulador ajustable negativo LM337 (TO-220)**<br><sub>`ic-lm337`</sub> | THT | TO-220-3 (3p, 2.54 mm) | LM337T | alta |
| **Reguladores negativos fijos 79xx (TO-220)**<br><sub>`ic-lm79xx`</sub> | THT | TO-220-3 (3p, 2.54 mm) | 7905 (−5 V), 7908 (−8 V), 7912 (−12 V), 7915 (−15 V), 7924 (−24 V) | alta |
| **Reguladores positivos fijos 78Lxx de baja corriente (TO-92)**<br><sub>`ic-78lxx`</sub> | THT/SMD | TO-92 (3p, 1.27 mm); SOT-89 (3p, 1.5 mm) | 78L05 (5 V), 78L09, 78L12, 78L15, 78L33 (3.3 V) | alta |
| **Regulador ajustable de baja corriente LM317L (TO-92)**<br><sub>`ic-lm317l`</sub> | THT/SMD | TO-92 (3p, 1.27 mm); SOIC-8 (8p, 1.27 mm, filas 5.4 mm) | LM317LZ (TO-92), LM317LCLPR, LM317LIDR (SOIC-8) | media |
| **Regulador de voltaje de precisión LM723 (DIP-14)**<br><sub>`ic-lm723`</sub> | THT/SMD | DIP-14 (14p, 2.54 mm, filas 7.62 mm); SOIC-14 (14p, 1.27 mm, filas 5.4 mm) | LM723CN, UA723CN | media |
| **Regulador LDO 1 A LM2940**<br><sub>`ic-lm2940`</sub> | THT/SMD | TO-220-3 (3p, 2.54 mm); TO-252 (DPAK) (3p, 2.28 mm) | LM2940CT-5.0, LM2940CT-12 | media |
| **Regulador LDO de bajo consumo HT7333 / HT7533**<br><sub>`ic-ht7333`</sub> | THT/SMD | TO-92 (3p, 1.27 mm); SOT-89 (3p, 1.5 mm) | HT7333 (3.3 V, entrada ≤12 V), HT7533 (3.3 V, entrada ≤24 V), HT7350 / HT7550 (5 V) | media |
| **Reguladores ajustables de alta corriente LM350 (3 A) / LM338 (5 A)**<br><sub>`ic-lm350-lm338`</sub> | THT | TO-220-3 (3p, 2.54 mm) | LM350T (3 A), LM338T (5 A) | media |
| **Reguladores negativos fijos 79Lxx de baja corriente (TO-92)**<br><sub>`ic-79lxx`</sub> | THT | TO-92 (3p, 1.27 mm) | 79L05 (−5 V), 79L12 (−12 V), 79L15 (−15 V) | media |
| **Reloj de tiempo real de precisión DS3231**<br><sub>`ic-ds3231`</sub> | SMD | SOIC-16 ancho (300 mil) (16p, 1.27 mm, filas 9.4 mm) | DS3231SN (SO-16), Módulo DS3231 con AT24C32 | alta |
| **Reloj de tiempo real DS1307**<br><sub>`ic-ds1307`</sub> | THT/SMD | DIP-8 (8p, 2.54 mm, filas 7.62 mm); SOIC-8 (8p, 1.27 mm, filas 5.4 mm) | DS1307+ (DIP-8), DS1307Z (SOIC-8), Módulo Tiny RTC con 24C32 | alta |
| **Reloj de tiempo real DS1302 (3 hilos)**<br><sub>`ic-ds1302`</sub> | THT/SMD | DIP-8 (8p, 2.54 mm, filas 7.62 mm); SOIC-8 (8p, 1.27 mm, filas 5.4 mm) | DS1302+ (DIP-8), Módulo DS1302 | media |
| **Reloj de tiempo real PCF8563**<br><sub>`ic-pcf8563`</sub> | THT/SMD | DIP-8 (8p, 2.54 mm, filas 7.62 mm); SOIC-8 (8p, 1.27 mm, filas 5.4 mm) | PCF8563P (DIP-8), PCF8563T (SO-8) | media |
| **Temporizador NE555**<br><sub>`ic-ne555`</sub> | THT/SMD | DIP-8 (8p, 2.54 mm, filas 7.62 mm); SOIC-8 (8p, 1.27 mm, filas 5.4 mm) | NE555P (TI), NE555N, NE555V (Steren), LM555CN, NE555 SMD (SOIC-8) | muy alta |
| **Temporizador doble NE556**<br><sub>`ic-ne556`</sub> | THT/SMD | DIP-14 (14p, 2.54 mm, filas 7.62 mm); SOIC-14 (14p, 1.27 mm, filas 5.4 mm) | NE556N, NE556P | alta |
| **Temporizador CMOS TLC555 / ICM7555**<br><sub>`ic-tlc555`</sub> | THT/SMD | DIP-8 (8p, 2.54 mm, filas 7.62 mm); SOIC-8 (8p, 1.27 mm, filas 5.4 mm) | TLC555CP, ICM7555IPA, LMC555CN | media |

<a id="placas_desarrollo"></a>
## Placas de desarrollo (Arduino, ESP, Raspberry Pi) y programadores

| Componente | Montaje | Encapsulado / huella | Valores o variantes comunes | Popularidad |
|---|---|---|---|---|
| **Adaptador USB a TTL serie CH340G**<br><sub>`brd-usb-serial-ch340g`</sub> | modulo | Header 1x6 (6p, 2.54 mm) | USB-A, Micro-USB, USB-C (CH340E/CH340C) | muy alta |
| **Adaptador USB a TTL serie CP2102**<br><sub>`brd-usb-serial-cp2102`</sub> | modulo | Header 1x6 (6p, 2.54 mm) | USB-A, Micro-USB | alta |
| **Adaptador USB a TTL serie FT232RL (FTDI)**<br><sub>`brd-usb-serial-ft232rl`</sub> | modulo | Header 1x6 (orden FTDI) (6p, 2.54 mm) | Mini-USB, USB-C | alta |
| **Adaptador / cable USB a TTL PL2303HX**<br><sub>`brd-usb-serial-pl2303`</sub> | modulo | Header 1x5 o cable de 4 hilos (5p, 2.54 mm) | Módulo USB-A, Cable de 4 hilos | media |
| **Arduino Mega 2560 R3 compatible (clon CH340)**<br><sub>`brd-arduino-mega-2560-clon-ch340`</sub> | modulo | Placa formato Arduino Mega (86p, 2.54 mm, filas 48.26 mm) | CH340G, Con cable USB | muy alta |
| **Arduino Nano V3 compatible (clon CH340, mini-USB)**<br><sub>`brd-arduino-nano-clon-ch340`</sub> | modulo | Nano DIP-30 (2x15) (30p, 2.54 mm, filas 15.24 mm) | Headers soldados, Headers sin soldar, Con cable mini-USB | muy alta |
| **Arduino UNO R3 compatible (clon CH340, ATmega328P DIP)**<br><sub>`brd-arduino-uno-r3-clon-ch340-dip`</sub> | modulo | Placa formato Arduino UNO R3 (32p, 2.54 mm, filas 48.26 mm) | CH340G + cristal 12 MHz, Con cable USB-B | muy alta |
| **Arduino UNO R3 compatible (clon CH340, ATmega328P SMD)**<br><sub>`brd-arduino-uno-r3-clon-ch340-smd`</sub> | modulo | Placa formato Arduino UNO R3 (32p, 2.54 mm, filas 48.26 mm) | CH340G, CH340C (sin cristal), Conector USB-B / micro-USB / USB-C | muy alta |
| **Arduino Nano compatible USB-C (CH340)**<br><sub>`brd-arduino-nano-clon-usb-c`</sub> | modulo | Nano DIP-30 (2x15) (30p, 2.54 mm, filas 15.24 mm) | CH340C, ATmega328P, ATmega328PB (variante) | alta |
| **Arduino Pro Mini 5 V / 16 MHz (compatible)**<br><sub>`brd-arduino-pro-mini-5v`</sub> | modulo | Pro Mini (2x12 + FTDI 1x6) (30p, 2.54 mm, filas 15.24 mm) | Headers sin soldar, ATmega328P-AU | alta |
| **Pro Micro ATmega32U4 (compatible SparkFun)**<br><sub>`brd-pro-micro-atmega32u4`</sub> | modulo | Pro Micro DIP-24 (2x12) (24p, 2.54 mm, filas 15.24 mm) | 5 V / 16 MHz, 3.3 V / 8 MHz, Micro-USB, USB-C | alta |
| **Arduino Pro Mini 3.3 V / 8 MHz (compatible)**<br><sub>`brd-arduino-pro-mini-3v3`</sub> | modulo | Pro Mini (2x12 + FTDI 1x6) (30p, 2.54 mm, filas 15.24 mm) | Headers sin soldar | media |
| **Arduino UNO R3 (original)**<br><sub>`brd-arduino-uno-r3`</sub> | modulo | Placa formato Arduino UNO R3 (32p, 2.54 mm, filas 48.26 mm) | Original Italia (A000066), Original SMD (A000073) | muy alta |
| **Arduino Mega 2560 R3 (original)**<br><sub>`brd-arduino-mega-2560-r3`</sub> | modulo | Placa formato Arduino Mega (86p, 2.54 mm, filas 48.26 mm) | Original (ATmega16U2) | alta |
| **Arduino Nano V3 (original, mini-USB)**<br><sub>`brd-arduino-nano-v3`</sub> | modulo | Nano DIP-30 (2x15) (30p, 2.54 mm, filas 15.24 mm) | Original (FT232RL), Con o sin headers soldados | alta |
| **Arduino Due**<br><sub>`brd-arduino-due`</sub> | modulo | Placa formato Arduino Mega (86p, 2.54 mm, filas 48.26 mm) | Original, Clon | media |
| **Arduino Leonardo**<br><sub>`brd-arduino-leonardo`</sub> | modulo | Placa formato UNO R3 (Leonardo) (32p, 2.54 mm, filas 48.26 mm) | Original, Clon (micro-USB) | media |
| **Arduino Micro**<br><sub>`brd-arduino-micro`</sub> | modulo | Micro DIP-34 (2x17) (34p, 2.54 mm, filas 15.24 mm) | Original, Clon | media |
| **Arduino Nano 33 IoT**<br><sub>`brd-arduino-nano-33-iot`</sub> | modulo | Nano DIP-30 (2x15) (30p, 2.54 mm, filas 15.24 mm) | Con headers, Sin headers | media |
| **Arduino Nano ESP32**<br><sub>`brd-arduino-nano-esp32`</sub> | modulo | Nano DIP-30 (2x15) (30p, 2.54 mm, filas 15.24 mm) | Con headers, Sin headers | media |
| **Arduino Nano Every**<br><sub>`brd-arduino-nano-every`</sub> | modulo | Nano DIP-30 (2x15) (30p, 2.54 mm, filas 15.24 mm) | Con headers, Sin headers | media |
| **Arduino UNO R4 Minima**<br><sub>`brd-arduino-uno-r4-minima`</sub> | modulo | Placa formato UNO R3 (R4 Minima) (32p, 2.54 mm, filas 48.26 mm) | R4 Minima | media |
| **Arduino UNO R4 WiFi**<br><sub>`brd-arduino-uno-r4-wifi`</sub> | modulo | Placa formato UNO R3 (R4 WiFi) (32p, 2.54 mm, filas 48.26 mm) | R4 WiFi | media |
| **Base de expansión para ESP32 DevKit 30 pines**<br><sub>`brd-base-esp32-30p`</sub> | modulo | Zócalo hembra 2x15 + tiras G-V-S (30p, 2.54 mm, filas 25.4 mm) | 30 pines, 38 pines, Con borneras de tornillo | alta |
| **Base de expansión para NodeMCU v3 (Lolin)**<br><sub>`brd-base-nodemcu-v3`</sub> | modulo | Zócalo hembra 2x15 + tiras G-V-S (30p, 2.54 mm, filas 27.94 mm) | Para v3 (Lolin), Doble zócalo v2/v3 | alta |
| **Nano I/O Shield / placa de expansión para Arduino Nano**<br><sub>`brd-shield-nano-io`</sub> | modulo | Zócalo hembra 2x15 (30p, 2.54 mm, filas 15.24 mm) | Con tiras G-V-S, Con borneras de tornillo | alta |
| **ESP32 DevKit V1 30 pines (DOIT)**<br><sub>`brd-esp32-devkit-v1-30p`</sub> | modulo | 2x15 pines (30p, 2.54 mm, filas 25.4 mm) | Micro-USB + CP2102, USB-C + CH340C, Headers soldados | muy alta |
| **ESP32 DevKitC 38 pines (ESP32-WROOM-32)**<br><sub>`brd-esp32-devkitc-38p`</sub> | modulo | 2x19 pines (38p, 2.54 mm, filas 25.4 mm) | CP2102, CH340C, Micro-USB, USB-C, WROOM-32 / WROOM-32U (antena externa) | alta |
| **ESP32-C3 SuperMini**<br><sub>`brd-esp32-c3-supermini`</sub> | modulo | 2x8 pines (16p, 2.54 mm, filas 15.24 mm) | Con headers, Sin headers | alta |
| **ESP32-CAM (AI-Thinker, cámara OV2640)**<br><sub>`brd-esp32-cam`</sub> | modulo | 2x8 pines (16p, 2.54 mm, filas 22.86 mm) | Con OV2640, Con antena IPEX, Kit con ESP32-CAM-MB | alta |
| **ESP32-S3 DevKitC-1 (N8R2 / N16R8)**<br><sub>`brd-esp32-s3-devkitc-1`</sub> | modulo | 2x22 pines (44p, 2.54 mm) | N8R2, N8R8, N16R8, Clones con CH343/CH340 | alta |
| **ESP32-C6 (DevKitC-1 / SuperMini)**<br><sub>`brd-esp32-c6-devkit`</sub> | modulo | Headers 2.54 mm (según placa) (2.54 mm) | DevKitC-1 (N8), SuperMini | media |
| **Heltec WiFi LoRa 32 V3 (ESP32-S3 + SX1262 + OLED)**<br><sub>`brd-heltec-wifi-lora-32-v3`</sub> | modulo | 2x18 pines (36p, 2.54 mm) | 863–928 MHz (usar 915 MHz en México), 433–510 MHz | media |
| **Wemos D1 R32 (ESP32 en formato UNO)**<br><sub>`brd-wemos-d1-r32`</sub> | modulo | Placa formato UNO R3 (D1 R32) (32p, 2.54 mm, filas 48.26 mm) | CH340G | media |
| **NodeMCU v2 ESP8266 (Amica, CP2102)**<br><sub>`brd-nodemcu-v2-cp2102`</sub> | modulo | 2x15 pines (30p, 2.54 mm, filas 22.86 mm) | CP2102, ESP-12E o ESP-12F | muy alta |
| **NodeMCU v3 ESP8266 (Lolin, CH340)**<br><sub>`brd-nodemcu-v3-lolin-ch340`</sub> | modulo | 2x15 pines (30p, 2.54 mm, filas 27.94 mm) | CH340G, ESP-12E/F | muy alta |
| **Wemos / LOLIN D1 mini (ESP8266)**<br><sub>`brd-wemos-d1-mini`</sub> | modulo | 2x8 pines (16p, 2.54 mm, filas 22.86 mm) | v3 (CH340G), v4 (USB-C), D1 mini Pro (16 MB, antena externa), Clones | alta |
| **Wemos D1 R2 (ESP8266 en formato UNO)**<br><sub>`brd-wemos-d1-r2`</sub> | modulo | Placa formato UNO R3 (D1 R2) (32p, 2.54 mm, filas 48.26 mm) | CH340G, Clones | media |
| **BBC micro:bit V2**<br><sub>`brd-microbit-v2`</sub> | modulo | Conector de borde (edge) 25 pistas (25p, 1.27 mm) | V2.2, Kit con portapilas | media |
| **Digispark ATtiny85 (USB)**<br><sub>`brd-digispark-attiny85`</sub> | modulo | 1x6 E/S + 1x3 alimentación (9p, 2.54 mm) | USB en PCB, Micro-USB | media |
| **Seeed Studio XIAO (ESP32-C3 / ESP32-S3 / RP2040 / SAMD21)**<br><sub>`brd-seeed-xiao`</sub> | modulo | 2x7 castellated (14p, 2.54 mm, filas 15.24 mm) | XIAO SAMD21, XIAO RP2040, XIAO ESP32C3, XIAO ESP32S3 (Sense con cámara), XIAO nRF52840, XIAO ESP32C6 | media |
| **Base programadora ESP32-CAM-MB (CH340)**<br><sub>`brd-esp32-cam-mb`</sub> | modulo | Header hembra 2x8 (16p, 2.54 mm, filas 22.86 mm) | Micro-USB, USB-C | alta |
| **Programador ST-Link V2 (clon, tipo USB)**<br><sub>`brd-prog-st-link-v2`</sub> | modulo | Header macho 2x5 (cables dupont) (10p, 2.54 mm, filas 2.54 mm) | Carcasa de aluminio, Clon con chip STM32F103/CKS32/APM32 | alta |
| **Programador USB para ESP-01 (CH340)**<br><sub>`brd-esp01-programador-usb`</sub> | modulo | Zócalo hembra 2x4 + USB-A (8p, 2.54 mm, filas 2.54 mm) | Con interruptor PROG/UART, Sin interruptor | alta |
| **Programador USBasp (AVR ISP)**<br><sub>`brd-prog-usbasp`</sub> | modulo | Conector IDC 2x5 (cable plano) (10p, 2.54 mm, filas 2.54 mm) | Con cable de 10 pines, Con adaptador 10 a 6 | alta |
| **Adaptador ESP-01 a 5 V (regulador + niveles)**<br><sub>`brd-esp01-adaptador-5v`</sub> | modulo | Zócalo 2x4 + header 1x4 (12p, 2.54 mm, filas 2.54 mm) | — | media |
| **Programador CH341A (EEPROM 24xx / Flash SPI 25xx)**<br><sub>`brd-prog-ch341a`</sub> | modulo | Zócalo ZIF 2x8 (DIP-8 24xx/25xx) (16p, 2.54 mm, filas 7.62 mm) | Con pinza SOIC-8, Con adaptador 1.8 V, Versión negra/verde | media |
| **Programador de PIC K150 / K128 (USB, ZIF 40)**<br><sub>`brd-prog-k150`</sub> | modulo | Zócalo ZIF 40 + ICSP 1x5/1x6 (40p, 2.54 mm, filas 15.24 mm) | K150 (USB, PL2303/CH340 + PIC16F628A), K128 (versión anterior) | media |
| **Programador PICkit 2 (clon)**<br><sub>`brd-prog-pickit2-clon`</sub> | modulo | Header ICSP 1x6 hembra (6p, 2.54 mm) | Solo programador, Con base de programación ZIF | media |
| **Programador PICkit 3 (clon)**<br><sub>`brd-prog-pickit3-clon`</sub> | modulo | Header ICSP 1x6 hembra (6p, 2.54 mm) | Clon, Con adaptador ZIF | media |
| **Programador universal XGecu TL866II Plus**<br><sub>`brd-prog-tl866ii-plus`</sub> | modulo | Zócalo ZIF 40 + ICSP (40p, 2.54 mm, filas 15.24 mm) | TL866II Plus, T48, Kit con adaptadores | media |
| **Programador/depurador PICkit 4 (MPLAB)**<br><sub>`brd-prog-pickit4`</sub> | modulo | Header 1x8 hembra (8p, 2.54 mm) | Original | media |
| **Raspberry Pi Pico (RP2040)**<br><sub>`brd-rpi-pico`</sub> | modulo | Pico 2x20 castellated/through-hole (40p, 2.54 mm, filas 17.78 mm) | Pico, Pico H (headers soldados y conector de depuración JST) | alta |
| **Raspberry Pi Pico W / WH (RP2040 + Wi-Fi)**<br><sub>`brd-rpi-pico-w`</sub> | modulo | Pico 2x20 castellated/through-hole (40p, 2.54 mm, filas 17.78 mm) | Pico W, Pico WH (headers soldados) | alta |
| **Raspberry Pi Pico 2 / Pico 2 W (RP2350)**<br><sub>`brd-rpi-pico-2`</sub> | modulo | Pico 2x20 castellated/through-hole (40p, 2.54 mm, filas 17.78 mm) | Pico 2, Pico 2 W (Wi-Fi/BT), Con headers (H/WH) | media |
| **Raspberry Pi 4 Model B**<br><sub>`brd-rpi-4b`</sub> | modulo | Header GPIO 2x20 (40p, 2.54 mm, filas 2.54 mm) | 2 GB, 4 GB, 8 GB, 1 GB (descontinuada en algunos mercados) | alta |
| **Raspberry Pi 5**<br><sub>`brd-rpi-5`</sub> | modulo | Header GPIO 2x20 (40p, 2.54 mm, filas 2.54 mm) | 2 GB, 4 GB, 8 GB, 16 GB | alta |
| **Raspberry Pi Zero 2 W**<br><sub>`brd-rpi-zero-2w`</sub> | modulo | Header GPIO 2x20 (sin poblar) (40p, 2.54 mm, filas 2.54 mm) | Zero 2 W, Zero 2 WH | alta |
| **Raspberry Pi 3 Model B+**<br><sub>`brd-rpi-3b-plus`</sub> | modulo | Header GPIO 2x20 (40p, 2.54 mm, filas 2.54 mm) | 1 GB | media |
| **CNC Shield V3 (GRBL, 4 drivers)**<br><sub>`brd-shield-cnc-v3`</sub> | modulo | Shield formato UNO R3 (32p, 2.54 mm, filas 48.26 mm) | Sin drivers, Kit con 4 A4988, Kit con DRV8825 | alta |
| **LCD Keypad Shield 16x2 (5 botones)**<br><sub>`brd-shield-lcd-keypad`</sub> | modulo | Shield formato UNO R3 (32p, 2.54 mm, filas 48.26 mm) | Azul/blanco | alta |
| **Motor Shield L293D (clon Adafruit v1)**<br><sub>`brd-shield-motor-l293d`</sub> | modulo | Shield formato UNO R3 (32p, 2.54 mm, filas 48.26 mm) | Clon v1 | alta |
| **Sensor Shield V5.0 para UNO**<br><sub>`brd-shield-sensor-v5`</sub> | modulo | Shield formato UNO R3 (32p, 2.54 mm, filas 48.26 mm) | V5.0 | alta |
| **Shield de prototipos (Proto Shield) para UNO**<br><sub>`brd-shield-protoshield-uno`</sub> | modulo | Shield formato UNO R3 (32p, 2.54 mm, filas 48.26 mm) | Con mini protoboard 170 puntos, Sin protoboard, Versión para Mega | alta |
| **Data Logger Shield (SD + RTC DS1307)**<br><sub>`brd-shield-data-logger`</sub> | modulo | Shield formato UNO R3 (32p, 2.54 mm, filas 48.26 mm) | DS1307 (clon Adafruit v1 / Deek-Robot), PCF8523 (Adafruit rev B) | media |
| **Ethernet Shield W5100 (con microSD)**<br><sub>`brd-shield-ethernet-w5100`</sub> | modulo | Shield formato UNO R3 (32p, 2.54 mm, filas 48.26 mm) | W5100 R3 clon, W5500 (versión moderna) | media |
| **Multi-function Shield (display 4 dígitos, botones, buzzer)**<br><sub>`brd-shield-multifuncion`</sub> | modulo | Shield formato UNO R3 (32p, 2.54 mm, filas 48.26 mm) | — | media |
| **RAMPS 1.4 (shield para Mega 2560)**<br><sub>`brd-shield-ramps-14`</sub> | modulo | Shield formato Mega (86p, 2.54 mm, filas 48.26 mm) | RAMPS 1.4, Kit con Mega + LCD 12864 + drivers | media |
| **STM32 Blue Pill (STM32F103C8T6)**<br><sub>`brd-stm32-blue-pill`</sub> | modulo | 2x20 pines + SWD 1x4 (44p, 2.54 mm, filas 15.24 mm) | STM32F103C8T6 (64 KB), Clones con CKS32/CS32F103 o STM32F103C6 | alta |
| **STM32 Black Pill (STM32F401/F411, WeAct)**<br><sub>`brd-stm32-black-pill`</sub> | modulo | 2x20 pines + SWD 1x4 (44p, 2.54 mm, filas 15.24 mm) | STM32F401CCU6 (84 MHz, 256 KB / 64 KB), STM32F411CEU6 (100 MHz, 512 KB / 128 KB), Con flash SPI opcional | media |

<a id="modulos_comunicacion"></a>
## Módulos de comunicación

| Componente | Montaje | Encapsulado / huella | Valores o variantes comunes | Popularidad |
|---|---|---|---|---|
| **Módulo Bluetooth HC-05 (maestro/esclavo)**<br><sub>`com-bt-hc05`</sub> | modulo | Header 1x6 (placa base ZS-040) (6p, 2.54 mm) | HC-05 ZS-040, HC-05 de 6 pines con botón | muy alta |
| **Módulo Bluetooth HC-06 (esclavo)**<br><sub>`com-bt-hc06`</sub> | modulo | Header 1x4 (4p, 2.54 mm) | 4 pines, 6 pines | alta |
| **Módulo Bluetooth JDY-31 (SPP, compatible HC-06)**<br><sub>`com-bt-jdy31`</sub> | modulo | Header 1x6 (6p, 2.54 mm) | — | media |
| **Módulo Bluetooth LE HM-10 (CC2541)**<br><sub>`com-ble-hm10`</sub> | modulo | Header 1x6 (6p, 2.54 mm) | HM-10 original (JNHuaMao), Clones AT-09 / MLT-BT05 | media |
| **Módulo Ethernet ENC28J60**<br><sub>`com-eth-enc28j60`</sub> | modulo | Header 2x5 (10p, 2.54 mm, filas 2.54 mm) | Versión azul 2x5, Versión mini para Nano | media |
| **Módulo Ethernet W5500**<br><sub>`com-eth-w5500`</sub> | modulo | Header 2x5 (10p, 2.54 mm, filas 2.54 mm) | Mini W5500, W5500 Lite (USR-ES1) | media |
| **Módulo GPS u-blox NEO-6M (GY-GPS6MV2)**<br><sub>`com-gps-neo6m`</sub> | modulo | Header 1x4 (4p, 2.54 mm) | Con antena cerámica, Con antena activa | alta |
| **Módulo GNSS u-blox NEO-M8N**<br><sub>`com-gps-neo-m8n`</sub> | modulo | Header 1x4 o conector GH 6 pines (4p, 2.54 mm) | Breakout, Domo para dron con brújula | media |
| **Módulo GSM/GPRS SIM800L**<br><sub>`com-gsm-sim800l`</sub> | modulo | 2 headers 1x6 en lados opuestos (12p, 2.54 mm) | SIM800L (rojo, 3.7–4.2 V), SIM800L EVB V2 (azul, 5 V con niveles) | alta |
| **Módulo 4G LTE Cat-1 SIMCom A7670 (A7670SA/E)**<br><sub>`com-4g-a7670`</sub> | modulo | Breakout con header (según fabricante) (2.54 mm) | A7670SA (Latinoamérica), A7670E (Europa/Asia), Con GNSS | media |
| **Shield GSM/GPRS SIM900 para Arduino**<br><sub>`com-gsm-sim900-shield`</sub> | modulo | Shield formato UNO R3 (32p, 2.54 mm, filas 48.26 mm) | — | media |
| **Transceptor infrarrojo IR por UART (YS-IRTM) y kit emisor/receptor IR**<br><sub>`com-ir-ys-irtm`</sub> | modulo | YS-IRTM header 1x5 / KY 1x3 (5p, 2.54 mm) | YS-IRTM, KY-022 receptor, KY-005 emisor, Control remoto de 21 teclas | media |
| **Módulo LoRa 915 MHz RFM95W / Ra-01H (SX1276)**<br><sub>`com-lora-rfm95w-915`</sub> | modulo | SMD 16 pads (16p, 2.0 mm) | RFM95W 915 MHz, Ra-01H, Breakout con SMA | media |
| **Módulo LoRa Ra-02 (SX1278, 433 MHz)**<br><sub>`com-lora-ra02-sx1278`</sub> | modulo | SMD medio-barreno 16 pads (16p, 2.0 mm) | Ra-02 (433 MHz), Ra-01 (antena resorte) | media |
| **Módulo LoRa UART EBYTE E32 (433/915 MHz)**<br><sub>`com-lora-e32`</sub> | modulo | Header 1x7 + SMA (7p, 2.54 mm) | E32-433T20D, E32-915T20D, E220 (LLCC68, nueva generación) | media |
| **Transceptor 2.4 GHz nRF24L01+ (antena PCB)**<br><sub>`com-nrf24l01`</sub> | modulo | Header 2x4 (8p, 2.54 mm, filas 2.54 mm) | Antena PCB, Versión SMD mini | muy alta |
| **Adaptador de 5 V a 3.3 V para nRF24L01**<br><sub>`com-nrf24l01-adaptador`</sub> | modulo | Zócalo 2x4 + header 1x8 (16p, 2.54 mm, filas 2.54 mm) | — | alta |
| **Transceptor nRF24L01+PA+LNA (antena SMA)**<br><sub>`com-nrf24l01-pa-lna`</sub> | modulo | Header 2x4 (8p, 2.54 mm, filas 2.54 mm) | Con antena 2 dBi, Con blindaje metálico | alta |
| **Receptor RF 433 MHz XY-MK-5V**<br><sub>`com-rf433-xy-mk-5v-rx`</sub> | modulo | Header 1x4 (4p, 2.54 mm) | 433 MHz, 315 MHz | muy alta |
| **Transmisor RF 433 MHz FS1000A**<br><sub>`com-rf433-fs1000a-tx`</sub> | modulo | Header 1x3 (3p, 2.54 mm) | 433 MHz, 315 MHz | muy alta |
| **Kit transmisor/receptor RF 315 MHz**<br><sub>`com-rf315-kit`</sub> | modulo | TX 1x3 / RX 1x4 (7p, 2.54 mm) | 315 MHz | media |
| **Receptor superheterodino 433 MHz RXB6**<br><sub>`com-rf433-rxb6`</sub> | modulo | Header 1x8 (8p, 2.54 mm) | 433 MHz, 315 MHz | media |
| **Transceptor serie HC-12 (SI4463, 433 MHz)**<br><sub>`com-hc12-433`</sub> | modulo | Header 1x5 + IPEX/antena resorte (5p, 2.54 mm) | Antena resorte, Antena SMA por IPEX | media |
| **Transceptor sub-GHz CC1101**<br><sub>`com-cc1101`</sub> | modulo | Header 2x4 o 2x5 (según versión) (8p, 2.54 mm, filas 2.54 mm) | 433 MHz, 868/915 MHz | media |
| **Lector RFID RC522 13.56 MHz (MFRC522)**<br><sub>`com-rfid-rc522`</sub> | modulo | Header 1x8 (8p, 2.54 mm) | Kit con tarjeta y llavero, Mini RC522 | muy alta |
| **Tarjetas y llaveros RFID 13.56 MHz (MIFARE Classic 1K)**<br><sub>`com-rfid-tags-13-56`</sub> | n/a | — | Tarjeta blanca CR80 (85.6 x 54 mm), Llavero azul, Sticker NTAG213/215, Tarjeta UID modificable ('magic') | alta |
| **Lector RFID 125 kHz RDM6300**<br><sub>`com-rfid-rdm6300`</sub> | modulo | Headers P1 1x5, P2 1x2, P3 1x3 (10p, 2.54 mm) | — | media |
| **Módulo NFC/RFID PN532 V3**<br><sub>`com-nfc-pn532`</sub> | modulo | Header 1x4 (I2C/HSU) + 1x8 (SPI) (12p, 2.54 mm) | V3 rojo, Mini PN532 azul | media |
| **Tarjetas y llaveros RFID 125 kHz (EM4100 / T5577)**<br><sub>`com-rfid-tags-125khz`</sub> | n/a | — | Tarjeta CR80, Llavero, T5577 regrabable | media |
| **Módulo RS-485 MAX485 (TTL a RS-485)**<br><sub>`com-rs485-max485`</sub> | modulo | Headers 1x4 + 1x4 en extremos + bornera 2 (10p, 2.54 mm) | MAX485, Versión automática sin DE/RE (XY-017/HW-519) | alta |
| **Módulo CAN bus MCP2515 + TJA1050**<br><sub>`com-can-mcp2515`</sub> | modulo | Header 1x7 + bornera 2 + jumper J1 (7p, 2.54 mm) | Cristal 8 MHz, Cristal 16 MHz | media |
| **Módulo TTL a RS-232 MAX3232 (DB9)**<br><sub>`com-rs232-max3232`</sub> | modulo | Header 1x4 + DB9 (4p, 2.54 mm) | DB9 hembra, DB9 macho | media |
| **Módulo Wi-Fi ESP-01 / ESP-01S (ESP8266)**<br><sub>`com-esp-01`</sub> | modulo | Header 2x4 macho (8p, 2.54 mm, filas 2.54 mm) | ESP-01 (azul, 512 KB–1 MB), ESP-01S (negro, 1 MB, pull-ups integrados) | muy alta |
| **Módulo ESP-12E / ESP-12F (ESP8266)**<br><sub>`com-esp-12f`</sub> | modulo | SMD castellated 22 pads (22p, 2.0 mm, filas 16.0 mm) | ESP-12E, ESP-12F (antena mejorada), Placa adaptadora blanca | alta |
| **Módulo ESP32-WROOM-32 / WROOM-32E (suelto)**<br><sub>`com-esp32-wroom-32`</sub> | modulo | SMD castellated 38 pads + pad térmico (39p, 1.27 mm) | WROOM-32E 4 MB, WROOM-32E 8/16 MB, WROOM-32UE (conector IPEX) | media |
| **Módulo Digi XBee S2C (Zigbee / 802.15.4)**<br><sub>`com-xbee-s2c`</sub> | modulo | THT 2x10 paso 2.0 mm (20p, 2.0 mm, filas 22.0 mm) | XBee S2C, XBee Pro S2C, Antena PCB / wire / RP-SMA / U.FL | media |

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

<a id="displays"></a>
## Displays y pantallas

| Componente | Montaje | Encapsulado / huella | Valores o variantes comunes | Popularidad |
|---|---|---|---|---|
| **Módulo display 4 dígitos TM1637**<br><sub>`dsp-tm1637-4digitos`</sub> | modulo | Módulo TM1637 0.36" (4p, 2.54 mm); Módulo TM1637 0.56" (4p, 2.54 mm) | Rojo 0.36" con dos puntos, Rojo 0.56", Azul, Blanco, Verde | muy alta |
| **Módulo display 7 segmentos 8 dígitos MAX7219**<br><sub>`dsp-max7219-8digitos`</sub> | modulo | Módulo 8 dígitos (10p, 2.54 mm) | Rojo | alta |
| **Módulo TM1638 LED&KEY (8 dígitos, 8 LEDs, 8 botones)**<br><sub>`dsp-tm1638-ledkey`</sub> | modulo | Módulo LED&KEY (5p, 2.54 mm) | — | media |
| **Display e-Paper (tinta electrónica) 1.54" / 2.9" SPI**<br><sub>`dsp-epaper`</sub> | modulo | Módulo e-Paper 1.54" 200x200 (8p, 2.54 mm); Módulo e-Paper 2.9" 296x128 (8p, 2.54 mm) | 1.54" B/N, 2.13", 2.9" B/N, Tricolor (rojo/negro/blanco) | media |
| **Adaptador I2C para LCD (backpack PCF8574)**<br><sub>`dsp-backpack-i2c-pcf8574`</sub> | modulo | Backpack LCM1602 IIC (20p, 2.54 mm) | PCF8574T (0x27), PCF8574AT (0x3F) | muy alta |
| **Display LCD 16x2 con adaptador I2C soldado**<br><sub>`dsp-lcd-16x2-i2c`</sub> | modulo | Módulo 1602 + backpack I2C (4p, 2.54 mm) | Fondo azul, Fondo verde-amarillo, Dirección 0x27 (PCF8574T), Dirección 0x3F (PCF8574AT) | muy alta |
| **Display LCD 16x2 HD44780 (paralelo)**<br><sub>`dsp-lcd-16x2`</sub> | modulo | Módulo 1602 estándar (16p, 2.54 mm) | Fondo azul, letras blancas, Fondo verde-amarillo, letras negras, Blanco/negro FSTN, Rojo negativo (AG: DYS-1602A-ROJO/NEGAT), Con o sin header soldado | muy alta |
| **Display LCD 20x4 con adaptador I2C**<br><sub>`dsp-lcd-20x4-i2c`</sub> | modulo | Módulo 2004 + backpack I2C (4p, 2.54 mm) | Fondo azul/letras amarillas o blancas, Fondo verde, 0x27 o 0x3F | alta |
| **Display LCD 20x4 HD44780 (paralelo)**<br><sub>`dsp-lcd-20x4`</sub> | modulo | Módulo 2004 estándar (16p, 2.54 mm) | Fondo azul, letras blancas, Fondo verde-amarillo, letras negras, Con o sin backpack I2C | alta |
| **Shield LCD 16x2 con teclado (LCD Keypad Shield)**<br><sub>`dsp-lcd-keypad-shield`</sub> | modulo | Shield formato Arduino UNO (2.54 mm) | — | alta |
| **Display LCD 16x1 HD44780**<br><sub>`dsp-lcd-16x1`</sub> | modulo | Módulo 1601 (16p, 2.54 mm) | Fondo azul, Fondo verde-amarillo | media |
| **Display LCD 8x2 HD44780**<br><sub>`dsp-lcd-8x2`</sub> | modulo | Módulo 0802 (16p, 2.54 mm) | Fondo azul, Fondo verde-amarillo | media |
| **LCD gráfico 128x64 ST7920 (12864B)**<br><sub>`dsp-lcd-12864-st7920`</sub> | modulo | Módulo 12864 ST7920 (20p, 2.54 mm) | Fondo azul, Fondo verde-amarillo | alta |
| **Display Nokia 5110 84x48 PCD8544**<br><sub>`dsp-nokia-5110`</sub> | modulo | Módulo Nokia 5110 (PCB roja o azul) (8p, 2.54 mm) | PCB roja, PCB azul | media |
| **LCD gráfico 128x64 KS0108**<br><sub>`dsp-lcd-12864-ks0108`</sub> | modulo | Módulo 12864 KS0108 (20p, 2.54 mm) | Fondo azul, Fondo verde-amarillo | media |
| **Tira LED direccionable WS2812B 5 V**<br><sub>`dsp-ws2812b-tira`</sub> | modulo | Tira 30/60/144 LED por metro (3p) | 30 LED/m, 60 LED/m, 144 LED/m, IP30 (sin cubierta), IP65 (silicón), IP67 (tubo), PCB negra o blanca | alta |
| **Anillo LED WS2812B (8/12/16/24 LEDs)**<br><sub>`dsp-ws2812b-anillo`</sub> | modulo | Anillo 8 LEDs (4p); Anillo 12 LEDs (4p); Anillo 16 LEDs (4p); Anillo 24 LEDs (4p) | 8, 12, 16, 24, 60 (4 segmentos) | media |
| **LED direccionable PL9823 THT (5 mm / 8 mm)**<br><sub>`dsp-pl9823`</sub> | THT | LED 5 mm (F5) 4 patas (4p); LED 8 mm (F8) 4 patas (4p) | 5 mm, 8 mm | media |
| **LED WS2812B suelto 5050 SMD**<br><sub>`dsp-ws2812b-led`</sub> | SMD | 5050 de 4 pads (4p); En mini PCB redonda (~10 mm) (3p) | — | media |
| **Matriz LED WS2812B 8x8 (64 LEDs)**<br><sub>`dsp-ws2812b-matriz-8x8`</sub> | modulo | Matriz rígida 8x8 (CJMCU) (3p); Matriz flexible 8x8 / 16x16 (3p) | 8x8 rígida, 8x8 flexible, 16x16 flexible, 8x32 flexible | media |
| **Módulo matriz LED 4 en 1 MAX7219 (32x8)**<br><sub>`dsp-max7219-4en1`</sub> | modulo | Módulo FC-16 4 en 1 (10p, 2.54 mm) | Rojo, Verde, Azul | alta |
| **Módulo matriz LED 8x8 con MAX7219**<br><sub>`dsp-max7219-matriz-8x8`</sub> | modulo | Versión DIP (MAX7219 DIP-24, PCB larga) (10p, 2.54 mm); Versión SMD (FC-16, PCB cuadrada) (10p, 2.54 mm) | Rojo, Verde, Azul | alta |
| **Módulo panel LED P10 32x16 (HUB12)**<br><sub>`dsp-panel-p10`</sub> | modulo | Panel P10 32x16 (16p, 2.54 mm, filas 2.54 mm) | Rojo, Bicolor, RGB (HUB75, otro conector), Interior / exterior | media |
| **Display OLED 0.96" 128x64 SSD1306 I2C (4 pines)**<br><sub>`dsp-oled-096-i2c`</sub> | modulo | Módulo OLED 0.96" I2C (4p, 2.54 mm) | Blanco, Azul, Bicolor amarillo (16 filas superiores)/azul | muy alta |
| **Display OLED 0.91" 128x32 SSD1306 I2C**<br><sub>`dsp-oled-091-128x32`</sub> | modulo | Módulo OLED 0.91" (4p, 2.54 mm) | Blanco, Azul | alta |
| **Display OLED 0.96" 128x64 SSD1306 SPI (7 pines)**<br><sub>`dsp-oled-096-spi`</sub> | modulo | Módulo OLED 0.96" SPI (7p, 2.54 mm) | Blanco, Azul, Amarillo/azul | alta |
| **Display OLED 1.3" 128x64 SH1106**<br><sub>`dsp-oled-13-sh1106`</sub> | modulo | Módulo OLED 1.3" I2C (4p, 2.54 mm); Módulo OLED 1.3" SPI (7p, 2.54 mm) | Blanco, Azul | alta |
| **Display OLED de caracteres 16x2 (Winstar WEH001602)**<br><sub>`dsp-oled-caracteres-16x2`</sub> | modulo | Módulo 1602 OLED (16p, 2.54 mm) | Blanco, Amarillo, Verde | media |
| **Display TFT 1.8" 128x160 ST7735 SPI con lector SD**<br><sub>`dsp-tft-18-st7735`</sub> | modulo | Módulo TFT 1.8" (PCB roja) (12p, 2.54 mm) | — | alta |
| **Display TFT 2.8" ILI9341 SPI con táctil XPT2046**<br><sub>`dsp-tft-28-ili9341-spi`</sub> | modulo | Módulo TFT 2.8" SPI (PCB roja) (14p, 2.54 mm) | 2.4", 2.8", 3.2" | alta |
| **Shield TFT 2.4" táctil 240x320 para Arduino UNO**<br><sub>`dsp-tft-24-shield`</sub> | modulo | Shield formato Arduino UNO (28p, 2.54 mm) | 2.4", 2.8" | alta |
| **Display TFT 1.44" 128x128 ST7735 SPI**<br><sub>`dsp-tft-144-st7735`</sub> | modulo | Módulo TFT 1.44" (PCB roja) (8p, 2.54 mm) | — | media |
| **Display TFT IPS 1.3"/1.54" 240x240 ST7789**<br><sub>`dsp-tft-ips-st7789`</sub> | modulo | Módulo IPS 1.3" (7 pines, sin CS) (7p, 2.54 mm) | 1.3" 240x240, 1.54" 240x240, 2.0" 240x320 | media |
| **Shield TFT 3.5" 320x480 para Arduino UNO/Mega**<br><sub>`dsp-tft-35-shield`</sub> | modulo | Shield formato Arduino UNO/Mega (2.54 mm) | — | media |
| **Controlador para tira LED RGB 12 V con control IR**<br><sub>`dsp-controlador-tira-rgb`</sub> | modulo | Controlador IR (4p) | 24 teclas, 44 teclas, Bluetooth/WiFi | alta |
| **Tira LED 12 V monocolor (5050 / 2835)**<br><sub>`dsp-tira-led-12v`</sub> | modulo | 5050, 60 LED/m (2p); 2835, 60/120 LED/m (2p) | Blanco frío, Blanco cálido, Rojo, Verde, Azul, IP20, IP65 | alta |
| **Tira LED RGB 12 V 5050 (ánodo común)**<br><sub>`dsp-tira-led-rgb-12v`</sub> | modulo | 5050 RGB 30/60 LED/m (4p) | 30 LED/m, 60 LED/m, IP20, IP65 | alta |

<a id="actuadores_y_audio"></a>
## Actuadores y audio (motores, servos, buzzers, bocinas)

| Componente | Montaje | Encapsulado / huella | Valores o variantes comunes | Popularidad |
|---|---|---|---|---|
| **Bocina miniatura 8 Ω 0.25–0.5 W (28–66 mm)**<br><sub>`act-bocina-miniatura-8ohm`</sub> | panel | Ø28 mm (2p); Ø36 mm (2p); Ø40 mm (2p); Ø50 mm (2p); Ø57 mm (2p); Ø66 mm (2p) | 8 Ω 0.25 W, 8 Ω 0.5 W, 8 Ω 1 W | muy alta |
| **Bocina 2" y 4" 8 Ω (Steren)**<br><sub>`act-bocina-2-4-pulgadas`</sub> | panel | 2" (5 cm) (2p); 4" (10 cm) (2p) | 2" 1.5 W PMPO 8 Ω, 4" 7 W PMPO 8 Ω | alta |
| **Bocina 2–3 W (4 Ω / 8 Ω) para módulos amplificadores**<br><sub>`act-bocina-2-3w`</sub> | panel | Redonda Ø40 mm (2p); Rectangular (tipo laptop/TV) (2p) | 4 Ω 3 W, 8 Ω 2 W, 8 Ω 3 W | alta |
| **Sirena electrónica 12 V para alarma**<br><sub>`act-sirena-12v`</sub> | panel | Sirena con soporte (2p) | 15 W, 20 W, 30 W, 1 tono, 6 tonos | media |
| **Tweeter piezoeléctrico (bocina de agudos)**<br><sub>`act-tweeter-piezo`</sub> | panel | Corneta rectangular / redonda (2p) | — | media |
| **Mini bomba de agua sumergible 3–6 V**<br><sub>`act-bomba-sumergible-3-6v`</sub> | panel | Bomba horizontal/vertical miniatura (2p) | Horizontal, Vertical | alta |
| **Bomba de agua 12 V (diafragma R385 o sumergible)**<br><sub>`act-bomba-12v`</sub> | panel | Bomba de diafragma R385 (2p) | Diafragma R385, Sumergible brushless 12 V | media |
| **Buzzer activo 5 V / 12 V (12 mm)**<br><sub>`act-buzzer-activo`</sub> | THT | Ø12 x 9.5 mm (2p, 7.6 mm) | 5 V, 12 V, 3.3 V | muy alta |
| **Buzzer pasivo (magnético) 12 mm**<br><sub>`act-buzzer-pasivo`</sub> | THT | Ø12 x 8.5 mm (2p, 7.6 mm) | 16 Ω, 42 Ω | alta |
| **Disco piezoeléctrico (12–35 mm)**<br><sub>`act-disco-piezo`</sub> | panel | Ø27 mm (2p); Ø35 mm (2p); Ø20 mm / Ø12 mm (2p) | 12 mm, 20 mm, 27 mm, 35 mm | alta |
| **Módulo buzzer (activo o pasivo) con transistor**<br><sub>`act-modulo-buzzer`</sub> | modulo | Módulo de 3 pines (3p, 2.54 mm) | Activo, Pasivo | alta |
| **Zumbador piezoeléctrico con carcasa 3–24 V (SFM-27)**<br><sub>`act-zumbador-piezo-carcasa`</sub> | panel | Carcasa con orejas (SFM-27) (2p) | Tono continuo, Tono intermitente | media |
| **Motor DC de juguete tamaño 130/140 (3–6 V)**<br><sub>`act-motor-dc-130`</sub> | panel | Carcasa tamaño 130 (FA-130) (2p) | 1.5–3 V, 3–6 V | muy alta |
| **Motor brushless A2212 (1000/1400/2200 KV)**<br><sub>`act-motor-brushless-a2212`</sub> | panel | Outrunner A2212 (3p) | 1000 KV, 1400 KV, 2200 KV | media |
| **Motor DC R260 (3–6 V)**<br><sub>`act-motor-dc-r260`</sub> | panel | Carcasa 260 (2p) | 3 V, 6 V | media |
| **Motor DC RF-300 (motor solar / bajo consumo)**<br><sub>`act-motor-dc-rf300`</sub> | panel | Carcasa RF-300 (2p) | 0.4–5.9 V | media |
| **Motor DC RS-385 (6–12 V)**<br><sub>`act-motor-dc-rs385`</sub> | panel | Carcasa 385 (2p) | 6 V, 12 V | media |
| **Motor DC RS-555 / RS-550 (12–24 V)**<br><sub>`act-motor-dc-rs555`</sub> | panel | Carcasa 555/550 (2p) | 12 V, 24 V | media |
| **Motor a pasos 28BYJ-48 5 V (unipolar)**<br><sub>`act-motor-pasos-28byj48`</sub> | panel | 28BYJ-48 (5p, 2.5 mm) | 5 V, 12 V | muy alta |
| **Motor a pasos NEMA 17 (17HS4401, bipolar)**<br><sub>`act-nema17-17hs4401`</sub> | panel | NEMA 17, 40 mm de largo (4p) | 17HS4401 (40 mm, 1.7 A), 17HS8401 / 48 mm (más torque), 17HS2408 (34 mm) | alta |
| **Motor a pasos NEMA 23 (bipolar)**<br><sub>`act-nema23`</sub> | panel | NEMA 23 (4p) | 1.2 N·m, 1.9 N·m, 2.8–3 N·m | media |
| **Motorreductor amarillo TT 3–6 V (recto y en L) con llanta**<br><sub>`act-motor-tt`</sub> | panel | TT recto (2p); TT en L (90°) (2p); Llanta 65 mm | Recto 1:48, En L 1:48, 1:120, Con llanta 65 mm, Con encoder de ranura (disco) | muy alta |
| **Micromotorreductor N20 (3/6/12 V), con o sin encoder**<br><sub>`act-motor-n20`</sub> | panel | N20 sin encoder (2p); N20 con encoder (6p) | 3 V, 6 V, 12 V, 30, 50, 100, 200, 300, 500, 1000 rpm | alta |
| **Motorreductor JGA25-370 12 V con encoder Hall**<br><sub>`act-motor-25ga370-encoder`</sub> | panel | Caja Ø25 mm + motor 370 (6p) | 6 V, 12 V, Varias rpm (e.g. 100–1000) | media |
| **Motorreductor metálico 12 V JGB37-520 (37 mm)**<br><sub>`act-motorreductor-jgb37-520`</sub> | panel | Caja Ø37 mm (2p) | 12 V, 24 V, 10–1000 rpm | media |
| **Micro servo SG90 9 g**<br><sub>`act-servo-sg90`</sub> | panel | Servo micro 9 g (3p, 2.54 mm) | 180°, 360° (rotación continua) | muy alta |
| **Servo MG996R (engranes metálicos, alto torque)**<br><sub>`act-servo-mg996r`</sub> | panel | Servo estándar (3p, 2.54 mm) | 180°, 360° | muy alta |
| **Micro servo MG90S (engranes metálicos)**<br><sub>`act-servo-mg90s`</sub> | panel | Servo micro 13 g (3p, 2.54 mm) | 180°, 360° | alta |
| **Servo MG995 estándar (engranes metálicos)**<br><sub>`act-servo-mg995`</sub> | panel | Servo estándar (3p, 2.54 mm) | 180°, 360° | alta |
| **Servo de rotación continua 360° (FS90R / SG90-360 / MG995-360)**<br><sub>`act-servo-continuo`</sub> | panel | Micro (9 g) (3p, 2.54 mm); Estándar (MG995 360°) (3p, 2.54 mm) | Micro 360°, Estándar 360° | media |
| **Cerradura eléctrica de solenoide 12 V**<br><sub>`act-cerradura-solenoide-12v`</sub> | panel | Cerradura tipo pestillo (2p) | 12 V, Pestillo inclinado o recto | media |
| **Electroimán de sujeción 12 V (KK-P20/15, KK-P25/20)**<br><sub>`act-electroiman-12v`</sub> | panel | KK-P20/15 (2p); KK-P25/20 (2p) | 2.5 kg, 5 kg, 10 kg | media |
| **Electroválvula solenoide 12 V 1/2" (normalmente cerrada)**<br><sub>`act-electrovalvula-12v`</sub> | panel | Rosca 1/2" (2p) | 12 V NC, 24 V, 110 V AC, 1/2", 3/4" | media |
| **Solenoide push-pull 12 V (JF-0530B)**<br><sub>`act-solenoide-push-pull-12v`</sub> | panel | JF-0530B (2p) | 5 V, 6 V, 12 V, 24 V, JF-0826B (más grande) | media |
| **Ventilador DC 5 V / 12 V (30–120 mm)**<br><sub>`act-ventilador-dc`</sub> | panel | 30 x 30 x 10 mm (2p); 40 x 40 x 10 mm (2p); 50 x 50 x 10/15 mm (2p); 60 x 60 x 15/25 mm (2p); 80 x 80 x 25 mm (3p); 92 / 120 mm (3p) | 5 V, 12 V, 24 V, 2 hilos, 3 hilos, 4 hilos PWM, Rodamiento de manga o de bolas | muy alta |
| **Motor vibrador tipo moneda 10 mm**<br><sub>`act-vibrador-moneda`</sub> | panel | 1027 (Ø10 x 2.7 mm) (2p); 1030 (Ø10 x 3 mm) (2p) | Ø8 mm, Ø10 mm | alta |
| **Motor vibrador cilíndrico (masa excéntrica) y módulo vibrador**<br><sub>`act-vibrador-cilindrico`</sub> | panel | Motor cilíndrico con contrapeso (2p); Módulo vibrador (3p, 2.54 mm) | — | media |

<a id="modulos_potencia"></a>
## Módulos de potencia y control

| Componente | Montaje | Encapsulado / huella | Valores o variantes comunes | Popularidad |
|---|---|---|---|---|
| **Módulo cargador de litio TP4056 (con y sin protección DW01)**<br><sub>`mod-tp4056`</sub> | modulo | Sin protección (4 pads) (4p); Con protección DW01 (6 pads) (6p) | Micro-USB, USB-C, Con protección, Sin protección | muy alta |
| **Módulo BMS / protección de litio 2S, 3S, 4S**<br><sub>`mod-bms-litio`</sub> | modulo | BMS 2S/3S/4S | 2S 7.4 V, 3S 11.1 V, 4S 14.8 V, 10 A, 20 A, 40 A, Con balanceo | alta |
| **Porta batería 18650 con cargador y salida USB (Battery Shield V3/V8)**<br><sub>`mod-shield-18650-usb`</sub> | modulo | Shield 1 celda (V3) (2.54 mm); Shield 2 celdas (V8) (2.54 mm) | 1 celda, 2 celdas | media |
| **Módulo detector de cruce por cero (AC)**<br><sub>`mod-cruce-por-cero`</sub> | modulo | Módulo detector (5p, 2.54 mm) | — | media |
| **Módulo dimmer AC con TRIAC y detector de cruce por cero**<br><sub>`mod-dimmer-ac-triac`</sub> | modulo | Módulo RobotDyn (8p, 2.54 mm); Dimmer 2000 W con potenciómetro (4p) | 1 canal, 2 canales, Manual 2000 W | media |
| **Módulo reductor DC-DC LM2596 (step-down ajustable)**<br><sub>`mod-lm2596`</sub> | modulo | Módulo azul LM2596 (4p) | Básico, Con display de voltaje, Con salida USB | muy alta |
| **Módulo elevador DC-DC MT3608 (step-up)**<br><sub>`mod-mt3608`</sub> | modulo | Módulo MT3608 (4p) | Pads, Con micro-USB | alta |
| **Módulo mini reductor DC-DC MP1584EN**<br><sub>`mod-mp1584en`</sub> | modulo | Módulo MP1584EN (4p) | Ajustable, Fijo 5 V / 3.3 V | alta |
| **Módulo reductor DC-DC XL4015 5 A (CV o CC/CV)**<br><sub>`mod-xl4015`</sub> | modulo | Módulo XL4015 (4p) | Voltaje constante, CC/CV (2 potenciómetros), Con voltímetro | alta |
| **Convertidor DC-DC aislado B0505S-1W (5 V → 5 V)**<br><sub>`mod-b0505s`</sub> | THT | SIP-4 (4p, 2.54 mm) | B0505S (5→5 V), B0512S (5→12 V), B1205S (12→5 V) | media |
| **Módulo DC-DC XL6009 (elevador o buck-boost)**<br><sub>`mod-xl6009`</sub> | modulo | Módulo XL6009 boost (4p); Módulo XL6009 buck-boost (4p) | Boost, Buck-boost | media |
| **Módulo elevador a 5 V con salida USB**<br><sub>`mod-step-up-5v-usb`</sub> | modulo | Módulo con USB-A hembra (2p) | 600 mA, 1 A, 2 A | media |
| **Módulo puente H L298N (driver doble de motores)**<br><sub>`mod-l298n`</sub> | modulo | Módulo rojo con disipador (13p, 2.54 mm) | — | muy alta |
| **Controlador PWM de velocidad para motor DC (CCM5D / 10 A)**<br><sub>`mod-pwm-motor-dc`</sub> | modulo | Módulo con bornera y perilla (4p) | 3 A, 5 A, 10 A, 20 A | alta |
| **Módulo driver de motor BTS7960 43 A (IBT-2)**<br><sub>`mod-bts7960`</sub> | modulo | Módulo con disipador (12p, 2.54 mm) | — | alta |
| **Módulo driver L9110S (2 motores DC)**<br><sub>`mod-l9110s`</sub> | modulo | Módulo L9110S (6p, 2.54 mm) | — | alta |
| **Módulo driver TB6612FNG (2 motores DC, MOSFET)**<br><sub>`mod-tb6612fng`</sub> | modulo | Breakout 16 pines (16p, 2.54 mm) | — | alta |
| **Shield de motores L293D para Arduino (Motor Shield v1)**<br><sub>`mod-l293d-shield`</sub> | modulo | Shield formato Arduino UNO (2.54 mm) | — | alta |
| **Módulo driver DRV8833 (2 motores DC)**<br><sub>`mod-drv8833`</sub> | modulo | Módulo DRV8833 (2.54 mm) | — | media |
| **Módulo driver MX1508 (2 motores DC)**<br><sub>`mod-mx1508`</sub> | modulo | Módulo MX1508 (8p, 2.54 mm) | — | media |
| **Variador ESC 30 A para motor brushless**<br><sub>`mod-esc-30a`</sub> | modulo | ESC en termoencogible (8p) | 20 A, 30 A, 40 A | media |
| **Driver de motor a pasos A4988 (Pololu/StepStick)**<br><sub>`mod-a4988`</sub> | modulo | StepStick 16 pines (16p, 2.54 mm, filas 12.7 mm) | Verde/rojo (clones), Pololu original | muy alta |
| **Placa driver ULN2003 para motor a pasos 28BYJ-48**<br><sub>`mod-uln2003-driver`</sub> | modulo | Placa ULN2003 (11p, 2.54 mm) | — | muy alta |
| **CNC Shield V3 para Arduino UNO (4 drivers StepStick)**<br><sub>`mod-cnc-shield-v3`</sub> | modulo | Shield formato Arduino UNO (2.54 mm) | — | alta |
| **Driver de motor a pasos DRV8825 (Pololu/StepStick)**<br><sub>`mod-drv8825`</sub> | modulo | StepStick 16 pines (16p, 2.54 mm, filas 12.7 mm) | — | alta |
| **Driver de motor a pasos silencioso TMC2208 / TMC2209**<br><sub>`mod-tmc2208-tmc2209`</sub> | modulo | StepStick 16 pines (16p, 2.54 mm, filas 12.7 mm) | TMC2208 v3, TMC2209 v1.2, TMC2225 | alta |
| **Fuente AC-DC encapsulada HLK-PM01 (220 V → 5 V 3 W)**<br><sub>`mod-hlk-pm01`</sub> | THT | Encapsulado HLK-PM (4p) | HLK-PM01 5 V 600 mA, HLK-PM03 3.3 V, HLK-PM12 12 V, HLK-5M05 (5 W) | alta |
| **Voltímetro digital de panel (0.28" / 0.56")**<br><sub>`mod-voltimetro-panel`</sub> | panel | 0.28" 3 dígitos (3p); 0.56" 3 dígitos (3p) | 0–30 V (2 hilos), 0–100 V (3 hilos), Rojo, Azul, Verde | alta |
| **Voltímetro/amperímetro digital de panel DC 100 V 10 A**<br><sub>`mod-voltamperimetro-panel`</sub> | panel | Panel 0.28" doble (5p) | 10 A, 50 A (shunt externo), 100 A (shunt externo) | alta |
| **Indicador de capacidad de batería (litio 1S–4S / plomo 12 V)**<br><sub>`mod-indicador-bateria`</sub> | modulo | Módulo 4 LEDs (2p) | 1S, 2S, 3S, 4S, 12 V plomo-ácido | media |
| **Módulo MOSFET IRF520**<br><sub>`mod-mosfet-irf520`</sub> | modulo | Módulo IRF520 (7p, 2.54 mm) | — | alta |
| **Módulo MOSFET doble AOD4184 (trigger switch 15 A)**<br><sub>`mod-mosfet-d4184`</sub> | modulo | Módulo D4184 (6p) | — | media |
| **Fuente para protoboard MB102 (YwRobot) 3.3 V / 5 V**<br><sub>`mod-mb102-fuente-protoboard`</sub> | modulo | Módulo MB102 (2.54 mm) | — | muy alta |
| **Módulo regulador AMS1117 3.3 V / 5 V**<br><sub>`mod-ams1117-33`</sub> | modulo | Módulo AMS1117 (3p, 2.54 mm) | 3.3 V, 5 V | alta |
| **Módulo regulador ajustable LM317**<br><sub>`mod-lm317-ajustable`</sub> | modulo | Módulo LM317 (4p) | — | media |
| **Módulo relevador 1 canal 5 V / 12 V**<br><sub>`mod-relevador-1ch`</sub> | modulo | Módulo 1 canal (6p, 2.54 mm) | 5 V, 12 V, Con optoacoplador, Jumper disparo alto/bajo | muy alta |
| **Módulo relevador 2 canales 5 V / 12 V con optoacoplador**<br><sub>`mod-relevador-2ch`</sub> | modulo | Módulo 2 canales (13p, 2.54 mm) | 5 V, 12 V | muy alta |
| **Módulo relevador 4 canales 5 V / 12 V con optoacoplador**<br><sub>`mod-relevador-4ch`</sub> | modulo | Módulo 4 canales (21p, 2.54 mm) | 5 V, 12 V | muy alta |
| **Módulo relevador 8 canales 5 V / 12 V con optoacoplador**<br><sub>`mod-relevador-8ch`</sub> | modulo | Módulo 8 canales (37p, 2.54 mm) | 5 V, 12 V | alta |
| **Módulo relevador 16 canales 12 V / 5 V**<br><sub>`mod-relevador-16ch`</sub> | modulo | Módulo 16 canales (2.54 mm) | 12 V, 5 V | media |
| **Relevador de estado sólido SSR Fotek SSR-25DA / SSR-40DA**<br><sub>`mod-ssr-fotek`</sub> | panel | Encapsulado industrial con 4 tornillos (4p) | 25 A (SSR-25DA), 40 A (SSR-40DA), 10 A, DD (DC→DC), AA (AC→AC) | alta |
| **Módulo relevador de estado sólido Omron G3MB-202P (1/2/4/8 canales)**<br><sub>`mod-ssr-g3mb-202p`</sub> | modulo | Módulo 1/2/4/8 canales (2.54 mm) | 1 canal, 2 canales, 4 canales, 8 canales, Disparo bajo, Disparo alto | media |

<a id="modulos_varios"></a>
## Módulos varios (RTC, SD, audio, ADC...)

| Componente | Montaje | Encapsulado / huella | Valores o variantes comunes | Popularidad |
|---|---|---|---|---|
| **Módulo lector microSD (SPI)**<br><sub>`mod-microsd`</sub> | modulo | Módulo Catalex (6p, 2.54 mm); Mini lector 3.3 V (sin regulador) (2.54 mm) | 5 V con convertidor de nivel, 3.3 V mini | muy alta |
| **Módulo lector de tarjeta SD tamaño completo**<br><sub>`mod-sd`</sub> | modulo | Módulo SD doble fila (16p, 2.54 mm, filas 2.54 mm) | — | media |
| **Módulo memoria EEPROM AT24C256 (I2C)**<br><sub>`mod-at24c256`</sub> | modulo | Módulo AT24C256 (4p, 2.54 mm) | — | media |
| **Módulo amplificador PAM8403 2 x 3 W (5 V)**<br><sub>`mod-pam8403`</sub> | modulo | Mini módulo (pads) (9p); Con potenciómetro de volumen (9p, 2.54 mm) | Sin volumen, Con potenciómetro | muy alta |
| **Módulo amplificador LM386**<br><sub>`mod-lm386`</sub> | modulo | Módulo LM386 (6p, 2.54 mm) | — | alta |
| **Módulo amplificador TPA3116D2 2 x 50 W (clase D)**<br><sub>`mod-tpa3116d2`</sub> | modulo | Módulo TPA3116D2 | 2 x 50 W, Mono 100 W, 2.1 (con subwoofer) | alta |
| **Módulo amplificador PAM8610 2 x 10 W (12 V)**<br><sub>`mod-pam8610`</sub> | modulo | Módulo PAM8610 (9p) | — | media |
| **Módulo amplificador TDA7297 2 x 15 W**<br><sub>`mod-tda7297`</sub> | modulo | Módulo TDA7297 con disipador | — | media |
| **Módulo reproductor MP3 DFPlayer Mini**<br><sub>`mod-dfplayer-mini`</sub> | modulo | Módulo DFPlayer (2 x 8 pines) (16p, 2.54 mm) | Original DFRobot, Clones (MP3-TF-16P) | muy alta |
| **Decodificador MP3 de panel 12 V (USB/SD/FM/Bluetooth)**<br><sub>`mod-decodificador-mp3-panel`</sub> | panel | Panel rectangular | 5 V, 12 V, Con amplificador 2 x 3 W | alta |
| **Módulo receptor de audio Bluetooth (estéreo)**<br><sub>`mod-receptor-bluetooth-audio`</sub> | modulo | Módulo receptor | Bluetooth 4.2, Bluetooth 5.0, Con amplificador integrado | alta |
| **Módulo de reconocimiento de voz V3 (Elechouse)**<br><sub>`mod-reconocimiento-voz-v3`</sub> | modulo | Módulo VR3 (2.54 mm) | — | media |
| **Módulo grabador/reproductor de voz ISD1820**<br><sub>`mod-isd1820`</sub> | modulo | Módulo ISD1820 (2.54 mm) | — | media |
| **Termostato digital XH-W1209 con relevador (12 V)**<br><sub>`mod-termostato-w1209`</sub> | modulo | Módulo W1209 (6p) | 12 V, 5 V (versión W1209 5V), 24 V | alta |
| **Módulo expansor de E/S PCF8574 (I2C, 8 bits)**<br><sub>`mod-pcf8574-expansor`</sub> | modulo | Módulo azul (PCF8574 DIP-16) (17p, 2.54 mm) | PCF8574 (0x20–0x27), PCF8574A (0x38–0x3F) | media |
| **Módulo multiplexor analógico 16 canales CD74HC4067**<br><sub>`mod-cd74hc4067`</sub> | modulo | Breakout 24 pines (24p, 2.54 mm) | — | media |
| **Kit generador de funciones XR2206 (1 Hz – 1 MHz)**<br><sub>`mod-xr2206-generador`</sub> | THT | Kit THT | — | media |
| **Módulo NE555 generador de pulsos de frecuencia ajustable**<br><sub>`mod-ne555-generador`</sub> | modulo | Módulo NE555 (3p, 2.54 mm) | — | media |
| **Módulo relevador temporizador con retardo (programable)**<br><sub>`mod-relevador-temporizador`</sub> | modulo | Módulo con display (5p) | 5 V, 12 V, 24 V, Con display LED, NE555 con potenciómetro | media |
| **Módulo ADC ADS1115 (16 bits) / ADS1015 (12 bits)**<br><sub>`mod-ads1115`</sub> | modulo | Módulo azul 10 pines (10p, 2.54 mm) | ADS1115 16 bits, ADS1015 12 bits | alta |
| **Módulo PWM/servos 16 canales PCA9685 (I2C)**<br><sub>`mod-pca9685`</sub> | modulo | Módulo PCA9685 (70p, 2.54 mm) | — | alta |
| **Módulo DAC MCP4725 (12 bits, I2C)**<br><sub>`mod-mcp4725`</sub> | modulo | Módulo MCP4725 (6p, 2.54 mm) | — | media |
| **Módulo reloj de tiempo real DS3231 (ZS-042)**<br><sub>`mod-rtc-ds3231`</sub> | modulo | Módulo ZS-042 (10p, 2.54 mm) | — | muy alta |
| **Módulo RTC DS1307 (Tiny RTC)**<br><sub>`mod-rtc-ds1307`</sub> | modulo | Tiny RTC (12p, 2.54 mm) | — | alta |
| **Convertidor de nivel lógico bidireccional 4 canales (BSS138)**<br><sub>`mod-convertidor-nivel-logico`</sub> | modulo | Breakout 12 pines (12p, 2.54 mm) | 4 canales, 8 canales (TXS0108E) | alta |

<a id="electromecanicos"></a>
## Electromecánicos (botones, interruptores, relevadores)

| Componente | Montaje | Encapsulado / huella | Valores o variantes comunes | Popularidad |
|---|---|---|---|---|
| **Interruptor de botón con enclavamiento 8x8 / 8.5x8.5 mm (6 pines)**<br><sub>`emc-selflock-8x8`</sub> | THT | THT 8x8 mm, 6 pines (2 filas de 3) (6p) | 8x8 mm, 8.5x8.5 mm, Con o sin capuchón | alta |
| **Interruptor de enclavamiento miniatura 7x7 / 5.8x5.8 mm (6 pines)**<br><sub>`emc-selflock-7x7`</sub> | THT | THT 7x7 mm, 6 pines (6p); THT 5.8x5.8 mm, 6 pines (6p) | 7x7 con retención, 7x7 momentáneo, 5.8x5.8 | media |
| **Botón pulsador de panel miniatura (PBS-110 / PBS-11A / PBS-11B / PBS-33B)**<br><sub>`emc-boton-panel-mini-pbs`</sub> | panel | Panel, 2 terminales de soldar (2p) | NA (OFF-(ON)) rojo, NA negro, NA verde/amarillo/azul/blanco, NC ((ON)-OFF), Botón cuadrado NA | muy alta |
| **Botón metálico antivandálico con LED (12/16/19/22 mm)**<br><sub>`emc-boton-metalico-led`</sub> | panel | Panel Ø16 mm, 4–5 terminales (5p); Panel Ø19 mm (5p); Panel Ø22 mm (5p) | Ø12 mm, Ø16 mm, Ø19 mm, Ø22 mm, LED 3–6 V / 12 V / 24 V / 110–220 V, Momentáneo o con retención, Anillo rojo/azul/verde/blanco | alta |
| **Botón arcade 24/30 mm con microswitch**<br><sub>`emc-boton-arcade`</sub> | panel | Panel 30 mm (3p); Panel 24 mm (3p) | 24 mm, 30 mm, Con LED 5 V/12 V, Colores surtidos | media |
| **Botón de paro de emergencia tipo hongo**<br><sub>`emc-boton-paro-emergencia`</sub> | panel | Panel 22 mm (estándar industrial) (4p); Panel 16 mm (mini) (2p) | 22 mm 1NC, 22 mm 1NA+1NC, 16 mm, Con caja amarilla | media |
| **Botón pulsador industrial 22 mm (LA38 / XB2)**<br><sub>`emc-boton-industrial-22mm`</sub> | panel | Panel 22 mm, bloque de tornillo (4p) | Verde (arranque), Rojo (paro), Amarillo, Negro, Con lámpara 24 V / 110–220 V | media |
| **Botón pulsador táctil 6x6 mm THT (4 pines)**<br><sub>`emc-tact-6x6-tht`</sub> | THT | THT 6x6 mm, 4 pines (4p, 4.5 mm, filas 6.5 mm) | Altura 4.3 mm, 5 mm, 6 mm, 7 mm, 8 mm, 9 mm, 10 mm, 11 mm, … (+4) | muy alta |
| **Botón táctil 12x12 mm THT con capuchón**<br><sub>`emc-tact-12x12`</sub> | THT | THT 12x12 mm, 4 pines (4p, 5.0 mm, filas 12.5 mm) | 12x12x7.3 mm, 12x12x4.3 mm, 12x12x8 mm, Capuchón rojo/azul/amarillo/verde/negro/blanco/gris | muy alta |
| **Botón táctil 6x6 mm SMD (4 pads)**<br><sub>`emc-tact-6x6-smd`</sub> | SMD | SMD 6x6 mm, 4 pads (4p, 4.5 mm) | 6x6x3.1 mm, 6x6x4.3 mm, 6x6x5 mm, 6.1x6.1 mm (SMDTS-FS66T-C-A) | alta |
| **Botón táctil 3x6 mm de 2 pines (THT/SMD)**<br><sub>`emc-tact-3x6-2p`</sub> | THT/SMD | SMD 3x6 mm, 2 pads (2p); THT 3x6 mm, 2 pines (2p) | 3x6x2.5 mm SMD, 3x6x4.3 mm THT, 3x6x5 mm THT | media |
| **Botón táctil SMD miniatura 3x4 / 4x4 / 5.1x5.1 mm**<br><sub>`emc-tact-smd-3x4`</sub> | SMD | SMD 3x4 mm, 4 pads (4p); SMD 5.1x5.1 mm, 4 pads (TS-1187A) (4p) | 3x4x2 mm, 4x4x1.5 mm, 5.1x5.1x1.5 mm, 3x6x2.5 mm (2 pads) | media |
| **DIP switch de 1 a 12 posiciones (paso 2.54 mm)**<br><sub>`emc-dip-switch`</sub> | THT | DIP-2N (N posiciones) (2.54 mm, filas 7.62 mm); SMD (gull-wing) 2.54 mm (2.54 mm) | 1 posición, 2 posiciones, 3, 4, 5, 6, 8, 10, … (+2) | muy alta |
| **Encoder rotativo incremental EC11 (5 pines, con botón)**<br><sub>`emc-encoder-ec11`</sub> | THT | THT, 3+2 pines + 2 patas de fijación (5p, 2.5 mm) | Eje 15 mm, Eje 20 mm, Eje 25 mm, Eje 30 mm, Eje D o estriado 18 dientes, 20 pulsos / 20 detenes, 15 pulsos / 30 detenes | alta |
| **Interruptor de balancín KCD1 (2 o 3 pines)**<br><sub>`emc-rocker-kcd1`</sub> | panel | Panel a presión, 2 terminales (KCD1-101) (2p); Panel a presión, 3 terminales (KCD1-102/103) (3p) | KCD1-101 SPST negro, Rojo, Blanco, KCD1-102 SPDT, Versión redonda Ø20 mm | muy alta |
| **Interruptor de balancín KCD3 / KCD4 con luz (127 V)**<br><sub>`emc-rocker-kcd3-kcd4-luz`</sub> | panel | Panel a presión, 3 terminales (SPST iluminado) (3p); Panel a presión, 4 terminales (DPST iluminado) (4p) | KCD3 rojo 3 pines, KCD3 4 pines DPST, KCD4, Lámpara 127 V / 250 V / 12 V | alta |
| **Interruptor deslizable SS12D00 (SPDT, 3 pines)**<br><sub>`emc-slide-ss12d00`</sub> | THT | THT vertical, 3 pines en línea (3p, 2.54 mm) | SS12D00G2, SS12D00G3, SS12D00G4, SS12D00G5 | muy alta |
| **Interruptor deslizable SS22 / SS-22F (DPDT, 6 pines)**<br><sub>`emc-slide-ss22`</sub> | THT | THT, 6 pines (2 filas de 3) (6p) | SS22F32, SS-22D07 (palanca 4–7 mm), Vertical / horizontal (90°) | alta |
| **Interruptor deslizable SMD miniatura MSK-12C02**<br><sub>`emc-slide-msk12c02`</sub> | SMD | SMD, 3 pads de señal + patas de fijación (7p, 1.5 mm) | MSK-12C02, MSK-12C01 | media |
| **Interruptor de palanca MTS-102 (SPDT ON-ON, 3 terminales)**<br><sub>`emc-toggle-mts102`</sub> | panel | Panel, 3 terminales de soldar (3p, 4.7 mm) | MTS-102 (ON-ON), Versión PCB recta, Versión PCB 90° (MTS-102-C4) | muy alta |
| **Interruptor de palanca MTS-101 (SPST ON-OFF, 2 terminales)**<br><sub>`emc-toggle-mts101`</sub> | panel | Panel, 2 terminales de soldar (2p, 4.7 mm) | MTS-101 (ON-OFF) | alta |
| **Interruptor de palanca MTS-103 (SPDT ON-OFF-ON, 3 terminales)**<br><sub>`emc-toggle-mts103`</sub> | panel | Panel, 3 terminales de soldar (3p, 4.7 mm) | MTS-103 (ON-OFF-ON), MTS-113 / MTS-123 (momentáneo (ON)-OFF-(ON), según marca) | alta |
| **Interruptor de palanca MTS-202 (DPDT ON-ON, 6 terminales)**<br><sub>`emc-toggle-mts202`</sub> | panel | Panel, 6 terminales (2 filas de 3) (6p, 4.7 mm, filas 4.7 mm) | MTS-201 (DPST ON-OFF), MTS-202 (DPDT ON-ON) | alta |
| **Interruptor de palanca MTS-203 (DPDT ON-OFF-ON, 6 terminales)**<br><sub>`emc-toggle-mts203`</sub> | panel | Panel, 6 terminales (2 filas de 3) (6p, 4.7 mm, filas 4.7 mm) | MTS-203 (ON-OFF-ON), MTS-223 ((ON)-OFF-(ON) momentáneo) | media |
| **Interruptor de palanca tipo avión con tapa de seguridad 12 V 20 A (con LED)**<br><sub>`emc-toggle-avion-12v`</sub> | panel | Panel 12 mm, 3 terminales faston (3p) | Rojo, Azul, Verde, Amarillo | media |
| **Micro switch / interruptor de límite KW11 (palanca, rodillo o botón)**<br><sub>`emc-microswitch-kw11`</sub> | panel | Cuerpo tipo V (KW11), 3 terminales (3p) | Sin palanca (botón), Palanca corta, Palanca larga, Palanca con rodillo, Terminales faston / soldar / PCB | muy alta |
| **Micro switch miniatura KW10 / KW12 (tipo SS, 20 x 10 mm)**<br><sub>`emc-microswitch-kw10-mini`</sub> | THT | Cuerpo tipo SS, 3 terminales (3p) | Botón, Palanca recta, Palanca con rodillo, Palanca de arco | alta |
| **Interruptor de límite industrial (ME-8104 / ME-8108 / TZ-8108)**<br><sub>`emc-limit-switch-industrial`</sub> | panel | Caja metálica, 4 terminales de tornillo (4p) | ME-8104 (palanca rodillo), ME-8108 (rodillo ajustable), ME-8107 (varilla) | media |
| **Reed switch de vidrio (ampolla 2 x 14 mm)**<br><sub>`emc-reed-switch`</sub> | THT | Axial (ampolla de vidrio) (2p) | 2x14 mm NA, 2.5x14 mm, 3x20 mm, Versión NC / conmutada (3 terminales) | alta |
| **Relevador Songle SRD-05VDC-SL-C (bobina 5 V, 10 A)**<br><sub>`emc-relevador-srd-05vdc`</sub> | THT | THT 5 pines (cuerpo T73) (5p, filas 12.0 mm) | SRD-05VDC-SL-C, SRD-03VDC, SRD-06VDC, SRD-09VDC | muy alta |
| **Relevador automotriz 12 V 30/40 A (4 o 5 terminales)**<br><sub>`emc-relevador-automotriz`</sub> | panel | Cubo ISO mini, terminales faston (5p) | 12 V 30 A 4 pines, 12 V 40 A 5 pines, 24 V, Con base y cables | alta |
| **Relevador Songle SRD-12VDC-SL-C (bobina 12 V, 10 A)**<br><sub>`emc-relevador-srd-12vdc`</sub> | THT | THT 5 pines (cuerpo T73) (5p, filas 12.0 mm) | SRD-12VDC-SL-C, SRD-24VDC-SL-C | alta |
| **Relevador de 2 polos HK19F (DPDT, 8 pines tipo DIP)**<br><sub>`emc-relevador-hk19f-dpdt`</sub> | THT | THT 8 pines (patrón DIP) (8p, 2.54 mm, filas 7.62 mm) | HK19F-DC5V-SHG, HK19F-DC12V-SHG, HK19F-DC3V-SHG | media |
| **Relevador de estado sólido de panel SSR-25DA (tipo Fotek)**<br><sub>`emc-ssr-fotek-25da`</sub> | panel | Cuerpo estándar 'hockey puck', 4 tornillos (4p) | SSR-10DA, SSR-25DA, SSR-40DA, SSR-25AA (control AC), SSR-25DD (salida DC) | media |
| **Relevador miniatura de señal (Omron G5V-1, Hongfa HFD2/HFD23, similares)**<br><sub>`emc-relevador-senal-mini`</sub> | THT | G5V-1 (1 Form C) (6p, 2.54 mm); HFD2 / G5V-2 (2 Form C) (8p, 2.54 mm, filas 7.62 mm) | 5 VCC, 12 VCC, 3 VCC, 24 VCC | media |
| **Relevador reed SIP (SIP-1A05 / SIP-1A12)**<br><sub>`emc-relevador-reed-sip`</sub> | THT | SIP-4 (rejilla 2.54) (4p, 2.54 mm) | SIP-1A05 (5 V), SIP-1A12 (12 V), SIP-1A24 | media |
| **Selector rotatorio de obleas (1P12T, 2P6T, 3P4T, 4P3T)**<br><sub>`emc-selector-rotatorio`</sub> | panel | Panel, terminales en círculo (13p) | 1 polo 12 posiciones, 2 polos 6 posiciones, 3 polos 4 posiciones, 4 polos 3 posiciones | media |
| **Teclado matricial de membrana 4x4 (16 teclas, 8 pines)**<br><sub>`emc-teclado-membrana-4x4`</sub> | modulo | Cinta con conector hembra 1x8, paso 2.54 (8p, 2.54 mm) | 4x4 negro/azul, 4x4 con teclas de colores | muy alta |
| **Teclado matricial de membrana 4x3 (12 teclas, 7 pines)**<br><sub>`emc-teclado-membrana-4x3`</sub> | modulo | Cinta con conector hembra 1x7, paso 2.54 (7p, 2.54 mm) | 4x3 negro | alta |
| **Teclado de 16 botones táctiles 4x4 en placa**<br><sub>`emc-teclado-botones-4x4-placa`</sub> | modulo | Header macho 1x8, paso 2.54 (8p, 2.54 mm) | 4x4 matricial, Versión 1 pin analógico (divisor resistivo) | media |
| **Teclado de membrana 1x4 (4 teclas, 5 pines)**<br><sub>`emc-teclado-membrana-1x4`</sub> | modulo | Cinta con conector hembra 1x5, paso 2.54 (5p, 2.54 mm) | 1x4, 1x5, 2x4 (8 teclas) | media |

<a id="conectores"></a>
## Conectores, bases y portapilas

| Componente | Montaje | Encapsulado / huella | Valores o variantes comunes | Popularidad |
|---|---|---|---|---|
| **Jack DC 5.5 x 2.1 mm para PCB (DC-005, 3 pines)**<br><sub>`con-dc-jack-pcb-2.1`</sub> | THT | DC-005 horizontal, 3 pines tipo pala (3p) | DC-005 negro 2.1 mm, DC-005 2.5 mm, Versión SMD, Versión con tuerca (panel) | muy alta |
| **Plug DC macho 5.5 x 2.1 / 2.5 mm (para soldar o con cable / bornera)**<br><sub>`con-dc-plug`</sub> | n/a | — | 5.5x2.1 para soldar, 5.5x2.5, Con bornera de tornillo, Cable con plug 1 m, Adaptadores 3.5x1.35, 4.0x1.7 | muy alta |
| **Jack DC de panel 5.5 x 2.1 / 2.5 mm con tuerca (DC-022 / DC-099)**<br><sub>`con-dc-jack-panel`</sub> | panel | Panel roscado (3p) | DC-022 plástico, DC-099 metálico, 5.5x2.1, 5.5x2.5 | alta |
| **Jack DC 5.5 x 2.5 mm para PCB**<br><sub>`con-dc-jack-pcb-2.5`</sub> | THT | Horizontal 3 pines (3p) | 5.5 x 2.5 mm | media |
| **Conector RCA hembra para PCB y de panel**<br><sub>`con-rca-hembra`</sub> | THT | RCA PCB 90° sencillo (3p); RCA de panel con tuerca (2p) | PCB sencillo, PCB doble (rojo/blanco), PCB triple (amarillo/blanco/rojo), Panel metálico, Panel dorado | alta |
| **Jack de audio 3.5 mm de panel (con tuerca)**<br><sub>`con-jack-3.5-panel`</sub> | panel | Panel roscado (3p) | Estéreo metálico, Estéreo plástico, Mono | alta |
| **Jack de audio 3.5 mm estéreo para PCB (PJ-307 / PJ-320 / PJ-313)**<br><sub>`con-jack-3.5-pcb`</sub> | THT/SMD | PJ-307 THT, 5 pines (5p); PJ-320 (A=SMD, D=THT), 4 pines (4p) | PJ-307 5P, PJ-320A 4P SMD, PJ-320D 4P THT, PJ-313 5P, Mono 3 pines | alta |
| **Jack de audio 6.3 mm (1/4") mono/estéreo, panel y PCB**<br><sub>`con-jack-6.3`</sub> | panel | Panel tipo abierto (open frame) (3p); PCB encapsulado (5p) | Mono, Estéreo, Con switch, Panel metálico, PCB | alta |
| **Plug de audio 3.5 mm macho para soldar (mono/estéreo)**<br><sub>`con-plug-3.5`</sub> | n/a | — | Mono TS, Estéreo TRS, TRRS (4 polos, micrófono), Metálico, Plástico | alta |
| **Plug RCA macho para soldar**<br><sub>`con-rca-macho`</sub> | n/a | — | Plástico rojo/negro, Metálico, Dorado | alta |
| **Conector XLR 3 pines (macho y hembra)**<br><sub>`con-xlr`</sub> | panel | XLR de panel (tipo D) (3p); XLR de cable (3p) | Macho de cable, Hembra de cable, Macho de panel, Hembra de panel, XLR 4/5 pines (DMX) | media |
| **Base / socket para CI DIP de lámina (6 a 40 pines)**<br><sub>`con-base-dip-lamina`</sub> | THT | Angosta 7.62 mm (DIP-6/8/14/16/18/20/24N/28N) (2.54 mm, filas 7.62 mm); Ancha 15.24 mm (DIP-24/28/40) (2.54 mm, filas 15.24 mm) | DIP-6, DIP-8, DIP-14, DIP-16, DIP-18, DIP-20, DIP-24 angosta/ancha, DIP-28 angosta/ancha, … (+1) | muy alta |
| **Base / socket DIP maquinada (pines torneados)**<br><sub>`con-base-dip-maquinada`</sub> | THT | Angosta 7.62 mm (2.54 mm, filas 7.62 mm); Ancha 15.24 mm (2.54 mm, filas 15.24 mm) | DIP-8, DIP-14, DIP-16, DIP-18, DIP-20, DIP-28, DIP-40 | media |
| **Zócalo ZIF 28 / 40 pines (tipo Textool)**<br><sub>`con-zif`</sub> | THT | ZIF-28 (28p, 2.54 mm, filas 15.24 mm); ZIF-40 (40p, 2.54 mm, filas 15.24 mm) | ZIF-28, ZIF-40, ZIF-14/16/20/24, ZIF-48 (programadores universales) | media |
| **Bornera de tornillo para PCB KF301, paso 5.0 mm (2/3 pines, apilable)**<br><sub>`con-bornera-kf301-5mm`</sub> | THT | KF301-2P (2p, 5.0 mm); KF301-3P (3p, 5.0 mm) | 2P azul, 3P azul, 2P verde, Paquetes de 10 | muy alta |
| **Regleta de clemas de plástico tipo 'chocolate' (12 polos)**<br><sub>`con-clema-chocolate`</sub> | n/a | — | 3 A, 6 A, 10 A, 16 A, 25 A, 12 polos blanco/negro | muy alta |
| **Bornera de tornillo para PCB paso 3.5 mm (KF350 / DG350)**<br><sub>`con-bornera-3.5mm`</sub> | THT | KF350-2P (2p, 3.5 mm); KF350-3P (3p, 3.5 mm) | 2P, 3P, 4P | alta |
| **Conector de palanca para empalme (tipo WAGO 221/222)**<br><sub>`con-conector-palanca-wago`</sub> | n/a | — | 2 vías, 3 vías, 5 vías | alta |
| **Bornera de tornillo de PCB paso 5.08 mm (tipo KF128 / DG128)**<br><sub>`con-bornera-5.08-baja`</sub> | THT | 5.08 mm, N pines (5.08 mm) | 2P, 3P, 4P, 6P, 8P, 12P | media |
| **Bornera enchufable 2EDG / 15EDG (plug + header), paso 5.08 / 3.81 mm**<br><sub>`con-bornera-2edg`</sub> | THT | 2EDGV (header recto) 5.08 mm (5.08 mm); 2EDGR (header 90°) 5.08 mm (5.08 mm); 15EDG 3.81 mm (3.81 mm) | 2P, 3P, 4P, 5P, 6P, 8P, 10P, 12P, … (+2) | media |
| **Regleta de bornes de barrera (barrier strip TB-1503, TB-2504…)**<br><sub>`con-bornera-barrier`</sub> | panel | TB-15xx (15 A); TB-25xx (25 A) | TB-1503 (3 pos), TB-1504, TB-1506, TB-1512, TB-2503, TB-2506, TB-4503 | media |
| **Conectores D-sub DB9 / DB15 / DB25 / HD15 (VGA), macho y hembra**<br><sub>`con-dsub`</sub> | THT | DE-9 (DB9) PCB 90° (9p, 2.77 mm, filas 2.84 mm); DA-15 (DB15) PCB (15p, 2.77 mm, filas 2.84 mm); DB-25 PCB (25p, 2.77 mm, filas 2.84 mm); DE-15 HD (VGA) PCB (15p, 2.29 mm, filas 1.98 mm) | DB9 macho, DB9 hembra, DB25, HD15 VGA, Carcasas plásticas/metálicas, Para soldar cable, PCB 90° | media |
| **Conector FFC/FPC para cable plano flexible (paso 0.5 y 1.0 mm)**<br><sub>`con-ffc-fpc`</sub> | SMD | FPC 0.5 mm, 4–60 pines (0.5 mm); FPC 1.0 mm, 4–30 pines (1.0 mm) | 0.5 mm 24P, 0.5 mm 40P (pantallas TFT), 1.0 mm 15P (cámara Raspberry Pi), 1.0 mm 24P, Adaptadores FPC a 2.54 | media |
| **Tira de pines hembra 1x40, paso 2.54 mm**<br><sub>`con-header-hembra-1x40`</sub> | THT | 1x40 hembra recta, 2.54 mm (40p, 2.54 mm) | 1x40, 1x20, 1x10, 1x8, 1x6, 1x4, 1x3, Altura 8.5 mm estándar, … (+1) | muy alta |
| **Tira de pines macho 1x40 recta, paso 2.54 mm**<br><sub>`con-header-macho-1x40-recto`</sub> | THT | 1x40 recto, 2.54 mm (40p, 2.54 mm) | 1x40 negro, Colores (rojo, azul, amarillo, blanco), Pin largo 15/17/20 mm, Dorado/estañado | muy alta |
| **Header hembra apilable (pin largo) para shields de Arduino**<br><sub>`con-header-hembra-arduino-largo`</sub> | THT | 1x8 apilable, 2.54 mm (8p, 2.54 mm); 1x6 apilable (6p, 2.54 mm); 1x10 apilable (10p, 2.54 mm); 2x3 apilable (ICSP) (6p, 2.54 mm, filas 2.54 mm) | Kit Uno R3 (1x10, 1x8 x2, 1x6), 1x8, 1x6, 2x3 ICSP | alta |
| **Jumper / puente (shunt) para pines 2.54 mm**<br><sub>`con-jumper-shunt`</sub> | n/a | Shunt 2.54 mm, 2 posiciones (2p, 2.54 mm) | 2.54 mm negro/rojo/azul/amarillo, Con lengüeta larga, 2.0 mm | alta |
| **Tira de pines doble fila 2x40 macho / hembra, paso 2.54 mm**<br><sub>`con-header-2x40`</sub> | THT | 2x40 macho recto (80p, 2.54 mm, filas 2.54 mm); 2x40 hembra (80p, 2.54 mm, filas 2.54 mm) | 2x40 macho, 2x40 hembra, 2x40 macho 90°, 2x20 hembra (RPi) | alta |
| **Tira de pines macho 1x40 en ángulo (90°), paso 2.54 mm**<br><sub>`con-header-macho-1x40-90`</sub> | THT | 1x40 90°, 2.54 mm (40p, 2.54 mm) | 1x40 90°, 2x40 90° | alta |
| **Headers paso 1.27 mm (macho y hembra)**<br><sub>`con-header-127mm`</sub> | THT/SMD | 1x40 macho 1.27 mm (40p, 1.27 mm); 2x40 macho 1.27 mm (80p, 1.27 mm, filas 1.27 mm) | 1x40 macho, 1x40 hembra, 2x5 SWD, 2x40 | media |
| **Headers paso 2.0 mm (macho y hembra, 1 y 2 filas)**<br><sub>`con-header-2mm`</sub> | THT | 1x40 macho 2.0 mm (40p, 2.0 mm); 1x40 hembra 2.0 mm (40p, 2.0 mm); 2x40 2.0 mm (80p, 2.0 mm, filas 2.0 mm) | 1x40 macho, 1x40 hembra, 2x40 macho, 1x10 hembra (XBee) | media |
| **Tira de pines torneados/maquinados macho y hembra 2.54 mm**<br><sub>`con-header-maquinado`</sub> | THT | Hembra maquinada 1x40 (40p, 2.54 mm); Macho maquinado 1x40 (40p, 2.54 mm) | 1x40 hembra, 1x40 macho, 2x40 hembra | media |
| **Box header IDC macho 2xN, paso 2.54 mm (6 a 40 pines)**<br><sub>`con-box-header-idc`</sub> | THT | 2x3 (6P) (6p, 2.54 mm, filas 2.54 mm); 2x5 (10P) (10p, 2.54 mm, filas 2.54 mm); 2x7 (14P) (14p, 2.54 mm, filas 2.54 mm); 2x8 (16P) (16p, 2.54 mm, filas 2.54 mm); 2x10 (20P) (20p, 2.54 mm, filas 2.54 mm); 2x13 (26P) (26p, 2.54 mm, filas 2.54 mm); 2x20 (40P) (40p, 2.54 mm, filas 2.54 mm) | 2x3, 2x4, 2x5, 2x7, 2x8, 2x10, 2x13, 2x17, … (+2) | alta |
| **Conector IDC hembra para cable plano (FC-6 a FC-40)**<br><sub>`con-idc-hembra-cable-plano`</sub> | n/a | — | FC-6, FC-8, FC-10, FC-14, FC-16, FC-20, FC-26, FC-34, … (+1) | alta |
| **Ranura / socket microSD para PCB (push-push o bisagra)**<br><sub>`con-microsd-socket`</sub> | SMD | microSD push-push SMD (9p, 1.1 mm) | Push-push, Bisagra (hinge), Push-pull | media |
| **Ranura / socket SD tamaño completo para PCB**<br><sub>`con-sd-socket`</sub> | SMD | SD SMD/THT (11p) | Push-push, Normal | media |
| **Broche para pila de 9 V (con cables o con terminales para PCB)**<br><sub>`con-broche-9v`</sub> | n/a | Broche con terminales para PCB (2p) | Suave con cables 15 cm, Rígido tipo T, Con plug DC 5.5x2.1 (Arduino), Portapila 9V con tapa e interruptor | muy alta |
| **Portapilas AA (x1, x2, x3, x4, x6, x8; con cables, con tapa e interruptor)**<br><sub>`con-portapilas-aa`</sub> | n/a | Portapilas con cables (2p); Portapilas para PCB (1xAA, 2xAA) (2p) | 1xAA (1.5 V), 2xAA (3 V), 3xAA (4.5 V), 4xAA (6 V), 6xAA (9 V), 8xAA (12 V), Con tapa e interruptor, Con broche 9 V | muy alta |
| **Portapila para batería de botón CR2032 (THT / SMD)**<br><sub>`con-portapila-cr2032`</sub> | THT/SMD | THT horizontal (2 pines) (2p); SMD (2p) | CR2032 THT, CR2032 SMD, CR2025/CR2016, CR1220 (12 mm), Con cables | alta |
| **Portapilas 18650 (x1, x2, x3, x4; con cables o para PCB)**<br><sub>`con-portapilas-18650`</sub> | THT | 1x18650 para PCB (2 pines) (2p); Portapilas con cables (2p) | 1x18650, 2x18650 serie, 2x18650 paralelo, 3x18650, 4x18650, Con pines para PCB | alta |
| **Portapilas AAA (x2, x3, x4; con cables o caja con interruptor)**<br><sub>`con-portapilas-aaa`</sub> | n/a | Portapilas con cables (2p) | 2xAAA (3 V), 3xAAA (4.5 V), 4xAAA (6 V), Caja con interruptor | alta |
| **Conector XT60 (macho/hembra)**<br><sub>`con-xt60`</sub> | n/a | XT60PW (PCB horizontal) (5p) | Par macho-hembra, XT60H con capuchón, Con cable 12 AWG, XT60PW para PCB | alta |
| **Conector Deans / tipo T (macho/hembra)**<br><sub>`con-deans-t`</sub> | n/a | — | Par macho-hembra, Con cable | media |
| **Conector JST-RCY / BEC rojo de 2 pines**<br><sub>`con-jst-rcy`</sub> | n/a | — | Par macho-hembra con cable 10–15 cm | media |
| **Conector XT30 (macho/hembra)**<br><sub>`con-xt30`</sub> | n/a | XT30PW (PCB) (4p) | Par macho-hembra, Con cable 16 AWG, XT30PW | media |
| **Pinza caimán con funda (caimanes)**<br><sub>`con-caiman`</sub> | n/a | — | Chico (~28 mm), Mediano (~35 mm), Grande (~50 mm), Para batería (5–100 A), Rojo/negro, Mini gancho de prueba (grabber) | muy alta |
| **Borne de conexión / binding post con hembra banana 4 mm**<br><sub>`con-binding-post`</sub> | panel | Panel con tuerca (1p) | Rojo, Negro, Verde (tierra), Hembra banana simple de panel | alta |
| **Conector banana macho 4 mm**<br><sub>`con-banana-macho`</sub> | n/a | — | Rojo, Negro, Apilable, Para soldar o tornillo, Mini banana 2 mm | alta |
| **Puntas de prueba para multímetro (test leads)**<br><sub>`con-punta-prueba`</sub> | n/a | — | Punta fina, Punta con funda (CAT III), Con caimanes intercambiables, Silicón flexible | alta |
| **Conector RJ11 / RJ12 hembra para PCB (6P4C / 6P6C)**<br><sub>`con-rj11`</sub> | THT | RJ11 90° THT (4p, 1.02 mm) | 6P4C, 6P6C, 4P4C (auricular) | media |
| **Conector RJ45 con magnéticos y LEDs HR911105A**<br><sub>`con-rj45-hr911105a`</sub> | THT | RJ45 MagJack 90°, 12 pines + blindaje (14p) | HR911105A, HR911103A, HR911130C | media |
| **Conector RJ45 hembra para PCB (sin magnéticos)**<br><sub>`con-rj45-pcb`</sub> | THT | RJ45 90° THT 8 pines (8p, 1.02 mm) | 90° sin blindaje, 90° con blindaje, Vertical | media |
| **Conector BNC hembra (panel y PCB) y macho**<br><sub>`con-bnc`</sub> | panel | BNC hembra de panel (2p); BNC hembra PCB 90° (3p) | 50 Ω (RG-58), 75 Ω (RG-59 CCTV), Panel, PCB 90°, Macho de compresión/crimpar | media |
| **Conector SMA hembra para PCB y de panel (antenas)**<br><sub>`con-sma`</sub> | THT | SMA vertical THT (5 pines) (5p); SMA de borde de placa (edge mount) (3p) | SMA hembra vertical, SMA de borde, SMA de panel con pigtail U.FL, RP-SMA (WiFi) | media |
| **Conector U.FL / IPEX (MHF1) SMD**<br><sub>`con-ufl-ipex`</sub> | SMD | U.FL SMD (3p) | U.FL SMD, Pigtail U.FL a SMA 10–20 cm | media |
| **Terminal faston hembra 2.8 / 4.8 / 6.3 mm (aislada y desnuda)**<br><sub>`con-faston-hembra`</sub> | n/a | — | 2.8 mm, 4.8 mm (0.187"), 6.3 mm (0.250"), Aislada roja (22–18 AWG), Aislada azul (16–14 AWG), Aislada amarilla (12–10 AWG), Desnuda + funda | muy alta |
| **Terminal faston macho y lengüeta para PCB (4.8 / 6.3 mm)**<br><sub>`con-faston-macho`</sub> | THT | Lengüeta 6.3 mm para PCB (2 patas) (2p); Lengüeta 4.8 mm para PCB (2p) | 4.8 mm, 6.3 mm, Para crimpar aislado, Para PCB | alta |
| **Terminales de ojillo (anillo) y horquilla para crimpar**<br><sub>`con-terminal-ojillo-horquilla`</sub> | n/a | — | Ojillo M3, M4, M5, M6, M8, Horquilla M3/M4, Aislada roja/azul/amarilla, Desnuda de cobre estañado | alta |
| **Punteras / terminales tubulares aislados (ferrules)**<br><sub>`con-puntera-ferrule`</sub> | n/a | — | 0.5 mm², 0.75 mm², 1.0 mm², 1.5 mm², 2.5 mm², Kits de 400–1200 pzs | media |
| **Conector Micro-USB hembra (SMD / THT)**<br><sub>`con-micro-usb`</sub> | SMD | Micro-B SMD (5p, 0.65 mm); Micro-B DIP (todos THT) (5p, 0.65 mm) | SMD 5 pines con anclaje THT, DIP, Breakout en placa | alta |
| **Conector USB tipo A hembra para PCB (THT 90°)**<br><sub>`con-usb-a-hembra-pcb`</sub> | THT | USB-A 90° THT (6p) | 90° THT, Vertical, Doble apilado, SMD | alta |
| **Conector USB-C hembra 16 pines (USB 2.0)**<br><sub>`con-usb-c-16p`</sub> | SMD | USB-C 16P SMD + anclajes THT (16p, 0.5 mm) | 16P SMD, 24P (completo, USB 3.x) | alta |
| **Conector USB-C hembra 6 pines (solo carga)**<br><sub>`con-usb-c-6p`</sub> | SMD | USB-C 6P SMD con anclajes THT (6p) | 6P SMD, 6P vertical, 2P (solo VBUS/GND, no recomendado) | alta |
| **Conector Mini-USB hembra (SMD con anclajes)**<br><sub>`con-mini-usb`</sub> | SMD | Mini-B SMD (5p, 0.8 mm) | SMD 5 pines, Versión DIP/THT | media |
| **Conector USB tipo A macho (para soldar / para PCB)**<br><sub>`con-usb-a-macho`</sub> | THT | USB-A macho THT (6p) | Para soldar con carcasa, Para PCB 90° | media |
| **Conector USB tipo B hembra para PCB (THT)**<br><sub>`con-usb-b-hembra-pcb`</sub> | THT | USB-B 90° THT (6p, 2.5 mm, filas 2.0 mm) | 90° THT, Vertical | media |
| **Conector JST-XH paso 2.5 mm (2 a 8 pines)**<br><sub>`con-jst-xh`</sub> | THT | Header vertical B#B-XH-A (2.5 mm); Header 90° S#B-XH-A (2.5 mm) | 2P, 3P, 4P, 5P, 6P, 7P, 8P, Con cable precrimpado 15/20/30 cm, … (+1) | muy alta |
| **Carcasas Dupont 2.54 mm (1 a 10 pines, 1 y 2 filas)**<br><sub>`con-dupont-carcasa`</sub> | n/a | 1xN (N=1..10) (2.54 mm); 2xN (2x2..2x10) (2.54 mm, filas 2.54 mm) | 1P, 2P, 3P, 4P, 5P, 6P, 8P, 10P, … (+5) | alta |
| **Conector de batería JST-PH 2 pines (para LiPo 1S)**<br><sub>`con-jst-ph-lipo`</sub> | THT/SMD | Header B2B-PH-K (vertical) o S2B-PH-SM4 (SMD) (2p, 2.0 mm) | 2P con cable rojo/negro 10–15 cm, Header vertical, Header 90° SMD | alta |
| **Conector JST-PH paso 2.0 mm (2 a 6 pines)**<br><sub>`con-jst-ph`</sub> | THT/SMD | Header vertical B#B-PH-K (2.0 mm); Header SMD 90° S#B-PH-SM4 (2.0 mm) | 2P, 3P, 4P, 5P, 6P, Con cable precrimpado | alta |
| **Conector tipo Molex KK 2.54 / KF2510**<br><sub>`con-molex-kk-kf2510`</sub> | THT | Header recto KF2510-NA (2.54 mm); Header 90° KF2510-NAW (2.54 mm) | 2P, 3P, 4P, 5P, 6P, 8P, 10P, 12P | alta |
| **Terminales Dupont para crimpar (macho y hembra)**<br><sub>`con-dupont-terminal`</sub> | n/a | — | Hembra, Macho, Para cable 22–28 AWG | alta |
| **Conector JST-SH paso 1.0 mm (Qwiic / STEMMA QT)**<br><sub>`con-jst-sh`</sub> | SMD | SMD 90° SM#B-SRSS-TB (1.0 mm) | 2P, 3P, 4P (Qwiic), 6P, Cables 4P precrimpados | media |
| **Conector Molex Mini-Fit Jr 4.2 mm (ATX / EPS / PCIe)**<br><sub>`con-molex-minifit-jr`</sub> | THT | Header 2xN recto (5566) / 90° (5569) (4.2 mm, filas 4.2 mm) | 2x2 (EPS 4P), 2x3 (PCIe 6P), 2x4, 2x10 (ATX 20P), 2x12 (ATX 24P) | media |
| **Conector JST-SM 2.5 mm (cable a cable, tiras LED)**<br><sub>`con-jst-sm`</sub> | n/a | — | 2P, 3P, 4P, 5P, Par macho-hembra con cable 15 cm | alta |

<a id="cables"></a>
## Cables y alambres

| Componente | Montaje | Encapsulado / huella | Valores o variantes comunes | Popularidad |
|---|---|---|---|---|
| **Tubo termocontráctil (termofit) 2:1, kits y por metro**<br><sub>`cab-tubo-termocontractil`</sub> | n/a | — | Ø 1, 1.5, 2, 2.5, 3, 4, 5, 6, 8, 10, 12, 20 mm, Kit 127/328/530 pzs, Negro, rojo, transparente, colores, Con adhesivo 3:1 | muy alta |
| **Alambre de cobre desnudo / estañado para puentes (bus wire)**<br><sub>`cab-cobre-desnudo-estanado`</sub> | n/a | — | 18 AWG, 20 AWG, 22 AWG, 24 AWG, Carrete o por metro | media |
| **Alambre magneto / alambre esmaltado (AWG 18 a 40)**<br><sub>`cab-alambre-magneto`</sub> | n/a | — | 18 AWG, 20 AWG, 22 AWG, 24 AWG, 26 AWG, 28 AWG, 30 AWG, 32 AWG, … (+7) | alta |
| **Cable blindado de audio / micrófono (1 o 2 conductores + malla)**<br><sub>`cab-blindado-audio`</sub> | n/a | — | 1 conductor + malla (mono), 2 conductores + malla (balanceado/estéreo), Cable de micrófono negro por metro, Multipar | alta |
| **Cable dúplex polarizado (cable de bocina rojo/negro)**<br><sub>`cab-duplex-polarizado`</sub> | n/a | — | 2x22 AWG, 2x20 AWG, 2x18 AWG, 2x16 AWG, 2x14 AWG, Rojo/negro, Transparente con traza, Por metro o rollo | muy alta |
| **Cable flexible de conexión (cable de un conductor) 18–30 AWG**<br><sub>`cab-flexible-calibres`</sub> | n/a | — | 18 AWG, 20 AWG, 22 AWG, 24 AWG, 26 AWG, 28 AWG, 30 AWG, Colores rojo/negro/azul/verde/amarillo/blanco, … (+1) | muy alta |
| **Cable sólido calibre 22 AWG para protoboard (carrete, colores)**<br><sub>`cab-solido-22awg`</sub> | n/a | — | 22 AWG rojo, negro, azul, verde, amarillo, blanco, Carrete 5–30 m, Kit de 6 colores, … (+1) | muy alta |
| **Cable de silicón ultraflexible (alta temperatura / alta corriente) 10–30 AWG**<br><sub>`cab-silicon`</sub> | n/a | — | 10 AWG, 12 AWG, 14 AWG, 16 AWG, 18 AWG, 20 AWG, 22 AWG, 24 AWG, … (+5) | alta |
| **Cable de uso rudo / cable POT 2x18–2x12 (127 V)**<br><sub>`cab-uso-rudo`</sub> | n/a | — | 2x18 AWG, 2x16 AWG, 2x14 AWG, 3x18 AWG (con tierra), Por metro | alta |
| **Cable multiconductor de control / alarma (2, 4, 6, 8 hilos 22 AWG)**<br><sub>`cab-multiconductor-alarma`</sub> | n/a | — | 2x22 AWG, 4x22 AWG, 6x22 AWG, 8x22 AWG, Con blindaje, Por metro | media |
| **Cable wire-wrap 30 AWG (Kynar) y herramienta**<br><sub>`cab-wire-wrap`</sub> | n/a | — | 30 AWG azul/rojo/amarillo/blanco/negro, Carrete 8–300 m, Herramienta WSU-30M (pelar, enrollar, desenrollar) | media |
| **Cable UTP Cat5e / Cat6 (4 pares)**<br><sub>`cab-utp`</sub> | n/a | — | Cat5e 24 AWG sólido, Cat6 23 AWG, Patch cord armado 1–10 m, Por metro / caja 305 m, Exterior (con gel o forro negro) | muy alta |
| **Cables USB para placas de desarrollo (A-B, mini, micro, USB-C)**<br><sub>`cab-usb-placas`</sub> | n/a | — | USB A-B 30 cm–1.8 m, USB A-mini B, USB A-micro B, USB A-C, USB C-C | muy alta |
| **Cable plano gris para IDC (10–40 hilos, paso 1.27 mm)**<br><sub>`cab-plano-idc`</sub> | n/a | — | 10 hilos, 14 hilos, 16 hilos, 20 hilos, 26 hilos, 34 hilos, 40 hilos, Por metro | alta |
| **Cable plano arcoíris (de colores) paso 1.27 mm**<br><sub>`cab-plano-arcoiris`</sub> | n/a | — | 10 hilos, 20 hilos, 40 hilos, Por metro | media |
| **Cable plano flexible FFC (paso 0.5 / 1.0 mm)**<br><sub>`cab-ffc-flex`</sub> | n/a | — | 0.5 mm 24P/30P/40P, 1.0 mm 15P (cámara RPi), Largos 5–30 cm, Tipo A / Tipo B | media |
| **Cables con caimanes en ambos extremos (juego de 10)**<br><sub>`cab-caiman-caiman`</sub> | n/a | — | Juego de 10 colores 50 cm, Caimán a banana, Caimán a Dupont macho, Caimán a gancho de prueba | muy alta |
| **Cable coaxial RG-59**<br><sub>`cab-coaxial-rg59`</sub> | n/a | — | RG-59, Por metro, Rollo | alta |
| **Cable coaxial RG-6**<br><sub>`cab-coaxial-rg6`</sub> | n/a | — | RG-6, Por metro, Rollo | alta |
| **Cable coaxial RG-174**<br><sub>`cab-coaxial-rg174`</sub> | n/a | — | RG-174, Por metro, Rollo | media |
| **Cable coaxial RG-58**<br><sub>`cab-coaxial-rg58`</sub> | n/a | — | RG-58, Por metro, Rollo | media |
| **Cables jumper Dupont macho-macho, macho-hembra y hembra-hembra**<br><sub>`cab-jumpers-dupont`</sub> | n/a | — | M-M 10 cm, M-M 20 cm, M-M 30 cm, M-H 10/20/30 cm, H-H 10/20/30 cm, Tira de 40 piezas, Kit de 120 (40 de cada tipo) | muy alta |
| **Kit de jumpers rígidos preformados para protoboard (65 / 140 / 350 piezas)**<br><sub>`cab-jumpers-rigidos-kit`</sub> | n/a | — | 140 piezas (14 longitudes), 350 piezas, 65 piezas flexibles con punta | alta |

<a id="mecanicos"></a>
## Mecánicos (disipadores, separadores, gabinetes)

| Componente | Montaje | Encapsulado / huella | Valores o variantes comunes | Popularidad |
|---|---|---|---|---|
| **Cintillos plásticos (cinchos / abrazaderas) y bases adhesivas**<br><sub>`mec-cintillos`</sub> | n/a | — | 2.5 x 100 mm, 3.6 x 150 mm, 3.6 x 200 mm, 4.8 x 200 mm, 4.8 x 300 mm, Negros (UV), Blancos, Base adhesiva 20x20 mm, … (+1) | muy alta |
| **Ojillos / pasacables de goma (grommets)**<br><sub>`mec-ojillos-pasacables`</sub> | panel | — | Para agujero 6, 8, 10, 12, 14, 16, 20 mm, Kits surtidos | media |
| **Patas de goma / topes adhesivos para gabinetes y PCB**<br><sub>`mec-patas-goma`</sub> | n/a | — | Ø 8, 10, 12, 16, 20 mm, Transparentes, Negras, Con tornillo | media |
| **Prensaestopas / conector de cable impermeable (PG7, PG9, PG11, PG13.5)**<br><sub>`mec-prensaestopas`</sub> | panel | PG7; PG9; PG11; PG13.5 | PG7, PG9, PG11, PG13.5, PG16, Métricos M12/M16/M20, Nylon negro/gris | media |
| **Kit aislante para TO-220 / TO-247 (mica o silicón + buje)**<br><sub>`mec-kit-aislante-to220`</sub> | n/a | — | Mica TO-220, Silicón TO-220, Mica TO-247/TO-3P, Buje para M3, Kits de 100 | alta |
| **Pasta térmica / grasa de silicón**<br><sub>`mec-pasta-termica`</sub> | n/a | — | Jeringa 1–30 g, Frasco, Blanca de silicón, Gris de alto rendimiento | alta |
| **Kit aislante para TO-3 (mica + 2 bujes)**<br><sub>`mec-kit-aislante-to3`</sub> | n/a | — | Mica TO-3, Silicón TO-3 | media |
| **Capuchones para botones táctiles 12x12 y 6x6**<br><sub>`mec-capuchon-boton`</sub> | n/a | — | Redondo A24 para 12x12 (rojo/azul/amarillo/verde/negro/blanco/gris), Cuadrado para 12x12, Para 6x6 vástago cuadrado/redondo, Kits surtidos | alta |
| **Disipador pequeño para TO-220 con clip o tornillo (tipo U / aleta)**<br><sub>`mec-disipador-to220-clip`</sub> | THT | Aleta en U estampada; Extruido con aletas y pines para PCB (2p) | 20 x 15 x 10 mm, 21 x 15 x 11 mm, 25 x 23 x 16 mm, 30 x 25 x 12 mm, Con clip, Con 2 pines para PCB, Negro anodizado / natural | muy alta |
| **Disipador extruido grande para TO-220/TO-247 (perfil de aluminio)**<br><sub>`mec-disipador-to220-grande`</sub> | panel | Perfil extruido | 40 mm, 60 mm, 100 mm, 150 mm, Con ventilador | alta |
| **Disipadores adhesivos para chips (Raspberry Pi, drivers A4988, reguladores)**<br><sub>`mec-disipador-chip`</sub> | n/a | Adhesivo | Kit Raspberry Pi (3 pzs), 8.8x8.8 mm para A4988/DRV8825, 14x14 mm, 40x40 mm, Cobre | alta |
| **Disipador para encapsulado TO-3**<br><sub>`mec-disipador-to3`</sub> | panel | Patrón TO-3 (2p) | Para 1 TO-3, Para 2 TO-3, Negro anodizado | media |
| **Disipador para TO-247 / TO-3P**<br><sub>`mec-disipador-to247`</sub> | THT | Patrón TO-247 (3p, 5.45 mm) | Para 1 TO-247, Perfil para varios | media |
| **Gabinetes / cajas de plástico para proyectos**<br><sub>`mec-gabinete-proyecto`</sub> | panel | Caja ABS | Chica (pila 9 V), Mediana, Grande, Negra, Gris, Transparente, Con tapa de aluminio | alta |
| **Caja estanca IP65 (registro hermético)**<br><sub>`mec-caja-estanca-ip65`</sub> | panel | Caja IP65 | 83x58x33, 100x68x50, 115x90x55, 158x90x60, 200x120x75, Tapa transparente | media |
| **Riel DIN 35 mm y accesorios (soportes para PCB en riel DIN)**<br><sub>`mec-riel-din`</sub> | panel | TS35 x 7.5 mm | TS35 7.5 mm, TS35 15 mm, Tope final, Soporte para PCB, Borneras para riel DIN (UK2.5B) | media |
| **Perillas para potenciómetro (eje 6 mm estriado, liso o D)**<br><sub>`mec-perilla-potenciometro`</sub> | n/a | — | Para eje estriado 6 mm (18 dientes, a presión), Para eje liso 6 mm (con tornillo prisionero), Para eje D 6 mm, Para eje 1/4" (6.35 mm), Ø 15–40 mm, Negra con marcador, Aluminio, Tipo Davies (plástico) | alta |
| **Porta LED / bisel para LED de 3 y 5 mm**<br><sub>`mec-portaled-bisel`</sub> | panel | Plástico 2 piezas; Metálico cromado con tuerca | 3 mm negro, 5 mm negro, Metálico 3 mm, Metálico 5 mm | media |
| **Separadores / postes hexagonales de latón M3 (macho-hembra y hembra-hembra)**<br><sub>`mec-separador-laton-m3`</sub> | n/a | Hexagonal M3 | M3 x 5, M3 x 6, M3 x 8, M3 x 10, M3 x 12, M3 x 15, M3 x 20, M3 x 25, … (+5) | alta |
| **Separadores de nylon M2.5 / M3 (kits para Raspberry Pi)**<br><sub>`mec-separador-nylon`</sub> | n/a | Hexagonal M2.5 / M3 nylon | Kit M2.5 (300 pzs), Kit M3, Negro, Blanco | alta |
| **Soportes plásticos para PCB (snap-in y autoadheribles)**<br><sub>`mec-soporte-pcb-plastico`</sub> | n/a | Snap-in con base adhesiva | 6 mm, 10 mm, 12 mm, 16 mm, 20 mm, 25 mm, Con adhesivo, Doble snap-in | media |
| **Tornillos, tuercas y rondanas M3**<br><sub>`mec-tornilleria-m3`</sub> | n/a | M3 | M3 x 6, M3 x 8, M3 x 10, M3 x 12, M3 x 16, M3 x 20, M3 x 30, Tuerca hexagonal, … (+3) | muy alta |
| **Tornillos y tuercas M2 / M2.5**<br><sub>`mec-tornilleria-m2-m2.5`</sub> | n/a | M2.5; M2 | M2 x 5, M2 x 8, M2.5 x 6, M2.5 x 10, Kits surtidos | media |

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
