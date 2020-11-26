pytube_cli:
	poetry run youtube

lint:
	poetry run flake8 youtube

.PHONY: youtube lint