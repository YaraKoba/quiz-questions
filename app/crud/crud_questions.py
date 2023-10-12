from app.crud.base import CRUDBase
from app.models import Question
from app.schemas import QuestionsCreate
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from typing import List


class CRUDQuestions(CRUDBase[Question, QuestionsCreate, QuestionsCreate]):
    pass


questions = CRUDQuestions(Question)
