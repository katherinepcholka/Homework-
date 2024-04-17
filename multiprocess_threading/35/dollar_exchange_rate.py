import requests

response = requests.get("https://www.nbrb.by/api/exrates/rates/431?periodicity=0")
data = response.json()
rate = data["Cur_OfficialRate"]
usd = int(input('Введите сумму в долларах: '))
byn = usd*rate
print(f"Сумма в бел.руб: {byn}\nКурс: {rate}")