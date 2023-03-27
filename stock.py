import openpyxl
from openpyxl import Workbook,load_workbook
from datetime import date

today = date.today()

date_string = today.strftime("%d-%m-%Y")


class StockExcell:
    def __init__(self,file_path='puffstock.xlsx'):
        self.file_path = file_path
        self.book = load_workbook(filename=file_path)
        self.sheet = self.book.active
        self.orders = [] 
        self.row_value =None
        s_sheet = self.book.create_sheet('Stock')
    
    
        
