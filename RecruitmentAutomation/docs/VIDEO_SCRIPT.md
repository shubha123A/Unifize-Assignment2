# Demo Video Script

## Title
Unifize Recruitment Automation Prototype — Backend Engineer (Automations) Demo

## Opening
- Brief introduction: "Hi, I’m [Your Name], and this is a backend automation prototype for Unifize recruiting operations."
- Explain the objective: "The goal is to automate candidate intake, screening, interview scheduling, and offer progression."

## Walkthrough sections

1. System overview
   - Show the repository structure.
   - Mention `app.py`, `services.py`, `db.py`, and `docs/SOLUTION.md`.

2. Creating a job
   - Demonstrate `POST /jobs` in Swagger or curl.
   - Explain how jobs anchor the recruiting process.

3. Adding a candidate
   - Create a candidate with `POST /candidates`.
   - Discuss how the system captures sourcing data and initial status.

4. Automation in action
   - Run `POST /automation/run`.
   - Show a screening interview created automatically.
   - Mention the action log entry for automation.

5. Completing an interview
   - Complete the interview via `POST /interviews/{id}/complete`.
   - Show candidate transition to `Offer` or `Rejected`.

6. Pipeline monitoring
   - Show `GET /dashboard` and `GET /actions`.
   - Highlight how a recruiter or hiring manager can see process health.

## Closing
- Recap the benefits:
  - faster intake
  - automated screening triggers
  - clear decision automation
  - transparent audit trail
- End with a call-out: "This is a foundation designed for Unifize’s next recruitment automation process."