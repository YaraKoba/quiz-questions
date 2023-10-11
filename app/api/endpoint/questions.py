from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import QuestionsCreate, PullQuestionCreate, QuestionAPI, QuestionsIn
from app.api.deps import get_db
import requests
from app.crud import pull, questions

router = APIRouter()

def fetch_questions(num: int) -> List[QuestionAPI]:
    url = f"https://jservice.io/api/random?count={num}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return [QuestionAPI(**question) for question in data]
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch question from the public API: {str(e)}")

def add_unrepeated_questions(db: Session, num: int, question_pull: int) -> List[QuestionsCreate]:
    added_questions = []
    while num > 0:
        new_questions = fetch_questions(num)
        new_questions = [QuestionsCreate(**question.model_dump(), pull_questions_id=question_pull) for question in new_questions]
        repeated, added = questions.create_multi(db=db, objs_in=new_questions)
        added_questions.extend(added)
        num = repeated
        print(num)
    return added_questions

@router.post('/add-new-questions-and-get-previous-questions', response_model=List[QuestionsCreate | None])
def get_empty_times(question_num: QuestionsIn, db: Session = Depends(get_db)):
    new_pull = pull.create(db=db, obj_in=PullQuestionCreate()).id
    added_questions = add_unrepeated_questions(db=db, num=question_num.questions_num, question_pull=new_pull)
    previos_questions = pull.get_previous_question(db=db, pull_id=new_pull)
    return previos_questions
