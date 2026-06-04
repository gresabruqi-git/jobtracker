# JobTracker

**A Full-Stack Web Application for Job Application Management**

| | |
|---|---|
| **Author** | gresabruqi |
| **Repository** | [github.com/gresabruqi-git/jobtracker](https://github.com/gresabruqi-git/jobtracker) |
| **Stack** | Django REST Framework · Vue 3 · JWT · SQLite |

---

## Abstract

JobTracker is a full-stack software system designed to support structured management of job search activities. The application enables authenticated users to record, update, and monitor job applications through a RESTful backend and a single-page frontend. Core capabilities include user registration and authentication, persistent storage of application records, status-based filtering, company search, and aggregated dashboard metrics. The system follows a client–server architecture with clear separation between the API layer and the presentation layer.

## 1. Introduction

### 1.1 Background

Managing multiple job applications across companies, roles, and hiring stages is a common challenge during active job search. Centralized tracking reduces information loss and supports consistent follow-up.

### 1.2 Purpose

The purpose of this project is to provide a practical, maintainable platform that:

1. Stores job application data in a structured relational model.
2. Enforces per-user data isolation through authentication.
3. Exposes a documented HTTP API for programmatic access.
4. Presents an accessible web interface for day-to-day use.

### 1.3 Scope

The current implementation covers user accounts, JWT-based session management, full CRUD operations on job applications, search and filtering, and dashboard statistics. Deployment to production environments and third-party integrations are outside the present scope unless extended in future work.

## 2. System Overview

### 2.1 Architecture

The system adopts a **three-tier** pattern:

- **Presentation tier** — Vue 3 SPA (Vite) communicating over HTTPS/HTTP with the API.
- **Application tier** — Django REST Framework views and serializers enforcing business rules and authorization.
- **Data tier** — SQLite relational database storing users and application entities.

Authentication uses **JSON Web Tokens (JWT)** issued by `djangorestframework-simplejwt`, with protected routes on both backend endpoints and frontend navigation guards.

### 2.2 Functional Requirements (Implemented)

| ID | Requirement |
|----|-------------|
| FR-01 | User registration and login |
| FR-02 | Token refresh and logout |
| FR-03 | Create, read, update, and delete job applications |
| FR-04 | Search applications by company name |
| FR-05 | Filter applications by status |
| FR-06 | Display dashboard statistics by status |

### 2.3 Technology Stack

| Layer | Components |
|-------|------------|
| Backend | Python 3.11+, Django, Django REST Framework, Simple JWT, django-cors-headers |
| Frontend | Vue 3, Vite, Vue Router, Pinia, Axios, Tailwind CSS |
| Database | SQLite |

## 3. Project Structure

```text
jobtracker/
├── backend/
│   ├── accounts/       # Authentication and user management
│   ├── applications/   # Job application domain model and API
│   ├── config/         # Django configuration and routing
│   └── manage.py
└── frontend/
    ├── src/            # Views, state management, API client
    ├── package.json
    └── vite.config.js
```

## 4. Data Model

Each **JobApplication** record is associated with a single authenticated user and contains:

| Field | Type | Description |
|-------|------|-------------|
| `company_name` | string | Employer or organization name |
| `position` | string | Role or job title |
| `date_applied` | date | Date the application was submitted |
| `status` | enum | One of: `applied`, `interview`, `offer`, `rejected` |
| `notes` | text | Optional free-form notes |

## 5. Installation and Execution

### 5.1 Prerequisites

- Python 3.11 or newer
- Node.js (LTS recommended) and npm
- Git

### 5.2 Repository Setup

```powershell
git clone https://github.com/gresabruqi-git/jobtracker.git
cd jobtracker
```

### 5.3 Backend Configuration

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install django djangorestframework djangorestframework-simplejwt django-cors-headers
.\.venv\Scripts\python.exe manage.py makemigrations
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py runserver
```

Default API base URL: `http://127.0.0.1:8000`

### 5.4 Frontend Configuration

```powershell
cd frontend
npm install
copy .env.example .env
npm run dev
```

Default application URL: `http://localhost:5173`

Environment variable `VITE_API_URL` (see `frontend/.env.example`) must point to the backend base URL.

### 5.5 Routine Operation

After initial setup, start the backend and frontend in separate terminals using `manage.py runserver` and `npm run dev` respectively. For a production-oriented frontend build, run `npm run build` followed by `npm run preview`.

### 5.6 Schema Migrations

When the data model changes, apply migrations from the `backend` directory:

```powershell
.\.venv\Scripts\python.exe manage.py makemigrations
.\.venv\Scripts\python.exe manage.py migrate
```

The database file is located at `backend/jobtracker.sqlite3`.

## 6. API Specification

All protected endpoints require a valid JWT in the `Authorization: Bearer <token>` header.

### 6.1 Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/auth/register/` | Create a new user account |
| `POST` | `/api/auth/login/` | Obtain access and refresh tokens |
| `POST` | `/api/auth/refresh/` | Renew access token |
| `POST` | `/api/auth/logout/` | Invalidate session (client-side token discard) |

### 6.2 Applications

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/applications/` | List applications (supports search and filter) |
| `POST` | `/api/applications/` | Create a new application |
| `GET` | `/api/applications/:id/` | Retrieve one application |
| `PUT` | `/api/applications/:id/` | Update an application |
| `DELETE` | `/api/applications/:id/` | Remove an application |

### 6.3 Dashboard

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/dashboard/stats/` | Return counts grouped by application status |

## 7. Development Notes

- The Python virtual environment (`.venv`) and `node_modules` must not be committed; they are excluded via `.gitignore`.
- Cross-origin requests from the frontend are permitted through `django-cors-headers` configuration in the backend.

## 8. Author

**gresabruqi**

GitHub: [https://github.com/gresabruqi-git](https://github.com/gresabruqi-git)

---

*Document version: 1.0 — JobTracker technical documentation.*
