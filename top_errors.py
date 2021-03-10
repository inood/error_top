import re
import sys
from collections import Counter


def get_top_error(file, top):
    reg_ex = f'Error=(\d+)'
    error_log = []
    file = open(file, 'r')
    for Line in file:
        error = re.findall(reg_ex, Line)
        error_log.append(int(error[0]))
    print(error_log)
    count_error = Counter(error_log).most_common(top)
    for x in count_error:
        print(f'Error={x[0]} - {x[1]}')


if __name__ == '__main__':
    file = sys.argv[1]
    top = int(sys.argv[2])
    print(f'Топ {top} по количеству ошибок')
    get_top_error(file, top)
