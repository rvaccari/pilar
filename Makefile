help:
	@echo -e "install             Initialize the environment."
	@echo -e "test                Run the full test suite."
	@echo -e "format              Black code formatter."
	@echo -e "lint                Code style checker."


install:
	sudo ./scripts/install.sh


test:
	pytest -ra --disable-warnings --color=yes $(ARGS)


format:
	black backend tests


ci:
	ENVIRONMENT_NAME=testing pytest tests -q -x --disable-warnings $(ARGS)


lint:
	rm -rf .mypy_cache
	rm -rf .pytest_cache
	rm -f .coverage
	ENVIRONMENT_NAME=testing pytest tests backend --mypy --black --disable-warnings $(ARGS)
