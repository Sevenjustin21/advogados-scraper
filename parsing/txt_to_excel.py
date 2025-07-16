import openpyxl
from utils.excel_helper import create_workbook_with_headers, save_workbook

def parse_txt_to_excel():
    headers = [
        "Nome", "Conselho Regional", "Cédula", "Localidade", "Data de Inscrição",
        "Email", "Morada", "Código Postal", "Telefone", "Telemóvel", "Fax", "Fax registado"
    ]
    labels = headers[1:]  # 除去 "Nome"

    with open("data/advogados_raw.txt", "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip() and line.strip("=") != ""]

    wb, sheet = create_workbook_with_headers(headers)

    record = {}
    i = 0
    while i < len(lines):
        line = lines[i]
        if line != "Activo" and (i + 1 < len(lines) and lines[i + 1] == "Activo"):
            if record:
                row = [record.get(h, "") for h in headers]
                sheet.append(row)
            record = {"Nome": line}
            i += 2
            continue
        if line in labels and i + 1 < len(lines):
            record[line] = lines[i + 1]
            i += 2
        else:
            i += 1

    if record:
        row = [record.get(h, "") for h in headers]
        sheet.append(row)

    save_workbook(wb, "data/advogados_ativos.xlsx")
    print("\n✅ 所有数据已成功写入 data/advogados_ativos.xlsx")