# Research AI Agent

A production-ready multi-agent AI research assistant built with FastAPI, React, MongoDB Atlas, and Groq.

## Features

- JWT Authentication
- User Signup & Login
- MongoDB Atlas Storage
- Research History
- Multi-Agent Workflow
- Report Generation
- Protected Routes
- Responsive Dashboard

## Multi-Agent Architecture

User Query
    ↓
Planner Agent
    ↓
Research Agent
    ↓
Review Agent
    ↓
Report Agent
    ↓
Final Research Report

### Planner Agent
Breaks research topics into tasks and questions.

### Research Agent
Collects facts and evidence.

### Review Agent
Validates information and removes inconsistencies.

### Report Agent
Generates a structured final report.

---

## Tech Stack

### Frontend

- React
- Vite
- TailwindCSS
- React Router

### Backend

- FastAPI
- Python

### Database

- MongoDB Atlas

### AI

- Groq API

### Authentication

- JWT
- bcrypt

---

## Screenshots

### Login Page

![Login](screenshots/login.png)

### Dashboard

![Dashboard](screenshots/dashboard.png)

### Research Workflow

![Research Running](screenshots/research-running.png)

---

## Project Structure

```text
backend/
│
├── api/
├── agents/
├── auth/
├── database/
├── models/
├── schemas/
└── services/

frontend/
│
├── components/
├── pages/
├── hooks/
└── services/
```

## Environment Variables

Backend:

```env
MONGODB_URI=
GROQ_API_KEY=
JWT_SECRET_KEY=
```

## Installation

### Backend

```bash
cd backend

python -m venv .venv

.venv\Scripts\activate

pip install -r requirements.txt

uvicorn main:app --reload
```

### Frontend

```bash
cd frontend

npm install

npm run dev
```

---

## Future Improvements

- LangGraph Integration
- Real-time Agent Monitoring
- PDF Export
- Source Verification
- Human-in-the-Loop Review
- Multi-Agent Parallel Research

---

## Author

Ragul N


GitHub: https://github.com/raguln24aid-cyber
<img width="1918" height="970" alt="Screenshot 2026-06-17 095420" src="https://github.com/user-attachments/assets/28b5e4d0-9e8c-4bd6-876f-6fc166bc427f" />
<img width="1918" height="970" alt="Screenshot 2026-06-17 095400" src="https://github.com/user-attachments/assets/34265e08-df99-4483-bc10-0b4b5d4e9775" />
<img width="1918" height="972" alt="Screenshot 2026-06-17 095346" src="https://github.com/user-attachments/assets/73480fb1-58da-4085-985c-c725e2bdfcca" />
<img width="1918" height="971" alt="Screenshot 2026-06-17 095210" src="https://github.com/user-attachments/assets/33cc9b2e-99c1-485b-b2c0-0f0e3b5d79fb" />
<img width="1918" height="972" alt="Screenshot 2026-06-17 095155" src="https://github.com/user-attachments/assets/7658e301-6eea-45bf-8747-a31ca4a584d7" />
<img width="1918" height="1031" alt="Screenshot 2026-06-17 095017" src="https://github.com/user-attachments/assets/af7658be-fdd2-4ba4-8ee2-d996613940af" />



