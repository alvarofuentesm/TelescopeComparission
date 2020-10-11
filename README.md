# Simple Script for Telescope Comparison

Simple script for easy comparison when buying a telescope.

Script simple para comparar telescopios a la hora de adquirir uno.

## 

TODO: Translate code to english. 

## Examples


### Reflector 76350 SOLARIX 76/350
```python

telescope_A = Telescope(76, 350, "Reflector", "SOLARIX 76/350")
telescope_A.get_all(ocular_list = [20, 4], barlow_list = [2])


=> SOLARIX 76/350 76350 Reflector
Iluminacion respecto al ojo humano: 190.94 veces
Resolucion: 1.53 arcosegundos (''arc)
Aumento máximo práctico 179.5x
F4.6
Aumento proporcionado con ocular 20[mm] es 17.5x
Aumento proporcionado con ocular 4[mm] es 87.5x
Aumento proporcionado con ocular 20[mm] + barlow x2 es 35.0x
Aumento proporcionado con ocular 4[mm] + barlow x2 es 175.0x
```

### Celestron FirstScope
```python
telescope_B = Telescope(76, 300, "Reflector", "Celestron FirstScope")
telescope_B.get_all(ocular_list = [20, 2.4])
```
