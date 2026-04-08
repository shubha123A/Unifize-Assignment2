from datetime import datetime
from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from db import init_db, SessionLocal, Event, EventSession, Attendee
from schemas import EventCreate, EventRead, EventSessionCreate, EventSessionRead, AttendeeCreate, AttendeeRead, ActionLogRead
import services

init_db()
app = FastAPI(title="Unifize Event Management")

@app.get("/")
def root_redirect():
    return RedirectResponse(url="/docs")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/events", response_model=EventRead)
def create_event(event: EventCreate, db: Session = Depends(get_db)):
    instance = Event(
        title=event.title,
        category=event.category,
        location=event.location,
        start_date=event.start_date,
        end_date=event.end_date,
        status="Draft",
        created_at=datetime.utcnow(),
    )
    db.add(instance)
    db.commit()
    db.refresh(instance)
    return instance

@app.post("/events/{event_id}/open-registration", response_model=EventRead)
def open_registration(event_id: int, db: Session = Depends(get_db)):
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return services.open_registration(db, event)

@app.post("/events/{event_id}/start", response_model=EventRead)
def start_event(event_id: int, db: Session = Depends(get_db)):
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    try:
        return services.start_event(db, event)
    except services.WorkflowError as exc:
        raise HTTPException(status_code=400, detail=str(exc))

@app.post("/events/{event_id}/complete", response_model=EventRead)
def complete_event(event_id: int, db: Session = Depends(get_db)):
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    try:
        return services.complete_event(db, event)
    except services.WorkflowError as exc:
        raise HTTPException(status_code=400, detail=str(exc))

@app.post("/sessions", response_model=EventSessionRead)
def create_session(session: EventSessionCreate, db: Session = Depends(get_db)):
    event = db.query(Event).filter(Event.id == session.event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    instance = EventSession(
        event_id=session.event_id,
        title=session.title,
        speaker=session.speaker,
        scheduled_at=session.scheduled_at,
        status="Pending",
    )
    db.add(instance)
    db.commit()
    db.refresh(instance)
    services.log_action(db, event=event, action="Session created", payload=session.title)
    return instance

@app.post("/attendees", response_model=AttendeeRead)
def create_attendee(attendee: AttendeeCreate, db: Session = Depends(get_db)):
    event = db.query(Event).filter(Event.id == attendee.event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    instance = Attendee(
        event_id=attendee.event_id,
        first_name=attendee.first_name,
        last_name=attendee.last_name,
        email=attendee.email,
        registration_status="Registered",
        created_at=datetime.utcnow(),
    )
    db.add(instance)
    db.commit()
    db.refresh(instance)
    services.register_attendee(db, instance)
    return instance

@app.post("/automation/run")
def run_automation(db: Session = Depends(get_db)):
    reminders = services.run_automation(db)
    return {"session_reminders": len(reminders)}

@app.get("/dashboard")
def dashboard(db: Session = Depends(get_db)):
    return {
        "events": db.query(Event).count(),
        "sessions": db.query(EventSession).count(),
        "attendees": db.query(Attendee).count(),
        "status_counts": {
            "Draft": db.query(Event).filter(Event.status == "Draft").count(),
            "Registration Open": db.query(Event).filter(Event.status == "Registration Open").count(),
            "In Progress": db.query(Event).filter(Event.status == "In Progress").count(),
            "Completed": db.query(Event).filter(Event.status == "Completed").count(),
            "Archived": db.query(Event).filter(Event.status == "Archived").count(),
        },
    }

@app.get("/actions", response_model=list[ActionLogRead])
def action_log(db: Session = Depends(get_db)):
    from db import ActionLog
    return db.query(ActionLog).order_by(ActionLog.created_at.desc()).limit(50).all()
