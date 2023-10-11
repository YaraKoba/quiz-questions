from app.crud.base import CRUDBase
from app.models import Question
from app.schemas import QuestionsCreate
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from typing import List


class CRUDQuestions(CRUDBase[Question, QuestionsCreate, QuestionsCreate]):
    def get_by_question(self, db: Session, *, question: str) -> Question | None:
        return db.query(Question).filter(Question.question == question).first()
    
    def create_multi(self, db: Session, *, objs_in: List[QuestionsCreate]) -> (int, List[Question | None]):
        added_questions = []
        count_repeated = 0
        for obj_in in objs_in:
            if not self.get_by_question(db=db, question=obj_in.question):
                db_obj = Question(**jsonable_encoder(obj_in))
                db.add(db_obj)
                db.commit()
                db.refresh(db_obj)
                added_questions.append(db_obj)
            else:
                count_repeated += 1
        return count_repeated, added_questions
            


questions = CRUDQuestions(Question)
