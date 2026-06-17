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
<img width="1918" height="970" alt="Screenshot 2026-06-17 095420" src="https://github.com/user-attachments/assets/ff5bf51b-01a0-404b-8ded-f859573112a8" />
<img width="1918" height="970" alt="Screenshot 2026-06-17 095400" src="https://github.com/user-attachments/assets/2112614c-9f5f-445f-b6f2-d4f7df559432" />
<img width="1918" height="972" alt="Screenshot 2026-06-17 095346" src="https://github.com/user-attachments/assets/5ef40ab0-063f-49eb-b919-8f6de00038fb" />
<img width="1918" height="971" alt="Screenshot 2026-06-17 095210" src="https://github.com/user-attachments/assets/63ff760d-ecca-44dd-8e60-dedddf94b429" />
<img width="1918" height="972" alt="Screenshot 2026-06-17 095155" src="https://github.com/user-attachments/assets/c554bf20-b409-467f-89e3-5431562c73b8" />
<img width="1918" height="1031" alt="Screenshot 2026-06-17 095017" src="https://github.com/user-attachments/assets/6a25cacf-8955-4e14-8d03-792814239b17" />




