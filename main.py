import sys
import requests
from PIL import Image
from io import BytesIO
import map_utils


search_query = " ".join(sys.argv[1:])
geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
geocoder_params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": search_query,
    "format": "json"}
response = requests.get(geocoder_api_server, params=geocoder_params)
if not response:
    pass
json_response = response.json()
toponym = json_response["response"]["GeoObjectCollection"][
    "featureMember"][0]["GeoObject"]
toponym_coordinates = toponym["Point"]["pos"]
toponym_longitude, toponym_latitude = toponym_coordinates.split(" ")
address_ll = ",".join([toponym_longitude, toponym_latitude])
response = map_utils.get_size_parms(address_ll)
Image.open(BytesIO(response.content)).show()
