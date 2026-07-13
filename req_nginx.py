import random
import time
import requests

TARGET_IP = "192.168.122.23"
PORT = "8080"
BASE_URL = f"http://{TARGET_IP}:{PORT}"

# Lista de endpoints
ENDPOINTS = [
    "/",
    "/index.html",
    "/about",
    "/contact",
    "/api/v1/status",
    "/products",
    "/login",
    "/favicon.ico",
    "/css/style.css",
    "/js/main.js"
]

for rodada in range(1, 21):
    # Sorteia um tempo de espera
    tempo_espera = random.uniform(1.0, 20.0)
    print(f"[{rodada}/20] Aguardando {tempo_espera:.2f} segundos antes da próxima requisição...")
    time.sleep(tempo_espera)

    endpoint = random.choice(ENDPOINTS)
    url = f"{BASE_URL}{endpoint}"

    try:
        # Executa a requisição GET sem enviar headers personalizados
        response = requests.get(url, timeout=5)
        print(f"[Enviado] GET {endpoint} | Status retornado: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"[Erro de Conexão]: {e}")

    print(f"Rodada {rodada} concluída")
    print("-" * 50)

print("\nSimulação finalizada")
