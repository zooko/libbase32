#!/usr/bin/env python
#
#  Copyright (c) 2002 Bryce "Zooko" Wilcox-O'Hearn
#  portions Copyright (c) 2001 Autonomous Zone Industries
#  This file is licensed under the
#    GNU Lesser General Public License v2.1.
#    See the file COPYING or visit http://www.gnu.org/ for details.
#
__cvsid = '$Id: humread.py,v 1.2 2002/05/10 01:43:44 zooko Exp $'

# standard modules
import string

# pyutil modules
import humanreadable

# libbase32 modules
import base32

# old-egtp modules
from idlib import _asciihash_re

printableascii = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_=+!@#$%^&*()`~[]\{}|;':\",./<>? \t" # I just typed this in by looking at my keyboard.  It probably doesn't matter much if I missed some, because I only use it to guess whether a 20-byte string should be represented as a string or as an ID.  If all of the characters in the string are found `printableascii', then we guess that it is a string, not an id.
nulltrans = string.maketrans('', '')

def abbrev(id, b2a_l=base32.b2a_l, trimnpad=base32.trimnpad):
    return '<' + b2a_l(trimnpad(id[:4], 25), 25) + '>'

class AbbrevRepr(humanreadable.BetterRepr):
    def __init__(self):
        humanreadable.BetterRepr.__init__(self)
        self.repr_string = self.repr_str

    def repr_str(self, obj, level, asciihashmatch=_asciihash_re.match, could_be_base32_encoded_l=base32.could_be_base32_encoded_l, translate=string.translate, nulltrans=nulltrans, printableascii=printableascii, abbrev=abbrev):
        if len(obj) == 20:
            # But maybe it was just a 20-character human-readable string, like "credit limit reached", so this is an attempt to detect that case.
            if len(translate(obj, nulltrans, printableascii)) == 0:
                if self.maxourstring >= 22:
                    return `obj`

                # inlining `repr.repr_string()' (with maxourstring) here... and with enable_unescaped_strings
                if self.enable_unescaped_strings:
                    s = str(obj[:self.maxourstring])
                    if len(s) > self.maxourstring:
                        i = max(0, (self.maxourstring-3)/2)
                        j = max(0, self.maxourstring-3-i)
                        s = str(obj[:i] + obj[len(obj)-j:])
                        s = s[:i] + '...' + s[len(s)-j:]
                        # ... done inlining `repr.repr_string()'
                    return s
                else:
                    s = `obj[:self.maxourstring]`
                    if len(s) > self.maxourstring:
                        i = max(0, (self.maxourstring-3)/2)
                        j = max(0, self.maxourstring-3-i)
                        s = `obj[:i] + obj[len(obj)-j:]`
                        s = s[:i] + '...' + s[len(s)-j:]
                        # ... done inlining `repr.repr_string()'
                    return s

            return abbrev(obj)
        elif (len(obj) == 27) and (asciihashmatch(obj)):
            # old "mojosixbit" base-64 encoding
            return '{' + obj[:4] + '}'
        elif could_be_base32_encoded_l(obj, 160):
            # new "libbase32" base-32 encoding
            return '<' + obj[:5] + '>'
        else:
            # inlining `repr.repr_string()' (with maxourstring) here... and with enable_unescaped_strings
            if self.enable_unescaped_strings:
                s = str(obj[:self.maxourstring])
                if len(s) > self.maxourstring:
                    i = max(0, (self.maxourstring-3)/2)
                    j = max(0, self.maxourstring-3-i)
                    s = str(obj[:i] + obj[len(obj)-j:])
                    s = s[:i] + '...' + s[len(s)-j:]
                # ... done inlining `repr.repr_string()'
                return s
            else:
                s = `obj[:self.maxourstring]`
                if len(s) > self.maxourstring:
                    i = max(0, (self.maxourstring-3)/2)
                    j = max(0, self.maxourstring-3-i)
                    s = `obj[:i] + obj[len(obj)-j:]`
                    s = s[:i] + '...' + s[len(s)-j:]
                # ... done inlining `repr.repr_string()'
                return s

myrepr = AbbrevRepr()
hr = myrepr.repr
humanreadable.hr = hr
