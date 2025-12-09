## Cheksum
El checksum es una comparativa, usando una puert (XOR), que indica si:
Cuando es 1, hay llevada para la siguiente columna (tambien cuenta con las llevadas).

El checksum es un valor numérico calculado a partir de una secuencia de datos.
Sirve como una firma o huella: si el dato cambia, el checksum también debería cambiar.

Se suman todos los bytes (o palabras) de los datos.
Se toma el complemento o el resto de esa suma (según el tipo de checksum).
Ese resultado se envía junto con los datos.
En el receptor, se repite el cálculo y se compara el resultado:

- Si coinciden → No hay error.
- Si difieren → Hubo una alteración.
```
0 y 0 = 0
0 y 1 = 1
1 y 0 = 1
1 y 1 = 0
```

**Ejemplo de ejercicio:**
```
1101000100101
1100010101101
0010110011010
-------------

Al final del checksum se invierten los digitos (0 es 1 y 1 es 0)
```

## CRC
El CRC es una técnica más avanzada que el checksum.
Utiliza aritmética polinómica binaria (mod 2) para detectar errores con mayor precisión.
Es muy usado en redes, discos duros, USB, Ethernet, etc.

Se interpreta el mensaje como un polinomio binario.
Se divide ese polinomio por un polinomio generador (G(x)) predefinido.
El resto de esa división es el CRC.
En el receptor, se realiza la misma división:

- Si el resto es 0, los datos están intactos.
- Si no es 0, hubo error.

**Ejemplo de ejercicio:**
```
11011010[10101 (dividido para)
10101
-------
 11100
 10101
-------
 010011
  10101
  ------
  0011000
    10101
    --------
    011010
     10101
     -------
     011110
      10101
      ------
      010110
       10101
       ------
       001100
```