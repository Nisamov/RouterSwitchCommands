# NAT PAT overload:

- NAT oculta las IP de los equipos de cara al publico, transforman las IP privada a IP públicas.
- Usa las mismas IP, diferenciando los equipos por puertos, permitiendo 60.000 equipos con la misma IP usando diferentes puertos.
- La NAT siempre se hace de cara al exterior
```prolog
enable
confi t
in gi0/0
ip nat inside
exit
in gi0/1
ip nat outside
exit
access-list 1 permit 10.0.0.0 0.255.255.255
ip nat inside source list 1 interface gi0/1 overload
```