from app.crud.base import CRUDBase
from app.models import PullQuestions, Question
from app.schemas import PullQuestionCreate
from sqlalchemy.orm import Session, joinedload
from typing import List


class CRUDPullQuestion(CRUDBase[PullQuestions, PullQuestionCreate, PullQuestionCreate]):
    def get_previous_question(self, db: Session, pull_id: int) -> List[Question] | None:
        if pull_id <= 0:
            return None
        qury = db.query(PullQuestions).filter(PullQuestions.id == pull_id-1).options(joinedload(PullQuestions.questions)).first()
        if qury:
            return qury.questions
        else:
            return None 


pull = CRUDPullQuestion(PullQuestions)
