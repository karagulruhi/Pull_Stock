import openpyxl
from openpyxl import Workbook,load_workbook
from datetime import date

today = date.today()

date_string = today.strftime("%d-%m-%Y")


class PufExcell:
    def __init__(self,file_path='puffstock.xlsx'):
        self.file_path = file_path
        self.book = load_workbook(filename=file_path)
        #self.sheet = self.book.create_sheet(title=date_string) if date_string not in self.book.sheetnames else self.book[date_string]#create new sheet every day
        self.sheet = self.book.active


    def save_workbook(self):
        self.book.save(self.file_path)

    
    def add_order(self,*args):
        
        if self.sheet.max_row == 1:
            self.sheet.append(('SİP_NO','EKLENME TARİHİ','İSİM', 'TELEFON NO', 'ÜRÜN', 'ADET','ÖDEME DURUMU'))        
        
        
        for i in range(self.sheet.max_row, self.sheet.max_row+1):
            print(i)
            self.sheet.append(([i] + list(args)))

        self.save_workbook()
        self.book.close() 

    
    def upload_order(self,order):
        
        self.orders=[]
        
        for row in self.sheet.iter_rows(min_row=1, min_col=1, max_row=None, max_col=2):
            for cell in row:  
                if cell.value == order:
                    print(cell.row)
                    for c in self.sheet.iter_cols(min_row=cell.row, max_row=cell.row):
                        for r in c:
                            self.orders.append(r.value)
        print(self.orders)
        self.save_workbook()
        self.book.close() 



