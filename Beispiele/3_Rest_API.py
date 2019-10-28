#pokeloader
#Beispiel für REST api calls

import requests
import json

from PIL import Image
from io import BytesIO

pokemon = '10'

url = 'https://pokeapi.co/api/v2/pokemon/'
call = requests.get(url+pokemon)
json = json.loads(call.content)

imgURL = json['sprites']['front_default']
response = requests.get(imgURL)
img = Image.open(BytesIO(response.content))

img.show()