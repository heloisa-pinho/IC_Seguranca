import smtplib
import imaplib
import time
import random
from email.message import EmailMessage

# ==================== CONFIGURAÇÃO ====================
TARGET_IP = "192.168.122.23"
SMTP_PORT = 25
IMAP_PORT = 143

USER_EMAIL = "admin@lab.local"
USER_PASS = "senha123"
# ======================================================

def acao_enviar_email():
    "Simula um funcionário enviando um relatório em texto claro."
    try:
        msg = EmailMessage()
        msg.set_content(f"Relatório de atividades fundamental. Timestamp: {time.time()}")
        msg['Subject'] = "Relatório V1"
        msg['From'] = USER_EMAIL
        msg['To'] = USER_EMAIL

        with smtplib.SMTP(TARGET_IP, SMTP_PORT) as server:
            server.send_message(msg)
            print("[SMTP] E-mail enviado.")
    except Exception as e:
        print(f"[SMTP] Erro: {e}")

def acao_checar_caixa():
    "Simula a checagem de caixa em texto claro."
    try:
        # Conexão direta na porta 143 sem STARTTLS
        mail = imaplib.IMAP4(TARGET_IP, IMAP_PORT)
        mail.login(USER_EMAIL, USER_PASS)
        mail.select("inbox")
        status, messages = mail.search(None, "ALL")
        print(f"[IMAP] Caixa checada com sucesso.")
        mail.logout()
    except Exception as e:
        print(f"[IMAP] Erro: {e}")

# ==================== EXECUÇÃO ====================
print("Iniciando tráfego de E-mail\n")

for rodada in range(1, 21):
    print(f"--- Rodada {rodada}/20 ---")
    if random.choice([True, False]):
        acao_enviar_email()
    else:
        acao_checar_caixa()
        
    tempo = random.uniform(3.0, 12.0)
    print(f"Aguardando {tempo:.2f} segundos...")
    time.sleep(tempo)
    print("")

print("\nTráfego V1 concluído!")
