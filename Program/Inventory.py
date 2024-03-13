class Inventory:
    def __init__(self, coin=0, keys=[], potions=[], weapons=[]):
        self._coin = coin
        self._keys = keys 
        self._potions = potions 
        self._weapons = weapons 

    # Method setter untuk set nilai setiap atribut pada kelas Inventory
    def set_coin(self, coin):
        self._coin = coin

    def set_keys(self, key):
        self._key = key

    def set_potions(self, potions):
        self._potions = potions

    def set_weapons(self, weapons):
        self._weapons = weapons

    # Method getter untuk mendapatkan nilai setiap atribut pada kelas Inventory
    def get_coin(self):
        return self._coin

    def get_keys(self):
        return self._keys

    def get_potions(self):
        return self._potions

    def get_weapons(self):
        return self._weapons
    
    # Method untuk coin yg dimiliki sekarang bertambah jika mendapat coin tambahan
    def tambah_coin(self, jumlah_coin):
        self._coin += jumlah_coin
        
    # Method untuk coin yg dimiliki sekarang dikurangi karena membeli sebuah item
    def kurang_coin(self, jumlah_coin):
        self._coin -= jumlah_coin

    # Method untuk menambah kunci ke inventory
    def tambah_key(self, key):
        self._keys.append(key)

    # Method untuk menambah potion ke inventory
    def tambah_potion(self, potion):
        self._potions.append(potion)

    # Method untuk menambah senjata ke inventory
    def tambah_weapon(self, weapon):
        self._weapons.append(weapon)
        
    # Method untuk menghapus kunci ke inventory
    def hapus_key(self, key):
        self._keys.remove(key)

    # Method untuk menghapus potion ke inventory
    def hapus_potion(self, potion):
        self._potions.remove(potion)

    # Method untuk menghapus senjata ke inventory
    def hapus_weapon(self, weapon):
        self._weapons.remove(weapon)
        
        
