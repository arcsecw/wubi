# -*- coding: utf-8 -*-

import os
import itertools
import unicodedata

import pickle

from _compat import u

__all__ = ['get']


# init wubi dict
data = {}
dat = os.path.join(os.path.dirname(__file__), "wubi.pickle")

with open(dat) as f:
    data = pickle.loads(f.read())


def _wubi_generator(chars):
    """Generate wubi for chars, if char is not chinese character,
    itself will be returned.
    Chars must be unicode list.
    """
    s = []
    for char in chars:
        # handle english in chinese
        var =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        if char ==' ':
            pass
        elif char in var :
                s.append(char)
                if char==chars[-1]:
                    yield ''.join(s)
        else:
            if len(s)!=0:
                yield ''.join(s)
                s=[]
            wubi = data['cw'].get(char)
            if wubi == None:
                wubi=char
            yield wubi


def _chinese_generator(chars, delimiter):
    """Generate chinese for chars, if char is not chinese character,
    itself will be returned.
    Chars must be unicode list.
    """
    for char in chars.split(delimiter):
        chinese = data['wc'].get(char)
        if chinese ==None:
                chinese=char
        yield chinese

def get(s,type='',delimiter=' '):
    """Return wubi of string, the string must be unicode
    """
    #pre process input string


    if type=='cw':
        return delimiter.join(_wubi_generator(u(s)))
    elif type =='wc':
        return ''.join(_chinese_generator(u(s),delimiter))
    else:
        return None
