#!/usr/bin/env python
#
# Copyright (c) 2002 Bryce "Zooko" Wilcox-O'Hearn
# mailto:zooko@zooko.com
# See the end of this file for the free software, open source license (BSD-style).

# CVS:
__cvsid = '$Id: GNUmakefile,v 1.4 2003/06/27 02:16:35 zooko Exp $'

NAME=base32

INCDIRS=-I../../libzutil/libzutil -I../../libzstr/libzstr
LIBDIRS=-L../../libzutil/libzutil -L../../libzstr/libzstr
LIBS=-lzstr -lzutil -lm

LIBPREFIX=lib
LIBSUFFIX=.a

RANLIB=ranlib
AR=ar

CC=gcc

CFLAGS=-DNDEBUG -Wall -O0 $(INCDIRS)
LDFLAGS=$(LIBDIRS) $(LIBS)

# SRCS=$(wildcard *.c)
SRCS=base32.c
TESTSRCS=test.c
OBJS=$(SRCS:%.c=%.o)
TESTOBJS=$(TESTSRCS:%.c=%.o)
TEST=testlb32
LIB=$(LIBPREFIX)$(NAME)$(LIBSUFFIX)

all: $(LIB) $(TEST)

include $(SRCS:%.c=%.d)

%.d: %.c
	@echo remaking $@
	@set -e; $(CC) -MM $(CFLAGS) $< \
	| sed 's/\($*\)\.o[ :]*/\1.o $@ : /g' > $@; \
	[ -s $@ ] || rm -f $@

$(LIB): $(OBJS)
	$(AR) -r $@ $+
	$(RANLIB) $@

$(TEST): $(TESTOBJS) $(LIB)
	$(CC) $+ -o $@ $(LDFLAGS)


clean:
	-rm $(LIB) $(OBJS) $(TEST) $(TESTOBJS) *.d

.PHONY: clean all

# Copyright (c) 2002 Bryce "Zooko" Wilcox-O'Hearn
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
