import openpyxl

def create_workbook_with_headers(headers):
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = "Advogados"
    sheet.append(headers)
    return wb, sheet

def save_workbook(wb, filepath):
    wb.save(filepath)