# imports
import time
import pandas as pd
from datetime import datetime
import pytz
import numpy as np
import requests
import json

# Inicializa o DataFrame para armazenar os dados
data = {'Datetime': [], 'Topic': [], 'Payload': [], 'Capacidade': []}
df = pd.DataFrame(data)

# Fuso horário desejado ('America/Sao_Paulo')
desired_timezone = 'America/Sao_Paulo'
local_timezone = pytz.timezone(desired_timezone)

# Endereço para a API InterSCity
api_base = 'https://cidadesinteligentes.lsdi.ufma.br/interscity_lh'
api_catalog = f'{api_base}/catalog'
api_adaptor = f'{api_base}/adaptor'
api_collector = f'{api_base}/collector'

# Caminho para salvar o CSV
csv_path = 'dados_climaticos.csv'

# Tópicos e capacidades relacionados ao clima
topicos_capacidades = {
    "esp32/bme280/temperatura": "Termômetro",
    "esp32/bme280/umidade": "Higrômetro",
    "esp32/bme280/pressao": "Barômetro",
    "esp32/bme280/altitude": "Altímetro"
}

def show_capacidades():
    r = requests.get(f'{api_catalog}/capabilities')
    if r.status_code == 200:
        content = json.loads(r.text)
        print(json.dumps(content, indent=2, sort_keys=True))
    else:
        print(f'Status code: {r.status_code}')

def show_resources():
    r = requests.get(f'{api_catalog}/resources')
    if r.status_code == 200:
        content = json.loads(r.text)
        print(json.dumps(content, indent=2, sort_keys=True))
    else:
        print(f'Status code: {r.status_code}')

def create_capability(nome, tipo, descricao):
    capability_json = {
        "name": nome,
        "description": descricao,
        "capability_type": tipo
    }
    r = requests.post(f'{api_catalog}/capabilities/', json=capability_json)
    if r.status_code == 201:
        content = json.loads(r.text)
        print(json.dumps(content, indent=2, sort_keys=True))
        return True
    else:
        print(f'Status code: {r.status_code}')
        print(f'Response: {r.text}')
        return False

def create_resource(descricao, latitude, longitude, capacidades):
    resource_json = {
        "data": {
            "description": descricao,
            "capabilities": capacidades,
            "status": "active",
            "city": "São Luís",
            "country": "BR",
            "state": "MA",
            "lat": latitude,
            "lon": longitude
        }
    }
    r = requests.post(f'{api_catalog}/resources', json=resource_json)
    if r.status_code == 201:
        resource = json.loads(r.text)
        uuid = resource['data']['uuid']
        print(json.dumps(resource, indent=2))
        return uuid
    else:
        print(f'Status code: {r.status_code}')
        print(f'Response: {r.text}')
        return ''

def prepare_API():
    capacidades_list = np.array(list(topicos_capacidades.values()))
    capacidades_unique = np.unique(capacidades_list)

    print("Preparando a API...")
    time.sleep(1)

    for nomeCapacidade in capacidades_unique:
        print(f"Criando a capacidade '{nomeCapacidade}'...")
        if not create_capability(nomeCapacidade, "sensor", "Dados climáticos"):
            return ""

    print("Criando recurso 'SmartWeather_Station'...")
    uuid_resource = create_resource("SmartWeather_Station", -2.55972052497871, -44.31196495361665, list(capacidades_unique))
    return uuid_resource

def addData_API(uuid_resource):
    try:
        df = pd.read_csv(csv_path)
        dates = df.Datetime.tolist()
        capacidades_ = df.Capacidade.tolist()
        payloads = df.Payload.tolist()

        capability_data_json = {
            "data": [
                {capacidade: float(value), 'timestamp': datetime.strptime(date, '%Y-%m-%d %H:%M:%S').isoformat()}
                for capacidade, value, date in zip(capacidades_, payloads, dates)
            ]
        }

        print("Adicionando dados das capacidades...")
        r = requests.post(f'{api_adaptor}/resources/{uuid_resource}/data/environment_monitoring', json=capability_data_json)
        if r.status_code == 201:
            print('Dados adicionados com sucesso!')
            
            # Consultando os dados adicionados
            print("\nConsultando dados do recurso...")
            r_collector = requests.get(f'{api_collector}/resources/{uuid_resource}/data')
            if r_collector.status_code == 200:
                content = json.loads(r_collector.text)
                print(json.dumps(content, indent=2, sort_keys=True))
            else:
                print(f'Erro ao consultar dados. Status code: {r_collector.status_code}')
        else:
            print(f'Erro ao adicionar dados. Status code: {r.status_code}')
            print(f'Response: {r.text}')
            return False
        return True
    except Exception as e:
        print(f'Erro ao processar dados: {str(e)}')
        return False

# Fluxo principal
if __name__ == "__main__":
    uuid = prepare_API()
    if uuid:
        print("Recurso criado com sucesso! Adicionando dados...")
        addData_API(uuid)
    else:
        print("Erro na criação do recurso.")
