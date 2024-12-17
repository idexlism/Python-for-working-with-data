from docx import Document

document = Document('document.docx')
table = document.tables[0]
atmega328Column = 0
for i, cell in enumerate(table.rows[0].cells):
    if cell.text == 'ATmega328':
        atmega328Column = i
        break
outDict = {}
for row in table.rows[1:]:
    outDict[row.cells[0].text] = row.cells[atmega328Column].text
print(outDict)