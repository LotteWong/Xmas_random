#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'LotteWong'

import random
import itchat
from itchat.content import TEXT
import code


# 保存原始状态
def save_state(state):
    temp = state
    return temp


# 打码
def dot_mark(plain):
    key = '23333333'
    cipher = code.encode(plain, key)
    print('Encode successfully!')
    return cipher


# 随机匹配
def distribute():
    # 初始化字典
    global people
    give_dict = {}.fromkeys(people, None)
    print(give_dict)
    recv_dict = {}.fromkeys(people, 0)
    print(recv_dict)

    for each in people:
        state = save_state(recv_dict[each])

        # 标记送礼物的人状态为-1
        recv_dict[each] = -1

        # 判断收礼物的人状态
        work = True
        while work:
            person = random.choice(people)
            # 0表示还未分配礼物
            if recv_dict[person] == 0:
                mark = dot_mark(itchat.search_friends(userName=person)['RemarkName'])
                if mark:
                    give_dict[each] = mark
                else:
                    give_dict[each] = dot_mark(my_remarkname)
                recv_dict[person] += 1
                work = False
                print('匹配成功！')
            # 其它情况表示已分配礼物或自己送给自己
            else:
                print('匹配失败！错误代码：%d.' % recv_dict[person])

            # 当最后的人只能送给自己时报错
            assert (each != my_remarkname or recv_dict[each] != 0), 'Fatal error. Try again.'

        recv_dict[each] = state

    return give_dict


# 消息处理
@itchat.msg_register([TEXT], isFriendChat=True)
def handle_request(msg):
    global people
    from_username = msg['FromUserName']
    from_nickname = itchat.search_friends(userName=from_username)['NickName']
    print('Msg From:{} || {}'.format(from_nickname, from_username))
    to_username = msg['ToUserName']
    to_nickname = itchat.search_friends(userName=to_username)['NickName']
    print('Msg To:{} || {}'.format(to_nickname, to_username))

    # 初始化列表
    if to_username == my_username and msg['Content'] == 'Merry Xmas!':
        people.append(from_username)
        print('Append successfully!')
    # 开始抽签
    elif from_username == my_username and msg['Content'] == 'Magic!':
        result = distribute()
        for each in result.items():
            gift_from, gift_to = each
            itchat.send_msg(msg='您抽到的幸运儿是：%s' % gift_to, toUserName=gift_from)
            print('Send successfully!')


if __name__ == '__main__':
    itchat.auto_login(hotReload=True)
    print()

    my_username = itchat.search_friends()['UserName']
    print(my_username)
    my_nickname = itchat.search_friends()['NickName']
    print(my_nickname)
    my_remarkname = input('请输入您的备注名称（注意保持所有备注名称的字长一致）：')
    people = []

    itchat.run()
