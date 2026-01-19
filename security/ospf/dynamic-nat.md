enable
configure terminal

! Configuración de interfaces
interface gi0/0
 ip nat inside
exit

interface gi0/1
 ip nat outside
exit

! Lista de acceso para definir qué IPs internas se traducen - esto = ip nat inside
access-list 1 permit 10.0.0.0 0.255.255.255

! Pool de IPs públicas para NAT dinámica es un rang de ips a las que se traducen
ip nat pool NATDinamica 20.0.0.3 20.0.0.6 netmask 255.255.255.0

! Aplicación del NAT dinámico
ip nat inside source list 1 pool NATDinamica