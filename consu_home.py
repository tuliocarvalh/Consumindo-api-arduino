import requests

#Defina a rota principal.
url = "https://9b36-187-85-94-50.sa.ngrok.io"

#Defina os parametros complementares com a funcao que retornara a rota para a execucao da tarefa.

def ligar_lamp():
    requisicao = requests.get(f"{url}/ligar_lamp")
    return requisicao

def desligar_lamp():
    requisicao = requests.get(f"{url}/desligar_lamp")
    return requisicao

