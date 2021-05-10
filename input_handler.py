import json
import logging
import re


class InputHandler:
    def __init__(self, username: str, message: str):
        self.username: str = username
        self.message: str = message
        self.result: str = ""
        self.handle_input()

    def handle_input(self) -> None:
        commands = [
            ("/username (?P<username>\\w+)$", self.process_username),
            ("(?P<message>.*)$", self.process_message),
        ]
        for pattern, handler in commands:
            m = re.match(pattern, self.message)
            if m is not None:
                handler(**m.groupdict())
                break
        else:
            logging.warning("Could not parse input")

    def process_username(self, username) -> None:
        self.process_event({
            "type": "set_username",
            "username": username,
        })

    def process_message(self, message) -> None:
        # TODO
        # if len(num) > 4 --> divide into packets

        num = 47 + len(self.username) + len(message)
        num = str(num).zfill(4)
        self.process_event({
            "len": num,
            "username": self.username,
            "type": "message",
            "body": message,
        })

    def process_event(self, event) -> None:
        self.result = json.dumps(event)

    def get_processed_message(self) -> str:
        return self.result
