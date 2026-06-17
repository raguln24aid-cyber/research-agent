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

- Real-time Agent Monitoring
- PDF Export
- Source Verification
- Human-in-the-Loop Review
- Multi-Agent Parallel Research

---

## Author

Ragul N


GitHub: https://github.com/raguln24aid-cyber

<img width="1918" height="1031" alt="Screenshot 2026-06-17 095017" src="https://github.com/user-attachments/assets/a380f311-7627-492d-afbc-3ccda0207c60" />
<img width="1918" height="972" alt="Screenshot 2026-06-17 095155" src="https://github.com/user-attachments/assets/0476b403-f664-44f2-a333-10c5f26430c8" />
<img width="1918" height="971" alt="Screenshot 2026-06-17 095210" src="https://github.com/user-attachments/assets/4b9977c2-c799-4df0-bacd-207006f19ace" />
<img width="1918" height="972" alt="Screenshot 2026-06-17 095346" src="https://github.com/user-attachments/assets/761ee6b6-86e0-43e4-bfb2-bd5e4c0ce3ec" />
<img width="1918" height="970" alt="Screenshot 2026-06-17 095400" src="https://github.com/user-attachments/assets/0594bd13-75fc-4f4e-90ac-505ca00398ae" />
<img width="1918" height="970" alt="Screenshot 2026-06-17 095420" src="https://github.com/user-attachments/assets/c9c73e4d-3aa2-4313-8469-fdb8a919ca9a" />






