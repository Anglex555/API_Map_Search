import requests


def get_size_parms(address):
    point = address
    delta_longitude = input("Введите масштаб долготы: ")
    delta_latitude = input("Введите масштаб ширины: ")

    map_params = {
        "ll": address,
        "spn": ",".join([delta_longitude, delta_latitude]),
        "l": "map",
        "pt": "{},pm2dgl".format(point)
    }

    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=map_params)
    return response
