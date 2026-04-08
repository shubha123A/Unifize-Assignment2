from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from db import Candidate, Interview, ActionLog

STAGE_FLOW = ["Applied", "Screening", "Interview", "Offer", "Hired", "Rejected"]

class WorkflowError(Exception):
    pass


def log_action(db: Session, candidate: Candidate, action: str, payload: str = ""):
    entry = ActionLog(candidate_id=candidate.id, action=action, payload=payload, created_at=datetime.utcnow())
    db.add(entry)
    candidate.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(candidate)


def advance_candidate(db: Session, candidate: Candidate):
    current_index = STAGE_FLOW.index(candidate.status)
    if current_index < len(STAGE_FLOW) - 2:
        candidate.status = STAGE_FLOW[current_index + 1]
        candidate.updated_at = datetime.utcnow()
        db.add(candidate)
        db.commit()
        db.refresh(candidate)
        log_action(db, candidate, "Stage advanced", candidate.status)
    else:
        raise WorkflowError(f"Candidate {candidate.id} cannot advance from {candidate.status}")
    return candidate


def schedule_screening_interview(db: Session, candidate: Candidate):
    candidate.status = "Screening"
    candidate.updated_at = datetime.utcnow()
    db.add(candidate)
    db.commit()
    db.refresh(candidate)
    interview = Interview(
        candidate_id=candidate.id,
        round_label="Phone Screen",
        interviewer="Recruiter Team",
        scheduled_at=datetime.utcnow() + timedelta(days=1),
        status="Pending",
    )
    db.add(interview)
    db.commit()
    db.refresh(interview)
    log_action(db, candidate, "Interview scheduled", f"Interview {interview.id} on {interview.scheduled_at.isoformat()}")
    return interview


def run_automation(db: Session):
    reminders = []
    now = datetime.utcnow()
    interviews = db.query(Interview).filter(Interview.status == "Pending").all()
    for interview in interviews:
        delta = interview.scheduled_at - now
        if timedelta(hours=0) <= delta <= timedelta(days=1):
            candidate = db.query(Candidate).filter(Candidate.id == interview.candidate_id).first()
            reminders.append((candidate, interview))
            log_action(db, candidate, "Reminder queued", f"Interview reminder for {interview.id}")
    candidates = db.query(Candidate).filter(Candidate.status == "Applied").all()
    for candidate in candidates:
        schedule_screening_interview(db, candidate)
    return reminders


def complete_interview(db: Session, interview: Interview, notes: str, decision: str):
    interview.status = "Completed"
    interview.notes = notes
    db.add(interview)
    db.commit()
    db.refresh(interview)
    candidate = db.query(Candidate).filter(Candidate.id == interview.candidate_id).first()
    log_action(db, candidate, "Interview completed", f"{interview.round_label} decision={decision}")
    if decision.lower() == "pass":
        candidate.status = "Offer"
    else:
        candidate.status = "Rejected"
    candidate.updated_at = datetime.utcnow()
    db.add(candidate)
    db.commit()
    db.refresh(candidate)
    log_action(db, candidate, "Candidate status updated", candidate.status)
    return interview
