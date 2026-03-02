import pygame
import random
import time
import csv
from datetime import datetime
from pathlib import Path

ANCHO = 800
ALTO = 600
TAM = 20
FPS = 10

NEGRO = (0, 0, 0)
VERDE = (0, 200, 0)
ROJO = (200, 0, 0)
AZUL = (0, 120, 255)
GRIS = (140, 140, 140)

ROJO_PASTEL = (245, 215, 215)
MORADO_PASTEL = (235, 225, 245)
AZUL_PASTEL = (205, 220, 245)

DURACION_RIESGO = 8

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)
CSV_PATH = DATA_DIR / "metrics.csv"

ESCENARIOS = {
    "FACIL": {
        "fondo": ROJO_PASTEL,
        "tec_min": 4,
        "tec_max": 8,
        "bonus_multiplicador": 3,
        "risk_min": 12,
        "risk_max": 18,
    },
    "MEDIO": {
        "fondo": MORADO_PASTEL,
        "tec_min": 7,
        "tec_max": 12,
        "bonus_multiplicador": 2,
        "risk_min": 8,
        "risk_max": 14,
    },
    "DIFICIL": {
        "fondo": AZUL_PASTEL,
        "tec_min": 10,
        "tec_max": 16,
        "bonus_multiplicador": 1,
        "risk_min": 5,
        "risk_max": 10,
    },
}

def posicion_aleatoria():
    return (
        random.randrange(0, ANCHO, TAM),
        random.randrange(0, ALTO, TAM),
    )

def proxima_cabeza(snake, dx, dy):
    if dx == 0 and dy == 0:
        return None
    return (snake[0][0] + dx, snake[0][1] + dy)

def posicion_libre(snake, comida, multiplicador, riesgos, dx, dy, evitar_proxima=True, max_intentos=3000):
    siguiente = proxima_cabeza(snake, dx, dy) if evitar_proxima else None
    for _ in range(max_intentos):
        p = posicion_aleatoria()
        if p in snake:
            continue
        if comida is not None and p == comida:
            continue
        if multiplicador is not None and p == multiplicador:
            continue
        if any(r["pos"] == p for r in riesgos):
            continue
        if siguiente is not None and p == siguiente:
            continue
        return p
    return posicion_aleatoria()

def guardar_metricas(escenario, score, multiplicadores, tiempo):
    nuevo = not CSV_PATH.exists()
    with open(CSV_PATH, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if nuevo:
            writer.writerow(["fecha", "escenario", "score", "multiplicadores", "tiempo_segundos"])
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            escenario,
            score,
            multiplicadores,
            round(tiempo, 2),
        ])

def menu_dificultad(pantalla, reloj):
    fuente_titulo = pygame.font.SysFont(None, 48)
    fuente = pygame.font.SysFont(None, 32)

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return None
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_1:
                    return "FACIL"
                if e.key == pygame.K_2:
                    return "MEDIO"
                if e.key == pygame.K_3:
                    return "DIFICIL"

        pantalla.fill(NEGRO)
        pantalla.blit(fuente_titulo.render("ELIGE DIFICULTAD", True, (240, 240, 240)), (250, 150))
        pantalla.blit(fuente.render("1 Facil", True, (240, 240, 240)), (330, 240))
        pantalla.blit(fuente.render("2 Medio", True, (240, 240, 240)), (330, 280))
        pantalla.blit(fuente.render("3 Dificil", True, (240, 240, 240)), (330, 320))
        pygame.display.flip()
        reloj.tick(30)

