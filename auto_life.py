#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-02-11 13:19:44
# @Author  : jiong (447991103@qq.com)
# @Version : $Id$

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


import random
import os
import time


def init(level):
    return random.randint(0, level)

dict = {' ': 0, 'a': 1}
cells = [[' ' for x in range(32)] for y in range(22)]
grid = [[' ' for x in range(32)] for y in range(22)]
while True:
    level = input('larger number,less cells (>0):')
    try:
        if int(level) > 0:
            for y in range(1, 21):
                for x in range(1, 31):
                    r = random.randint(0, int(level))
                    if r == 0:
                        cells[y][x] = 'a'
            break
    except:
        pass

for y in cells:
    print(' '.join(y))
print("press key to begin...")

# 暂停
os.system('pause >nul')
i = 0
while True:
    for y in range(1, 21):
        for x in range(1, 31):
        	# 周围的8个cells
            num = dict[cells[y - 1][x - 1]] +\
                dict[cells[y - 1][x + 1]] +\
                dict[cells[y - 1][x]] +\
                dict[cells[y + 1][x - 1]] +\
                dict[cells[y + 1][x + 1]] +\
                dict[cells[y + 1][x]] +\
                dict[cells[y][x - 1]] +\
                dict[cells[y][x + 1]]
            # 如果值为3，那么该格赋值为a，为2，不变，否则为' '
            if num == 3:
                grid[y][x] = 'a'
            elif num == 2:
                grid[y][x] = cells[y][x]
            else:
                grid[y][x] = ' '

    for y in range(1, 21):
        for x in range(1, 31):
            cells[y][x] = grid[y][x]
    time.sleep(0.5)
    os.system('cls')
    i += 1
    print('time: ' + str(i))
    for y in cells:
        print(' '.join(y))
