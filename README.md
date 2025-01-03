# DynamoDB Local Sandbox
This is a simple project to demonstrate how to use DynamoDB Local. The project includes a simple Flask application, and also provides a local admin interface to facilitate the management of tables and items.

## Requirements
- Python 3.12
- Docker Desktop (or compatible container runtime offering `docker-compose`)
- AWS CLI (optional)

## Setup
1. Clone the repository
```bash
git clone https://github.com/ThatsNinja/dynamodb-local.git
```
2. Change to the project directory
```bash
cd dynamodb-local
```

## Running the Application
1. Start the Docker Compose stack
```bash
docker-compose up
```
This will result in DynamoDB Local running in a Docker container, which exposes the service on the host machine at port 8000. Additionally, you have an instance of the dynamodb-admin GUI interface exposed at port 8001.

The included Flask application is configured to start on port 5000. The application only exposes one path at this endpoint, which is a simple health check. You can access it at [http://localhost:5000/healthcheck](http://localhost:5000/healthcheck).