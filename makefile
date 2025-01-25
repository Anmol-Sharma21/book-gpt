# Makefile for PDF QA API

.PHONY: install run format lint test clean setup help

VENV = venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

help:  ## Show this help
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

setup:  ## Create virtual environment
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip

install:  ## Install dependencies
	$(PIP) install -r requirements.txt
	$(PIP) install -U langchain-huggingface

run:  ## Run the Flask application
	TOKENIZERS_PARALLELISM=false FLASK_APP=run.py $(PYTHON) -m flask run --host=0.0.0.0 --port=5000

format:  ## Format code with black and isort
	$(VENV)/bin/black app/
	$(VENV)/bin/isort app/

lint:  ## Lint code with flake8
	$(VENV)/bin/flake8 app/ --max-line-length=88 --exclude=venv

test:  ## Run tests
	$(PYTHON) -m pytest tests/ -v

clean:  ## Clean temporary files
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache
	rm -rf .mypy_cache

distclean: clean  ## Full clean including virtual environment
	rm -rf $(VENV)

requirements:  ## Update requirements.txt
	$(PIP) freeze > requirements.txt

pinecone-init:  ## Initialize Pinecone index
	$(PYTHON) -c "from app.utils.pinecone_utils import pinecone_index; pinecone_index()"