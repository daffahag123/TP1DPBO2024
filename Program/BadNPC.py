from NPC import NPC

class BadNPC(NPC):
    def __init__(self, difficulty_level="", reward={}, status="Hidup", id_character="", name_character="", gender="", role="", hp=0, defense=0, weapon={}, skills=[], NPC_type="", location=""):
        super().__init__(NPC_type, location, id_character, name_character, gender, role, hp, defense, weapon, skills)
        self._difficulty_level = difficulty_level
        self._reward = reward 
        self._status = status
        
    # Method setter untuk set nilai setiap atribut pada kelas BadNPC
    def set_difficulty_level(self, difficulty_level):
        self._difficulty_level = difficulty_level
        
    def set_reward(self, reward):
        self._reward = reward

    def set_status(self, status):
        self._status = status
        
    # Method getter untuk mendapatkan nilai setiap atribut pada kelas BadNPC
    def get_difficulty_level(self):
        return self._difficulty_level

    def get_reward(self):
        return self._reward

    def get_status(self):
        return self._status
