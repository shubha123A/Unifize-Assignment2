# Unifize Event Management Solution

This prototype is a separate Unifize process for event planning and execution. It complements the recruitment automation prototype by covering a different operational domain.

## What it does
- Creates events and event sessions
- Registers attendees for events
- Opens registration automatically for upcoming events
- Sends session reminder signals before sessions
- Advances overall event status from Draft to Completed

## Why this is a different process
- Recruitment automation is hiring-focused.
- Event management is planning-focused.
- Both are built on the same organization, but they automate separate workflows in Unifize.

## Technical approach
- FastAPI for an HTTP workflow API
- SQLite persistence for event, attendee, session, and action log entities
- A lightweight automation worker in `services.py`
- Event lifecycle states: `Draft` → `Registration Open` → `In Progress` → `Completed`

## Key user journeys
1. Event planner creates an event.
2. Coordinator schedules sessions.
3. Marketing opens registration and collects attendees.
4. Automation opens registration automatically for events starting soon.
5. Day-of reminders are triggered for sessions.
6. The event completes and logs the outcome.

## Unifize org relationship
This process is intended as an independent workflow within the same Unifize org, demonstrating the flexibility to add new operational processes without changing the existing recruitment workflow.
