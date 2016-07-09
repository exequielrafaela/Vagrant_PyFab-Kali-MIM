# Vagrant_PyFab-Kali-MIM
Kali Linux MIM implementation using Vagrant and Python Fabric

Trabajo Final Integrador

El trabajo consiste en aplicar varios conocimientos del curso de Seguridad en Linux de la Diplomatura en OS GNU/Linux de UNC Córdoba.

1) Instalar un servidor web, que acepte conexiones https.

* Utilizar Apache

* Deberá escuchar en el puerto 443

* Emitir certificado autofirmado

* Extra: que el navegador reconozca automáticamente el certificado y no detecte el sitio como sospechoso.

2) Realizar un ataque MitM a un cliente

* El cliente debería acceder de manera transparente  a un sitio, donde realizará un login. Se utilizara un ataque MitM para capturar las credenciales.

Extra: es deseable que el cliente no se de cuenta del ataque. Los navegadores podrian advertirle.

Extra 2: cuando el cliente acceda a un sitio, que sea un sitio fake. Deberá utilizar DHCP, DNS y generar un sitio falso.

3) Crear un script para realizar backups diarios (encriptados) de los servicios configurador. Generar un tar.gz
