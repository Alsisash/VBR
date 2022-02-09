from pandas import *

def vozvrat_tel():
    for key, value in slov_tel.items():
        print(str(value))

        # return str(value)



xls = ExcelFile('ForViber_1.xlsx')
df = xls.parse(xls.sheet_names[0])
a = df.to_dict()
slov_tel = a['telephon']
vozvrat_tel()
