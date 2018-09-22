#!usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'LotteWong'


def decode(ciphertext, key):
    ciphertext = ciphertext.split(',')
    key = key * (len(ciphertext) // len(key)) + key[:len(ciphertext) % len(key)]
    plaintext = []
    for idx in range(len(ciphertext)):
        plaintext.append(chr(int(ciphertext[idx]) ^ ord(key[idx])))
    plaintext = ''.join(plaintext)
    return plaintext


key = '23333333'
cipher = '[打码后的密文]' # [打码后的密文]修改成对应的即可
plain = decode(cipher, key)
print('被您抽到的幸运儿是：%s' % plain)
