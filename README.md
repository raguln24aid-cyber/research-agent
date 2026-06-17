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
<img width="1918" height="1031" alt="Screenshot 2026-06-17 095017" src="https://github.com/user-attachments/assets/1a1ef30f-ae4a-4521-8a0f-9db6b4eeadef" />
<img width="1918" height="970" alt="Screenshot 2026-06-17 095420" src="https://github.com/user-attachments/assets/af4f6213-6a44-4181-b108-00d27cc0133d" />
<img width="1918" height="970" alt="Screenshot 2026-06-17 095400" src="https://github.com/user-attachments/assets/e07d871a-7930-4520-b90d-0dfcd0183856" />
<img width="1918" height="972" alt="Screenshot 2026-06-17 095346" src="https://github.com/user-attachments/assets/2e2d0ce6-e99e-4dba-ad30-abda29e06c77" />
<img width="1918" height="971" alt="Screenshot 2026-06-17 095210" src="https://github.com/user-attachments/assets/94ec46bf-45c9-4e16-82d7-8b981fcdace6" />
<img width="1918" height="972" alt="Screenshot 2026-06-17 095155" src="https://github.com/user-attachments/assets/5a936561-e678-4f0d-bf1b-2e31c80846b5" />




