# User Journeys for Unifize Recruitment Automation

## Hiring manager: Open a new backend role
1. Log in to the Unifize recruiting dashboard.
2. Use `POST /jobs` to create a role for "Backend Engineer (Automations)".
3. Confirm the role is visible in the pipeline and ready for candidate intake.

## Sourcer: Add a candidate into the process
1. Source a qualified candidate and collect contact details.
2. Submit the candidate through `POST /candidates`.
3. The system records the candidate and prepares them for screening.
4. A scheduled automation run books a phone screen automatically.

## Recruiter: Run automation and monitor progress
1. Use `POST /automation/run` each morning or configure cron to execute automatically.
2. The automation engine schedules interviews for all newly applied candidates.
3. The recruiter sees the pending interviews and follow-up reminders in `GET /actions`.

## Interviewer: Complete evaluation
1. After the screening interview, submit notes and a decision through `POST /interviews/{id}/complete`.
2. If the candidate passes, the system advances them to `Offer`.
3. If the candidate does not match, they move to `Rejected` and the action log keeps the audit trail.

## Talent operations: Review pipeline health
1. Open `GET /dashboard` to view stage counts.
2. Identify bottlenecks like high numbers in `Screening` or `Interview`.
3. Use the activity stream from `GET /actions` to see how quickly candidates are moving.
