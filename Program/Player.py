class Player:
    def __init__(self, name_player="", gender="", character=None):
        self._name_player = name_player
        self._gender = gender
        self._character = character

    # Method setter untuk set nilai setiap atribut pada kelas Player
    def set_name_player(self, name_player):
        self._name_player = name_player

    def set_gender(self, gender):
        self._gender = gender
    
    def set_character(self, character):
        self._character = character
        
    # Method getter untuk mendapatkan nilai setiap atribut pada kelas Player
    def get_name_player(self):
        return self._name_player

    def get_gender(self):
        return self._gender
    
    def get_character(self):
        return self._character
