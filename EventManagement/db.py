from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

DATABASE_URL = "sqlite:///./eventmgmt.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)
Base = declarative_base()

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    category = Column(String, nullable=False)
    location = Column(String, nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    status = Column(String, default="Draft")
    created_at = Column(DateTime, default=datetime.utcnow)

    sessions = relationship("EventSession", back_populates="event")
    attendees = relationship("Attendee", back_populates="event")

class EventSession(Base):
    __tablename__ = "event_sessions"

    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey("events.id"), nullable=False)
    title = Column(String, nullable=False)
    speaker = Column(String, nullable=False)
    scheduled_at = Column(DateTime, nullable=False)
    status = Column(String, default="Pending")

    event = relationship("Event", back_populates="sessions")

class Attendee(Base):
    __tablename__ = "attendees"

    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey("events.id"), nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    registration_status = Column(String, default="Registered")
    created_at = Column(DateTime, default=datetime.utcnow)

    event = relationship("Event", back_populates="attendees")

class ActionLog(Base):
    __tablename__ = "action_logs"

    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey("events.id"), nullable=True)
    attendee_id = Column(Integer, ForeignKey("attendees.id"), nullable=True)
    action = Column(String, nullable=False)
    payload = Column(Text, default="")
    created_at = Column(DateTime, default=datetime.utcnow)

    event = relationship("Event")
    attendee = relationship("Attendee")


def init_db():
    Base.metadata.create_all(bind=engine)
