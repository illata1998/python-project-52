lint:
	poetry run flake8 task_manager

install:
	poetry install

dev:
	poetry run python3 manage.py runserver

migrate:
	poetry run python3 manage.py makemigrations
	poetry run python3 manage.py migrate