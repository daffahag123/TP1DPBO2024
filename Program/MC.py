from Character import Character

class MC(Character):
    def __init__(self, level=1, exp=0, inventory={}, id_character="", name_character="", gender="", role="", hp=0, defense=0, weapon={}, skills=[]):
        super().__init__(id_character, name_character, gender, role, hp, defense, weapon, skills)
        self._level = level
        self._exp = exp
        self._inventory = inventory

    # Method setter untuk set nilai setiap atribut pada kelas MC
    def set_level(self, level):
        self._level = level

    def set_exp(self, exp):
        self._exp = exp

    def set_inventory(self, inventory):
        self._inventory = inventory

    # Method getter untuk mendapatkan nilai setiap atribut pada kelas MC
    def get_level(self):
        return self._level

    def get_exp(self):
        return self._exp

    def get_inventory(self):
        return self._inventory
    
    # Method jika mendapatkan exp, level karakter akan bertambah
    def tambah_exp(self, exp):
        self._exp += exp
        if self._exp >= 100:
            self._level += 1
            self._exp -= 100
            print(f"Selamat! karakter kamu naik ke level {self._level}!")
            
    
