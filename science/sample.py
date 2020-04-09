# data source provided by Nationale Plattform für geographische Daten (NPGEO-DE)
# https://npgeo-corona-npgeo-de.hub.arcgis.com/

import pandas 

df = pandas.read_csv('https://opendata.arcgis.com/datasets/dd4580c810204019a7b8eb3e0b329dd6_0.csv')

print (df.head())