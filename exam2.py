from openpyxl import *

# == 시트 생성 ==
w2 = load_workbook('test.xlsx')

# 새로운 시트 하나 생성

new_ws = w2.create_sheet()

#새로만큰 시트의 이름 설정
#기본이름 sheet1 sheet2
new_ws.title = '마지막_시트'

#변경사항 저장
w2.save('test.xlsx')