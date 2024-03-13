class Skill:
    def __init__(self, name_skill="", skill_type="", value={}):
        self._name_skill = name_skill
        self._skill_type = skill_type
        self._value = value

    # Method setter untuk set nilai setiap atribut pada kelas Skill
    def set_name_skill(self, name_skill):
        self._name_skill = name_skill

    def set_skill_type(self, skill_type):
        self._skill_type = skill_type
    
    def set_value(self, value):
        self._value = value
        
    # Method getter untuk mendapatkan nilai setiap atribut pada kelas Skill
    def get_name_skill(self):
        return self._name_skill

    def get_skill_type(self):
        return self._skill_type
    
    def get_value(self):
        return self._value
