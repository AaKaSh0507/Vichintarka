#!/bin/bash

# Docker Development Helper Script for Vichintarka
# Usage: ./scripts/docker-dev.sh [command]

set -e

PROJECT_NAME="vichintarka"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Helper functions
print_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Functions
help() {
    echo "Docker Development Helper for Vichintarka"
    echo ""
    echo "Usage: ./scripts/docker-dev.sh [command]"
    echo ""
    echo "Commands:"
    echo "  build          Build all Docker images"
    echo "  up             Start all services"
    echo "  down           Stop all services"
    echo "  restart        Restart all services"
    echo "  logs           Show logs for all services"
    echo "  logs-app       Show logs for app service only"
    echo "  logs-db        Show logs for database service only"
    echo "  logs-redis     Show logs for Redis service only"
    echo "  shell          Open shell in app container"
    echo "  db-shell       Open PostgreSQL shell"
    echo "  redis-shell    Open Redis CLI"
    echo "  test           Run tests in Docker"
    echo "  migrate        Run database migrations"
    echo "  clean          Clean up Docker resources"
    echo "  status         Show status of all services"
    echo "  tools          Start management tools (pgAdmin, Redis Commander)"
    echo "  help           Show this help message"
}

build() {
    print_info "Building Docker images..."
    docker-compose build --no-cache
    print_success "Docker images built successfully!"
}

up() {
    print_info "Starting services..."
    docker-compose up -d
    print_success "Services started successfully!"
    print_info "App is available at: http://localhost:8000"
    print_info "API docs at: http://localhost:8000/docs"
}

down() {
    print_info "Stopping services..."
    docker-compose down
    print_success "Services stopped successfully!"
}

restart() {
    print_info "Restarting services..."
    docker-compose restart
    print_success "Services restarted successfully!"
}

logs() {
    docker-compose logs -f
}

logs_app() {
    docker-compose logs -f app
}

logs_db() {
    docker-compose logs -f db
}

logs_redis() {
    docker-compose logs -f redis
}

shell() {
    print_info "Opening shell in app container..."
    docker-compose exec app /bin/bash
}

db_shell() {
    print_info "Opening PostgreSQL shell..."
    docker-compose exec db psql -U postgres -d vichintarka
}

redis_shell() {
    print_info "Opening Redis CLI..."
    docker-compose exec redis redis-cli
}

test() {
    print_info "Running tests..."
    docker-compose exec app pytest
}

migrate() {
    print_info "Running database migrations..."
    docker-compose exec app alembic upgrade head
    print_success "Migrations completed!"
}

clean() {
    print_warning "This will remove all containers, networks, and volumes!"
    read -p "Are you sure? (y/N) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        print_info "Cleaning up Docker resources..."
        docker-compose down -v --remove-orphans
        docker system prune -f
        print_success "Cleanup completed!"
    else
        print_info "Cleanup cancelled."
    fi
}

status() {
    print_info "Service status:"
    docker-compose ps
}

tools() {
    print_info "Starting management tools..."
    docker-compose --profile tools up -d pgadmin redis-commander
    print_success "Management tools started!"
    print_info "pgAdmin available at: http://localhost:5050"
    print_info "  Email: admin@vichintarka.com"
    print_info "  Password: admin"
    print_info "Redis Commander available at: http://localhost:8081"
}

# Main script
case "${1:-help}" in
    build)
        build
        ;;
    up)
        up
        ;;
    down)
        down
        ;;
    restart)
        restart
        ;;
    logs)
        logs
        ;;
    logs-app)
        logs_app
        ;;
    logs-db)
        logs_db
        ;;
    logs-redis)
        logs_redis
        ;;
    shell)
        shell
        ;;
    db-shell)
        db_shell
        ;;
    redis-shell)
        redis_shell
        ;;
    test)
        test
        ;;
    migrate)
        migrate
        ;;
    clean)
        clean
        ;;
    status)
        status
        ;;
    tools)
        tools
        ;;
    help|*)
        help
        ;;
esac