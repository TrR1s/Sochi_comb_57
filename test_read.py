import pandas as pd
from utils import read_json
from core.config import CSV_FILES_PATH


comb5= read_json()
print(len(comb5))
print(comb5)
comb5_flat_dict_list =[]
for key, (name, nn) in comb5.items():
    comb5_flat_dict_list.append(
        {
            'str_key': key,
            'name':name,
            'nn':nn,
            
        }
    )
df = pd.DataFrame(comb5_flat_dict_list)
df.set_index('nn')
file_name='comb5.csv'
df.to_csv(f'{CSV_FILES_PATH}/{file_name}',index=False)
print(df)