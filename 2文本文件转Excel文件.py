from random import choices
from openpyxl import Workbook

def generate(txtFileName):
    with open(txtFileName, 'w') as fp:
        fp.write('field1,field2,field3,field4\n')
        for _ in range(20):
            line = choices(range(100), k=4)
            fp.write(','.join(map(str, line))+'\n')
        
def main(txtFileName):
    new_XlsxFileName = txtFileName[:-3] + 'xlsx'
    wb = Workbook()
    ws = wb.worksheets[0]
    with open(txtFileName) as fp:
        for line in fp:
            line = line.strip().split(',')
            ws.append(line)
    wb.save(new_XlsxFileName)

fn = 'test.txt'
generate(fn)
main(fn)

