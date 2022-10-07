"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd
import numpy as np
import sys
import re

def format_date(str_date):
    d = re.search(r'(^\d+)\/(\d+)\/(\d+)', str_date, re.IGNORECASE)
    day = d.group(1)
    month = d.group(2)
    year = d.group(3)
    if len(day)>2:
        date = year + '/' + month + '/' + day
        return date
    else:
        date = day + '/' + month + '/' + year
        return date

# def limpiar_data(data):
#     data = [row.replace('\n','') for row in data]
#     # data = [line.strip() for line in data]
#     # data = [row.split(';') for row in data]
#     data = [row[1:] for row in data]
#     head = data[0]
#     data = data[1:]
#     data = [re.sub(r'_|-', ' ', str(line)) for line in data]
#     data = [re.sub(r'\$', '', line) for line in data]
#     # # # data = [re.sub(re.search('\d(,)\d',line).group(1), '', line) for line in data]
#     data = [line.lower() for line in data]
#     data = [line.split(';') for line in data]
#     data = [line[1:] for line in data]
#     data = [[row.strip() for row in line] for line in data]
#     # data = [[i[0], i[1], i[2],i[3],i[4],i[]]
#     for i in data:
#         i[6] = format_date(i[6])
#     head = head.split(';')
#     # head = head[1:]
#     return head, data
# # df = pd.read_csv("solicitudes_credito.csv", sep=";")
# def clean_data():

#     with open('solicitudes_credito.csv', encoding="utf-8") as file:
#         data = file.readlines()

#     head, data = limpiar_data(data)
#     df = pd.DataFrame(data, columns=head)
#     df = df.replace('', np.nan)
#     df.fecha_de_beneficio = pd.to_datetime(df.fecha_de_beneficio, dayfirst=True)
#     df.estrato = df.estrato.map(lambda x: int(x))
#     df.comuna_ciudadano = pd.to_numeric(df['comuna_ciudadano'], errors='coerce').apply(np.floor).astype('float64')
#     # # 

#     df.monto_del_credito = df.monto_del_credito.str.replace(',','')
#     df.monto_del_credito = df.monto_del_credito.map(lambda x:float(x))
#     df.comuna_ciudadano = df.comuna_ciudadano.map(lambda x: float(x))
#     df.drop_duplicates(inplace=True)
#     df.dropna(inplace=True, how='any')

#     return df

# clean_data()

def clean_data():
    df = pd.read_csv('solicitudes_credito.csv', sep=';')
    df= df[df.columns[1:]]
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)

    for i in df.columns:
        try:
            df[i] = df[i].str.lower()
            # df[i] = df[i].str.strip()
        except:
            pass
    df.idea_negocio = df.idea_negocio.map(lambda x: re.sub(r'_|-', ' ', str(x)))
    df.barrio = df.barrio.map(lambda x: re.sub(r'-', ' ', str(x)))
    df.barrio = df.barrio.map(lambda x: re.sub(r'\s', '_', str(x)))
    df.fecha_de_beneficio = df.fecha_de_beneficio.apply(format_date)
    df.monto_del_credito = df.monto_del_credito.map(lambda x: re.sub(r'\$', '', str(x)))
    df.monto_del_credito = df.monto_del_credito.map(lambda x: float(x.replace(',', '')))
    df['línea_credito'] = df['línea_credito'].map(lambda x: re.sub(r'_|-', ' ', str(x)))
    for i in df.columns:
        try:
            df[i] = df[i].str.lower()
            df[i] = df[i].str.strip()
        except:
            pass
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)
    return df