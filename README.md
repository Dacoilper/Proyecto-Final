Nombre del estudiante: Oswaldo Villarreal
Materia: LOGICA DE PROGRAMACION 2
Fecha: 1 de marzo de 2026
Actividad: Proyecto Final


EL IMPACTO DE LAS NUEVAS TECNOLOGÍAS EN LA SOCIEDAD: VISUALIZACIÓN DEL FUTURO
Proyecto Integrador

Introducción

Las nuevas tecnologías han transformado de manera profunda la forma en que la sociedad se desarrolla, influyendo en ámbitos como la economía, el empleo, la educación y la vida cotidiana. Si bien estos avances han generado beneficios importantes, también han provocado nuevos riesgos y desafíos sociales que requieren ser analizados de forma responsable.

Este proyecto presenta un simulador interactivo desarrollado en Python que permite visualizar, de manera práctica, cómo el uso de nuevas tecnologías puede generar distintos resultados dependiendo del contexto en el que se implementan. El objetivo principal es fomentar la reflexión sobre el equilibrio entre beneficios tecnológicos y riesgos sociales.

Objetivo del proyecto

Desarrollar un software educativo que permita simular distintos escenarios sociales mediante un videojuego tipo Snake, con el fin de analizar el impacto de la adopción tecnológica y los riesgos asociados a lo largo del tiempo.

Descripción general del software

El proyecto consiste en un videojuego tipo Snake desarrollado con la librería Pygame. En este simulador, el jugador controla un sistema que representa a la sociedad, el cual crece y se desarrolla a medida que interactúa con elementos positivos y negativos dentro del entorno.

Durante la simulación, aparecen tecnologías que representan avances beneficiosos, así como riesgos sociales que simbolizan consecuencias negativas del uso inadecuado o descontrolado de la tecnología. El comportamiento del sistema varía según la dificultad seleccionada al inicio del juego.

Dificultades del simulador

El programa cuenta con tres niveles de dificultad, cada uno representando un contexto social distinto.

En la dificultad Fácil, las tecnologías aparecen con mayor frecuencia y los riesgos son menos comunes. Este escenario representa una sociedad con buena regulación y acceso equilibrado a la tecnología. El fondo del escenario es de color rojo pastel.

En la dificultad Medio, existe un equilibrio entre la aparición de tecnologías y riesgos. Este escenario simboliza una adopción tecnológica moderada, con beneficios y desafíos en proporciones similares. El fondo del escenario es de color morado pastel.

En la dificultad Difícil, las tecnologías aparecen con menor frecuencia y los riesgos son más comunes. Representa una sociedad con baja regulación y mayores impactos negativos. El fondo del escenario es de color azul pastel.

Tecnologías

Las tecnologías se representan mediante elementos de color azul que aparecen de forma periódica durante la simulación. Al interactuar con ellas, el sistema obtiene beneficios reflejados en el aumento del puntaje. Cada tecnología recogida se contabiliza como un evento positivo dentro de la simulación.

Riesgos sociales

Los riesgos sociales se representan mediante obstáculos de color gris que aparecen de forma dinámica en el entorno. Estos riesgos permanecen en pantalla durante un tiempo limitado y finalizan la simulación si el sistema entra en contacto con ellos. Su aparición y duración varían según la dificultad seleccionada.

Los riesgos nunca aparecen sobre el sistema ni en su siguiente movimiento, garantizando una experiencia de simulación justa.

Métricas registradas

Al finalizar cada partida, el programa guarda automáticamente información relevante de la simulación en un archivo de tipo CSV ubicado en la carpeta data. Los datos registrados incluyen la fecha de la simulación, la dificultad seleccionada, el puntaje final, la cantidad de tecnologías recogidas y el tiempo total de supervivencia.

Estas métricas permiten realizar comparaciones entre escenarios y analizar el comportamiento del sistema bajo distintas condiciones.

Estructura del proyecto

El proyecto se organiza en una carpeta principal que contiene el código fuente del programa, una carpeta para los datos generados, el archivo README y el entorno virtual de Python.

Requisitos del sistema

Para ejecutar el proyecto se requiere Python 3 y la librería pygame-ce instalada en un entorno virtual.

Ejecución del programa

Una vez activado el entorno virtual y con las dependencias instaladas, el programa se ejecuta mediante el siguiente comando desde la carpeta principal del proyecto.

python src/proyecto_final.py

Resultados y análisis

Los resultados obtenidos a partir de las simulaciones muestran que el impacto de la tecnología depende directamente del contexto social en el que se implementa. En escenarios más controlados, los beneficios predominan, mientras que en escenarios más complejos los riesgos limitan el crecimiento del sistema.

Conclusiones

El simulador permite comprender de forma práctica cómo la adopción de nuevas tecnologías puede generar distintos efectos en la sociedad. Una implementación responsable maximiza los beneficios, mientras que una falta de regulación incrementa los riesgos. El proyecto cumple su objetivo educativo al promover una reflexión crítica sobre el uso futuro de la tecnología.

Limitaciones

El simulador utiliza modelos simplificados y no representa datos reales ni predicciones exactas. Los resultados dependen de parámetros definidos con fines educativos y no deben interpretarse como conclusiones definitivas.

OSWALDO VILLARREAL