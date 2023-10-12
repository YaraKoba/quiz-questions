from typing import List
from sqlalchemy.orm import Session
from app.schemas import QuestionsCreate
from app.crud import questions
from app.core.fetching import fetch_questions


def filter_only_unique_question(new_questions: List[QuestionsCreate], db: Session) -> List[QuestionsCreate]:
    unique_questions = []
    for new_question in new_questions:
        if not questions.get(db=db, id=new_question.id):
            unique_questions.append(new_question)
    return unique_questions


def add_unrepeated_questions(db: Session, num: int, question_pull: int) -> List[QuestionsCreate]:
    """
        Add unrepeated questions to the database.

    Args:
        db (Session): The SQLAlchemy database session.
        num (int): The number of unrepeated questions to add.
        question_pull (int): The ID of the question pull associated with the questions.

    Returns:
        List[QuestionsCreate]: A list of newly added questions in the form of QuestionsCreate objects.
    """
    unique_questions = []
    while num > 0:
        new_questions = fetch_questions(num)
        new_questions = [QuestionsCreate(**question.model_dump(), pull_questions_id=question_pull)
                         for question in new_questions]
        filter_questions = filter_only_unique_question(new_questions, db=db)
        unique_questions.extend(filter_questions)
        num -= len(unique_questions) 

    return unique_questions