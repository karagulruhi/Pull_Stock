from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from functools import partial
from kivy.uix.textinput import TextInput

from puffExcel import PufExcell


puff_excel = PufExcell()


class MainScreen(Screen):
   
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)




class SearchScreen(Screen):
    def __init__(self, **kwargs):
        super(SearchScreen, self).__init__(**kwargs)
        
    def get_order(self):
        orders = puff_excel.find_order_excel(self.ids.name_search.text)
        # Sadece bir sipariş varsa, bu siparişi bir liste içine yerleştirin

        return orders
            
class ChooseOrderScreen(Screen):        
    def __init__(self, **kwargs):
        super(ChooseOrderScreen, self).__init__(**kwargs)
        self.orders = []
        self.create_buttons()
        
    def on_enter(self):
       
        search_screen = self.manager.get_screen('search')
        self.orders = search_screen.get_order()
        
        self.create_buttons()

    def create_buttons(self):
        layout = BoxLayout(orientation='vertical')
        for order in self.orders:
            print(order)
            id = ''.join(str(i) for i in order[0:2])
            text='***'.join(str(i) for i in order[0:7])
            btn = Button(text=text)
            btn.id = id
            btn.size_hint = (0.9, 0.5)
            btn.pos_hint = {'center_x': 0.5, 'center_y': 1}
            btn.bind(on_press=partial(self.switch_to_next_screen, order=order))
            btn.background_color = (0., 0.4, 0.4, 1)
            layout.add_widget(btn)
   
        self.add_widget(layout)
    def switch_to_next_screen(self, instance,order):
        print(order)
        self.manager.current = 'update'
        columns=[['isim_u',order[1]],['telefon_no_u',order[2]],['urun_u',order[3]],['adet_u',order[4]],['note_u',order[5]],['pay_info_button_u',order[6]]]
        # order_infos= [order[1],order[2],order[4],order[5]]
        for column in columns:
            self.manager.get_screen('update').ids[f"{column[0]}"].text= column[1]
            
        if str(order[6]) == 'ÖDEME ALINDI':
        
            self.manager.get_screen('update').ids.pay_info_button_u.background_color= 0.0, 1.0, 0.0, 1.0
        else:
             
            self.manager.get_screen('update').ids.pay_info_button_u.background_color= 1.0, 0.0, 0.0, 1.0
        send_row= order[0]+1
        
        puff_excel.saving_private_row(send_row)
    
    
        
    
    
class UpdateOrderScreen(Screen):
    def __init__(self, **kwargs):
        super(UpdateOrderScreen, self).__init__(**kwargs)               
    def paymentInfo_u(self):
        self.current_color = self.ids.pay_info_button_u.background_color
        
        if self.current_color == [1.0, 0.0, 0.0, 1.0]:
            self.ids.pay_info_button_u.background_color = 0.0, 1.0, 0.0, 1.0
            self.ids.pay_info_button_u.text = "ÖDEME ALINDI"
        elif self.current_color == [0.0, 1.0, 0.0, 1.0]:
            self.ids.pay_info_button_u.background_color = 1.0, 0.0, 0.0, 1.0
            self.ids.pay_info_button_u.text = "ÖDEME ALINMADI"

    
    def update_order(self):
        
        
        puff_excel.update_order_excel(self.ids.isim_u.text,self.ids.telefon_no_u.text,self.ids.urun_u.text,self.ids.adet_u.text,self.ids.note_u.text,self.ids.pay_info_button_u.text)
        # print(self.orders)
    
    def dalete_order(self):
        puff_excel.update_order_excel(self.ids.isim_u.text,self.ids.telefon_no_u.text,self.ids.urun_u.text,self.ids.adet_u.text,self.ids.note_u.text,self.ids.pay_info_button_u.text)


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


        
    # def update_order(self):
      

        















class PuffStock(App):
    
    def build(self):
        Builder.load_file("puffstock.kv")
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(NewOrderScreen(name='new'))
        sm.add_widget(SearchScreen(name='search'))
        sm.add_widget(ChooseOrderScreen(name='choose'))
        sm.add_widget(UpdateOrderScreen(name='update'))

        return sm




if __name__ == '__main__':
    PuffStock().run()
