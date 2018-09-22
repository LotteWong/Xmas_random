#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'LotteWong'

import easygui
import sys


# 利用地板除和余数运算进行异或加密
def encode(plaintext, key):
    key = key * (len(plaintext) // len(key)) + key[:len(plaintext) % len(key)]  # 保持明文和密钥的长度一致
    ciphertext = []
    for idx in range(len(plaintext)):
        ciphertext.append(str(ord(plaintext[idx]) ^ ord(key[idx])))
    ciphertext = ','.join(ciphertext)
    return ciphertext


# 利用地板除和余数运算进行异或解密
def decode(ciphertext, key):
    ciphertext = ciphertext.split(',')
    key = key * (len(ciphertext) // len(key)) + key[:len(ciphertext) % len(key)]  # 保持密文和密钥的长度一致
    plaintext = []
    for idx in range(len(ciphertext)):
        plaintext.append(chr(int(ciphertext[idx]) ^ ord(key[idx])))
    plaintext = ''.join(plaintext)
    return plaintext


# 保存文件
def save(text):
        filetypes = ['*.txt', '*.md', '*.doc', '*.docx']
        filename = easygui.filesavebox('请选择需要保存的文件', '资源管理器', filetypes=filetypes)
        with open(filename, 'a+', encoding='utf-8', newline='\n') as f:
            f.write(text + '\n')


if __name__ == '__main__':
    while True:
        choices = ['加密', '解密', '退出']
        choice = easygui.buttonbox("请选择您需要的功能：", "欢迎进入秘密箱！", choices)

        # 加密
        if choice == '加密':
            types = ['字符串', '文件']
            type = easygui.buttonbox('请选择您需要加密的类型：', '加密中...', types)

            # 字符串加密
            if type == '字符串':
                plaintext = easygui.enterbox('请输入您的明文：', '加密中...')
                key = easygui.passwordbox('请输入您的密钥', '加密中...')
                ciphertext = encode(plaintext, key)
                easygui.textbox('已加密...\n\n您的密文是：', '加密成功!', ciphertext)

                # 保存密文
                buttons = ['保存', '不保存']
                button = easygui.boolbox('是否需要保存密文？', '保存', buttons)
                if button == '保存':
                    save(ciphertext)
                else:
                    continue

            # 文件加密
            elif type == '文件':
                filetypes = ['*.txt', '*.md', '*.doc', '*.docx']
                plainfile = easygui.fileopenbox('请选择需要加密的文件', '资源管理器', filetypes=filetypes)
                with open(plainfile, 'rt', encoding='utf-8', newline='\n') as f:
                    plaintext = ''.join(f.readlines())
                    key = easygui.passwordbox('请输入您的密钥', '加密中...')
                    ciphertext = encode(plaintext, key)
                    easygui.textbox('已加密...\n\n您的密文是：', '加密成功!', ciphertext)

                    # 保存密文
                    buttons = ['保存', '不保存']
                    button = easygui.buttonbox('是否需要保存密文？', '保存', buttons)
                    if button == '保存':
                        save(ciphertext)
                    else:
                        continue

        # 解密
        elif choice == '解密':
            types = ['字符串', '文件']
            type = easygui.buttonbox('请选择您需要解密的类型：', '解密中...', types)

            # 字符串解密
            if type == '字符串':
                ciphertext = easygui.enterbox('请输入您的密文：', '解密中...')
                key = easygui.passwordbox('请输入您的密钥', '解密中...')
                plaintext = decode(ciphertext, key)
                easygui.textbox('已解密...\n\n您的明文是：', '解密成功!', plaintext)

                # 保存明文
                buttons = ['保存', '不保存']
                button = easygui.boolbox('是否需要保存明文？', '保存', buttons)
                if button == '保存':
                    save(plaintext)
                else:
                    continue

            # 文件解密
            elif type == '文件':
                filetypes = ['*.txt', '*.md', '*.doc', '*.docx']
                cipherfile = easygui.fileopenbox('请选择需要解密的文件', '资源管理器', filetypes=filetypes)
                with open(cipherfile, 'rt', encoding='utf-8', newline='\n') as f:
                    ciphertext = ''.join(f.readlines())
                    key = easygui.passwordbox('请输入您的密钥', '解密中...')
                    plaintext = decode(ciphertext, key)
                    easygui.textbox('已解密...\n\n您的明文是：', '解密成功!', plaintext)

                # 保存明文
                buttons = ['保存', '不保存']
                button = easygui.boolbox('是否需要保存明文？', '保存', buttons)
                if button == '保存':
                    save(plaintext)
                else:
                    continue

        # 退出
        else:
            sys.exit()
