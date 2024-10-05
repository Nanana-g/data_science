import pandas as pd

data_2022 = pd.read_excel(r'C:\Users\vique\OneDrive\Documentos\Python Scripts\data_science\estadsticaspoliciales2022_modificado.xlsx')
data_2023 = pd.read_excel(r'C:\Users\vique\OneDrive\Documentos\Python Scripts\data_science\estadsticaspoliciales2023_modificado.xlsx')

print("Lo siguiente es el head del 2022 para probar si funciona")
print(data_2022.head()) #si funciona? si funciona
print("𓆝 𓆟 𓆞 𓆝 𓆟 𓆝 𓆟 𓆞 𓆝 𓆟 𓆝 𓆟 𓆞 𓆝 𓆟 𓆝 𓆟 𓆞 𓆝 𓆟 𓆝 𓆟 𓆞 𓆝 𓆟 𓆝 𓆟 𓆞 𓆝 𓆟 𓆝 𓆟 𓆞 𓆝 𓆟 𓆝 𓆟 𓆞 𓆝 𓆟 𓆝 𓆟 𓆞 𓆝 𓆟")


#info básica de los datos
print("Lo siguiente es la info básica (num de filas, columnas, tipo de datos y valores faltantes)")
print(data_2022.info())
print(data_2023.info()) 
print("𓆝 𓆟 𓆞 𓆝 𓆟 𓆝 𓆟 𓆞 𓆝 𓆟 𓆝 𓆟 𓆞 𓆝 𓆟 𓆝 𓆟 𓆞 𓆝 𓆟 𓆝 𓆟 𓆞 𓆝 𓆟 𓆝 𓆟 𓆞 𓆝 𓆟 𓆝 𓆟 𓆞 𓆝 𓆟 𓆝 𓆟 𓆞 𓆝 𓆟 𓆝 𓆟 𓆞 𓆝 𓆟")


#conteo de valores originales y typos de las columnas
print(data_2022['Delito'].value_counts())
print(data_2023['Delito'].value_counts())

#arreglar typos (mayusculas y espacios en blanco al principio y al final)
data_2022['Delito_clean'] = data_2022['Delito'].str.upper().str.strip()
data_2023['Delito_clean'] = data_2023['Delito'].str.upper().str.strip()
print("── .✦ ── .✦ ── .✦ ── .✦ ── .✦ ── .✦ ── .✦ ── .✦ ── .✦ ── .✦ ── .✦ ── .✦ ── .✦ ── .✦")
print(data_2022['Delito_clean'])
print(data_2023['Delito_clean'])

print("𓆝 𓆟 𓆞 𓆝 𓆟 𓆝 𓆟 𓆞 𓆝 𓆟 𓆝 𓆟 𓆞 𓆝 𓆟 𓆝 𓆟 𓆞 𓆝 𓆟 𓆝 𓆟 𓆞 𓆝 𓆟 𓆝 𓆟 𓆞 𓆝 𓆟 𓆝 𓆟 𓆞 𓆝 𓆟 𓆝 𓆟 𓆞 𓆝 𓆟 𓆝 𓆟 𓆞 𓆝 𓆟 ")

#comparar los delitos de cada año por valores únicos
delito_2022 = data_2022['Delito_clean'].unique()
delito_2023 = data_2023['Delito_clean'].unique()

print(set(delito_2022) - set(delito_2023))
print(set(delito_2023) - set(delito_2022))
print("𓆝 𓆟 𓆞 𓆝 𓆟 𓆝 𓆟 𓆞 𓆝 𓆟 𓆝 𓆟 𓆞 𓆝 𓆟 𓆝 𓆟 𓆞 𓆝 𓆟 𓆝 𓆟 𓆞 𓆝 𓆟 𓆝 𓆟 𓆞 𓆝 𓆟 𓆝 𓆟 𓆞 𓆝 𓆟 𓆝 𓆟 𓆞 𓆝 𓆟 𓆝 𓆟 𓆞 𓆝 𓆟 ")


