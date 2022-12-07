help:
	@echo -e "install             Initialize the environment."
	@echo -e "test                Run the full test suite."
	@echo -e "format              Black code formatter."


install:
	sudo ./scripts/install.sh


test:
	pytest -ra --disable-warnings --color=yes $(ARGS)


format:
	black backend tests


ci:
	ENVIRONMENT_NAME=testing pytest tests -q -x --disable-warnings
