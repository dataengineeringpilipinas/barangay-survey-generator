from fastapi import FastAPI, Request, Form, HTTPException, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship
from datetime import datetime
from typing import List, Optional
import os

# Database setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./barangay_surveys.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Models
class Survey(Base):
    __tablename__ = "surveys"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    is_active = Column(Boolean, default=True)
    
    questions = relationship("Question", back_populates="survey", cascade="all, delete-orphan")
    responses = relationship("Response", back_populates="survey", cascade="all, delete-orphan")

class Question(Base):
    __tablename__ = "questions"
    
    id = Column(Integer, primary_key=True, index=True)
    survey_id = Column(Integer, ForeignKey("surveys.id"), nullable=False)
    question_text = Column(Text, nullable=False)
    question_type = Column(String(50), nullable=False)  # text, multiple_choice, single_choice
    options = Column(Text)  # JSON string for multiple/single choice options
    is_required = Column(Boolean, default=True)
    order = Column(Integer, default=0)
    
    survey = relationship("Survey", back_populates="questions")
    answers = relationship("Answer", back_populates="question", cascade="all, delete-orphan")

class Response(Base):
    __tablename__ = "responses"
    
    id = Column(Integer, primary_key=True, index=True)
    survey_id = Column(Integer, ForeignKey("surveys.id"), nullable=False)
    respondent_name = Column(String(100))
    submitted_at = Column(DateTime, default=datetime.utcnow)
    
    survey = relationship("Survey", back_populates="responses")
    answers = relationship("Answer", back_populates="response", cascade="all, delete-orphan")

class Answer(Base):
    __tablename__ = "answers"
    
    id = Column(Integer, primary_key=True, index=True)
    response_id = Column(Integer, ForeignKey("responses.id"), nullable=False)
    question_id = Column(Integer, ForeignKey("questions.id"), nullable=False)
    answer_text = Column(Text, nullable=False)
    
    response = relationship("Response", back_populates="answers")
    question = relationship("Question", back_populates="answers")

# Create tables
Base.metadata.create_all(bind=engine)

# FastAPI app
app = FastAPI(title="Barangay Survey Generator", description="A simple survey generator for barangay management")

# Templates and static files
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Routes
@app.get("/", response_class=HTMLResponse)
async def home(request: Request, db: Session = Depends(get_db)):
    surveys = db.query(Survey).filter(Survey.is_active == True).all()
    return templates.TemplateResponse("home.html", {"request": request, "surveys": surveys})

@app.get("/create", response_class=HTMLResponse)
async def create_survey_form(request: Request):
    return templates.TemplateResponse("create_survey.html", {"request": request})

@app.post("/create")
async def create_survey(
    title: str = Form(...),
    description: str = Form(""),
    db: Session = Depends(get_db)
):
    survey = Survey(title=title, description=description)
    db.add(survey)
    db.commit()
    db.refresh(survey)
    return RedirectResponse(url=f"/survey/{survey.id}/edit", status_code=303)

@app.get("/survey/{survey_id}", response_class=HTMLResponse)
async def view_survey(request: Request, survey_id: int, db: Session = Depends(get_db)):
    survey = db.query(Survey).filter(Survey.id == survey_id).first()
    if not survey:
        raise HTTPException(status_code=404, detail="Survey not found")
    
    questions = db.query(Question).filter(Question.survey_id == survey_id).order_by(Question.order).all()
    return templates.TemplateResponse("survey.html", {
        "request": request, 
        "survey": survey, 
        "questions": questions
    })

@app.get("/survey/{survey_id}/edit", response_class=HTMLResponse)
async def edit_survey(request: Request, survey_id: int, db: Session = Depends(get_db)):
    survey = db.query(Survey).filter(Survey.id == survey_id).first()
    if not survey:
        raise HTTPException(status_code=404, detail="Survey not found")
    
    questions = db.query(Question).filter(Question.survey_id == survey_id).order_by(Question.order).all()
    return templates.TemplateResponse("edit_survey.html", {
        "request": request, 
        "survey": survey, 
        "questions": questions
    })

@app.post("/survey/{survey_id}/submit")
async def submit_survey(
    survey_id: int,
    request: Request,
    db: Session = Depends(get_db)
):
    form_data = await request.form()
    
    # Create response
    response = Response(
        survey_id=survey_id,
        respondent_name=form_data.get("respondent_name", "Anonymous")
    )
    db.add(response)
    db.commit()
    db.refresh(response)
    
    # Create answers
    questions = db.query(Question).filter(Question.survey_id == survey_id).all()
    for question in questions:
        answer_text = form_data.get(f"question_{question.id}", "")
        if answer_text:
            answer = Answer(
                response_id=response.id,
                question_id=question.id,
                answer_text=answer_text
            )
            db.add(answer)
    
    db.commit()
    return RedirectResponse(url=f"/survey/{survey_id}/thanks", status_code=303)

@app.get("/survey/{survey_id}/thanks", response_class=HTMLResponse)
async def survey_thanks(request: Request, survey_id: int):
    return templates.TemplateResponse("thanks.html", {"request": request, "survey_id": survey_id})

@app.get("/survey/{survey_id}/results", response_class=HTMLResponse)
async def survey_results(request: Request, survey_id: int, db: Session = Depends(get_db)):
    survey = db.query(Survey).filter(Survey.id == survey_id).first()
    if not survey:
        raise HTTPException(status_code=404, detail="Survey not found")
    
    questions = db.query(Question).filter(Question.survey_id == survey_id).order_by(Question.order).all()
    responses = db.query(Response).filter(Response.survey_id == survey_id).all()
    
    # Get answers for each response
    for response in responses:
        response.answers = db.query(Answer).filter(Answer.response_id == response.id).all()
    
    return templates.TemplateResponse("results.html", {
        "request": request,
        "survey": survey,
        "questions": questions,
        "responses": responses
    })

@app.post("/survey/{survey_id}/add-question")
async def add_question(
    survey_id: int,
    question_text: str = Form(...),
    question_type: str = Form(...),
    options: str = Form(""),
    is_required: bool = Form(True),
    db: Session = Depends(get_db)
):
    # Get the next order number
    max_order = db.query(Question).filter(Question.survey_id == survey_id).count()
    
    question = Question(
        survey_id=survey_id,
        question_text=question_text,
        question_type=question_type,
        options=options if options else None,
        is_required=is_required,
        order=max_order + 1
    )
    
    db.add(question)
    db.commit()
    db.refresh(question)
    
    return {"status": "success", "question_id": question.id}

@app.delete("/survey/{survey_id}/question/{question_id}/delete")
async def delete_question(
    survey_id: int,
    question_id: int,
    db: Session = Depends(get_db)
):
    question = db.query(Question).filter(
        Question.id == question_id,
        Question.survey_id == survey_id
    ).first()
    
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    
    db.delete(question)
    db.commit()
    
    return {"status": "success"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
