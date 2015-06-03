#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Rightpeter'
import rsa
import sys
import os
import os.path
import re

enc_pattern = re.compile(r'.*\.enc$')
dec_pattern = re.compile(r'.*\.dec$')
pickle_pattern = re.compile(r'.*\.pickle$')
zip_pattern = re.compile(r'.*\.zip$')


def enc(content, pubkey):
    # print 'content: ', content
    # content = content[:245]

    crypto = ''
    # print '========start========='
    while content:
        message = content[:245]
        content = content[245:]

        enc_message = rsa.encrypt(message, pubkey)
        crypto += enc_message
        # print '-----------------message: -------------\n', message
        # print '-----------------content: -------------\n', content
        # print '-----------------enc_message: ---------\n', enc_message
        # print '-----------------crypto: --------------\n', crypto

    # crypto = rsa.encrypt(content, pubkey)
    # print 'crypto: ', crypto

    return crypto