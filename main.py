class User():
    def __init__(self, ID, name):
        self.__ID = ID
        self.__name = name
        self.__access_level = 'user'

    def get_ID(self):
        return self.__ID

    def get_name(self):
        return self.__name

    def get_access_level(self, access_level):
        return self.__access_level

    def set_name(self, name):
        self.__name = name


class Admin(User):
    def __init__(self, ID, name):
        super().__init__(ID, name)
        self.__access_level = 'admin'

    def add_user(self, userlist, user):
        userlist.append(user)
        print('Пользователь успешно добавлен в список')
        print(userlist)

    def remove_user(self, userlist, user):
        userlist.remove(user)
        print('Пользователь был успешно удалён')
        print(userlist)

users = []
admin = Admin('777', 'Вася')
user1 = User('6473246872', 'Петя')

print(user1.get_name())
admin.add_user(users, user1)
print(users)