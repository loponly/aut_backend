# FastAPI Application

This is a simple FastAPI application with a Docker setup for easy deployment.

## Features

- Basic FastAPI setup with a root endpoint.
- Serves a `favicon.ico`.
- Dockerfile for containerization.
- Ready for deployment on platforms like DigitalOcean.

## Requirements

- Python 3.11
- Docker
- FastAPI
- Uvicorn

## Setup

1. **Clone the repository**:

   ```bash
   git clone <your-repo-url>
   cd <your-repo-directory>
   ```

2. **Install dependencies**:

   If you're not using Docker, create a virtual environment and install dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Run the application**:

   ```bash
   uvicorn app:app --reload
   ```

   Access the application at `http://127.0.0.1:8000/`.

## Docker Setup

1. **Build the Docker image**:

   ```bash
   docker build -t my-fastapi-app .
   ```

2. **Run the Docker container**:

   ```bash
   docker run -d -p 8000:8000 my-fastapi-app
   ```

   Access the application at `http://localhost:8000/`.

## Deployment

This application is ready for deployment on platforms like DigitalOcean. Follow the platform-specific instructions to deploy using the provided Dockerfile.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.