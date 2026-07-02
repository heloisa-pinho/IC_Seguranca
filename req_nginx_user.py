import random
import time
import requests

TARGET_IP = "192.168.122.23"  
PORT = "8080"                
BASE_URL = f"http://{TARGET_IP}:{PORT}"

# Lista de endpoints para simular navegação real
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

# User-Agents variados
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2.1 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"
]

print("Iniciando simulação de 20 rodadas com intervalos (1 a 20s)...\n")

for rodada in range(1, 21):
    # Sorteia um tempo float entre 1.0 e 20.0 segundos
    tempo_espera = random.uniform(1.0, 20.0)
    
    print(f"[{rodada}/20] Aguardando {tempo_espera:.2f} segundos antes da próxima requisição...")
    time.sleep(tempo_espera)
    
    # --- LÓGICA DA REQUISIÇÃO (APENAS GET) ---
    endpoint = random.choice(ENDPOINTS)
    url = f"{BASE_URL}{endpoint}"
    headers = {"User-Agent": random.choice(USER_AGENTS)}
    
    try:
        # Executa exclusivamente a requisição GET
        response = requests.get(url, headers=headers, timeout=5)
        print(f"[Enviado] GET {endpoint} | Status retornado: {response.status_code}")
        
    except requests.exceptions.RequestException as e:
        # Captura timeouts ou quedas de conexão sem quebrar o script
        print(f"[Erro de Conexão]: {e}")
    
    print(f"Rodada {rodada} concluída!")
    print("-" * 50)
