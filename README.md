📘 Unifize Process Automation Demo
🚀 Overview

This project demonstrates the design and implementation of two independent workflow systems within a single environment:

Recruitment Management System
Event Management System

Both workflows are built with a focus on:

Process clarity
Automation of repetitive tasks
Real-time visibility through dashboards

The goal is to show how structured workflows can improve efficiency and reduce manual intervention.

🧠 Problem Statement

Organizations often rely on manual coordination for hiring and event management, which leads to:

Lack of visibility across stages
Delays due to manual updates
Inefficient communication
Difficulty tracking progress

This solution addresses these challenges by introducing automation-driven workflows.

⚙️ System Architecture

The system consists of two separate services:

Service	Port	Description
Recruitment API	8000	Handles hiring workflow
Event Management API	8001	Handles event lifecycle

Each service exposes REST APIs with clearly defined stages and actions.

🧩 Recruitment Workflow
🔹 Key Stages
Job Creation
Candidate Application
Interview Scheduling (Automated)
Interview Feedback
Offer Stage
🔹 Key Features
Automated interview scheduling
Candidate status tracking
Pipeline visibility via dashboard
🔹 Sample Flow
Create Job
Add Candidate
Run Automation (Interview scheduled)
Complete Interview
Candidate moves to Offer stage
🎉 Event Management Workflow
🔹 Key Stages
Event Creation
Session Planning
Attendee Registration
Event Execution
Completion
🔹 Key Features
Automated registration handling
Reminder scheduling
Centralized dashboard
🔹 Sample Flow
Create Event
Add Session
Register Attendee
Run Automation
Start & Complete Event
🤖 Automation Logic

Automation is a core part of the system:

Recruitment
Auto-schedules interviews
Moves candidates between stages
Event Management
Opens registration based on event timing
Triggers reminders for attendees
📊 Dashboard & Monitoring

Each service includes:

Dashboard (/dashboard)
Displays counts of entities (candidates, events, etc.)
Action Logs (/actions)
Tracks system activities for transparency and debugging
🧪 API Endpoints
Recruitment API (Port 8000)
POST /jobs
POST /candidates
POST /automation/run
POST /interviews/{id}/complete
GET /dashboard
Event Management API (Port 8001)
POST /events
POST /sessions
POST /attendees
POST /automation/run
POST /events/{id}/start
POST /events/{id}/complete
GET /dashboard
GET /actions
▶️ How to Run
1. Start Services

Run both services in separate terminals:

# Recruitment Service
uvicorn recruitment_app:app --port 8000

# Event Management Service
uvicorn event_app:app --port 8001
2. Access API Docs
Recruitment → http://127.0.0.1:8000/docs
Event Management → http://127.0.0.1:8001/docs
🎥 Demo Walkthrough
Recruitment
Create job → Add candidate → Run automation
Complete interview → Candidate moves to offer
Event Management
Create event → Add session → Register attendee
Run automation → Start → Complete event
🧭 Key Design Decisions
Separation of workflows → Improves modularity
Automation-first approach → Reduces manual effort
API-driven design → Easy to extend and integrate
Dashboards & logs → Improve visibility and tracking
🔮 Future Improvements
AI-based candidate screening
Smart event recommendations
Email/SMS notification integration
Advanced analytics dashboards
🏁 Conclusion

This project demonstrates how structured workflows + automation can:

Improve operational efficiency
Reduce manual errors
Provide real-time insights

It highlights the ability to design scalable systems with minimal supervision and clear process thinking.

📎 Additional Notes

Refer to:
UNIFIZE_ORG_PROCESS_DASHBOARD.md for an organization-level summary of both workflows.
