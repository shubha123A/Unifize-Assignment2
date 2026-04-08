# Unifize Org Process Catalog

This workspace now contains two separate process prototypes for the same Unifize organization:

1. **Recruitment Automation**
   - Location: `RecruitmentAutomation/`
   - Process type: hiring workflow automation
   - Key actions: job creation, candidate intake, interview scheduling, pass/fail decision automation

2. **Event Management**
   - Location: `EventManagement/`
   - Process type: event planning and execution
   - Key actions: event creation, session scheduling, attendee registration, reminder automation

## Same org, different processes
The prototypes are designed to coexist conceptually within the Unifize org as independent operational workflows. They share the same architecture pattern and automation mindset, but they serve different teams and business objectives:

- Recruitment: HR and talent acquisition
- Event management: operations, marketing, and customer engagement

## How to run each process
- Recruitment prototype:
  - `cd RecruitmentAutomation`
  - `pip install -r requirements.txt`
  - `uvicorn app:app --reload --port 8000`
  - API docs: `http://127.0.0.1:8000/docs`

- Event management prototype:
  - `cd EventManagement`
  - `pip install -r requirements.txt`
  - `uvicorn app:app --reload --port 8001`
  - API docs: `http://127.0.0.1:8001/docs`

## Why this is useful for Unifize
- Demonstrates how Unifize can model multiple operational processes in the same organization.
- Provides clear separation of concerns for teams while reusing automation architecture.
- Helps show process-first engineering capability for a Backend Engineer (Automations) role.
