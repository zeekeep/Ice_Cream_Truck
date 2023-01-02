import os
import glob
from openpyxl import load_workbook
import pandas as pd

path = '/home/abhishekraj/python/Python_Script/all_policy/'
csv_files = glob.glob(os.path.join(path, "*.xlsx"))
for f in csv_files:
    xl = pd.ExcelFile(f)
    try:
        filepath=f.split("\\")[-1]
        wb=load_workbook(filepath)
        wb.remove(wb['Sheet'])
        wb.save(filepath)
    except:
        print("file not found")