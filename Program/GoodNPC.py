from NPC import NPC

class GoodNPC(NPC):
    def __init__(self, quest=[], inventory={}, id_character="", name_character="", gender="", role="", hp=0, defense=0, weapon={}, skills=[], NPC_type="", location=""):
        super().__init__(NPC_type, location, id_character, name_character, gender, role, hp, defense, weapon, skills)
        self._quest = quest
        self._inventory = inventory

    # Method setter untuk set nilai setiap atribut pada kelas GoodNPC
    def set_quest(self, quest):
        self._quest = quest
        
    def set_inventory(self, inventory):
        self._inventory = inventory
        
    # Method getter untuk mendapatkan nilai setiap atribut pada kelas GoodNPC
    def get_quest(self):
        return self._quest
    
    def get_inventory(self):
        return self._inventory
    
    
    
    
