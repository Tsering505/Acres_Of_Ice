import pandas as pd
import numpy as np
import datetime

file_path = 'C:/Users/lenovo/OneDrive/Desktop/ConvertCSVAssignment/Results (1).csv'
df=pd.read_csv(file_path)
df['time']=pd.to_datetime(df['time'], unit='ms').dt.strftime('%Y-%m-%d %H:%M:%S.%f')
df['site_names']=df['site_name']

unpiv_df = df.melt(id_vars=["time", "site_names"],var_name="measure_name",value_name="value",)
unpiv_df["measure_value:varchar"] = np.where(unpiv_df["value"].apply(lambda x: isinstance(x, str)), unpiv_df["value"], np.nan)
unpiv_df["measure_value:double"] = np.where(unpiv_df["value"].apply(lambda x: isinstance(x, float)), unpiv_df["value"], np.nan)
unpiv_df["measure_value:bigint"] = np.where(unpiv_df["value"].apply(lambda x: isinstance(x, int)), unpiv_df["value"], np.nan)
unpiv_df = unpiv_df[["site_names", "measure_name", "time", "measure_value:varchar", "measure_value:double", "measure_value:bigint"]]

file_path = 'C:/Users/lenovo/OneDrive/Desktop/ConvertCSVAssignment/Res_To_AOI.csv'
unpiv_df.to_csv(file_path, index=False)






