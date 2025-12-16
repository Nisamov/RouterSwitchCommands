# Asiganción de Ruta Estática Por Defecto
Es mas rápido, pero menos seguro.
Permite agregar todas las redes a partir de un punto de forma automática.
Solo puede agregarse en un sentido de la red (generalmente hacia donde hay más redes), tras esto, deben agregarse las restantes de forma manual.

- Habilitar router.
- Aplicación de IP Estática por defecto.
- La IP es el salto hacia el puerto del router al que nos queremos conectar (en este caso nuestro ruter tiene la IP `60.0.0.1` el router objetivo es `60.0.0.2`).
- Asignación manual de la IP `10.0.0.0` con máscara `255.0.0.0`, accediendo a esta por la IP `50.0.0.1`.
```
Router>en
Router#confi t
Router(config)#ip route 0.0.0.0 0.0.0.0 60.0.0.2
Router(config)#ip route 10.0.0.0 255.0.0.0 50.0.0.1
```