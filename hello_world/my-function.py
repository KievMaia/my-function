import requests


def lambda_handler(event, context):
    # Evento a ser enviado para o Hookdeck
    payload = {
        "event": "event",
    }
    header = {
        'Content-Type': 'application/json',
        'x-prolog-delivery': "eventId"
    }

    # URL do webhook fornecida pelo Hookdeck
    webhook_url = "https://events.hookdeck.com/e/src_kI53GvQfyYeNjGnJRstsGJze"

    # Enviar o evento para o Hookdeck via HTTP POST
    response = requests.post(url=webhook_url, json=payload, headers=header)

    # Verificar o status da resposta
    if response.status_code == 200:
        print("Evento enviado com sucesso para o Hookdeck")
    else:
        print(f"Falha ao enviar evento para o Hookdeck. Código de status: {response.status_code}")

    return {
        'statusCode': 200,
        'body': 'Evento enviado para o Hookdeck'
    }
