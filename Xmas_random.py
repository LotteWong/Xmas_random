#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'LotteWong'

import code
import random


# 保存原始状态
def save_state(state):
    temp = state
    return temp


# 还原原始状态
def reset_state(each, state):
    global recv_dict
    recv_dict[each] = state


# 打码
def dot_mark(give_name, recv_name):
    code_key = '23333333'
    plain = recv_name
    cipher = code.encode(plain, code_key)
    text = '{} -> {}'.format(give_name, cipher)

    filename = 'Xmas_random.txt'
    with open(filename, 'a+', encoding='utf-8', newline='\n') as f:
        f.write(text + '\n')


if __name__ == '__main__':
    give_dict = {'爸爸':None, '妈妈':None, '姐姐':None, '詹韬':None, '玉米':None, '洒萍':None}
    recv_dict = {'爸爸':0, '妈妈':0, '姐姐':0, '詹韬':0, '玉米':0, '洒萍':0}

    for each in list(give_dict.keys()):
        state = save_state(recv_dict[each])

        # 标记送礼物的人状态为-1
        recv_dict[each] = -1

        # 判断收礼物的人状态
        work = True
        while work:
            person = random.choice(list(recv_dict.keys()))
            if recv_dict[person] == 0:  # 0表示还未分配礼物
                give_dict[each] = person
                recv_dict[person] += 1
                work = False
                print('匹配成功！')
            else:   # 其它情况表示已分配礼物或自己送给自己
                print('匹配失败！错误代码：%d.' % recv_dict[person])

            # 当最后的人只能送给自己时报错
            assert(each != '洒萍' or recv_dict[each] != 0), 'Fatal error. Try again.'

        reset_state(each, state)

        dot_mark(each, give_dict[each])
