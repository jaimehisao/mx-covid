import requests  # pylint: disable=import-error
from zipfile import ZipFile
import os, glob, re
import logging



url_covid = "http://datosabiertos.salud.gob.mx/gobmx/salud/datos_abiertos/datos_abiertos_covid19.zip"
url_catalogue = "http://datosabiertos.salud.gob.mx/gobmx/salud/datos_abiertos/diccionario_datos_covid19.zip"
file_name_covid_csv = "covid.zip"
file_name_catalogue = "diccionario_datos_covid19.zip"


def get_records():
    print('Getting records!')
    """Retrieves a PDF document from the specified URL
    Saves it as regs.pdf"""
    path = os.getcwd()
    os.chdir(path)
    if os.path.exists("covid.csv"):
        os.remove("covid.csv")
    if os.path.exists("covid.zip"):
        os.remove("covid.zip")

    response = requests.get(url_covid)
    open(file_name_covid_csv, "wb").write(response.content)

    # opening the zip file in READ mode
    with ZipFile(file_name_covid_csv, 'r') as zip:
        # printing all the contents of the zip file
        zip.printdir()

        # extracting all the files
        logging.info('Extracting all the files now...')
        zip.extractall()
        logging.info('Done!')

    for name in glob.glob(os.getcwd() + '/*'):
        match = re.findall(r'.csv$', name, flags=re.IGNORECASE)
        if len(match) != 0:
            logging.info(name)
            os.rename(name, os.getcwd() + '/covid.csv')
    print('records retrieved!')


def get_catalogue():
    """Retrieves a PDF document from the specified URL
        Saves it as regs.pdf"""
    response = requests.get(url_catalogue)
    open(file_name_catalogue, "wb").write(response.content)

    # opening the zip file in READ mode
    with ZipFile(file_name_catalogue, 'r') as zip:
        # printing all the contents of the zip file
        zip.printdir()

        # extracting all the files
        logging.info('Extracting all the files now...')
        zip.extractall()
        logging.info('Done! 2')

    for name in glob.glob(os.getcwd() + '/*'):
        match = re.findall(r'catalogos.xlsx$', name, flags=re.IGNORECASE)
        if len(match) != 0:
            logging.info(name)
            os.rename(name, os.getcwd() + '/catalogos.xlsx')

