#!/usr/bin/env python
#
# Copyright (c) 2002, 2003 Bryce "Zooko" Wilcox-O'Hearn
# mailto:zooko@zooko.com
# See the end of this file for the free software, open source license (BSD-style).

__version__ = "$Revision: 1.4 $"
# $Source: /home/zooko/playground/libbase32/rescue-party/gw/../libbase32/libbase32/test/test_base32.py,v $

import random, unittest

# http://sf.net/projects/pyutil
from pyutil import randutil

from base32 import *

class base32TestCase(unittest.TestCase):
    def test_ende(self):
        bs = randutil.insecurerandstr(2**3)
        as=b2a(bs)
        bs2=a2b(as)
        assert bs2 == bs, "bs2: %s, bs: %s" % (`bs2`, `bs`,)

    def test_ende_long(self):
        bs = randutil.insecurerandstr(2**3)
        as=b2a_long(bs)
        bs2=a2b_long(as)
        assert bs2 == bs, "bs2: %s, bs: %s" % (`bs2`, `bs`,)

    def test_both(self):
        bs = randutil.insecurerandstr(2**3)
        as=b2a(bs)
        asl=b2a_long(bs)
        assert as == asl, "as: %s, asl: %s" % (`as`, `asl`,)
        as=b2a(bs)
        bs2=a2b(as)
        bs2l=a2b_long(as)
        assert bs2 == bs2l
        assert bs2 == bs

    def test_big(self):
        bs = randutil.insecurerandstr(2**9)
        as=b2a(bs)
        asl=b2a_long(bs)
        assert as == asl, "as: %s, asl: %s" % (`as`, `asl`,)
        as=b2a(bs)
        bs2=a2b(as)
        bs2l=a2b_long(as)
        assert bs2 == bs2l
        assert bs2 == bs

    def DISABLED_test_odd_sizes_violates_preconditions(self):
        """
        The Python implementation of b2a_l() actually works if you pass any lengthinbits, and if you don't zero out the unused least significant bits.  The precondition assertions are (a) because the high speed C implementation does not work in those cases and (b) because it might help people discover errors in their own code.  Anyway, if you have assertion-checking turned off, then this test should pass, too.
        """
        for j in range(2**6):
            lib = random.randrange(1, 2**8)
            bs = randutil.insecurerandstr(random.randrange(1, 2**5))
            as = b2a_l(bs, lib)
            assert len(as) == (lib+4)/5 # the size of the base-32 encoding must be just right
            asl = b2a_l_long(bs, lib)
            assert len(asl) == (lib+4)/5 # the size of the base-32 encoding must be just right
            assert as == asl
            bs2 = a2b_l(as, lib)
            assert len(bs2) == (lib+7)/8 # the size of the result must be just right
            bs2l = a2b_l_long(as, lib)
            assert len(bs2l) == (lib+7)/8 # the size of the result must be just right
            assert bs2 == bs2l
            assert trimnpad(bs, lib) == bs2, "trimnpad(%s, %s): %s, bs2: %s" % (`bs`, lib, `trimnpad(bs, lib)`, `bs2`,)

    def test_odd_sizes(self):
        for j in range(2**6):
            lib = random.randrange(1, 2**8)
            bs = randutil.insecurerandstr((lib+7)/8)
            # zero-out unused least-sig bits
            if lib%8:
                b=ord(bs[-1])
                b = b >> (8 - (lib%8))
                b = b << (8 - (lib%8))
                bs = bs[:-1] + chr(b)
            as = b2a_l(bs, lib)
            assert len(as) == (lib+4)/5 # the size of the base-32 encoding must be just right
            asl = b2a_l_long(bs, lib)
            assert len(asl) == (lib+4)/5 # the size of the base-32 encoding must be just right
            assert as == asl
            bs2 = a2b_l(as, lib)
            assert len(bs2) == (lib+7)/8 # the size of the result must be just right
            bs2l = a2b_l_long(as, lib)
            assert len(bs2l) == (lib+7)/8 # the size of the result must be just right
            assert bs2 == bs2l
            assert trimnpad(bs, lib) == bs2, "trimnpad(%s, %s): %s, bs2: %s" % (`bs`, lib, `trimnpad(bs, lib)`, `bs2`,)

    def test_n8mo4_is_an_encoding(self):
        self.failUnless(could_be_base32_encoded_l('n8mo4', 25))

    def test_could_be(self):
        # base-32 encoded strings could be
        for j in range(2**9):
            rands = randutil.insecurerandstr(random.randrange(1, 2**7))
            randsenc = b2a(rands)
            assert could_be_base32_encoded(randsenc), "rands: %s, randsenc: %s, a2b(randsenc): %s" % (`rands`, `randsenc`, `a2b(randsenc)`,)

        # base-32 encoded strings with unusual bit lengths could be, too
        for j in range(2**9):
            bitl = random.randrange(1, 2**7)
            bs = randutil.insecurerandstr((bitl+7)/8)
            # zero-out unused least-sig bits
            if bitl%8:
                b=ord(bs[-1])
                b = b >> (8 - (bitl%8))
                b = b << (8 - (bitl%8))
                bs = bs[:-1] + chr(b)
            assert could_be_base32_encoded_l(b2a_l(bs, bitl), bitl)

        # anything with a bogus character couldn't be
        s = b2a(randutil.insecurerandstr(random.randrange(3, 2**7)))
        assert not could_be_base32_encoded('\x00' + s)
        assert not could_be_base32_encoded(s + '\x00')
        assert not could_be_base32_encoded(s[:1] + '\x00' + s[1:])
        assert not could_be_base32_encoded(s[:1] + '\x00' + s[2:])

        # a base-32 encoded string with an alleged lengthinbits of 16 but with 1-bits in the 18th, 19th,
        # and 20th location couldn't be.
        assert not could_be_base32_encoded_l('yyz', 16)

def _help_bench_e(N):
    return b2a(randutil.insecurerandstr(N))
def _help_bench_ed(N):
    return a2b(b2a(randutil.insecurerandstr(N)))
def _help_bench_e_l(N):
    return b2a_long(randutil.insecurerandstr(N))
def _help_bench_ed_l(N):
    return a2b_long(b2a_long(randutil.insecurerandstr(N)))

def benchem():
    import benchfunc # from pyutil
    print "e: "
    benchfunc.bench(_help_bench_e, TOPXP=13)
    print "ed: "
    benchfunc.bench(_help_bench_ed, TOPXP=13)
    print "e_l: "
    benchfunc.bench(_help_bench_e_l, TOPXP=13)
    print "ed_l: "
    benchfunc.bench(_help_bench_ed_l, TOPXP=13)

def suite():
    suite = unittest.makeSuite(base32TestCase, 'test')
    return suite

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
