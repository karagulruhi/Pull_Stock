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
        self.orders = [] 

    def save_workbook(self):
        self.book.save(self.file_path)

    
    def add_order(self,*args):
        
        if self.sheet.max_row == 1:
            self.sheet.append(('SİP_NO','İSİM', 'TELEFON NO', 'ÜRÜN', 'ADET','ÖDEME DURUMU','SİPARİŞ TARİHİ','NOT'))        
        
        
        for i in range(self.sheet.max_row, self.sheet.max_row+1):
            print(i)
            self.sheet.append(([i] + list(args)+[date_string]))

        self.save_workbook()
        self.book.close() 

    
    def update_order_excel(self,order):
        
        
        if len(self.orders)==0:
            for row in self.sheet.iter_rows(min_row=1, min_col=1, max_row=None, max_col=2):
                
                temp_orders=[]
                for cell in row:  
                    
                    if cell.value == order:
                        
                        
                        for c in self.sheet.iter_cols(min_row=cell.row, max_row=cell.row):
                            
                            for r in c:
                                
                                
                                temp_orders.append(r.value)
                            
                        self.orders.append(temp_orders)
                            
        self.save_workbook()
        self.book.close() 
        
        return self.orders



