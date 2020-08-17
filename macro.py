import pandas as pd
from pyxlsb import open_workbook as open_xlsb
import pprint
df = []

with open_xlsb('VAT_CN_BlueTable_Macro.xlsb') as wb:
    with wb.get_sheet(1) as sheet:
        for row in sheet.rows():
            df.append([item.v for item in row])

# df = pd.DataFrame(df[1:], columns=df[0])

pprint.pprint(df)