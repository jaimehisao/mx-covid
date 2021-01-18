import requests  # pylint: disable=import-error

url_covid = "http://datosabiertos.salud.gob.mx/gobmx/salud/datos_abiertos/datos_abiertos_covid19.zip"
url_catalogue = "http://datosabiertos.salud.gob.mx/gobmx/salud/datos_abiertos/diccionario_datos_covid19.zip"
file_name_covid_csv = "covid.zip"
file_name_catalogue = "catalogos.xlsx"


def get_records():
    """Retrieves a PDF document from the specified URL
    Saves it as regs.pdf"""
    response = requests.get(url_covid)
    open(file_name_covid_csv, "wb").write(response.content)


def get_catalogue():
    """Retrieves a PDF document from the specified URL
    Saves it as regs.pdf"""
    response = requests.get(url_catalogue)
    open(file_name_catalogue, "wb").write(response.content)
