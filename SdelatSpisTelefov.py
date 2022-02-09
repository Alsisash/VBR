from pandas import *


xls = ExcelFile('ForViber_1.xlsx')
df = xls.parse(xls.sheet_names[0])
a = df.to_dict()
slov_tel = a['telephon']
spisTel = []
for key, value in slov_tel.items():
    spisTel.append(value)
print(spisTel)
it = iter(spisTel)
print(it)
# return next(it)