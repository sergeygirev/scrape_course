import xlsxwriter
from main import array
def writer(parametr):
    book =  xlsxwriter.Workbook('books.xlsx')
    page = book.add_worksheet('items')
    
    row = 0
    coloumn = 0
    
    page.set_column('A:A', 70)
    page.set_column('B:B', 50)
    page.set_column('C:C', 100) 
    
    for item in parametr():
        page.write(row, coloumn, item['name'])
        page.write(row, coloumn + 1, item['price'])
        page.write(row, coloumn + 2, item['url_img'])
        row += 1
    
    book.close()
writer(array())