# Unifize Event Management Prototype

This repository contains a second prototype backend for a separate Unifize process: event management.

## What it is
- A lightweight event planning and registration workflow for internal or external events.
- Built with Python FastAPI and SQLite.
- Designed to run alongside the recruitment automation prototype as another Unifize process.

## Run locally
1. Activate the same Python virtual environment used for the recruitment prototype.

```powershell
cd C:\Users\sshub\OneDrive\Desktop\Assignment 2\EventManagement
..\venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app:app --reload
```

2. Open `http://127.0.0.1:8001/docs` to explore the event API.

## Notes
- This process is intentionally distinct from recruitment.
- It supports event planning, attendee registration, session scheduling, and automation for reminders.
