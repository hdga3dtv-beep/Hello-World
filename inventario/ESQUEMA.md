# Esquema común para el inventario de componentes

Cada agente escribe UN archivo JSON válido (UTF-8) con esta forma:

```json
{
  "group": "<id del grupo asignado>",
  "sources": ["https://...", "..."],
  "items": [ <componente>, ... ]
}
```

## Forma de cada <componente>

```json
{
  "id": "res-carbon-1-4w",
  "name": "Resistor de película de carbón 1/4 W",
  "aliases": ["resistencia 1/4 W", "CFR-25", "carbon film resistor"],
  "category": "resistores",
  "subcategory": "resistores_fijos",
  "description": "Una o dos frases claras en español.",
  "mounting": "THT",
  "packages": [
    {
      "name": "Axial (DO-35 aprox.)",
      "pins": 2,
      "pitch_mm": 10.16,
      "row_spacing_mm": null,
      "body_mm": "6.3 x 2.4 (largo x diámetro)",
      "lead_diameter_mm": 0.6,
      "notes": "Se dobla a 7.62 mm (0.3 in) o 10.16 mm (0.4 in) en PCB."
    }
  ],
  "pinout": [
    {"pin": "1", "name": "A", "function": "Terminal 1 (sin polaridad)"}
  ],
  "common_values": ["10 Ω", "100 Ω", "220 Ω", "330 Ω", "1 kΩ", "10 kΩ"],
  "specs": {"potencia": "0.25 W", "tolerancia": "±5 %", "voltaje_max": "250 V"},
  "schematic_symbol": "resistor",
  "typical_uses": ["Limitar corriente de LEDs", "Divisores de voltaje", "Pull-up/pull-down"],
  "stores": ["Steren", "AG Electrónica", "UNIT Electronics"],
  "popularity": "muy_alta",
  "price_mxn_approx": "$1–3 c/u",
  "notes": ""
}
```

### Reglas de campos
- `id`: kebab-case, único, ASCII, sin acentos. Prefijo sugerido por grupo (te lo da tu prompt).
- `name`, `description`, `notes`, `typical_uses`: en español.
- `aliases`: números de parte equivalentes, nombres en inglés, nombres coloquiales (p. ej. "resistencia", "foquito LED", "pushbutton").
- `mounting`: uno de `"THT"`, `"SMD"`, `"THT/SMD"`, `"modulo"` (placa ya armada con pines), `"panel"` (montaje en panel/chasis), `"n/a"` (materiales, herramientas, consumibles).
- `packages`: lista (puede ser vacía `[]` para materiales/herramientas). Esto es CRÍTICO para la app de diseño de pistas: da pines, paso entre pines (`pitch_mm`), separación entre filas (`row_spacing_mm`, p. ej. DIP = 7.62), dimensiones del cuerpo y diámetro de terminal cuando se conozcan. Usa `null` si no aplica o no se conoce; NO inventes medidas — si es aproximado dilo en `notes`.
- `pinout`: obligatorio para circuitos integrados, transistores, reguladores, módulos y placas (lista de pines del header). Para componentes de 2 terminales basta indicar polaridad (ánodo/cátodo, +/−) o dejarlo `[]` si no hay polaridad.
- `common_values`: valores/variantes que realmente se encuentran en tienda (resistencias E12, capacitores típicos, calibres, colores, voltajes, etc.).
- `specs`: objeto libre clave→texto (claves en snake_case español).
- `schematic_symbol`: id sugerido de símbolo esquemático. Usa uno de esta lista si encaja, o propone uno nuevo en snake_case:
  resistor, resistor_variable, potenciometro, trimpot, ldr, termistor, varistor, capacitor, capacitor_polarizado, capacitor_variable, inductor, inductor_nucleo, transformador, cristal, fusible, diodo, diodo_zener, diodo_schottky, diodo_tvs, puente_rectificador, led, led_rgb, fotodiodo, fototransistor, optoacoplador, transistor_npn, transistor_pnp, mosfet_n, mosfet_p, jfet_n, scr, triac, diac, ic, regulador, amp_op, compuerta_logica, microcontrolador, modulo, conector, header, bornera, boton, interruptor, interruptor_conmutado, relevador, buzzer, bocina, motor, servo, motor_paso, bateria, tierra, display_7seg, antena, ninguno
- `stores`: tiendas donde típicamente se encuentra (Steren, AG Electrónica, UNIT Electronics, Geek Factory, Electrónica 5Hz, Mercado Libre, tiendas de electrónica locales de la Rep. del Salvador / Centro CDMX, etc.). Si lo verificaste en el sitio de la tienda, mejor.
- `popularity`: `"muy_alta"` (lo tiene casi cualquier tienda/kit de estudiante), `"alta"`, `"media"`.
- `price_mxn_approx`: rango aproximado en pesos mexicanos o `null` si no lo sabes. Nunca inventes; mejor `null`.
