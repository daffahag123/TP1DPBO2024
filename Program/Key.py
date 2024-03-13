class Key:
    def __init__(self, item_type="", name_key="", key_type="", price=0):
        self._item_type = item_type
        self._name_key = name_key
        self._key_type = key_type
        self._price = price

    # Method setter untuk set nilai setiap atribut pada kelas Key
    def set_item_type(self, item_type):
        self._item_type = item_type
        
    def set_name_key(self, name_key):
        self._name_key = name_key

    def set_key_type(self, key_type):
        self._key_type = key_type
        
    def set_price(self, price):
        self._price = price
        
    # Method getter untuk mendapatkan nilai setiap atribut pada kelas Key
    def get_item_type(self):
        return self._item_type
    
    def get_name_key(self):
        return self._name_key

    def get_key_type(self):
        return self._key_type

    def get_price(self):
        return self._price
