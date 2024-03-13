from Attack import Attack
from Heal import Heal

class Weapon:
    def __init__(self, item_type="", name_weapon="", weapon_type="", value={}, price=0):
        self._item_type = item_type
        self._name_weapon = name_weapon
        self._weapon_type = weapon_type
        self._value = value
        self._price = price

    # Method setter untuk set nilai setiap atribut pada kelas Weapon
    def set_item_type(self, item_type):
        self._item_type = item_type
        
    def set_name_weapon(self, name_weapon):
        self._name_weapon = name_weapon

    def set_weapon_type(self, weapon_type):
        self._weapon_type = weapon_type
    
    def set_value(self, value):
        self._value = value
        
    def set_price(self, price):
        self._price = price
        
    # Method getter untuk mendapatkan nilai setiap atribut pada kelas Weapon
    def get_item_type(self):
        return self._item_type
    
    def get_name_weapon(self):
        return self._name_weapon

    def get_weapon_type(self):
        return self._weapon_type
    
    def get_value(self):
        return self._value
    
    def get_price(self):
        return self._price
    
        
