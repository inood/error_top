import random
import string
import sys


def gen_short_string(length):
    letters = string.ascii_letters
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string


def log_string_gen():
    A = gen_short_string(random.randint(1,100))
    error_text = 'Error='+str(random.randint(1,200))
    B = gen_short_string(random.randint(1,100))
    log = f'{A}{error_text}{B}'
    return log


def log_gen(file, count):
    file = open(file, 'w')
    for x in range(count):
        file.write(log_string_gen()+'\n')
    file.close()


if __name__ == '__main__':
    file = sys.argv[1]
    count_lines = int(sys.argv[2])
    log_gen(file, count_lines)

