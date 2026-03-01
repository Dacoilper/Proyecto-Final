import pygame
import random
import time
import csv
from datetime import datetime
from pathlib import Path

ANCHO = 800
ALTO = 600
TAM_BLOQUE = 20
FPS = 10

NEGRO = (0, 0, 0)
VERDE = (0, 200, 0)
ROJO = (200, 0, 0)
AZUL = (0, 120, 255)
GRIS = (120, 120, 120)
BLANCO = (245, 245, 245)

ROJO_PASTEL = (245, 215, 215)
MORADO_PASTEL = (235, 225, 245)
AZUL_PASTEL = (205, 220, 245)

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)
METRICS_FILE = DATA_DIR / "metrics.csv"

DURACION_RIESGO = 8  # segundos que vive un riesgo

ESCENARIOS = {
    "FACIL": {
        "tec_min": 4,
        "tec_max": 8,
        "tec_bonus": 3,
        "risk_min": 12,
        "risk_max": 18,
        "fondo": ROJO_PASTEL
    },
    "MEDIO": {
        "tec_min": 7,
        "tec_max": 12,
        "tec_bonus": 2,
        "risk_min": 8,
        "risk_max": 14,
        "fondo": MORADO_PASTEL
    },
    "DIFICIL": {
        "tec_min": 10,
        "tec_max": 16,
        "tec_bonus": 1,
        "risk_min": 5,
        "risk_max": 10,
        "fondo": AZUL_PASTEL
    },
}

def posicion_aleatoria():
    x = random.randrange(0, ANCHO, TAM_BLOQUE)
    y = random.randrange(0, ALTO, TAM_BLOQUE)
    return x, y

def proxima_cabeza(snake, dx, dy):
    if dx == 0 and dy == 0:
        return None
    return (snake[0][0] + dx, snake[0][1] + dy)

def posicion_libre(snake, comida, tecnologia, riesgos, dx, dy, evitar_proxima=True, max_intentos=2000):
    siguiente = proxima_cabeza(snake, dx, dy) if evitar_proxima else None

    for _ in range(max_intentos):
        p = posicion_aleatoria()
        if p in snake:
            continue
        if comida is not None and p == comida:
            continue
        if tecnologia is not None and p == tecnologia:
            continue
        if any(r["pos"] == p for r in riesgos):
            continue
        if siguiente is not None and p == siguiente:
            continue
        return p

    return posicion_aleatoria()

def guardar_metricas(escenario, score, tecnologias, tiempo):
    existe = METRICS_FILE.exists()
    with open(METRICS_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not existe:
            writer.writerow(["fecha", "escenario", "score", "tecnologias", "tiempo_segundos"])
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            escenario,
            score,
            tecnologias,
            round(tiempo, 2)
        ])

def menu_escenario(pantalla, reloj):
    fuente_titulo = pygame.font.SysFont(None, 48)
    fuente = pygame.font.SysFont(None, 32)

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return None
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_1:
                    return "FACIL"
                if evento.key == pygame.K_2:
                    return "MEDIO"
                if evento.key == pygame.K_3:
                    return "DIFICIL"

        pantalla.fill(NEGRO)
        pantalla.blit(fuente_titulo.render("ELIGE DIFICULTAD", True, BLANCO), (250, 150))
        pantalla.blit(fuente.render("1 Facil", True, BLANCO), (330, 240))
        pantalla.blit(fuente.render("2 Medio", True, BLANCO), (330, 280))
        pantalla.blit(fuente.render("3 Dificil", True, BLANCO), (330, 320))
        pygame.display.flip()
        reloj.tick(30)

