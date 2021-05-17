from core.server import AsyncTCPServer

import argparse


def main():
    args = parse_args()
    server = AsyncTCPServer('localhost', args.port)
    server.serve()

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('port', type=int)
    return parser.parse_args()


if __name__ == '__main__':
    main()
