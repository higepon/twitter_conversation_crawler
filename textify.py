import argparse
import sqlite3
import sys


class Dumper:
    def __init__(self, db):
        self.db = db

    def dump(self):
        conn = sqlite3.connect(self.db)
        cursor = conn.cursor()

        cursor.execute(
            "select sid1, sid2, sid3 from conversation")
        for row in cursor:
            sid1, sid2, sid3 = row
            text1 = self.tweet_text(conn, sid1)
            text2 = self.tweet_text(conn, sid2)
            text3 = self.tweet_text(conn, sid3)
            if text1 is None or text2 is None or text3 is None:
                continue
            print("{}\n{}\n{}".format(text1, text2, text3))
        conn.close()

    @staticmethod
    def tweet_text(conn, sid):
        text = None
        cursor = conn.cursor()
        cursor.execute("select text from status where id = ?", [sid])
        for row in cursor:
            text = row[0]
        return text


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--db', type=str, required=True,
                        help='path to sqlite3 db')
    args = parser.parse_args()

    dumper = Dumper(args.db)
    dumper.dump()


if __name__ == '__main__':
    sys.exit(main())
