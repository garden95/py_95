
from openpyxl import *
from openpyxl.styles import PatternFill

#셀 배경 색 바꾸기

wb = Workbook()
ws = wb.active

#헤더
ws['A1'] = '이름'
ws['B1'] = '국어'
ws['C1'] = '수학'

color = PatternFill(fill_type = 'solid', fgColor = 'FF0000')

#반복을 통해 셍의 배경색 바꾸기

for cell in ws [1]: #1행 전체
    cell.fill = color

wb.save('test_1/bg_color.xlsx')