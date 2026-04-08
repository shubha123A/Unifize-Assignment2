# Event Management User Journeys

## Event planner: create a new event
1. Create an event via `POST /events`.
2. Set the event title, category, dates, and location.
3. Track the new event in the dashboard.

## Program manager: schedule sessions
1. Create sessions using `POST /sessions`.
2. Assign speakers and dates to each session.
3. Confirm the event experience is planned end-to-end.

## Marketing: add attendees
1. Register attendees using `POST /attendees`.
2. Verify attendees are linked to the right event.
3. Use the action log to monitor registration activity.

## Operations: run automation
1. Execute `POST /automation/run` daily.
2. The system opens registration for events starting within one week.
3. It queues reminders for sessions due in the next 24 hours.
4. It completes events whose end date has passed.

## Leadership: review the event pipeline
1. Use `GET /dashboard` for counts of events, sessions, and attendees.
2. Review status counts to see how many events are in planning, registration, or completion.
3. Use `GET /actions` to audit key state changes.
