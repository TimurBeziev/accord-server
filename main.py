import argparse

from core.server import AsyncTCPSocketServer
from core.connection_handler import UnsecureTCPConnectionHandler


def main():
    args = parse_args()
    server = AsyncTCPSocketServer('localhost', args.port,
                                  UnsecureTCPConnectionHandler)
    server.serve()


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('port', type=int)
    return parser.parse_args()


if __name__ == '__main__':
    main()
