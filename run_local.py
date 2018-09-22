#!usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'LotteWong'

import code
import easygui

key = '23333333'
cipher = easygui.enterbox('请输入您的密文：', '解密中...')
plain = code.decode(cipher, key)

easygui.msgbox('被您抽到的幸运儿是：%s' % plain, '已解密!')
