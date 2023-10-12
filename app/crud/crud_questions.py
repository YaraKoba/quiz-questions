from app.crud.base import CRUDBase
from app.models import Question
from app.schemas import QuestionsCreate
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from typing import List


class CRUDQuestions(CRUDBase[Question, QuestionsCreate, QuestionsCreate]):
    def create_multi(self, db: Session, *, objs_in: List[QuestionsCreate]) -> (int, List[Question | None]):
        added_questions = []
        count_repeated = 0
        for obj_in in objs_in:
            if not self.get(db=db, id=obj_in.id):
                db_obj = Question(**jsonable_encoder(obj_in))
                added_questions.append(db_obj)
            else:
                count_repeated += 1
        
        db.add_all(added_questions)
        db.commit()
        for db_obj in added_questions:
            db.refresh(db_obj)
        return count_repeated, added_questions
            


questions = CRUDQuestions(Question)
