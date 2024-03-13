class Heal:
    def __init__(self, heal=0, defense=0):
        self._heal = heal
        self._defense = defense

    # Method setter untuk set nilai setiap atribut pada kelas Heal
    def set_heal(self, heal):
        self._heal = heal

    def set_defense(self, defense):
        self._defense = defense
        
    # Method getter untuk mendapatkan nilai setiap atribut pada kelas Heal
    def get_heal(self):
        return self._heal

    def get_defense(self):
        return self._defense
