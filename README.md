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

<img width="1918" height="970" alt="Screenshot 2026-06-17 095420" src="https://github.com/user-attachments/assets/f99984eb-15e3-4f97-a476-1b4c727b6f87" />
