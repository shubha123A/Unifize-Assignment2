from datetime import datetime
from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from db import init_db, SessionLocal, Job, Candidate, Interview, ActionLog
from schemas import JobCreate, JobRead, CandidateCreate, CandidateRead, InterviewCreate, InterviewRead, ActionLogRead
import services

init_db()
app = FastAPI(title="Unifize Recruitment Automations")

@app.get("/")
def root_redirect():
    return RedirectResponse(url="/docs")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/jobs", response_model=JobRead)
def create_job(job: JobCreate, db: Session = Depends(get_db)):
    instance = Job(title=job.title, team=job.team, location=job.location)
    db.add(instance)
    db.commit()
    db.refresh(instance)
    return instance

@app.post("/candidates", response_model=CandidateRead)
def create_candidate(candidate: CandidateCreate, db: Session = Depends(get_db)):
    existing = db.query(Candidate).filter(Candidate.email == candidate.email).first()
    if existing:
        raise HTTPException(status_code=409, detail="Candidate with this email already exists")
    instance = Candidate(
        first_name=candidate.first_name,
        last_name=candidate.last_name,
        email=candidate.email,
        phone=candidate.phone,
        source=candidate.source,
        job_id=candidate.job_id,
        status="Applied",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )
    db.add(instance)
    db.commit()
    db.refresh(instance)
    services.log_action(db, instance, "Candidate created", f"Job {candidate.job_id}")
    return instance

@app.get("/candidates", response_model=list[CandidateRead])
def list_candidates(db: Session = Depends(get_db)):
    return db.query(Candidate).order_by(Candidate.created_at.desc()).all()

@app.post("/candidates/{candidate_id}/advance", response_model=CandidateRead)
def advance_candidate(candidate_id: int, db: Session = Depends(get_db)):
    candidate = db.query(Candidate).filter(Candidate.id == candidate_id).first()
    if not candidate:
        raise HTTPException(status_code=404, detail="Candidate not found")
    try:
        return services.advance_candidate(db, candidate)
    except services.WorkflowError as exc:
        raise HTTPException(status_code=400, detail=str(exc))

@app.post("/candidates/{candidate_id}/schedule-screening", response_model=InterviewRead)
def schedule_screening(candidate_id: int, db: Session = Depends(get_db)):
    candidate = db.query(Candidate).filter(Candidate.id == candidate_id).first()
    if not candidate:
        raise HTTPException(status_code=404, detail="Candidate not found")
    return services.schedule_screening_interview(db, candidate)

@app.post("/interviews/{interview_id}/complete", response_model=InterviewRead)
def complete_interview(interview_id: int, notes: str, decision: str, db: Session = Depends(get_db)):
    interview = db.query(Interview).filter(Interview.id == interview_id).first()
    if not interview:
        raise HTTPException(status_code=404, detail="Interview not found")
    if interview.status != "Pending":
        raise HTTPException(status_code=400, detail="Interview already completed")
    services.complete_interview(db, interview, notes, decision)
    db.refresh(interview)
    return interview

@app.post("/automation/run")
def run_automation(db: Session = Depends(get_db)):
    reminders = services.run_automation(db)
    return {"reminders_created": len(reminders)}

@app.get("/dashboard")
def dashboard(db: Session = Depends(get_db)):
    jobs = db.query(Job).count()
    candidates_total = db.query(Candidate).count()
    pipeline = {
        "Applied": db.query(Candidate).filter(Candidate.status == "Applied").count(),
        "Screening": db.query(Candidate).filter(Candidate.status == "Screening").count(),
        "Interview": db.query(Candidate).filter(Candidate.status == "Interview").count(),
        "Offer": db.query(Candidate).filter(Candidate.status == "Offer").count(),
        "Hired": db.query(Candidate).filter(Candidate.status == "Hired").count(),
        "Rejected": db.query(Candidate).filter(Candidate.status == "Rejected").count(),
    }
    return {
        "jobs": jobs,
        "candidates": candidates_total,
        "pipeline": pipeline,
    }

@app.get("/actions", response_model=list[ActionLogRead])
def action_log(db: Session = Depends(get_db)):
    return db.query(ActionLog).order_by(ActionLog.created_at.desc()).limit(50).all()