#comparar por meses
data_2022['Fecha'] = pd.to_datetime(data_2022['Fecha'])
data_2023['Fecha'] = pd.to_datetime(data_2023['Fecha'])
data_2022['Mes'] = data_2022['Fecha'].dt.month
data_2023['Mes'] = data_2023['Fecha'].dt.month

data_2022_filtered = data_2022[data_2022['Mes'] <= 8]


#la unica forma que pense hacer las correcciones en cod
correcciones_delito= {
    'DELITOS CONTRA LA PROPIEDADDDDDDDDDDD': 'DELITOS CONTRA LA PROPIEDAD',
    'DELITOS CONTRA LA PROPIEDAAAAAAD': 'DELITOS CONTRA LA PROPIEDAD',
    'DELITOS CONTRA LA VIDAAAA': 'DELITOS CONTRA LA VIDA',
    'DELITOS CONTRA LA LIBERTAD LIBERTAD': 'DELITOS CONTRA LA LIBERTAD',
    'DELITOS CONTRA LA VIDA VIDA VISA': 'DELITOS CONTRA LA VIDA',
    'DELITS SEXUALES': 'DELITOS SEXUALES',
    'OTROS OTROS DELITOS': 'OTROS DELITOS',
    'DELITOS DELITOS  DELITOS CONTRA LA PROPIEDAD': 'DELITOS CONTRA LA PROPIEDAD',
    'DELITOS CONTRA LA PROPIEDADDDDDDD': 'DELITOS CONTRA LA PROPIEDAD',
    'DLITOS INFORMATICOS': 'DELITOS INFORMATICOS',
    'DELITOS CONTRA LA VIDAHOLA': 'DELITOS CONTRA LA VIDA',
    'NO DELITO NO DELITOOOOOOOOOOOOOOO': 'NO DELITO',
    'DELITOSSSSS SEXUALES': 'DELITOS SEXUALES',
    'DELITOS CONTRA LA VIDA LA VIDA LA VIDA': 'DELITOS CONTRA LA VIDA',
    'DELITOS CONTRA LA PROPIEDA': 'DELITOS CONTRA LA PROPIEDAD',
    'OTROS DELITOS CONTRA LA PRRRROPIEDAD': 'OTROS DELITOS CONTRA LA PROPIEDAD',
    'DELITOS CONTRA LA LIBERTADSSSSSSS': 'DELITOS CONTRA LA LIBERTAD',
    'ESTAFAS Y OTRAS DEFRAUDACIONESSWWW': 'ESTAFAS Y OTRAS DEFRAUDACIONES',
    'ESTAFAS Y OTRAS DEFRAUDACIONES YEI': 'ESTAFAS Y OTRAS DEFRAUDACIONES'
}

data_2022['Delito'] = data_2022['Delito'].replace(correcciones_delito)
data_2023['Delito'] = data_2023['Delito'].replace(correcciones_delito)

#rev.
print(data_2022['Delito'].unique())
print(data_2023['Delito'].unique())
print("𓆝 𓆟 𓆞 𓆝 𓆟 𓆝 𓆟 𓆞 𓆝 𓆟 𓆝 𓆟 𓆞 𓆝 𓆟 𓆝 𓆟 𓆞 𓆝 𓆟 𓆝 𓆟 𓆞 𓆝 𓆟 𓆝 𓆟 𓆞 𓆝 𓆟 𓆝 𓆟 𓆞 𓆝 𓆟 𓆝 𓆟 𓆞 𓆝 𓆟 𓆝 𓆟 𓆞 𓆝 𓆟 ")


#guardar los cambios
data_2022.to_excel(r'C:\Users\vique\Descargas\OIJ_2022_LIMPIO.xlsx', index=False)
data_2023.to_excel(r'C:\Users\vique\Descargas\OIJ_2023_LIMPIO.xlsx', index=False)