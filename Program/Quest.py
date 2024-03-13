class Quest:
    def __init__(self, id_quest="", name_quest="", description="", reward={}, status="Incomplete"):
        self._id_quest = id_quest
        self._name_quest = name_quest
        self._description = description
        self._reward = reward
        self._status = status

    # Method setter untuk set nilai setiap atribut pada kelas Quest
    def set_id_quest(self, id_quest):
        self._id_quest = id_quest
    
    def set_name_quest(self, name_quest):
        self._name_quest = name_quest

    def set_description(self, description):
        self._description = description
    
    def set_reward(self, reward):
        self._reward = reward
        
    def set_status(self, status):
        self._status = status
        
    # Method getter untuk mendapatkan nilai setiap atribut pada kelas Quest
    def get_id_quest(self):
        return self._id_quest
    
    def get_name_quest(self):
        return self._name_quest

    def get_description(self):
        return self._description
    
    def get_reward(self):
        return self._reward
    
    def get_status(self):
        return self._status
