from app.crud.base import CRUDBase
from app.models import Question
from app.schemas import QuestionsCreate
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from typing import List


class CRUDQuestions(CRUDBase[Question, QuestionsCreate, QuestionsCreate]):
    def create_multi(self, db: Session, *, questions_in: List[QuestionsCreate]) -> List[QuestionsCreate]:
        db_questions = [Question(**jsonable_encoder(que))
                        for que in questions_in if not self.get(db=db, id=que.id)]
        db.add_all(db_questions)
        db.commit()
        for db_que in db_questions:
            db.refresh(db_que)
        return db_questions


questions = CRUDQuestions(Question)