def main():
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Snake Impacto de Tecnologias")
    reloj = pygame.time.Clock()
    fuente = pygame.font.SysFont(None, 32)

    escenario = menu_escenario(pantalla, reloj)
    if escenario is None:
        pygame.quit()
        return

    cfg = ESCENARIOS[escenario]

    snake = [(ANCHO // 2, ALTO // 2)]
    dx = dy = 0

    tecnologia = None
    riesgos = []

    comida = posicion_libre(snake, None, tecnologia, riesgos, dx, dy, evitar_proxima=False)

    prox_tec = time.time() + random.randint(cfg["tec_min"], cfg["tec_max"])
    prox_risk = time.time() + random.randint(cfg["risk_min"], cfg["risk_max"])

    score = 0
    tecnologias = 0
    inicio = time.time()
    game_over = False

    corriendo = True
    while corriendo:
        ahora = time.time()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False

            if evento.type == pygame.KEYDOWN:
                if game_over and evento.key == pygame.K_r:
                    tiempo = time.time() - inicio
                    guardar_metricas(escenario, score, tecnologias, tiempo)
                    main()
                    return

                if not game_over:
                    if evento.key == pygame.K_UP and dy == 0:
                        dx, dy = 0, -TAM_BLOQUE
                    elif evento.key == pygame.K_DOWN and dy == 0:
                        dx, dy = 0, TAM_BLOQUE
                    elif evento.key == pygame.K_LEFT and dx == 0:
                        dx, dy = -TAM_BLOQUE, 0
                    elif evento.key == pygame.K_RIGHT and dx == 0:
                        dx, dy = TAM_BLOQUE, 0

        # eliminar riesgos vencidos
        riesgos = [r for r in riesgos if ahora - r["t"] < DURACION_RIESGO]

        if tecnologia is None and ahora >= prox_tec:
            tecnologia = posicion_libre(snake, comida, None, riesgos, dx, dy)
            prox_tec = ahora + random.randint(cfg["tec_min"], cfg["tec_max"])

        if ahora >= prox_risk:
            pos = posicion_libre(snake, comida, tecnologia, riesgos, dx, dy)
            riesgos.append({"pos": pos, "t": ahora})
            prox_risk = ahora + random.randint(cfg["risk_min"], cfg["risk_max"])

        if not game_over and (dx != 0 or dy != 0):
            cabeza = (snake[0][0] + dx, snake[0][1] + dy)

            if (
                cabeza in snake
                or any(r["pos"] == cabeza for r in riesgos)
                or not (0 <= cabeza[0] < ANCHO and 0 <= cabeza[1] < ALTO)
            ):
                game_over = True
            else:
                snake.insert(0, cabeza)

                if cabeza == comida:
                    score += 1
                    comida = posicion_libre(snake, None, tecnologia, riesgos, dx, dy, evitar_proxima=False)
                else:
                    snake.pop()

                if tecnologia is not None and cabeza == tecnologia:
                    score += cfg["tec_bonus"]
                    tecnologias += 1
                    tecnologia = None

        pantalla.fill(cfg["fondo"])

        pygame.draw.rect(pantalla, ROJO, (*comida, TAM_BLOQUE, TAM_BLOQUE))

        if tecnologia is not None:
            pygame.draw.rect(pantalla, AZUL, (*tecnologia, TAM_BLOQUE, TAM_BLOQUE))

        for r in riesgos:
            pygame.draw.rect(pantalla, GRIS, (*r["pos"], TAM_BLOQUE, TAM_BLOQUE))

        for b in snake:
            pygame.draw.rect(pantalla, VERDE, (*b, TAM_BLOQUE, TAM_BLOQUE))

        pantalla.blit(fuente.render(f"Dificultad: {escenario}", True, NEGRO), (10, 10))
        pantalla.blit(fuente.render(f"Score: {score}", True, NEGRO), (10, 35))
        pantalla.blit(fuente.render(f"Tecnologias: {tecnologias}", True, NEGRO), (10, 60))

        if game_over:
            pantalla.blit(fuente.render("GAME OVER  Presiona R", True, NEGRO), (250, 300))

        pygame.display.flip()
        reloj.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()