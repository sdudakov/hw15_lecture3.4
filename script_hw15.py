import osa

URL1 = "http://www.webservicex.net/ConvertTemperature.asmx?WSDL"
URL2 = "http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL"
URL3 = "http://www.webservicex.net/length.asmx?WSDL"


def average_temperature(file_name):
    client = osa.client.Client(URL1)
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
    print("Средняя температура по цельсию: {}\n".format(round(celsius / count, 1)))


def trip_cost(file_name):
    client = osa.client.Client(URL2)
    total_cost = 0
    with open(file_name, "r", encoding="utf-8") as file:
        items = file.readlines()
    for item in items:
        item = item.strip()
        item = item.split(" ")
        response = client.service.ConvertToNum(fromCurrency=item[2], toCurrency="RUB", amount=int(item[1]),
                                               rounding=True)
        print("Стоимость перелета в рублях {} {}".format(item[0], round(response)))
        total_cost += response
    print("\nОбщая стоимость путешествия в рублях {} \n".format(round(total_cost)))


def trip_length(file_name):
    client = osa.client.Client(URL3)
    total_length = 0
    with open(file_name, "r", encoding="utf-8") as file:
        items = file.readlines()
    for item in items:
        item = item.strip()
        item = item.split(" ")
        length_in_miles = float(item[1].replace(',',''))
        response = client.service.ChangeLengthUnit(LengthValue=length_in_miles, fromLengthUnit="Miles", toLengthUnit="Kilometers")
        print("Длинна пути в километрах {} {}".format(item[0], round(response, 2)))
        total_length += response
    print("\nСуммарное расстояние пути в километрах {} ".format(round(total_length, 2)))

average_temperature("temps.txt")
trip_cost("currencies.txt")
trip_length("travel.txt")
