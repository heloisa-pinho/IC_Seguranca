#!/bin/bash

# Define o alvo (IP ou Hostname)
TARGET="192.168.122.23"

echo "Iniciando bateria de escaneamento em: $TARGET"
echo "------------------------------------------------"

# 1. TCP Connect Scan
# Explicação: Completa o aperto de mão TCP (Three-way handshake). Não exige privilégios de root.
echo "[+] Executando TCP Connect Scan..."
nmap -sT $TARGET

# 2. SYN Scan (Half-open)
# Explicação: Mais furtivo, não fecha a conexão completa. Exige sudo.
echo "[+] Executando SYN Scan..."
sudo nmap -sS $TARGET

# 3. ACK Scan
# Explicação: Usado para mapear regras de firewall e verificar se as portas são filtradas.
echo "[+] Executando ACK Scan..."
sudo nmap -sA $TARGET

# 4. Xmas Scan
# Explicação: Envia flags FIN, PSH e URG. Útil contra sistemas que seguem estritamente a RFC 793 (comum em Unix).
echo "[+] Executando Xmas Scan..."
sudo nmap -sX $TARGET

# 5. FIN Scan
# Explicação: Envia apenas a flag FIN. Pode passar por firewalls que barram pacotes SYN.
echo "[+] Executando FIN Scan..."
sudo nmap -sF $TARGET

# 6. NULL Scan
# Explicação: Envia um pacote sem nenhuma flag definida.
echo "[+] Executando NULL Scan..."
sudo nmap -sN $TARGET

# 7. UDP Scan
# Explicação: Procura por portas UDP abertas (ex: DNS, DHCP, SNMP). É mais lento que o TCP.
echo "[+] Executando UDP Scan..."
sudo nmap -sU $TARGET

# 8. ICMP Scan (Ping Sweep / Echo Request)
# Explicação: Verifica se o host responde a requisições de eco ICMP.
echo "[+] Executando ICMP Scan..."
sudo nmap -sn -PE --send-ip $TARGET

# 9. ARP Scan
# Explicação: Descobre hosts na rede local usando requisições ARP. Muito eficiente em redes locais.
echo "[+] Executando ARP Scan..."
sudo nmap -sn -PR $TARGET

echo "------------------------------------------------"
echo "Escaneamento finalizado."
