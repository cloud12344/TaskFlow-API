# TaskFlow API

## Module and Coursework Context
This repository contains my individual coursework project for the **Web Services and Web Data** module (`XJCO3011`). The project implements a data-driven web API backed by a SQL database and is designed to satisfy the coursework requirement for a fully functional CRUD-based API system.

## Project Overview
TaskFlow API is a task management system built with **Django**, **Django REST Framework**, and **SQLite**. It supports full CRUD operations for a single `Task` resource and returns structured JSON responses for API consumers. In addition to the API endpoints, the project also includes simple HTML navigation pages to make the system easier to demonstrate during the oral examination.

The application allows users to:
- create tasks
- view all tasks
- view one task by ID
- update tasks
- delete tasks
- navigate between task pages using simple buttons and links

## Why This Project
I selected a task management domain because it is a realistic and easy-to-understand use case for a web API. It is suitable for demonstrating:
- relational database integration
- REST-style CRUD operations
- data validation
- structured HTTP responses
- future extensibility for analytics, authentication, and filtering

## Main Features
- Full CRUD support for a `Task` resource
- SQL database integration using SQLite
- Django ORM model design
- Django REST Framework JSON API endpoints
- Validation for required and controlled fields
- Timestamp tracking for created and updated records
- Custom HTML pages for easier local demonstration and task navigation
- Modular Django app structure

## Technology Stack
- **Programming language:** Python
- **Framework:** Django
- **API framework:** Django REST Framework
- **Database:** SQLite
- **ORM:** Django ORM
- **Interface for demonstration:** Django templates

## Task Data Model
The system currently manages one main entity: `Task`.

### Fields
- `id`: unique task identifier
- `title`: short task title
- `description`: optional longer text description
- `status`: `pending`, `in_progress`, or `completed`
- `priority`: `low`, `medium`, or `high`
- `due_date`: optional due date/time
- `created_at`: record creation timestamp
- `updated_at`: record update timestamp

## Project Structure
```text
cwk1/
├── manage.py
├── requirements.txt
├── README.md
├── taskflow.db
├── taskflow_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── tasks/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   └── templates/
└── docs/
    ├── api_documentation.md
    └── technical_report.md
```

## Setup Instructions
### 1. Create and activate a virtual environment
On Windows:
```bash
python -m venv .venv
.venv\Scripts\activate
```

On macOS / Linux:
```bash
python -m venv .venv
source .venv/bin/activate
```

### 2. Install project dependencies
```bash
pip install -r requirements.txt
```

### 3. Apply migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Run the development server
```bash
python manage.py runserver
```

### 5. Open the project locally
After starting the server, open:

- Main task page: [http://127.0.0.1:8000/api/tasks/](http://127.0.0.1:8000/api/tasks/)
- Task selector page: [http://127.0.0.1:8000/api/tasks/select/](http://127.0.0.1:8000/api/tasks/select/)
- Raw API list endpoint: [http://127.0.0.1:8000/api/tasks/api/](http://127.0.0.1:8000/api/tasks/api/)

## API Endpoints
### JSON API Endpoints
- `GET /api/tasks/api/` - return all tasks
- `POST /api/tasks/api/` - create a new task
- `GET /api/tasks/<id>/` - return one task
- `PUT /api/tasks/<id>/` - update an existing task
- `DELETE /api/tasks/<id>/` - delete a task

### HTML Demonstration Pages
These pages were added to make the system easier to present during the oral exam:
- `GET /api/tasks/` - task home page with task list and create form
- `GET /api/tasks/select/` - task selector page
- `GET /api/tasks/page/<id>/` - navigable task detail page

## Example JSON Request
```json
{
  "title": "Finish coursework report",
  "description": "Write the final technical report section",
  "status": "pending",
  "priority": "high",
  "due_date": "2026-04-25T12:00:00Z"
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
  "due_date": "2026-04-25T12:00:00Z",
  "created_at": "2026-04-20T10:00:00Z",
  "updated_at": "2026-04-20T10:00:00Z"
}
```

## HTTP Status Codes Used
- `200 OK` - successful read or update
- `201 Created` - resource created successfully
- `204 No Content` - resource deleted successfully
- `400 Bad Request` - invalid request data
- `404 Not Found` - requested task does not exist

## Validation Rules
- `title` is required and cannot be blank
- `status` must be one of: `pending`, `in_progress`, `completed`
- `priority` must be one of: `low`, `medium`, `high`
- `due_date` is optional


## Testing Approach
The current project has been manually tested in local development by:
- creating tasks through the HTML task page
- retrieving all tasks from the JSON API
- viewing individual tasks by ID
- updating tasks through the API
- deleting tasks through the API
- checking navigation between the custom task pages
- confirming that migrations and database persistence work correctly




