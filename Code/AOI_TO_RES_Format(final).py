import pandas as pd
import numpy as np

file_path = 'C:/Users/lenovo/OneDrive/Desktop/ConvertCSVAssignment/Acres_of_Ice.csv'
df=pd.read_csv(file_path)
df.columns = ['site_name', 'measure_name', 'time', 'measure_value:varchar', 'measure_value:double', 'measure_value:bigint']
df["value"] = df[["measure_value:varchar", "measure_value:double", "measure_value:bigint"]].apply(lambda row: row.dropna().iloc[0], axis=1)
df.rename(columns={'site_name':'site_names'},inplace=True)
pivoted_df = df.pivot_table(index=["time","site_names"], columns="measure_name", values="value", aggfunc='first')
pivoted_df = pivoted_df.reset_index()
pivoted_df.columns.name = None
pivoted_df.drop(columns=['site_names'],inplace=True)
file_path = 'C:/Users/lenovo/OneDrive/Desktop/ConvertCSVAssignment/AOI_To_Res.csv'
pivoted_df.to_csv(file_path, index=False)

