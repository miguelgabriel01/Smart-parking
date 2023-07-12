import random
import time
import json
import datetime
import os
from paho.mqtt import client as mqtt_client

broker = 'broker.emqx.io'
port = 1883
topic = "python/mqtt"
client_id = f'python-mqtt-{random.randint(0, 100)}'

def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set('emqx', 'public')
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        payload = msg.payload.decode('utf-8')
        payload = json.loads(payload.replace("'", '"'))
        novo_json = processar_payload(payload)
        novo_json_string = json.dumps(novo_json, indent=4)
        print(novo_json_string)

        # Salvar o novo_json no arquivo dadosVagas.json
        with open('dadosVagas.json', 'w') as file:
            json.dump(novo_json, file, indent=4)

        time.sleep(5)  # Atraso de 5 segundos

    client.subscribe(topic)
    client.on_message = on_message

def processar_payload(payload):
    vagas_livres = sum(1 for item in payload if item['situacao'] == 'livre')
    vagas_ocupadas = sum(1 for item in payload if item['situacao'] == 'ocupada')
    total_vagas = len(payload)

    porcentagem_vagas_ocupadas = round((vagas_ocupadas / total_vagas) * 100)
    porcentagem_vagas_livres = round((vagas_livres / total_vagas) * 100)

    ultima_atualizacao_hora = payload[0]['horaDaUltimaAtualizacao']
    ultima_atualizacao_data = payload[0]['dataDaUltimaAtualizacao']
    localizacao = payload[0]['localizacao']

    # Adicionar a estrutura situacaoVagas
    situacao_vagas = []
    for item in payload:
        vaga = {
            "id": item["id"],
            "situacao": item["situacao"]
        }
        situacao_vagas.append(vaga)

    novo_json = {
        "vagasLivres": vagas_livres,
        "vagasOcupadas": vagas_ocupadas,
        "porcentagemDeVagasOcupadas": porcentagem_vagas_ocupadas,
        "porcentagemDeVagasLivres": porcentagem_vagas_livres,
        "ultimaAtualizacaoHora": ultima_atualizacao_hora,
        "ultimaAtualizacaoData": ultima_atualizacao_data,
        "localizacao": localizacao,
        "situacaoVagas": situacao_vagas  # Adiciona situacaoVagas ao JSON
    }

    return novo_json

def run():
    # Verifica se o arquivo já existe e carrega seu conteúdo
    if os.path.exists('dadosVagas.json'):
        with open('dadosVagas.json', 'r') as file:
            dados_vagas = json.load(file)
    else:
        dados_vagas = []

    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()

    # Salva o novo_json no arquivo dadosVagas.json
    with open('dadosVagas.json', 'w') as file:
        json.dump(dados_vagas, file, indent=4)

if __name__ == '__main__':
    run()
