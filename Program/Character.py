class Character:
    def __init__(self, id_character="", name_character="", gender="", role="", hp=0, defense=0, weapon={}, skills=[]):
        self._id_character = id_character
        self._name_character = name_character
        self._gender = gender
        self._role = role
        self._hp = hp
        self._defense = defense
        self._weapon = weapon
        self._skills = skills

    # Method setter untuk set nilai setiap atribut pada kelas Character
    def set_id_character(self, id_character):
        self._id_character = id_character
        
    def set_name_character(self, name_character):
        self._name_character = name_character

    def set_gender(self, gender):
        self._gender = gender
    
    def set_role(self, role):
        self._role = role
        
    def set_hp(self, hp):
        self._hp = hp
        
    def set_defense(self, defense):
        self._defense = defense
        
    def set_weapon(self, weapon):
        self._weapon = weapon
        
    def set_skills(self, skills):
        self._skills = skills
        
    # Method getter untuk mendapatkan nilai setiap atribut pada kelas Character
    def get_id_character(self):
        return self._id_character
    
    def get_name_character(self):
        return self._name_character
    
    def get_gender(self):
        return self._gender
    
    def get_role(self):
        return self._role
    
    def get_hp(self):
        return self._hp
    
    def get_defense(self):
        return self._defense
    
    def get_weapon(self):
        return self._weapon
    
    def get_skills(self):
        return self._skills
    
        

        
    