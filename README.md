# Casa Iscali

## contenido
<details>
  <summary>Tabla contenidos</summary>
  <ol>
    <li>
      <a href="#acerca-del-proyecto">Acerca Del Proyecto</a>
      <ul>
        <li><a href="#construido-con">Construido Con</a></li>
      </ul>
    </li>
    <li>
      <a href="#iniciando">Iniciando</a>
      <ul>
        <li><a href="#requisitos">Prerrequisitos</a></li>
        <li><a href="#instalacion">Instalación</a></li>
      </ul>
    </li>
    <li><a href="#uso">Uso</a></li>
    <li><a href="#guias">Guias</a></li>
    <li><a href="#contribucion">Contribución</a></li>
    <li><a href="#licencia">licencia</a></li>
    <li><a href="#contacto">Contacto</a></li>
    <li><a href="#participantes">Participantes</a></li>
    <li><a href="#referencias">Referencias</a></li>
  </ol>
</details>

<!-- Acerca del proyecto -->
## Acerca del proyecto

### Nombre del proyecto
**Casa Iscali**

### Justificación del proyecto

<div style="text-align: justify;">

> El servicio al cliente es lo primordial de un servicio y que mejor manera que pueda acceder a el desde cualquier parte del mundo a cualquier hora del dia o noche.

> En Casa Iscali podemos ver que la cantidad de nuestros clientes han aumentado y la forma en que ellos necesitan ser atendidos necesita un cambio de ahi la necesidad de crear una pagina web como una nueva forma para que nuestros clientes obtengan información rapido y desde la comodidad de su hogar, trabajo o cualquier lugar donde se encuentren. 

>Dolores hidalgo es una ciudad donde se puede apreciar que le crecimiento de su pobloacion y necesidaddes estan en un punto importante y los poryectos como Casa Iscali necesitan adaptarse a la formas actuales de darse a conocer al publico, la forma de brindar servicios y como mejorar los servicios que otros proyectos(competidores) o lugares ofrecen. Sabemos que en la actulidad las paginas web son un elemento inprecindible cuando de promocionarse y llevar un registro de los clientes se habla. 

>La pagina web brindara a nuestros usuarios una forma mas rapida para crear una reservaciones, algo importante de la creacion de la pagina web es para que la persona que esta encargada de Casa Iscali tenga una forma mas sencilla de llevar el registro de reservaciones, citas y pueda publicar promociones, los servicios que ofrecen en Casa Iscali y los eventos que se celebran para mejorar la experiencia de los clientes. Casa Iscali tambien necesita que mas gente la conozca y la pagina web puede hacer que el crecimeitno sea aun mayor del que tiene actualmente.  
</div>

### Objetivo del proyecto: 

> Crear una pagina web para mejorar la experiencia y los resultados de la asistencia de los clientes de "Casa Iscali", mostrando eventos, promociones, los servicios que se ofrecen y productos, permitiendole tambien al proyecto crecer como empresa, asi tambien como facilitar la labor de los administradores de Casa Iscali. Sabiendo que los clientes ahora se rigen mucho por lo que encuntran en Internet la creacion de la pagina web intenta dar un salto para la administracion de reservaciones(citas) con los prefesionales que conforman Casa Iscali. 

### Descripción general del proyecto

> Se creará un circuito que permitirá medir la temperatura en la sala de masajes para tener un control de la misma y que el cliente tenga la mejor experiencia, buscando tambine optimiazar funcionamiento de establecimiento.Ademas se creará una página web, el la cual se explicara sobre el establecimiento y sus funciones, es decir; sala de masajes y una consultoría de psicología, asi mismo, en la página web se podrán hacer reservaciones(citas) para la consultoría y los masajes, se podrá ver un calendario donde se verán las reservaciones y poder seleccionar el día que esté disponible o sea más cómodo asistir. Además, se crearán secciones para mostrar el trabajo que han realizado estos profesionales, su trayectoria e inicios y como último requisito se creara una sección donde se mostrara el trabajo de un diseñador digital, pintor y profesor de arte que imparte clases los fines de semana. Se añadirán las diferentes formas de contactar a estos profesionales.



