import pandas as pd

file = "data/raw/ethiopia_fi_unified_data.xlsx"

excel = pd.ExcelFile(file)

print(excel.sheet_names)
