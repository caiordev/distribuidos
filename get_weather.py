import requests
import json



api_key = 'bc6e69275e67f5f3224f972b84a638a0'
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = "São Luís,BR"
complete_url = base_url + "appid=" + api_key + "&q=" + city_name + "&units=metric"

response = requests.get(complete_url)
x = response.json()

# Verificar o status da resposta
if response.status_code != 200:
    print(complete_url)
    print(f"Erro na API: {response.status_code}, {x.get('message', 'Erro desconhecido')}")
    exit()

# Verificar se a chave 'main' está presente
if "main" not in x:
    print("Erro: Chave 'main' não encontrada no JSON.")
    exit()

# Obter os dados principais
y = x["main"]
current_temp = y["temp"]
max_temp = round(y["temp_max"])
min_temp = round(y["temp_min"])
humidity = y["humidity"]
pressure = y["pressure"]
feels = y["feels_like"]
previous_temp = 23

# Funções

def arg1():
    return current_temp

def arg2():
    return previous_temp

def arg3():
    return max_temp


def temp_difference(current_temp, previous_temp, max_temp):
    if max_temp == 0:
        return "Erro: Temperatura máxima é zero."
    change_percent = ((current_temp - max_temp) / max_temp) * 100
    change_percent = int(change_percent)
    if previous_temp > current_temp:
        return f"{change_percent}%"
    elif previous_temp < current_temp:
        return f"+{change_percent}%"
    else:
        return "0%"

def get_temp():
    return f"{current_temp} °C"

def get_temp_min():
    return f"{min_temp} °C"

def get_temp_max():
    return f"{max_temp} °C"

def get_humidity():
    return str(humidity)

def get_pressure():
    return str(pressure)

def get_feel():
    return f"{feels} °C"

# Exibir os dados
print(f"Temperatura Atual: {get_temp()}")
print(f"Temperatura Máxima: {get_temp_max()}")
print(f"Temperatura Mínima: {get_temp_min()}")
print(f"Umidade: {get_humidity()}%")
print(f"Pressão: {get_pressure()} hPa")
print(f"Sensação Térmica: {get_feel()}")
