# Casa Iscali
[![Contribuidores][contribuidores-shield]][contributors-url]

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
        <li>
        <li>
        <li>
        <li>
        <li>
        <li>
      </ul>
    </td>
    <td>1</td>
  </tr> 

</table>

#### Requerimientos
|No.  |Requerimiento  |
|---  |-------------  |
| 1   |El sistema deberá permitir dar la bienvenida al cliente o visitante a través de lectura de rostro, si la persona es un cliente mediante un Display y/o un repetidor de Voz dará la bienvenida. A su vez, el empleado recibirá una notificación a su dispositivo móvil para su atención.               |
| 2   |Mediante lectura de código QR a través de dispositivo móvil la persona podrá observar la descripción del producto. |
| 3   |Mediante realidad aumentada a través de dispositivo móvil el cliente o turista podrá interactuar con las características y uso del producto.|
| 4   |La persona podrá solicitar la atención del empleado a través de su dispositivo móvil ya sea para muestra del producto o venta del mismo.|
| 5   |La persona podrá responder la encuesta de salida si fue agradable el servicio al cliente, etc.|
| 6   |El gerente o dueño del negocio podrá ver estadísticas como: Número de visitantes que llegaron al establecimiento. Número de visitantes que realizaron compra. Encuesta de satisfacción de salida.  |

#### Diagrama inicial
![image](https://user-images.githubusercontent.com/8560750/166749650-89fba768-4bbc-45c4-93d3-df9e5d08ad4c.png)


### Prototipo
![Captura de pantalla 2022-06-23 222828](https://user-images.githubusercontent.com/97042355/175456470-01a2394a-4d79-475e-8c9b-7b4d02d2bfe8.png)

<!-- Construido con -->


<!-- Construido con -->
### Construido con
Construido con.

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
Contacto.

## Participantes
Pablo Uriel Rosas Vargas
Christopher Ivan Garcia Avila
