import openpyxl
from openpyxl import Workbook,load_workbook
from datetime import date

today = date.today()

date_string = today.strftime("%d-%m-%Y")


class StockExcell:
    def __init__(self,file_path='puffstock.xlsx'):
        self.file_path = file_path
        self.book = load_workbook(filename=file_path)
        if "Stock" in self.book.sheetnames:
            self.s_sheet = self.book["Stock"]
        else:
            self.s_sheet = self.book.create_sheet("Stock")
            self.s_sheet.append(('TÜR', 'ADET'))
    def save_workbook(self):
        self.book.save(self.file_path)

    
    def add_stock(self,*args):   

        for i in range(self.s_sheet.max_row, self.s_sheet.max_row+1):
            self.s_sheet.append(args)

            self.save_workbook()
     
        # for i in range(self.sheet.max_row, self.sheet.max_row+1):
            