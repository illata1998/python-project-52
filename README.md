# Task Manager
[![Actions Status](https://github.com/illata1998/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/illata1998/python-project-52/actions)

## Description
Task Manager is a simple web application that helps users manage their tasks.

## Installation
Clone this repository to your local machine.
```bash
git clone git@github.com:illata1998/python-project-52.git
cd python-project-52
```
Install dependencies using [Poetry](https://python-poetry.org/docs/).
```bash
make install
```
Create the new .env file and define SECRET_KEY, DEBUG, DATABASE_URL and WEB_CONCURRENCY variables there. For example,
```bash
echo "SECRET_KEY=secret_key" >> .env
echo "DEBUG=False" >> .env
echo "DATABASE_URL=postgresql://user:password@host:port/database_name" >> .env
echo "WEB_CONCURRENCY=4" >> .env
```
Initialize the build script.
```bash
make build
```
Run the app.
```bash
# using Gunicorn
make start

# or using the Django development server with debug mode
make dev
```

## Demo
Check out Page Analyzer by clicking [here](https://python-project-52-u7be.onrender.com).
