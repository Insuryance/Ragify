.PHONY: dev build stop clean test lint install help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-18s\033[0m %s\n", $$1, $$2}'

dev: ## Start all services (frontend + backend + chromadb)
	docker compose up --build

dev-d: ## Start all services in background
	docker compose up --build -d

stop: ## Stop all services
	docker compose down

clean: ## Stop and remove volumes
	docker compose down -v

install: ## Install all deps locally
	cd app && npm install
	cd backend && pip install -r requirements.txt

test: ## Run all tests
	cd backend && pytest tests/ -v
	cd app && npm test -- --watchAll=false

test-backend: ## Run backend tests only
	cd backend && pytest tests/ -v --tb=short

lint: ## Lint frontend and backend
	cd backend && black . --check && flake8 .
	cd app && npm run lint

format: ## Auto-format backend
	cd backend && black .

logs: ## Tail all logs
	docker compose logs -f

logs-backend: ## Tail backend logs
	docker compose logs -f backend