def main():
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Snake Impacto de Tecnologias")
    reloj = pygame.time.Clock()
    fuente = pygame.font.SysFont(None, 32)

    escenario = menu_dificultad(pantalla, reloj)
    if escenario is None:
        pygame.quit()
        return

    cfg = ESCENARIOS[escenario]

    snake = [(ANCHO // 2, ALTO // 2)]
    dx = 0
    dy = 0

    riesgos = []
    comida = posicion_libre(snake, None, None, riesgos, dx, dy, evitar_proxima=False)
    multiplicador = None

    prox_multiplicador = time.time() + random.randint(cfg["tec_min"], cfg["tec_max"])
    prox_riesgo = time.time() + random.randint(cfg["risk_min"], cfg["risk_max"])

    score = 0
    multiplicadores = 0
    inicio = time.time()
    game_over = False

    corriendo = True
    while corriendo:
        ahora = time.time()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                corriendo = False

            if e.type == pygame.KEYDOWN:
                if game_over and e.key == pygame.K_r:
                    tiempo = time.time() - inicio
                    guardar_metricas(escenario, score, multiplicadores, tiempo)
                    main()
                    return

                if not game_over:
                    if e.key == pygame.K_UP and dy == 0:
                        dx, dy = 0, -TAM
                    elif e.key == pygame.K_DOWN and dy == 0:
                        dx, dy = 0, TAM
                    elif e.key == pygame.K_LEFT and dx == 0:
                        dx, dy = -TAM, 0
                    elif e.key == pygame.K_RIGHT and dx == 0:
                        dx, dy = TAM, 0

        riesgos = [r for r in riesgos if ahora - r["t"] < DURACION_RIESGO]

        if multiplicador is None and ahora >= prox_multiplicador:
            multiplicador = posicion_libre(snake, comida, None, riesgos, dx, dy, evitar_proxima=True)
            prox_multiplicador = ahora + random.randint(cfg["tec_min"], cfg["tec_max"])

        if ahora >= prox_riesgo:
            pos = posicion_libre(snake, comida, multiplicador, riesgos, dx, dy, evitar_proxima=True)
            riesgos.append({"pos": pos, "t": ahora})
            prox_riesgo = ahora + random.randint(cfg["risk_min"], cfg["risk_max"])

        if not game_over and (dx != 0 or dy != 0):
            cabeza_nueva = (snake[0][0] + dx, snake[0][1] + dy)

            fuera = not (0 <= cabeza_nueva[0] < ANCHO and 0 <= cabeza_nueva[1] < ALTO)
            toca_riesgo = any(r["pos"] == cabeza_nueva for r in riesgos)

            va_a_comer = (cabeza_nueva == comida)
            cuerpo_a_evitar = snake if va_a_comer else snake[:-1]
            toca_cuerpo = (cabeza_nueva in cuerpo_a_evitar)

            if fuera or toca_riesgo or toca_cuerpo:
                game_over = True
            else:
                snake.insert(0, cabeza_nueva)

                if va_a_comer:
                    score += 1
                    comida = posicion_libre(snake, None, multiplicador, riesgos, dx, dy, evitar_proxima=False)
                else:
                    snake.pop()

                if multiplicador is not None and cabeza_nueva == multiplicador:
                    score += cfg["bonus_multiplicador"]
                    multiplicadores += 1
                    multiplicador = None

        pantalla.fill(cfg["fondo"])

        pygame.draw.rect(pantalla, ROJO, (*comida, TAM, TAM))

        if multiplicador is not None:
            pygame.draw.rect(pantalla, AZUL, (*multiplicador, TAM, TAM))

        for r in riesgos:
            pygame.draw.rect(pantalla, GRIS, (*r["pos"], TAM, TAM))

        for parte in snake:
            pygame.draw.rect(pantalla, VERDE, (*parte, TAM, TAM))

        pantalla.blit(fuente.render(f"Dificultad: {escenario}", True, NEGRO), (10, 10))
        pantalla.blit(fuente.render(f"Score: {score}", True, NEGRO), (10, 35))
        pantalla.blit(fuente.render(f"Multiplicadores: {multiplicadores}", True, NEGRO), (10, 60))

        if game_over:
            pantalla.blit(fuente.render("GAME OVER  Presiona R", True, NEGRO), (250, 300))

        pygame.display.flip()
        reloj.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()