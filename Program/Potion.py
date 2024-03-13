class Potion:
    def __init__(self, item_type="", name_potion="", potion_type="", value={}, price=0):
        self._item_type = item_type
        self._name_potion = name_potion
        self._potion_type = potion_type
        self._value = value
        self._price = price

    # Method setter untuk set nilai setiap atribut pada kelas Potion
    def set_item_type(self, item_type):
        self._item_type = item_type
    
    def set_name_potion(self, name_potion):
        self._name_potion = name_potion

    def set_potion_type(self, potion_type):
        self._potion_type = potion_type
    
    def set_value(self, value):
        self._value = value
        
    def set_price(self, price):
        self._price = price
        
    # Method getter untuk mendapatkan nilai setiap atribut pada kelas Potion
    def get_item_type(self):
        return self._item_type
    
    def get_name_potion(self):
        return self._name_potion

    def get_potion_type(self):
        return self._potion_type
    
    def get_value(self):
        return self._value
    
    def get_price(self):
        return self._price