### Material de uso:
<table> <tr> <th>Componente</th><th>Imagen</th><th>Descripción</th><th>Cantidad</th></tr>
  <tr>
    <td> Placa Arduino UNO</td>
    <td>
    <img src="https://m.media-amazon.com/images/I/71z22cRPeeL.jpg" alt="Placa Arduino UNO" width="100"/>
    </td>
     <td><ul>
      <li>Microcontrolador: ATMega328P.
      <li>Velocidad de reloj: 16 MHz.
      <li>Voltaje de trabajo: 5V.
      <li>Voltaje de entrada: 7,5 a 12 voltios.
      <li>Pinout: 14 pines digitales (6 PWM)  y 6 pines analógicos.
      <li>1 puerto serie por hardware.
      <li>Memoria: 32 KB Flash (0,5 para bootloader), 2KB RAM y 1KB Eeprom
       </ul></td>
    <td>1</td>
  </tr> 
  <tr>
    <td>Sensor de temperatura LM35</td>
    <td>
    <img src="https://natytec.com.mx/wp-content/uploads/2018/10/lm35dz.jpg"  alt="ESP32 Cam" width="100"/>
    </td>
    <td><ul>
      <li>Modelo: LM35
      <li>Voltaje de alimentación: 4V – 30V (5V recomendado)
      <li>Rango de sensado temperatura: -55℃ hasta +150℃
      <li>Precisión en el rango de -10°C hasta +85°C: ±0.5°C
      <li>Pendiente: 10mV/ºC
      <li>Bajo consumo energético: 60uA
      <li>No necesita componentes adicionales
      <li>Pines: +VCC, V salida, GND
      <li>Baja impedancia de salida
    </ul></td>
    <td>1</td>
  </tr> 
  <tr>
    <td>Display LCD 16x2</td>
    <td><img src="https://user-images.githubusercontent.com/8560750/166756741-813b8a4a-d952-4e20-aa89-b7699ffeb30d.jpg" alt="Lcd Display" width="100"/></td>
    <td>
      <ul>
        <li>Voltaje: 5 V</li>
        <li>Un pin de selección de registro (RS) que controla en qué parte de la memoria de la pantalla LCD está escribiendo datos. </li>
        <li>Un pin de lectura/escritura (R/W) que selecciona el modo de lectura o el modo de escritura</li>
        <li>Un pin Habilitar que permite escribir en los registros</li>
        <li>8 pines de datos (D0 -D7) . Los estados de estos pines (alto o bajo) son los bits que estás escribiendo en un registro cuando escribes, o los valores que estás leyendo cuando lees,</li>
      </ul>
    </td>
    <td>1</td>
  </tr> 
  <tr>
    <td>Cables </td>
    <td><img src="https://leantec.es/wp-content/uploads/2018/02/p_6_8_1_681-40-CABLES-MACHO-HEMBRA-10cm-jumpers-dupont-254-arduino.jpg" width="100" alt="App de realidad aumentada"/></td>
    <td>
      <ul>
        <li>Conectores tipo A y B que cumplen con el estándar USB
        <li>Excelente conductividad eléctrica
        <li>Aproximadamente 20 cm de largo
        <li>Ideal para utilizar en en computadoras portátiles debido a su longitud
        <li>Elaborado en plástico color azul translucido
        <li>Compatible con cualquier otro periférico o dispositivo USB que tenga los mismos conectores
        </ul>    
    </td>
    <td>2 </td>
  </tr>
  <tr>
    <td>Modulo wifi </td>
    <td><img src="https://rdteam.mx/wp-content/uploads/2020/11/762365-mla31063767605_062019-o-233358ad17b62cb14815638265858625-640-0.jpg" width="100" alt="Modulo WiFi"/></td>
    <td>
      <ul>
        <li>Procesador de 32 bit de bajo consumo
        <li>Velocidad de 80MHz (máximo de 160MHz)
        <li>32 KiB RAM instrucciones, 32 KiB RAM cache
        <li>80 KiB RAM para datos de usuario
        <li>Memoria flash externa hasta 16MiB
        <li>Pila de TCP/IP integrada
        <li>Wifi 802.11 b/g/n 2.4GHz (soporta WPA/WPA2)
        <li>Certificado por FCC, CE, TELEC, WiFi Alliance y SRRC
        <li>16 pins GPIO
        <li>PWM en todos los pines (10 bits)
        <li>Conversor analógico digital de 10 bits
        <li>UART (2x TX y 1x RX)
        <li>SPI, I2C, I2S
        <li>Voltaje de operación 3.0 a 3.6V
        <li>Consumo medio 80mA
        <li>Modo consumo stand-by (1mW) y deep sleep (1uA).
      </ul>
    </td>
    <td>1</td>
  </tr> 

