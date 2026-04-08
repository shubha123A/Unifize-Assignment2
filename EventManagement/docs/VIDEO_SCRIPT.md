# Event Management Demo Video Script

## Title
Unifize Event Management Prototype — Backend Engineer (Automations) Demo

## Opening
- "Hi, I’m [Your Name]. This demo shows a second Unifize process for events, built as a separate automation workflow."
- Explain the goal: "Create, register, schedule, and automate event delivery."

## Walkthrough
1. System introduction
   - Show `EventManagement/app.py`, `services.py`, and `db.py`.
   - Explain the event lifecycle.

2. Creating an event
   - Use `POST /events`.
   - Describe why event planning is a separate process from recruiting.

3. Scheduling sessions
   - Use `POST /sessions`.
   - Explain session reminders and operational handoff.

4. Registering attendees
   - Use `POST /attendees`.
   - Show how attendee records are captured.

5. Automation run
   - Use `POST /automation/run`.
   - Explain registration opening and session reminders.

6. Monitoring
   - Show `GET /dashboard` and `GET /actions`.
   - Highlight the event pipeline and audit trail.

## Closing
- Recap the value: "Two separate Unifize processes now exist in the same org: recruitment and event management."
- Mention that this approach demonstrates process modularity and scalable backend automation.
