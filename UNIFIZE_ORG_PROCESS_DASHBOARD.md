# Unifize Org Process Dashboard

This workspace contains two separate automation processes for the Unifize organization.

## Process 1: Recruitment Automation
- Folder: `RecruitmentAutomation`
- Purpose: automate hiring workflows for Backend Engineer (Automations) roles
- Key features:
  - Create jobs and candidate records
  - Schedule screening interviews automatically
  - Complete interviews and transition candidates to `Offer` or `Rejected`
  - Track pipeline status and action logs
- Run it on port `8000` with:
  ```powershell
  cd "C:\Users\sshub\OneDrive\Desktop\Assignment 2\RecruitmentAutomation"
  ..\venv\Scripts\Activate.ps1
  pip install -r requirements.txt
  uvicorn app:app --reload --port 8000
  ```
- API docs:
  `http://127.0.0.1:8000/docs`

## Process 2: Event Management
- Folder: `EventManagement`
- Purpose: automate event planning, session scheduling, attendee registration, and reminders
- Key features:
  - Create events and session schedules
  - Register attendees for events
  - Automatically open registration for upcoming events
  - Queue session reminders and complete events after the end date
- Run it on port `8001` with:
  ```powershell
  cd "C:\Users\sshub\OneDrive\Desktop\Assignment 2\EventManagement"
  ..\venv\Scripts\Activate.ps1
  pip install -r requirements.txt
  uvicorn app:app --reload --port 8001
  ```
- API docs:
  `http://127.0.0.1:8001/docs`

## Why this matters for Unifize
- Demonstrates how multiple processes can be hosted under the same org with separate workflows.
- Shows backend automation design across distinct domains: recruiting and event operations.
- Provides a reusable structure for future Unifize workflows.

## Recommended next steps
1. Use `RecruitmentAutomation` for hiring process demos.
2. Use `EventManagement` for operations or marketing process demos.
3. Extend either process with email notifications, calendar integration, or a shared org dashboard.
