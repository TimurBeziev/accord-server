from core.peer import AsyncAccordPeer as Peer
import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('port', type=int)
    return parser.parse_args()


def main():
    args = parse_args()
    peer = Peer(('127.0.0.1', args.port))
    peer.connect()


if __name__ == '__main__':
    main()
