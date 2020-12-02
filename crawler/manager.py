from crawler.models import Impressora
from .utils import obter_porcentagem
from bs4 import BeautifulSoup
import requests

class ImpressoraManager():
    def __init__(self, impressora_id):
        self.impressora = Impressora.objects.get(id=impressora_id)

    def obter_status(self):
        url = f"http://{self.impressora.ip}/general/status.html"
        
        try:
            pagina = requests.get(url)
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout, requests.exceptions.HTTPError):
            self.impressora.status = '0'
            self.impressora.obs = "-"
            self.impressora.nivel_toner = 0
            self.impressora.save()
            return

        soup = BeautifulSoup(pagina.text, 'html.parser')
        soup_nivel = soup.find_all(class_='tonerremain')
        
        nivel = soup_nivel[0].get("height")
        self.impressora.nivel_toner = obter_porcentagem(nivel)

        soup_status = soup.find_all(id='moni_data')
        status = soup_status[0].select_one("span")

        self.impressora.obs = status.text
        self.impressora.status = '1'
        
        self.impressora.save()