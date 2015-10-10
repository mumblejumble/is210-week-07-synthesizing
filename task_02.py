#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Authentication Process"""


import authentication
import getpass


def login(username, maxattempts=3):
    """This function decides whether password is authenticated.

    Args:
        username(str): the name of the user to authenticate.

        maxattempts(int): times that each username is allowed to try,
            default to 3.

    Returns:
        bool: True is the username and password are correct and didn't
            exceed more than maxattempts, else False.

    Examples:
        >>> import task_02
        >>> task_02.login('mike', 4)
        Please enter your password:
        Incorrect username or password. You have 3 attempts left.
        Please enter your password:
        Incorrect username or password. You have 2 attempts left.
        Please enter your password:
        Incorrect username or password. You have 1 attempts left.
        Please enter your password:
        Incorrect username or password. You have 0 attempts left.
        False

        correct password entered on second attempt
        >>>task_02.login('mike', 4)
        Please enter your password:
        Incorrect username or password. You have 3 attempts left.
        Please enter your password:
        True

    """
    auth_mes = False
    en_pw1 = 'Please enter your password:'
    en_pw2 = 'Incorrect username or password. You have {} attempts left.'
    num_tried = 1

    while (not auth_mes) and (num_tried <= maxattempts):
        auth_mes = authentication.authenticate(username,
                                               getpass.getpass(en_pw1))
        if auth_mes:
            auth_mes = True
        else:
            print en_pw2.format(maxattempts - num_tried)
        num_tried += 1
    return auth_mes
