from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing import List, Optional

class JobCreate(BaseModel):
    title: str
    team: str
    location: str

class JobRead(JobCreate):
    id: int
    status: str
    created_at: datetime

    class Config:
        from_attributes = True

class CandidateCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: Optional[str] = None
    source: Optional[str] = "Referral"
    job_id: int

class CandidateRead(CandidateCreate):
    id: int
    status: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class InterviewCreate(BaseModel):
    candidate_id: int
    round_label: str
    interviewer: str
    scheduled_at: datetime

class InterviewRead(InterviewCreate):
    id: int
    status: str
    notes: Optional[str]

    class Config:
        from_attributes = True

class ActionLogRead(BaseModel):
    id: int
    candidate_id: int
    action: str
    payload: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True
