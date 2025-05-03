import pandas as pd

hospitales = pd.read_csv('/workspaces/estructura_datos/excel/Poblaci_n_atendida_en_el_Hospital_General_de_Medell_n_20250426.csv')
print(hospitales.head())
print(hospitales.dtypes)
hospitales['AÑO'] = hospitales['AÑO'].str.replace(',','')
print(hospitales.head())
print(hospitales.dtypes) 
hospitales['AÑO'] = hospitales['AÑO'].astype(int)
print(hospitales.head())
print(hospitales.dtypes) 