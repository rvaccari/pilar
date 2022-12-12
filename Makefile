help:
	@echo "install             Initialize the environment."
	@echo "test                Run the full test suite."
	@echo "format              Black code formatter."
	@echo "lint                Code style checker."
	@echo "run                 Run app."
	@echo "docker-build        Build docker image."
	@echo "docker-up           Start docker container."
	@echo "docker-stop         Stop docker container."


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


run:
	flask run


docker-build:
	docker build .


docker-up:
	docker compose up -d


docker-stop:
	docker compose stop
