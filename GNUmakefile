NAME=base32

INCDIRS=-I../libzutil -I../libzstr
LIBDIRS=-L../libzutil -L../libzstr
LIBS=-lzutil -lzstr -lm

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
TEST=test
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

$(TEST): $(LIB) $(TESTOBJS)
	$(CC) $(LDFLAGS) $+ -o $@


clean:
	-rm $(LIB) $(OBJS) $(TEST) $(TESTOBJS) *.d

.PHONY: clean all
