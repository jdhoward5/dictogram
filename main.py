import math

DICT_FILE = '/usr/share/dict/usa'

def count_letters(word: str, master_dict: dict) -> None:
    for c in word.lower():
        if c in master_dict:
            master_dict[c] += 1

def pretty_print(master_dict: dict) -> None:
    s = '|'
    # Y Axis scaled to 20 character height
    limit = max(master_dict.values())
    scaled_dict = {
        c: ['X' if x <= math.floor(v/limit*20) else ' ' for x in range(1, 21)] for c, v in master_dict.items()
    }
    for i in range(19, 0, -1):
        for x in scaled_dict.keys():
            s += scaled_dict[x][i] + ' '
        s += '\r\n|'
    s += '--'*len(scaled_dict.keys())+'\r\n '
    for key in scaled_dict.keys():
        s += str(key) + ' '
    s += '\r\n'
    print(s)


def histogram() -> None:
    master_dict = {c: 0 for c in 'abcdefghijklmnopqrstuvwxyz'}
    with open(DICT_FILE, 'r') as df:
        words = df.readlines()
        for word in words:
            count_letters(word, master_dict)
    pretty_print(master_dict)

if __name__ == '__main__':
    histogram()
