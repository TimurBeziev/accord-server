from typing import List


class ChatRoom:
    def __init__(self, users=None) -> None:
        self.num_of_members = 1
        self.list_of_users: List[tuple] = []
        if users is not None:
            self.list_of_users.extend(users)

    def add_users(self, users: List) -> None:
        self.num_of_members += 1
        self.list_of_users.extend(users)

    def get_users_info(self) -> List[tuple]:
        return self.list_of_users
