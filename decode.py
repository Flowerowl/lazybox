#!/usr/bin/env python
# encoding: utf-8
def decode_utf8_to_unicode(s,is_strict=True):
    if not s:
        return u''
    if isinstance(s, unicode):
        return s
    try:
        if not is_strict:
            return s.decode('utf-8', 'ignore')
        else:
            return s.decode('utf-8')
    except (UnicodeDecodeError, UnicodeEncodeError):
        return u''


def decode_gbk_to_unicode(s,is_strict=True):
    if not s:
        return u''
    if isinstance(s, unicode):
        return s
    try:
        if not is_strict:
            return s.decode('gbk', 'ignore')
        else:
            return s.decode('gbk')
    except (UnicodeDecodeError, UnicodeEncodeError):
        return u''
