# Unifize Recruitment Automation Solution

## Overview
This solution is a recruitment automation backend built for Unifize. It models a hiring process with candidate intake, automated screening, interview orchestration, and offer-stage progression.

The prototype is designed for an Automations-focused Backend Engineer role, with a process that can be configured and extended for Unifize recruiting teams.

## Process Design
The system contains two core workflows:

1. Candidate intake and automated screening
   - A recruiter or sourcer creates a candidate record for an open job.
   - The system automatically assigns the candidate the `Screening` stage.
   - It schedules a phone screen interview and logs the action.

2. Interview completion and decision automation
   - Recruiters update interviews with notes and pass/fail decisions.
   - The system transitions the candidate to `Offer` when passed, or `Rejected` when failed.
   - All stage changes and reminders are logged.

## Technical architecture
- FastAPI provides an HTTP API layer for workflow orchestration.
- SQLite stores jobs, candidates, interviews, and action logs.
- A lightweight workflow engine in `services.py` handles stage transitions and reminder generation.

## Differences from an existing Unifize process
- This workflow focuses on recruitment pipeline automation rather than customer onboarding or sales processes.
- It provides explicit candidate state transitions and automated interview reminders, using a process-based orchestration model.
- It emphasizes backend automation triggers and actionable logging for audits and notifications.

## Key user journeys

### 1. Hiring manager creates a role
- Create a `Job` via `POST /jobs`.
- The role becomes available for recruiters and sourcers.

### 2. Sourcer adds a new candidate
- Create a `Candidate` via `POST /candidates`.
- The system logs the candidate intake and assigns `Applied`.
- A later automation run schedules a screening interview and moves the candidate into `Screening`.

### 3. Recruiter completes the phone screen
- Recruiter marks the `Interview` complete via `POST /interviews/{id}/complete`.
- If the decision is `pass`, candidate status becomes `Offer`.
- If the decision is `fail`, status becomes `Rejected`.

### 4. Recruiter monitors the pipeline
- `GET /dashboard` shows counts per stage.
- `GET /actions` provides a recent activity timeline.

## How it maps to the role
- Demonstrates backend engineering with REST API design and workflow automation.
- Shows ability to convert process logic into data-driven automation.
- Provides a maintainable foundation for future Unifize automations such as email notifications, calendar integrations, or ATS synchronization.
