pytube_cli:
	poetry run pytube_cli

lint:
	poetry run flake8 pytube_cli

.PHONY: pytube_cli lint