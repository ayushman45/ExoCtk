import requests
from bs4 import BeautifulSoup

class ExoCtk:
    def __init__(self) -> None:
        self.URL="https://exoctk.stsci.edu/generic?temperature={}&gravity={}&r_planet={}&r_star={}&condensation=local&metallicity=%2B0.0&c_o=0.35&haze=0001&cloud=0.00"
    def generate_values(self,temp,g,r_planet,r_star):
        response = requests.get(self.URL.format(temp,g,r_planet,r_star))
        try:
            soup = BeautifulSoup(response.content, 'html.parser')
            input_tag = soup.find_all("input")
            data_file = None
            for i in input_tag:
                if i.get("name")=="data_file":
                    data_file=i.get("value")
                    break
            return data_file
        except:
            return None