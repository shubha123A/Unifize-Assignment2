# Unifize Recruitment Automation Prototype

This repository contains a prototype backend for a recruitment automation system targeted at a Backend Engineer (Automations) role at Unifize.

## What it is
- A hiring workflow automation engine for candidate screening, interview scheduling, reminders, and offer-stage progression.
- Built as a lightweight Python FastAPI backend with SQLite persistence.
- Designed to be a process-driven solution for Unifize recruiting operations.

## Key features
- Job creation and candidate intake
- Automated stage transitions
- Interview scheduling and automated reminders
- Pipeline dashboard + action log
- Configurable automation flows for recruiting teams

## Run locally
1. Install dependencies:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

2. Start the API:

```bash
uvicorn app:app --reload
```

3. Open `http://127.0.0.1:8000/docs` for API exploration.
