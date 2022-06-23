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

> El mejor servicio al cliente que podemos tener, es no tener la necesidad de usar el servicio al cliente.

> El servicio al cliente bajo la óptica del Internet de las Cosas se vuelve una actividad esencial, automática, proactiva y constante. El mejor servicio al cliente es aquel que logramos visualizar antes que los clientes noten el problema; y para ello, necesitas modificar tus operaciones y flujos de trabajo.

> Dolores Hidalgo se encuentra en la zona norte del estado de Guanajuato, pocas ciudades del país pueden decir que viven completamente de la artesanía. El centro de  Dolores Hidalgo, Guanajuato, encontrarás calles repletas de todo tipo de objetos artesanales cerámicos. Además de ser cuna de la Independencia Nacional, Dolores Hidalgo es una población fantástica donde innumerables alfareros y ceramistas han hecho de la cerámica de talavera su forma de vida al trabajarla en diversas formas  y tonos multicolores que engalanan al México popular país con un hondo espíritu folclórico.
> El principal turista de ocio que llega a la Cuna de la Independencia, es de tipo familiar por el potencial que tenemos en el personaje de José Alfredo Jiménez y la cerámica tipo Talavera, pero una de los grandes incovenientes es que el turista dura en la ciudad de uno a dos días y después se van a otras ciudades como Guanajuato, San Miguel de Allende, San Luis de la Paz. Generalmente, los pequeños negocios de artesanías que comercializan los productos de Talavera contratan a personal femenino para el servicio de atención al cliente, pero una de las grandes inquietudes que tienen los empresarios de los estos comercios es usar la tecnología para atrapar al turista e incrementar sus ventas. 

### Objetivo del proyecto: 

> Mejorar la experiencia y los resultados de la asistencia de los clientes a "Casa Iscali", permitiendole tambien a la organizacion crecer como empresa, asi tambien como facilitar la labor de los empleados de la misma.

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
    <td>Lector QR </td>
    <td><img src="https://user-images.githubusercontent.com/8560750/166768412-b0cddffc-1a08-49cf-a9d5-4d46b3501678.jpg" width="100" alt="Lector de código QR"/> </td>
    <td>
      <ul>
        <li>Dispositivo móvil con sistema operativo Android 8.0 o superior.</li>
        <li>App para lectura de QR.</li>
        <li>Observar detalles y características de producto.</li>
      </ul>
      </td>
    <td>2</td>
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
    <td>ISD1820 </td>
    <td><img src="https://user-images.githubusercontent.com/8560750/166772317-71c55285-568d-478c-aa4a-080df56c719b.jpg" width="100" alt="ISD1820"/></td>
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
* [Gerardo Reyna Ibarra]()
* [Anastasio Rodríguez García]()
* [Gabriel Barrón Rodríguez]()

[contribuidores-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
