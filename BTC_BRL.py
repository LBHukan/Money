import requests
import json
import time
import datetime



def BTC():
    requisicao = requests.get("https://www.eobot.com/api.aspx?coin=BTC")
    text = json.loads(requisicao.text)
    return text

def BRL():
    requisicao = requests.get("https://www.eobot.com/api.aspx?coin=BRL")
    text = json.loads(requisicao.text)
    return text


while True:
    hora_atual = datetime.datetime.now()
    print("*********************", hora_atual, "*********************")
    print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    print("############Cotacao BitCoins: R$ %.4f" %(BRL()*BTC()),"##########################")
    print("############Cotacao BRL: R$ %.2f" %BRL(),"#####################################")
    print("######################################################################")
time.sleep(30)
