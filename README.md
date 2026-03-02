# EL IMPACTO DE LAS NUEVAS TECNOLOGÍAS EN LA SOCIEDAD: VISUALIZACIÓN DEL FUTURO

Nombre del estudiante: Oswaldo Villarreal  
Materia: Lógica de Programación 2  
Fecha: 1 de marzo de 2026  
Actividad: Proyecto Final  

---

## Introducción

Las nuevas tecnologías han transformado de manera profunda la forma en que la sociedad se desarrolla, influyendo en ámbitos como la economía, el empleo, la educación y la vida cotidiana. Si bien estos avances han generado beneficios importantes, también han provocado nuevos riesgos y desafíos sociales que requieren ser analizados de forma responsable.

Este proyecto presenta un simulador interactivo desarrollado en Python que permite visualizar, de manera práctica, cómo el uso de nuevas tecnologías puede generar distintos resultados dependiendo del contexto en el que se implementan. El objetivo principal es fomentar la reflexión sobre el equilibrio entre beneficios tecnológicos y riesgos sociales.

---

## Objetivo del proyecto

Desarrollar un software educativo que permita simular distintos escenarios sociales mediante un videojuego tipo Snake, con el fin de analizar el impacto de la adopción tecnológica y los riesgos asociados a lo largo del tiempo.

---

## Descripción general del software

El proyecto consiste en un videojuego tipo Snake desarrollado con la librería Pygame. En este simulador, el jugador controla un sistema que representa a la sociedad, el cual se desplaza y crece a medida que interactúa con distintos elementos dentro del entorno.

El sistema incluye tres tipos de elementos principales:
- Comida, que permite el crecimiento básico del sistema.
- Multiplicadores, que representan beneficios tecnológicos adicionales.
- Riesgos sociales, que representan consecuencias negativas.

El programa se estructura a partir de un bucle principal que controla el estado del juego, la interacción del usuario y la actualización constante del entorno.

Ejemplo del bucle principal del programa:

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

Este fragmento permite mantener el programa en ejecución y gestionar los eventos del sistema.

---

## Dificultades del simulador

El programa cuenta con tres niveles de dificultad, cada uno representando un contexto social distinto. La dificultad se selecciona antes de iniciar la simulación y modifica la frecuencia de aparición de multiplicadores y riesgos, así como el color del entorno.

La configuración de las dificultades se define mediante una estructura de datos:

ESCENARIOS = {
    "FACIL": {
        "bonus_multiplicador": 3
    },
    "MEDIO": {
        "bonus_multiplicador": 2
    },
    "DIFICIL": {
        "bonus_multiplicador": 1
    }
}


En la dificultad Fácil, los multiplicadores aparecen con mayor frecuencia y los riesgos son menos comunes. El fondo del escenario es de color rojo pastel.

En la dificultad Medio, existe un equilibrio entre beneficios y riesgos. El fondo del escenario es de color morado pastel.

En la dificultad Difícil, los multiplicadores aparecen con menor frecuencia y los riesgos son más comunes. El fondo del escenario es de color azul pastel.

---

## Comida del sistema

La comida se representa mediante un cuadro de color rojo. Cada vez que el sistema interactúa con la comida, el Snake crece y el puntaje aumenta en una unidad.

Este elemento representa el crecimiento básico y constante del sistema.

---

## Multiplicadores

Los multiplicadores se representan mediante cuadros de color azul que aparecen de forma periódica durante la simulación. Al interactuar con ellos, el sistema obtiene un aumento adicional en el puntaje según la dificultad seleccionada.

Ejemplo de interacción con un multiplicador:

if multiplicador is not None and cabeza_nueva == multiplicador:
    score += cfg["bonus_multiplicador"]
    multiplicadores += 1
    multiplicador = None

Cada multiplicador recogido se registra como un evento positivo dentro de la simulación.

---

## Riesgos sociales

Los riesgos sociales se representan mediante obstáculos de color gris que aparecen de forma dinámica en el entorno. Estos riesgos tienen una duración limitada y desaparecen automáticamente después de cierto tiempo, evitando que el sistema se vuelva injusto o imposible de completar.

El control de la duración de los riesgos se realiza mediante el uso del tiempo:

riesgos = [r for r in riesgos if ahora - r["t"] < DURACION_RIESGO]

Si el sistema entra en contacto con un riesgo, la simulación finaliza, representando el impacto negativo de una mala gestión tecnológica.

---

## Métricas registradas

Al finalizar cada partida, el programa guarda automáticamente información relevante de la simulación en un archivo CSV ubicado en la carpeta data.

Los datos registrados incluyen:

Fecha y hora de la simulación

Dificultad seleccionada

Puntaje final

Cantidad de multiplicadores obtenidos

Tiempo total de supervivencia

Ejemplo del registro de métricas:

writer.writerow([
    datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    escenario,
    score,
    multiplicadores,
    round(tiempo, 2)
])

Estas métricas permiten realizar comparaciones entre escenarios y analizar el comportamiento del sistema bajo distintas condiciones.

---

## Requisitos del sistema

Para ejecutar el proyecto se requiere Python 3 y la librería pygame-ce instalada en un entorno virtual.

---

## Resultados y análisis

Los resultados obtenidos muestran que el impacto de la tecnología depende directamente del contexto social en el que se implementa. En escenarios más controlados, los beneficios predominan, mientras que en escenarios más complejos los riesgos limitan el crecimiento del sistema.

---

## Conclusiones

El simulador permite comprender de forma práctica cómo la adopción de nuevas tecnologías puede generar distintos efectos en la sociedad. Una implementación responsable maximiza los beneficios, mientras que una falta de regulación incrementa los riesgos.

---

## Limitaciones

El simulador utiliza modelos simplificados y no representa datos reales ni predicciones exactas. Los resultados deben interpretarse únicamente con fines educativos.

Oswaldo Villarreal