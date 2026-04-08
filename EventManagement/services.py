from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from db import Event, EventSession, Attendee, ActionLog

STATUS_FLOW = ["Draft", "Registration Open", "In Progress", "Completed", "Archived"]

class WorkflowError(Exception):
    pass


def log_action(db: Session, event=None, attendee=None, action: str = "", payload: str = ""):
    entry = ActionLog(
        event_id=event.id if event else None,
        attendee_id=attendee.id if attendee else None,
        action=action,
        payload=payload,
        created_at=datetime.utcnow(),
    )
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry


def open_registration(db: Session, event: Event):
    event.status = "Registration Open"
    db.add(event)
    db.commit()
    db.refresh(event)
    log_action(db, event=event, action="Registration opened", payload=event.title)
    return event


def start_event(db: Session, event: Event):
    if event.status != "Registration Open":
        raise WorkflowError("Event must be in Registration Open state before starting")
    event.status = "In Progress"
    db.add(event)
    db.commit()
    db.refresh(event)
    log_action(db, event=event, action="Event started", payload=event.title)
    return event


def complete_event(db: Session, event: Event):
    if event.status != "In Progress":
        raise WorkflowError("Event must be in progress to complete")
    event.status = "Completed"
    db.add(event)
    db.commit()
    db.refresh(event)
    log_action(db, event=event, action="Event completed", payload=event.title)
    return event


def register_attendee(db: Session, attendee: Attendee):
    attendee.registration_status = "Registered"
    db.add(attendee)
    db.commit()
    db.refresh(attendee)
    event = db.query(Event).filter(Event.id == attendee.event_id).first()
    log_action(db, event=event, attendee=attendee, action="Attendee registered", payload=attendee.email)
    return attendee


def run_automation(db: Session):
    now = datetime.utcnow()
    reminders = []

    events = db.query(Event).filter(Event.status == "Draft").all()
    for event in events:
        if event.start_date - now <= timedelta(days=7):
            open_registration(db, event)

    sessions = db.query(EventSession).filter(EventSession.status == "Pending").all()
    for session in sessions:
        delta = session.scheduled_at - now
        if timedelta(hours=0) <= delta <= timedelta(days=1):
            reminders.append(session)
            event = db.query(Event).filter(Event.id == session.event_id).first()
            log_action(db, event=event, action="Session reminder queued", payload=session.title)

    in_progress_events = db.query(Event).filter(Event.status == "In Progress", Event.end_date <= now).all()
    for event in in_progress_events:
        complete_event(db, event)

    return reminders
