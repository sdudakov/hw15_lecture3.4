import osa

URL = "http://www.webservicex.net/ConvertTemperature.asmx?WSDL"


def average_temperature(file_name):
    client = osa.client.Client(URL)
    celsius = 0
    count = 0
    with open(file_name, "r", encoding="utf-8") as file:
        items = file.readlines()
    for item in items:
        item = item.strip()
        item = item.split(" ")
        response = client.service.ConvertTemp(Temperature=item[0], FromUnit="degreeFahrenheit", ToUnit="degreeCelsius")
        count += 1
        celsius += float(response)
    print("Средняя температура по цельсию: {}" .format(round(celsius / count, 1)))

average_temperature("temps.txt")