</table>

#### Requerimientos
|No.  |Requerimiento  |
|---  |-------------  |
| 1   |Eventos: La aplicación web tendra una zona que sera llamada  eventos donde se podran revisar las diferentes planeaciones de Casa Iscali donde se veran los eventos con la fecha y el servicio que se ofrece en el evento. |
| 2   |Servicios: Se tendra de igual forma una zona donde se escribira la información de los servicios que se ofrecen en Casa Iscali enfocado en los masajes donde se podra obtener informacion de su costo, días disponibles para hacer cita, etc.|
| 3   |Historia: Se creara una seccíón donde las personas podran revisar la trayectoria de los profesionales en Casa Iscali, donde se mostraran sus inicios como organización y diefrentes certificaciones, titulos y experiencia que han obtenido a lo largo de la existencia de Casa Iscali.|
| 4   |Zona Psicologia: Casa Iscali cuenta con varios profesionales que desempeñan diferentes tareas una ellas es psicologi, se quiere crear un apartado exclusivo para esto donde se mostrara informacion de servicios, tipo de ayuda que puede ofrecer y costos.|
| 5   |Productos: En Casa Iscali se ofrecen diferentes productos para los tratamientos terapeuticos que son propios de los masajes, se quiere crear una apartado donde se muestron los productos que se venden en Casa Iscali como cremas, pomadas, cafe, etc.|
| 6   |Promociones: Se quiere un apartado donde se estaran dando información de las promociones que Casa Iscali puede ofrecer por ejemplo por día del niño, día de la madre, etc.|
| 7   |Apartados extra: Se creara un partado donde se mostrara información de un diseñador digital, que tambien tiene una cerigrafia, tambien se mostrara información de los costos, paquetes que se ofrecen, etc. |
| 8   |Sensor de Temperatura: Se creara un circuito con Arduino que medira la temperatura de la sala de masajes donde se este guardando esta informacion en una base de datos el circuito busca poder manipular la temperatura del lugar aunque se empezara con solo mostrarla en la pantalla LCD. |

#### Diagrama inicial
![image](https://user-images.githubusercontent.com/97042355/175753575-91ad17fe-b591-4862-919d-2d0b193e136d.png)


### Prototipo
![Captura de pantalla 2022-06-23 222828](https://user-images.githubusercontent.com/97042355/175456470-01a2394a-4d79-475e-8c9b-7b4d02d2bfe8.png)

<!-- Construido con -->


<!-- Construido con -->
### Construido con
Python 3.10.2
Visual Studio Code 
Django
Arduino Uno 
Arduino IDE 

<!-- Iniciando -->
## Iniciando
Iniciando.

<!-- Requisitos -->
### Requisitos
Requisitos.

<!-- Instalación -->
### Instalacion
Instalación.

<!-- Uso -->
### Uso
Uso.

## Guias
Guias.

## contribucion
Contribucion.

## Licencia
Licencia.

## Contacto
<ul>
  <li>Nombre: Pablo Uriel Rosas Vargas
  <li>Correo: urielvargas127@gmail.com
  <li>Num. Celular: 418 139 7629 
</ul>

## Participantes
* [Pablo Uriel Rosas Vargas]()
* [Gabriel Barrón Rodríguez]()
* [Christopher Ivan Garcia Avila]()

[contribuidores-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors

## Referencias
### Imagenes
<ul>
<li>Amazon. (s.f.). Amazon. Obtenido de Google: https://m.media-amazon.com/images/I/71z22cRPeeL.jpg
<li>Github. (s.f.). Github.com. Obtenido de Google: https://user-images.githubusercontent.com/8560750/166756741-813b8a4a-d952-4e20-aa89-b7699ffeb30d.jpg
<li>Leantec. (s.f.). leantec.com. Obtenido de Google: https://leantec.es/wp-content/uploads/2018/02/p_6_8_1_681-40-CABLES-MACHO-HEMBRA-10cm-jumpers-dupont-254-arduino.jpg
<li>ratytec. (s.f.). ratytec.com. Obtenido de Google: https://natytec.com.mx/wp-content/uploads/2018/10/lm35dz.jpg
<li>rdteam. (s.f.). rdteam.mx. Obtenido de Google: https://rdteam.mx/wp-content/uploads/2020/11/762365-mla31063767605_062019-o-233358ad17b62cb14815638265858625-640-0.jpg
</ul>




