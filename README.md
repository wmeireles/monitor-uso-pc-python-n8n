# 📊 Monitor de Uso do PC com Python + n8n

Este projeto automatiza o monitoramento de tempo de uso de um computador com **Python** e **n8n**, salvando os dados em **Google Sheets** e permitindo o envio de **relatórios diários por e-mail**.

## ✅ Funcionalidades

- ⏱️ Registra tempo ligado desde o último boot
- 🧠 Coleta o uso médio da CPU
- 📂 Identifica os aplicativos ativos no momento
- 🔁 Envia os dados automaticamente a cada 5 minutos para um Webhook no n8n
- 📊 Armazena os dados em uma planilha do Google Sheets
- 📬 (Opcional) Gera e envia relatórios diários por e-mail com os dados coletados

## 🧰 Tecnologias Utilizadas

- Python (`psutil`, `requests`)
- n8n (Workflow automation)
- Google Sheets (armazenamento dos dados)
- Webhook para integração

## 🚀 Como funciona

1. O script `monitor_uso_pc.py` roda localmente no seu PC.
2. A cada 5 minutos, coleta:
   - Tempo de atividade da máquina
   - Uso de CPU
   - Aplicativos ativos
3. Envia via `POST` para um Webhook n8n.
4. O n8n salva os dados em uma aba no Google Sheets.

### Exemplo de JSON enviado:

```json
{
  "timestamp": "2025-06-11T09:31:36.786245",
  "uptime_minutes": 38959,
  "cpu_percent": 23.5,
  "active_apps": ["TextInputHost", "Code", "ms-teams", "cmd", "ONENOTE"],
  "user": "HOSTNAME MAQUINA"
}
```

## 📝 Pré-requisitos

- Conta no [n8n Cloud](https://n8n.io/)
- Conta Google com permissão no Google Sheets
- Python 3.8+ com bibliotecas:

```bash
pip install psutil requests
```

## 📂 Estrutura

```
📁 monitor-uso-pc/
├── monitor_uso_pc.py     # Script principal de monitoramento
└── README.md             # Instruções e documentação do projeto
```

## 🔐 Segurança

Este projeto é local e não armazena dados sensíveis. Para ambientes corporativos, recomenda-se criptografar os dados ou armazenar localmente com backup em nuvem.

## 🧑‍💻 Autor

Desenvolvido por **Willian Meireles**  
🔗 [linkedin.com/in/willianmeireles](https://linkedin.com/in/willianmeireles)  
📧 willianmeireles2021@gmail.com

---

🗓️ Última atualização: 11/06/2025
