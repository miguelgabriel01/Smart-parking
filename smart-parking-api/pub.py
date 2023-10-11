import random
import time
import json
from paho.mqtt import client as mqtt_client
from datetime import date, datetime

numberPub = random.randint(1, 52)

currentDate = date.today()
currentTime = datetime.now()

dateInText = '{}/{}/{}'.format(currentDate.day, currentDate.month, currentDate.year)
updateTime = currentTime.strftime('%H:%M')

broker = 'broker.emqx.io'
port = 1883
topic = "python/mqtt"
client_id = f'python-mqtt-{random.randint(0, 1000)}'

def connect_mqtt():
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

dadosSobreAsVagas = []
for i in range(1, 33):
    situacao = random.choice(["ocupada", "livre"])
    registro = {
        "id": i,
        "situacao": situacao,
        "dataDaUltimaAtualizacao": dateInText,
        "horaDaUltimaAtualizacao": updateTime,
        "localizacao": "shopping north way"
    }
    dadosSobreAsVagas.append(registro)

totalParkingSpaces = 32

def publish(client):
    print('-----------------------------')
    print("*       Smarth-parking      *")
    print('-----------------------------')

    while True:
        print(" ")
        print("Numero total de vagas no estacionamento: " + str(totalParkingSpaces))
        print(" ")
        print("Status atual sobre as vagas: ")
        print(" ")
        print(json.dumps(dadosSobreAsVagas, indent=4))
        print("    ")
        idSelect = int(input("Digite a vaga que deseja alterar (ou 0 para sair): "))

        if idSelect == 0:
            break

        if idSelect > 0 and idSelect <= len(dadosSobreAsVagas):
            print("    ")
            idSelectStatus = 0
            if idSelect == dadosSobreAsVagas[idSelect - 1]["id"]:
                print("Situação atual da vaga: " + dadosSobreAsVagas[idSelect - 1]["situacao"])
                print("Deseja alterar o status desta vaga?")
                print("1 - Sim / 2 - Não ")
                idSelectStatus = int(input())

                if idSelectStatus == 1:
                    if dadosSobreAsVagas[idSelect - 1]["situacao"] == "ocupada":
                        dadosSobreAsVagas[idSelect - 1]["situacao"] = "livre"
                    else:
                        dadosSobreAsVagas[idSelect - 1]["situacao"] = "ocupada"
            else:
                print("Vaga indisponível no momento!")
        else:
            print("Número de vaga inválido. Tente novamente.")

def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)

if __name__ == '__main__':
    run()
