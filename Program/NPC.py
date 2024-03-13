from Character import Character

class NPC(Character):
    def __init__(self, NPC_type="", location="", id_character="", name_character="", gender="", role="", hp=0, defense=0, weapon={}, skills=[]):
        super().__init__(id_character, name_character, gender, role, hp, defense, weapon, skills)
        self._NPC_type = NPC_type
        self._location = location

    # Method setter untuk set nilai setiap atribut pada kelas NPC
    def set_NPC_type(self, NPC_type):
        self._NPC_type = NPC_type

    def set_location(self, location):
        self._location = location

    # Method getter untuk mendapatkan nilai setiap atribut pada kelas NPC
    def get_NPC_type(self):
        return self._NPC_type

    def get_location(self):
        return self._location
