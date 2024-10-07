import pandas as pd

def merge_csv(file1, file2, output_file):
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)
    merged_df = pd.merge(df1, df2)
    merged_df.to_csv(output_file, index=False)
    print("Données fusionnées et exportées avec succès !")

file1 = 'chemin_vers_fichier1.csv'
file2 = 'chemin_vers_fichier2.csv'
output_file = 'chemin_vers_fichier_final.csv'

merge_csv(file1, file2, output_file)




# import pandas as pd
# from pathlib import Path

# def load_data(filename, columns):
#     data_vva = Path() / f'Dataset_Clean/{filename}'
#     data = pd.read_csv(data_vva, usecols=columns)
#     print("Données chargées avec succès !")
#     return data


# df1 = pd.read_csv('Dataset_Clean/VVA_f1_data_modified7.csv')
# df2 = pd.read_csv('Dataset_Clean/VVA_weather.csv')
# df2 = df2.rename(columns={'weatherLocation': 'racename', 'weatherYear': 'year'})
# df2 = df2.round(2)

# df3 = pd.merge(df1, df2, on=['racename', 'year'])

# df3.to_csv('VVA_f1_data_final.csv', index=False)

# print("Données fusionnées et exportées avec succès !")

#merged_df = pd.merge(df1, df2, on=['racename', 'year']