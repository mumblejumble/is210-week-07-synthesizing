#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Authentication Process"""


import authentication
import getpass


def login(username, maxattempts=3):
    auth_mes = False
    en_pw1 = 'Please enter your password:'
    en_pw2 = 'Incorrect username or password. You have {} attempts left.'
    num_tried = 0

    while (not auth_mes) and (num_tried <= maxattempts):
        if num_tried >= 1:
            anth_mes = authentication.authenticate(username, getpass.getpass(en_pw1))
            print en_pw2.format(maxattempts - num_tried)
        elif auth_mes == True:
            print authenticated
        if auth_mes:
            break
        num_tried += 1
    return auth_mes
