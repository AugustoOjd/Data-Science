archivo = open('Emisiones_CO2.csv', 'r')
dicc_emisiones = {  'cod_pais' : [],
                    'nom_pais' : [],
                    'region' : [],
                    'anio' : [],
                    'co2' : [],
                    'co2_percapita' : []}

for i in archivo:
    i.strip()
    campos = i.split('|')
    dicc_emisiones['cod_pais'].append(campos[0])
    dicc_emisiones['nom_pais'].append(campos[1])
    dicc_emisiones['region'].append(campos[2])
    dicc_emisiones['anio'].append(campos[3])
    dicc_emisiones['co2'].append(campos[4])
    dicc_emisiones['co2_percapita'].append(campos[5])


# 1) cuantas variables existen
set_code_pais = set(dicc_emisiones['cod_pais'])
set_nom_pais = set(dicc_emisiones['nom_pais'])
set_region = set(dicc_emisiones['region'])
set_anio = set(dicc_emisiones['anio'])
set_co2 = set(dicc_emisiones['co2'])
set_co2_percapita = set(dicc_emisiones['co2'])

# print(len(set_nom_pais))

# 2) 


# 4) Hay datos faltantes?
validate_nan_co2 = None in dicc_emisiones['co2']
print(validate_nan_co2)

