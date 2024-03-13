class Attack:
    def __init__(self, attack=0, damage=0):
        self._attack = attack
        self._damage = damage

    # Method setter untuk set nilai setiap atribut pada kelas Attack
    def set_attack(self, attack):
        self._attack = attack

    def set_damage(self, damage):
        self._damage = damage
        
    # Method getter untuk mendapatkan nilai setiap atribut pada kelas Attack
    def get_attack(self):
        return self._attack

    def get_damage(self):
        return self._damage
    
