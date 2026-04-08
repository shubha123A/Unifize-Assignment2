from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

DATABASE_URL = "sqlite:///./recruitment.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)
Base = declarative_base()

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    team = Column(String, nullable=False)
    location = Column(String, nullable=False)
    status = Column(String, default="Open")
    created_at = Column(DateTime, default=datetime.utcnow)

    candidates = relationship("Candidate", back_populates="job")

class Candidate(Base):
    __tablename__ = "candidates"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    phone = Column(String, nullable=True)
    source = Column(String, default="Referral")
    status = Column(String, default="Applied")
    job_id = Column(Integer, ForeignKey("jobs.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    job = relationship("Job", back_populates="candidates")
    interviews = relationship("Interview", back_populates="candidate")
    actions = relationship("ActionLog", back_populates="candidate")

class Interview(Base):
    __tablename__ = "interviews"

    id = Column(Integer, primary_key=True, index=True)
    candidate_id = Column(Integer, ForeignKey("candidates.id"), nullable=False)
    round_label = Column(String, nullable=False)
    interviewer = Column(String, nullable=False)
    scheduled_at = Column(DateTime, nullable=False)
    status = Column(String, default="Pending")
    notes = Column(Text, default="")

    candidate = relationship("Candidate", back_populates="interviews")

class ActionLog(Base):
    __tablename__ = "action_logs"

    id = Column(Integer, primary_key=True, index=True)
    candidate_id = Column(Integer, ForeignKey("candidates.id"), nullable=False)
    action = Column(String, nullable=False)
    payload = Column(Text, default="")
    created_at = Column(DateTime, default=datetime.utcnow)

    candidate = relationship("Candidate", back_populates="actions")


def init_db():
    Base.metadata.create_all(bind=engine)
