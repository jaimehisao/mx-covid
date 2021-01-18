import csv

import xlrd
from pymongo import MongoClient

client = MongoClient("services.hisao.org", 27017)
db = client.salud
col = db.covid

with open("covid.csv", encoding="ISO-8859-1") as csv_file:
    wb = xlrd.open_workbook("catalogos.xlsx")
    sheet = wb.sheet_by_index(0)  # Origen
    origen = {}
    for i in range(1, sheet.nrows):
        origen[str(int(sheet.cell_value(i, 0)))] = sheet.cell_value(i, 1)

    sheet = wb.sheet_by_index(1)  # Sector
    sector = {}
    for i in range(1, sheet.nrows):
        sector[str(int(sheet.cell_value(i, 0)))] = sheet.cell_value(i, 1)

    sheet = wb.sheet_by_index(2)  # Sexo
    sexo = {}
    for i in range(1, sheet.nrows):
        sexo[str(int(sheet.cell_value(i, 0)))] = sheet.cell_value(i, 1)

    sheet = wb.sheet_by_index(3)  # Tipo Paciente
    tipo_paciente = {}
    for i in range(1, sheet.nrows):
        tipo_paciente[str(int(sheet.cell_value(i, 0)))] = \
            sheet.cell_value(i, 1)

    sheet = wb.sheet_by_index(4)  # Si/No
    si_no = {}
    for i in range(1, sheet.nrows):
        si_no[str(int(sheet.cell_value(i, 0)))] = sheet.cell_value(i, 1)

    sheet = wb.sheet_by_index(5)  # Nacionalidad
    nacionalidad = {}
    for i in range(1, sheet.nrows):
        nacionalidad[str(int(sheet.cell_value(i, 0)))] = sheet.cell_value(i, 1)

    sheet = wb.sheet_by_index(6)  # Resultado Lab
    res_lab = {}
    for i in range(2, sheet.nrows):
        res_lab[str(int(sheet.cell_value(i, 0)))] = sheet.cell_value(i, 1)

    sheet = wb.sheet_by_index(7)  # Clasf Final
    clasf_final = {}
    for i in range(3, sheet.nrows):
        clasf_final[str(int(sheet.cell_value(i, 0)))] = sheet.cell_value(i, 1)

    sheet = wb.sheet_by_index(8)  # Entidades
    entidades = {}
    for i in range(1, sheet.nrows):
        entidades[str(int(sheet.cell_value(i, 0)))] = sheet.cell_value(i, 1)

    sheet = wb.sheet_by_index(9)  # Municipios
    municipios = {}

    for i in range(1, sheet.nrows):
        municipios.setdefault(str(int(sheet.cell_value(i, 2))), {})[
            str(int(sheet.cell_value(i, 0)))
        ] = sheet.cell_value(i, 1)
    print(municipios)

with open("covid.csv", encoding="ISO-8859-1") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    already_added = 0

    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            case = {}
            case["fecha_actualizado"] = row[0].strip()
            case["_id"] = row[1].strip()
            case["origen"] = origen[row[2]].strip()
            case["sector"] = sector[row[3]].strip()
            case["entidad_um"] = entidades[str(int(row[4]))].strip()
            case["sexo"] = sexo[row[5]].strip()
            case["entidad_nacimiento"] = entidades[str(int(row[6]))].strip()
            case["entidad_residencia"] = entidades[str(int(row[7]))].strip()
            try:
                case["municipio"] = municipios[str(int(row[7])).strip()][
                    str(int(row[8]))
                ].strip()
            except Exception:
                case["municipio"] = "NO ESPECIFICADO"
            case["tipo_paciente"] = tipo_paciente[row[9]].strip()
            case["fecha_ingreso"] = row[10].strip()
            case["fecha_sintomas"] = row[11].strip()
            case["fecha_defuncion"] = row[12].strip()
            case["intubado"] = si_no[row[13]].strip()
            case["neumonia"] = si_no[row[14]].strip()
            case["edad"] = row[15].strip()
            case["nacionalidad"] = nacionalidad[row[16]].strip()
            case["embarazo"] = si_no[row[17]].strip()
            case["habla_lengua_indigena"] = si_no[row[18]].strip()
            case["indigena"] = si_no[str(int(row[19]))].strip()
            case["diabetes"] = si_no[row[20]].strip()
            case["epoc"] = si_no[row[21]].strip()
            case["asma"] = si_no[row[22]].strip()
            case["inmusupr"] = si_no[row[23]].strip()
            case["hipertension"] = si_no[row[24]].strip()
            case["otra_com"] = si_no[row[25]].strip()
            case["cardiovascular"] = si_no[row[26]].strip()
            case["na"] = si_no[row[27]].strip()
            case["renal_cronica"] = si_no[row[28]].strip()
            case["tabaquismo"] = si_no[row[29]].strip()
            case["otro_caso"] = si_no[row[30]].strip()
            case["toma_muestra"] = si_no[row[31]].strip()
            case["resultado"] = res_lab[row[32]].strip()
            case["clasificacion"] = clasf_final[row[33]].strip()
            case["migrante"] = si_no[str(int(row[34]))].strip()
            case["pais_nacionalidad"] = row[35].strip()
            if row[36] == "97":
                case["pais_origen"] = "Mexico"
            else:
                case["pais_origen"] = row[36].strip()
            case["uci"] = si_no[row[37]].strip()
            res = col.find({"_id": case["_id"]}).count()
            if res != 0:
                col.insert_one(case)
                already_added += 1
            else:
                line_count += 1
            print("New entries: " + line_count)
            print("Already added entries: " + already_added)
