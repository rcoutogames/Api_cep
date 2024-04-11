import requests
import json

cep = int(input("Digite seu Cep"))

link = (f'https://cep.awesomeapi.com.br/json/{cep}') 

zip_code = requests.get(link)
 
print(zip_code)

print(zip_code.json())