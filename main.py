class User():
    def __init__(self, ID, name, access_level):
        self.ID = ID
        self.name = name
        self.access_level = access_level

    def info(self):
        print(f'ID - {self.ID}')
        print(f'Имя - {self.name}')
        print(f'Уровень доступа - {self.access_level}')