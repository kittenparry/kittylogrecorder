PREFIX ?= /usr/bin
NAME = logrecorder

all:
	@echo Run \'make install\' to install $(NAME).

install:
	@cp $(NAME) $(PREFIX)/$(NAME)
	@chmod 755 $(PREFIX)/$(NAME)
	@echo $(NAME) has been installed.

uninstall:
	@rm -rf $(PREFIX)/$(NAME)
	@echo $(NAME) has been removed.
