# -*- coding: utf-8 -*-

import os
import itertools
import unicodedata

import cPickle

from _compat import u

__all__ = ['get']


# init wubi dict
data = {}
dat = os.path.join(os.path.dirname(__file__), "wubi.cPickle")

with open(dat) as f:
    data = cPickle.loads(f.read())


def _wubi_generator(chars):
    """Generate wubi for chars, if char is not chinese character,
    itself will be returned.
    Chars must be unicode list.
    """
    for char in chars:
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
    """Return pinyin of string, the string must be unicode
    """
    if type=='cw':
        return delimiter.join(_wubi_generator(u(s)))
    elif type =='wc':
        return ''.join(_chinese_generator(u(s),delimiter))
    else:
        return None
