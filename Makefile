PREFIX ?= /usr/bin
MANDIR ?= /usr/share/man
NAME = logrecorder
MAN = $(NAME).1

all:
	@echo Run \'make install\' to install $(NAME).

install:
	@echo Starting copying files...
	@cp $(NAME) $(PREFIX)/$(NAME)
	@echo Program has been copied.
	@cp $(MAN) $(MANDIR)/man1/$(MAN)
	@echo Man page has been copied.
	@echo Handling permissions...
	@chmod 755 $(PREFIX)/$(NAME)
	@chmod 644 $(MANDIR)/man1/$(MAN)
	@echo $(NAME) has been installed.

uninstall:
	@rm $(PREFIX)/$(NAME)
	@rm $(MANDIR)/man1/$(MAN)
	@echo $(NAME) and its man page has been removed.
