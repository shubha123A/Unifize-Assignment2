from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing import Optional

class EventCreate(BaseModel):
    title: str
    category: str
    location: str
    start_date: datetime
    end_date: datetime

class EventRead(EventCreate):
    id: int
    status: str
    created_at: datetime

    class Config:
        from_attributes = True

class EventSessionCreate(BaseModel):
    event_id: int
    title: str
    speaker: str
    scheduled_at: datetime

class EventSessionRead(EventSessionCreate):
    id: int
    status: str

    class Config:
        from_attributes = True

class AttendeeCreate(BaseModel):
    event_id: int
    first_name: str
    last_name: str
    email: EmailStr

class AttendeeRead(AttendeeCreate):
    id: int
    registration_status: str
    created_at: datetime

    class Config:
        from_attributes = True

class ActionLogRead(BaseModel):
    id: int
    event_id: Optional[int]
    attendee_id: Optional[int]
    action: str
    payload: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True
