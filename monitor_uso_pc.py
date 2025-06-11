import psutil
import time
import datetime
import requests
import platform
import subprocess

# URL do webhook do n8n (ajustaremos depois)
WEBHOOK_URL = "https://willian-meireles.app.n8n.cloud/webhook-test/monitor-uso-pc"

def tempo_ligado_em_minutos():
    boot_time = psutil.boot_time()
    agora = time.time()
    return round((agora - boot_time) / 60)

def uso_cpu():
    return psutil.cpu_percent(interval=1)

def apps_ativos():
    try:
        if platform.system() == "Windows":
            # Usa PowerShell para pegar janela em primeiro plano
            output = subprocess.check_output(
                'powershell "Get-Process | Where-Object {$_.MainWindowTitle} | Select-Object -ExpandProperty ProcessName"',
                shell=True, universal_newlines=True)
            apps = list(set(output.strip().split('\n')))
            return apps[:5]  # Limita a 5 apps
        else:
            return ["monitor não implementado para Linux/Mac"]
    except Exception as e:
        return [f"Erro ao obter apps: {e}"]

def enviar_para_n8n(payload):
    try:
        response = requests.post(WEBHOOK_URL, json=payload)
        print(f"[{datetime.datetime.now()}] Enviado: {response.status_code}")
    except Exception as e:
        print(f"Erro ao enviar dados: {e}")

def main():
    while True:
        payload = {
            "timestamp": datetime.datetime.now().isoformat(),
            "uptime_minutes": tempo_ligado_em_minutos(),
            "cpu_percent": uso_cpu(),
            "active_apps": apps_ativos(),
            "user": platform.node()
        }
        enviar_para_n8n(payload)
        time.sleep(300)  # Espera 5 minutos (300s)

if __name__ == "__main__":
    main()
