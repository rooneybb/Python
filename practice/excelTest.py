import openpyxl
wb = openpyxl.load_workbook('example.xlsx')
type(wb)
print(wb.get_sheet_names())

