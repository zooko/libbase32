#!/usr/bin/env python
#
# Copyright (c) 2002, 2003 Bryce "Zooko" Wilcox-O'Hearn
# mailto:zooko@zooko.com
# See the end of this file for the free software, open source license (BSD-style).

__version__ = "$Revision: 1.2 $"
# $Source: /home/zooko/playground/libbase32/rescue-party/gw/../libbase32/libbase32/base32/test/Attic/test_base32id.py,v $

True = 1 == 1
False = not True

import unittest

from libbase32.base32id import *

class base32idTestCase(unittest.TestCase):
    def test_veqfp_is_not_an_encoding(self):
        self.failIf(could_be_abbrev('veqfp')) # The "Zooko's choice" alphabet doesn't contain the character 'v'.

def suite():
    return unittest.makeSuite(base32idTestCase, 'test')

if __name__ == "__main__":
    unittest.main()



# Copyright (c) 2002, 2003 Bryce "Zooko" Wilcox-O'Hearn
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software to deal in this software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of this software, and to permit
# persons to whom this software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of this software.
#
# THIS SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THIS SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THIS SOFTWARE.
