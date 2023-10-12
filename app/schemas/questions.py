from pydantic import BaseModel
from pydantic.functional_validators import AfterValidator
import datetime
from typing import Optional, Annotated


def check_num(num: int) -> int:
    assert 0 < num <= 100, f"{num}, must be 0 < number < 100"
    return num


ValidNumber = Annotated[int, AfterValidator(check_num)]


class QuestionsIn(BaseModel):
    questions_num: ValidNumber
    
    
class QuestionsBase(BaseModel):
    id: int
    question: str
    answer: str
    created_at: datetime.datetime


class QuestionAPI(QuestionsBase):
    pass
    

class QuestionsCreate(QuestionsBase):
    pull_questions_id: int
    

class QuestionsInDB(QuestionsBase):
    id: int
    add_date: datetime.date
    pull_questions_id: int


class PullQuestionCreate(BaseModel):
    pass