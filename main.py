import socket
import threading
from typing import List
import peer


def main():
    ip_address: str = "127.0.0.1"
    port: int = int(input("Enter your port: "))
    username: str = input("Enter your username: ")
    person = peer.Peer(ip_address=ip_address, port=port, username=username)
    wait_for_inc_conn_th = threading.Thread(target=person.wait_for_incoming_connections, args=())
    wait_for_inc_conn_th.start()
    print("---------------------------------------------")
    print("Add your friend")
    opponent_ip = ip_address
    opponent_port: int = int(input("Enter friends port: "))
    usr: tuple = (opponent_ip, opponent_port)
    print("----------------------------------------------")
    create_chat_room_th = threading.Thread(target=person.create_chat_room, args=([usr],))
    create_chat_room_th.start()
    create_chat_room_th.join()
    wait_for_inc_conn_th.join()


if __name__ == '__main__':
    main()
