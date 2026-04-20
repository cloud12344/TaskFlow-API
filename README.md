# TaskFlow API

## Project Overview
TaskFlow API is a data-driven web API for managing personal task items. It allows users to create, read, update, and delete tasks stored in a relational database. The API also validates user input and returns appropriate HTTP status codes for successful and failed requests.

This project was developed for the Web Services and Web Data coursework and demonstrates the core principles of API design, database integration, input validation, and structured JSON responses.

## Current Features
- Full CRUD operations for `Task`
- SQLite database integration with SQLAlchemy ORM
- Request and response validation with Pydantic
- Automatic OpenAPI / Swagger documentation via FastAPI
- Error handling for missing resources
- Structured task fields including status, priority, and due date

## Task Model
Each task currently contains the following fields:
- `id`
- `title`
- `description`
- `status` (`pending`, `in_progress`, `completed`)
- `priority` (`low`, `medium`, `high`)
- `due_date`
- `created_at`
- `updated_at`

## Technology Stack
- **Language**: Python
- **Framework**: FastAPI
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Validation**: Pydantic
- **Server**: Uvicorn

## Project Structure
```text
cwk1/
├── app/
│   ├── __init__.py
│   ├── crud.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   └── schemas.py
├── README.md
├── requirements.txt
└── XJCO3011_Coursework1_Brief__2025_2026.pdf
```

## Setup Instructions
### 1. Create a virtual environment
On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

On Linux / macOS:
```bash
python -m venv venv
source venv/bin/activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the API
```bash
uvicorn app.main:app --reload
```

### 4. Open the documentation
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## API Endpoints
### Task endpoints
- `POST /tasks` - create a new task
- `GET /tasks` - retrieve all tasks
- `GET /tasks/{task_id}` - retrieve a specific task
- `PUT /tasks/{task_id}` - update a specific task
- `DELETE /tasks/{task_id}` - delete a specific task

## Example JSON Request
### Create a task
```json
{
  "title": "Finish coursework report",
  "description": "Write the final technical report section",
  "status": "pending",
  "priority": "high",
  "due_date": "2026-04-25T12:00:00"
}
```

## Example JSON Response
```json
{
  "id": 1,
  "title": "Finish coursework report",
  "description": "Write the final technical report section",
  "status": "pending",
  "priority": "high",
  "due_date": "2026-04-25T12:00:00",
  "created_at": "2026-04-20T10:00:00",
  "updated_at": null
}
```

## Error Handling
The API currently returns standard HTTP status codes such as:
- `201 Created` when a task is created successfully
- `200 OK` when a task is retrieved or updated successfully
- `204 No Content` when a task is deleted successfully
- `404 Not Found` when a task does not exist
- `422 Unprocessable Entity` when validation fails

## Documentation and Coursework Materials
The repository should include the following submission materials:
- API documentation PDF
- Technical report PDF
- Presentation slides
- Public GitHub repository with commit history

Draft coursework support files prepared in this repository:
- `API_DOCUMENTATION.md`
- `TECHNICAL_REPORT_DRAFT.md`
- `PRESENTATION_SLIDES_OUTLINE.md`

## Current Status
Completed:
- Project structure
- Database configuration
- Task model definition
- CRUD endpoints
- Input validation
- Basic error handling

Planned next steps:
- Add testing
- Add filtering or analytics endpoints
- Improve modular code structure
- Prepare PDF documentation and presentation slides

## Notes for Submission
Before final submission, make sure to:
- export the API documentation to PDF
- convert the technical report into PDF
- prepare the presentation in PowerPoint format
- include a GenAI declaration and selected conversation logs as appendix material

## Deployment on PythonAnywhere
This project is now prepared to be deployed more safely by using an environment-aware database configuration.

### Deployment-related improvements
- `app/database.py` now supports a `DATABASE_URL` environment variable.
- If `DATABASE_URL` is not set, the app falls back to a local SQLite database file.
- SQLite automatically uses the correct SQLAlchemy `check_same_thread` option.
- `requirements.txt` now uses pinned dependency versions for more stable deployment.

### Recommended PythonAnywhere workflow
1. Push the project to GitHub.
2. Log into PythonAnywhere and open a Bash console.
3. Clone the repository:
   ```bash
   git clone <your-repository-url>
   ```
4. Create a virtual environment and install dependencies:
   ```bash
   mkvirtualenv --python=/usr/bin/python3.10 taskflow-env
   workon taskflow-env
   pip install -r requirements.txt
   ```
5. Create a new web app from the PythonAnywhere dashboard.
6. Point the web app to this project and configure the virtualenv path.
7. Set the source directory so Python can import the `app` package.
8. Configure the app entry point to load `app.main:app`.
9. Reload the web app.

### Database configuration on PythonAnywhere
If you want to keep using SQLite on PythonAnywhere, set a full absolute path through `DATABASE_URL`, for example:

```bash
export DATABASE_URL="sqlite:////home/yourusername/cwk1/taskflow.db"
```

This avoids issues caused by relative file paths when the app runs on the server.

### Suggested next deployment step
Before deploying, test locally with:
```bash
uvicorn app.main:app --reload
```
and confirm the API works at `/docs` and `/redoc`.

