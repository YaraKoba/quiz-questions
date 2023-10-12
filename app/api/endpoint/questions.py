from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import QuestionsCreate, PullQuestionCreate, QuestionAPI, QuestionsIn
from app.api.deps import get_db
from app.core.questions_manager import add_unrepeated_questions
from app.crud import pull, questions

router = APIRouter()


@router.post('/add-new', response_model=List[QuestionsCreate | None])
def add_new_questions(question_num: QuestionsIn, db: Session = Depends(get_db)):
    new_pull = pull.create(db=db, obj_in=PullQuestionCreate()).id
    added_questions = add_unrepeated_questions(db=db, num=question_num.questions_num, question_pull=new_pull)
    return added_questions
