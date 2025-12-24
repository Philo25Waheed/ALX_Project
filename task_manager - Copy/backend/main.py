from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import engine, SessionLocal
from models import Base, Task

app = FastAPI()
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/tasks")
def create_task(title: str, owner: str, db: Session = Depends(get_db)):
    task = Task(title=title, owner=owner)
    db.add(task)
    db.commit()
    return {"message": "Task created"}

@app.get("/tasks")
def get_tasks(owner: str, db: Session = Depends(get_db)):
    return db.query(Task).filter(Task.owner == owner).all()
