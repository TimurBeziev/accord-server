import argparse

from core.server import AsyncTCPSocketServer


def main():
    args = parse_args()
    server = AsyncTCPSocketServer('localhost', args.port)
    server.serve()


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('port', type=int)
    return parser.parse_args()


if __name__ == '__main__':
    main()
