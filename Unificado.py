#pip install pandas openpyxl
#pip install pandas
#pip install openpyxl

import os
import pandas as pd

folder_path = './ARCHIVOS'
all_data = []

for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
    #if filename.endswith('.xlsx'):
        file_path = os.path.join(folder_path, filename)
        df = pd.read_csv(file_path, delimiter='\t') 
        #df = pd.read_excel(file_path) 
        columns = df.columns
        break


for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
    #if filename.endswith('.xlsx'):
        file_path = os.path.join(folder_path, filename)
        df = pd.read_csv(file_path, delimiter='\t')
        #df = pd.read_excel(file_path)  
        #//verificar que las columnas sean iguales
        if list(df.columns) == list(columns):
            all_data.append(df)
        else:
            print(f"El archivo {filename} tiene columnas inconsistentes.")

# //Concatenar info
combined_data = pd.concat(all_data, ignore_index=False)

# //Guardar archivo unificado
output_file_path = './archivo_unificado.csv'
#output_file_path = './archivo_unificado.xlsx'
#combined_data.to_excel(output_file_path, index=False)  
combined_data.to_csv(output_file_path, index=False)