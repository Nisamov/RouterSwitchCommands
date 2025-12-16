# NAT Estática

- La NAT siempre se hace de cara al exterior.
- Se habilita el router.
- Indicación de puerto de entrada y puerto de salida.
```prolog
enable
confi t
in gi0/0
ip nat insisde
in gi0/1
ip nat outside
exit
```
- IP Interna `10.0.0.2`, para conexiones externas, se ve como `20.0.0.3`.
- IP Interna `10.0.0.3`, para conexiones externas, se ve como `20.0.0.4`.
```prolog
ip nat inside source static 10.0.0.2 20.0.0.3
ip nat inside source static 10.0.0.3 20.0.0.4
```
- Mostrar transformación de IPs de interna a externa.
```prolog
Router#show ipnat translations
```
- Eliminar NAT
```prolog
Router(config)#no ip nat inside source static 10.0.0.2 20.0.0.3
```