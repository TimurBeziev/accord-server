from typing import List


class ChatRoom:
    def __init__(self) -> None:
        self.num_of_members = 1
        self.list_of_users: List = []

    def add_users(self, users: List) -> None:
        self.num_of_members += 1
        for user in users:
            print(str(user) + " joined")
            self.list_of_users.append(user)

    def get_users_info(self) -> List:
        return self.list_of_users
