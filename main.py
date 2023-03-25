from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from puffExcel import PufExcell

puff_excel = PufExcell()


class MainScreen(Screen):
   
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)




class SearchScreen(Screen):
    def __init__(self, **kwargs):
        super(SearchScreen, self).__init__(**kwargs)
    def get_order(self):
         puff_excel.upload_order(self.ids.name_search.text)




class UpdateOrderScreen(Screen):
    def __init__(self, **kwargs):
        super(UpdateOrderScreen, self).__init__(**kwargs)
    def get_order(self):
         puff_excel.upload_order(self.ids.name_search.text)
 

class NewOrderScreen(Screen):
    def __init__(self, **kwargs):
        super(NewOrderScreen, self).__init__(**kwargs)

    def paymentInfo(self):
        self.current_color = self.ids.pay_info_button.background_color
        
        if self.current_color == [1.0, 0.0, 0.0, 1.0]:
            self.ids.pay_info_button.background_color = 0.0, 1.0, 0.0, 1.0
            self.ids.pay_info_button.text = "ÖDEME ALINDI"
        elif self.current_color == [0.0, 1.0, 0.0, 1.0]:
            self.ids.pay_info_button.background_color = 1.0, 0.0, 0.0, 1.0
            self.ids.pay_info_button.text = "ÖDEME ALINMADI"

    def add_new_order(self):
  
        puff_excel.add_order(self.ids.isim.text,self.ids.telefon_no.text,self.ids.urun.text,self.ids.adet.text,self.ids.note.text,self.ids.pay_info_button.text )

















class PuffStock(App):
    
    def build(self):

        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(NewOrderScreen(name='new'))
        sm.add_widget(SearchScreen(name='search'))
        sm.add_widget(UpdateOrderScreen(name='update'))

        return sm




if __name__ == '__main__':
    PuffStock().run()
