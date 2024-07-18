import requests


def get_size_parms(json_response, address_ll):

    # Получаем координаты ответа.
    org_point = address_ll
    print("Введите размеры [1] Например 0.006 -- >")
    delta1 = input()
    print("Введите размеры [2] Например 0.006 -- >")
    delta2 = input()
    # Собираем параметры для запроса к StaticMapsAPI:
    map_params = {
        "ll": address_ll,
        "spn": ",".join([delta1, delta2]),
        "l": "map",
        "pt": "{},pm2dgl".format(org_point)
    }

    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=map_params)
    return response
