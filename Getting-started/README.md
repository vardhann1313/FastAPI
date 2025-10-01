# Backend using FastAPI
Exploring Python's Backend framework "FastAPI", Creating mini backend projects.
FastAPI is a modern, high-performance web framework for building APIs with Python. It is designed for ease of use.

## How to get started with FastAPI
### Tech used 
- uv for env and dependency management.
- FastAPI as backend framework.
- uvicorn for server.
### Installation 
- Install python from official website.
- Install uv (powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex").
### Creating first project 
- Create project using command (uv init “project_name”)
- Navigate to project (cd “project_name”)
- Add framework & packages (uv add fastapi uvicorn pydantic python_jose passlib python_multipart python_dotenv )
- If you wrote any dependency manually in .poml file sync it using uv (uv sync)
- Write server code inside “main.py”
- Run project (uv run main.py)