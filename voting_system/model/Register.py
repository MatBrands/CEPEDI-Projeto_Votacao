import json
import os

class Register:
    def __init__(self, path: str = './controller/database.json') -> None:
        self.path = path
        if not os.path.exists(self.path):
            with open(path, 'w', encoding='utf-8') as file:
                json.dump({}, file, indent=4, ensure_ascii=False)

    def create_user(self, **user_data) -> bool:
        with open(self.path, encoding='utf-8') as file:
            data = json.load(file)

        id = user_data['user']

        if id in data:
            return False

        new_user = {
            id: {
                'password': user_data['password'],
                'name': user_data['name'],
                'age': user_data['age'],
                'role': user_data['role']
            }
        }

        if user_data['role']:
            new_user[id]['proposal'] = user_data['proposal']

        data.update(new_user)

        with open(self.path, "w", encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        return True

    def update_user(self, **user_data) -> bool:
        with open(self.path, encoding='utf-8') as file:
            data = json.load(file)

        id = user_data['user']
        
        if id not in data:
            return False

        new_user = {
            id: {
                'password': user_data['password'],
                'name': user_data['name'],
                'age': user_data['age'],
                'role': user_data['role']
            }
        }

        if user_data['role']:
            new_user[id]['proposal'] = user_data['proposal']

        data.update(new_user)

        with open(self.path, "w", encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        return True

    def read_user(self, id_user: str):
        with open(self.path, encoding='utf-8') as file:
            data = json.load(file)

        if id_user in data:
            return data[id_user]
        else:
            return False

    def delete_user(self, id_user: str) -> bool:
        with open(self.path, encoding='utf-8') as file:
            data = json.load(file)

        if id_user not in data:
            return False
        
        data.pop(id_user)
        
        with open(self.path, "w", encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
            
        return True